---
layout: post
title: Adding GitLab CI Support
date: 2018-01-22
---

I recently made [a post](/blog/2018/01/exploring-alternatives-to-buddybuild/) detailing several continuous integration systems and the one I ultimately decided on: [GitLab CI](https://about.gitlab.com/gitlab-ci/). Today, I’m pulling another one of my projects over to the new service, and I thought I’d put together a play-by-play on what exactly I’m doing to build and deploy this project with GitLab CI.

## About the Project
The project in question is [Scrawl Notes](https://notes.scrawlapp.com) for iOS. It’s a relatively simple app with relatively simple requirements. It has a single dependency[^1], which is managed by [Carthage](https://github.com/Carthage/Carthage). There are two test targets (both UI and unit tests)[^2], and I’d like to run them both whenever I push to my GitLab server. Finally, I deploy this app to beta testers via Apple’s TestFlight, so I’d like to automatically upload builds there when I push to my `master` branch.

## Fastlane
Getting all of this set up on another project was made way easier with [Fastlane](https://fastlane.tools), so I’m going to be using that here again. Scrawl Notes isn’t using Fastlane yet, so adding that will be the first step.

    $ fastlane setup

As part of the setup process, Fastlane asks me for my Apple ID. I have a separate Apple developer account just for my continuous integration systems. This is mainly so that if it goes completely haywire, at least it’s limited to only **my** work, and not my employer’s or any of our clients’.

After setup completes, Fastlane has created a couple of files for me:

    $ git status
    On branch 1.2-release
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)
  
        new file:   fastlane/Appfile
        new file:   fastlane/Deliverfile
        new file:   fastlane/Fastfile
        …

The main one I care about here is the `Fastfile`, which describes all the tasks I want Fastlane to run. The default generated file has a **ton** of stuff in it, and I don’t want all that right now. Here’s what I’ve got instead:

{% highlight ruby %}
min_fastlane_version("2.73.0")
  
default_platform(:ios)

platform :ios do
  desc "Runs all the tests"
  lane :test do
    # Run all tests in the scheme named "Scrawl"
    run_tests(scheme: "Scrawl")
  end

  desc "Submit a new Beta Build to Apple TestFlight"
  desc "This will also make sure the profile is up to date"
  lane :beta do
    # Download signing credentials from ADC
    get_certificates 
    get_provisioning_profile(platform: "ios")

    # Update the Xcode project with the correct signing credentials
    disable_automatic_code_signing
    update_project_provisioning(build_configuration: "Release")

    # Set the build number to the number of Git commits
    build_number = sh "git log --oneline --no-merges | wc -l"
    increment_build_number(build_number: build_number)
    
    # Build the app for App Store
    build_app(
      export_method: "app-store",
      scheme: "Scrawl")

    # Just upload the build to TestFlight, no other changes
    upload_to_testflight(
      app_platform: "ios",
      skip_submission: true,
      skip_waiting_for_build_processing: true)
  end
end
{% endhighlight %}

This file describes two lanes. The first is `test`, which simply runs all the tests in the “Scrawl” target (my main app target). The other is `beta`, which does quite a bit more:
- Downloads my signing certificate and provisioning profile from the Apple Developer portal.
- Disables Xcode’s “automatic signing” feature.
- Edits the project file to add the signing credentials downloaded earlier.
- Updates the build number to the number of Git commits that have been made so far.
- Builds the app.
- Uploads the built products to iTunes Connect, but does not automatically submit it for TestFlight release.

Unfortunately, this is where I hit a few snags. Something I forgot to mention about the project above is that while it’s a simple **app** project… the app isn’t the only target. Embedded within the Scrawl Notes app are <s>three</s>[^3] two app extensions: a Today widget and a Siri intent. It was these that gave me some problems; they weren’t getting signed with the appropriate provisioning profiles for each. Ultimately, I added two extra lines for each extension target:

{% highlight ruby %}
get_provisioning_profile(
  app_identifier: "com.cocoatype.Scratch.Widget",
  filename: "widget.mobileprovision",
  platform: "ios")

update_project_provisioning(
  build_configuration: "Release",
  target_filter: "Widget",
  profile: "./widget.mobileprovision")
{% endhighlight %}

This did the trick. I’m not sure if it’s the most appropriate way to handle this case, but it seemed like the most straightforward.

## GitLab CI
At this point, I have a working Fastlane setup with two commands to run: `fastlane test` will run my tests and `fastlane beta` will build the app and upload it to TestFlight. However, that’s only available locally; GitLab won’t run these commands for me when I push to my repository.

In order to get GitLab to run CI commands when I push, I have to include a file named `.gitlab-ci.yml` in the root of my repository. Here’s what that file looks like:

{% highlight yaml %}
stages:
  - test
  - beta
variables:
  LC_ALL: "en_US.UTF-8"
  LANG: "en_US.UTF-8"
test:
  dependencies: []
  stage: test
  artifacts:
    paths:
      - fastlane/screenshots
      - fastlane/logs
      - fastlane/test_output
  script:
    - fastlane test
  tags:
    - xcode
beta:
  dependencies: []
  stage: beta
  artifacts:
    paths:
      - fastlane/screenshots
      - fastlane/logs
  script:
    - fastlane beta
  tags:
    - xcode
  only:
    - master
{% endhighlight %}

This defines two CI stages: `test` and `beta`. Those names should look familiar: they’re the same as the Fastlane lanes we defined above. They have the same behaviors: `test` runs the tests, and `beta` uploads to TestFlight.

We specify a few behaviors for each stage:
- `artifacts` is the list of files we want GitLab to keep around from each build. We keep any screenshots taken during the build, the logs of the build, and (when applicable) the results of the test runs.
- `script` is what command we want run. We simply run our Fastlane commands, exactly as we would from the command line.
- `tags` defines what GitLab “runner” we want to have run our commands. `xcode` is my Mac that does all my iOS builds. If I wanted to, I could have several different machines[^4] all tagged `xcode`, and GitLab CI would pick the first available free runner for me.
- `only` is specified on the `beta` stage. This tells GitLab CI I only want this stage to be run which a push is made to the `master` branch. It doesn’t make sense for me to upload builds for unfinished feature branches.

One quick commit and push later, and my build is running! Followed quickly by not running and a big red X indicating a build failure. Good thing we kept those logs!

    ▸ CloudCoordinator.swift:8:8: no such module 'Majima'
    ▸ import Majima

…oops. Remember how I said this project had only one dependency, and that it was managed by Carthage? I’ve forgotten to run Carthage! Fortunately, this is easy to fix. Let’s add a single line to each `script` section:

{% highlight yaml %}
  - "carthage bootstrap --platform ios --no-use-binaries"
{% endhighlight %}

Just like that, we’ve turned that red X into a green checkmark!

## Wrapping Up
There you have it: a blow-by-blow recap of setting up an iOS project for GitLab CI, complete with stupid mistakes and code signing issues! I’ve posted my final `Fastfile` and `gitlab-ci.yml` as [Gists on GitHub](https://gist.github.com/Arclite/c62e1cd143525c5005b2e6eeb3fd7913), so go take a look if you want to copy them for your own usage.

---- 

[^1]:	Majima, a library for handling three-way merges.

[^2]:	I mean… there’s no actual **tests** in these targets, per se. But there might be eventually!

[^3]:	Definitely not a feature announcement.

[^4]:	Physical machines or virtual ones, it doesn’t matter.