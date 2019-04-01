---
layout: post
title: My First 20 Minutes in an iOS Project
date: 2019-03-31
excerpt: I’m someone that likes to create a lot of small app projects whenever an idea strikes me. Like, a **lot** of app projects. Most of them don’t really go anywhere, but I’ve gotten pretty good at starting things, and I’d like to publicly document the steps that I take to get a new iOS project off the ground.
---
I’m someone that likes to create a lot of small app projects whenever an idea strikes me. Like, a **lot** of app projects. Most of them don’t really go anywhere, but I’ve gotten pretty good at starting things, and I’d like to publicly document the steps that I take to get a new iOS project off the ground.[^1]

The title from this post and the basic idea is shamelessly stolen from [My First 10 Minutes on a Server](https://www.codelitt.com/blog/my-first-10-minutes-on-a-server-primer-for-securing-ubuntu/). Like that post, this one is meant to be a **base**, not a definitive guide to creating an iOS app project. A lot of these steps are specific to my personal whims and code style. Don’t feel like you have to copy things exactly. If you prefer something else, great! Hopefully this guide can fill in some blanks, act as a reminder of things commonly forgotten, or just show insight into a different way of working.

## Creating the Project
First things first, let’s create our new Xcode project. Click the “Create a new Xcode project” button on the “Welcome to Xcode” window, or select New \> Project… from the File menu.

Xcode gives us a bunch of templates to choose from. I prefer to alway use the “Single View App” template, even if my project is going to eventually match one of the other templates (such as “Master-Detail App”, because it gives me the least amount of boilerplate and the most freedom to architect a project the way I want.

Fill out the information on the next page. Most of the information on this page is pretty straightforward (product name, organization name). Per Apple’s recommendation, your organization identifier should be your domain name, reversed (e.g., `name.pado` for the domain this blog is hosted on). I’m sure you have your own opinions on language choice, but come on, are you really going to not pick Swift by now?

The set of three checkboxes at the bottom is a little bit trickier. Personally, I only check “Include Unit Tests”. Even if my project is going to use Core Data (most of them don’t), I prefer being able to set up the Core Data stack my own way rather than using the boilerplate Apple provides. And UI tests have always seemed like more work than they’re worth, and flaky in the last few versions of Xcode to boot.

Save your project somewhere on disk. I have a Developer folder in my home directory, which itself contains four folders based on the seriousness of the project: one for projects related to my real job, one for projects that I’m planning on releasing to the world, one for personal tools, and one for silly toy projects. Lastly, check the “Create Git repository on my Mac” checkbox. While this does some silly things I don’t really like (more on that later), it’s still simpler than creating a Git repo by hand.

## Removing Boilerplate
Now we’ve got our basic project created, but there’s a bunch of stuff included that I don’t want to keep around. Let’s get rid of it.

Let’s get the most controversial one out of the way first: I start by deleting `Main.storyboard` and removing the associated Info.plist key (`UIMainStoryboardFile`). Interface Builder as a tool is fine[^2], but I grew out of it during a time when I switched to using [JetBrains AppCode](https://www.jetbrains.com/objc/), and now I just… don’t. We’ll set up our own window later.

Next, the `AppDelegate` file. So many functions to implement! Let’s not. Leave the `window` property, change `didFinishLaunchingWithOptions` to `willFinishLaunchingWithOptions`, and delete all the rest. If we need them later, we can always recreate them. Oh, and get rid of the comment in `willFinishLaunchingWithOptions` while you’re at it.

Onto `ViewController`. Let’s start by renaming it `AppViewController`, for reasons I’ll expand on later. Delete the one function (`viewDidLoad`) that’s included in it.

That’s it for the unnecessary additions to our project. Personally, I also like to trim down the file headers to just the creation date and copyright lines, but that’s just personal preference; make ‘em look however you want.

## Displaying the First View
If you build and run your app now, you’re going to be pretty disappointed; no UI gets set up at all and you’re left staring at a black screen. Let’s get something visible before we call this project “ready”.

### Window
First, let’s create our window. I start by creating an `AppWindow` subclass[^3]. This class is mostly to clean up the setup of our UI that we’ll eventually be doing in `AppDelegate`. Here’s the code I use:

<script src="https://gist.github.com/Arclite/691146cd9e7461c9b7c523064b23c4f8.js"></script>

With the way I build UIs, I see that `required init(coder: NSCoder)` a lot. Because we aren’t using Interface Builder, there’s no need to implement `init(coder:)`, but the compiler won’t let us **not** implement it, so we’re forced to sprinkle it throughout the codebase. I long ago set up an Xcode snippet to be able to put this in without much typing; a shortcut of `ric` will fill it out for me. The `@available(*, unavailable)` [attribute](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html) prevents anyone from accidentally calling it directly.

### View Controller
Next, let’s make our view controller actually display something. For now, I’m just going to put a bright red view on the screen so we know our UI is actually set up correctly. Here’s the code for a basic `AppViewController`:

<script src="https://gist.github.com/Arclite/645d0f10c23776248bca2ee86b355efa.js"></script>

The `init` method is pretty straightforward: just call `super.init(nibName:bundle:)` with `nil` because we aren’t using Interface Builder. Creating our own `init` method cleans up the call-site a bit, and gives us a place to do real initialization later.

I use `loadView` here rather than `viewDidLoad` because eventually I’ll be creating my own view subclass to load in here rather than using the view created by the system. For this reason, [Apple doesn’t recommend calling `super` here](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621454-loadview#); that’s one of the first things you should change after the initial project setup.

### App Delegate
Now that we’ve got our window and view controller ready, let’s get them on screen. All this requires is filling our our `application(_:willFinishLaunchingWithOptions:)` method:

<script src="https://gist.github.com/Arclite/1075363f7fdaf686101022ca4af594b4.js"></script>

This is all pretty straightforward: create an instance of our `AppWindow`, set its `rootViewController` to an instance of our `AppViewController`, and make it visible. Save it into our `window` property to keep it around, and we’re done!

Build and run the app now and you should see a bright red screen rather than the black one from before.

## Committing Changes
Okay, now that we have a basic working project, let’s save the changes we have so far. Let’s start by telling Git what files we **don’t** want. I use [a tool called `gibo`](https://github.com/simonwhitaker/gibo) to access the [GitHub `.gitignore` boilerplates](https://github.com/github/gitignore), but you can grab them yourself and copy them into a `.gitignore` file by hand just as easily. Grab the [Swift](https://github.com/github/gitignore/blob/master/Swift.gitignore)[^4] and [Xcode](https://github.com/github/gitignore/blob/master/Global/Xcode.gitignore) files and paste their contents into yours. If you don’t have a global gitignore set up, you may want to follow [GitHub’s guide](https://help.github.com/articles/ignoring-files/#create-a-global-gitignore) and add the [macOS](https://github.com/github/gitignore/blob/master/Global/macOS.gitignore) file to that while you’re at it.

Next, let’s remove some user-specific files that Xcode added that we don’t actually want to keep in our repository:

`git rm -r --cached *.xcodeproj/xcuserdata`

This will keep the files on disk, but delete them from your repository. These files are only used for you, so there’s no need to publish them to other developers (and for you to receive others in return).

Now that we’ve got our repository ready to go, let’s commit our working project:

`git commit -a -m "Setup initial project"`[^5]

## Hosting Code Online
Once you’ve got your basic project set up, you’ll want to host your code somewhere that’s not just on your machine. Even if you aren't sharing this project with other people, hosting your code online means you have it backed up, and that you can access it from other computers should you need to.

There are a lot of options out there for hosting source code, such as [GitHub](https://github.com), but personally I self-host a [GitLab](https://about.gitlab.com) instance. Whatever your tool of choice, there’s certainly a “New Project” button around somewhere. Click that, fill out whatever information is needed, and create your project.

Once that’s done, find the address for your new project. Depending on whether you’re using HTTPS or SSH, it’ll look like one of these:
- `git@git.pado.name:highlighter/app.git`
- `https://git.pado.name/highlighter/app.git`

Use the address for your repo to create a new remote in your Git repository (created by Xcode when we created the project):

`git remote add origin <address>`

…then push your changes to the server:

`git push -u origin master`

If all goes well, your code should be saved online. Refresh the UI for your code host and you should see your changes.

## Automating Your Build with Continuous Integration
I consider this an important step of any project that isn’t an obvious toy (and even some that are), but I’ve already covered it pretty thoroughly in two other blog posts of mine: [Exploring Alternatives to Buddybuild](https://pado.name/blog/2018/01/exploring-alternatives-to-buddybuild/) and [Adding GitLab CI Support](https://pado.name/blog/2018/01/adding-gitlab-ci-support/), so I’m just going to provide a quick overview in this post. For more detail, see those two posts.
1. Add the [Ruby](https://github.com/github/gitignore/blob/master/Ruby.gitignore) boilerplate to your gitignore.
2. Create a `Gemfile` to install Fastlane:
    <script src="https://gist.github.com/Arclite/8526848d85a2b4a576141e16748d435f.js"></script>
3. Create the basic Fastlane files by running `bundle exec fastlane init`, selecting the manual setup option, and hitting Enter until it stops.
4. Create lanes in your Fastfile and add your Apple ID to your Appfile (see [Adding GitLab CI Support](https://pado.name/blog/2018/01/adding-gitlab-ci-support/) for sample code).
5. Open your Xcode project, navigate to the project build settings, and find the “Code Signing Identity” setting. Click the arrow to the left of it to display nested build configurations. Change the setting for the “Release” configuration to “iOS Distribution”.
6. Configure your project for [Apple Generic Versioning](https://developer.apple.com/library/archive/qa/qa1827/_index.html).
7. Create a [GitLab CI YAML file](https://pado.name/blog/2018/01/adding-gitlab-ci-support/) to enable CI builds on GitLab (if applicable), or the equivalent on [your CI provider of choice](https://pado.name/blog/2018/01/exploring-alternatives-to-buddybuild/).

With an automated build setup, you can quickly issue new versions of your app to testers on TestFlight, make sure your app is building on machines other than your own, and have builds readily available on App Store Connect to submit for release.

## Next Steps
After this, you’re ready to begin building your next great (or not-so-great) app idea. Typically, I’m itching to get going at this point, but if you’re still not ready to start writing code, there’s a few other things you may want in a project:
- Add commonly-used frameworks with a dependency manager like [CocoaPods](https://cocoapods.org) or [Carthage](https://github.com/carthage/carthage).
- Copy over personal code that you share between many projects.
- Set up a code-cleanliness tool like [SwiftLint](https://github.com/realm/SwiftLint). 

Don’t get too carried away in setup and forget to start coding, however! Good luck on your new project!

[^1]:	This post is also meant to provide some additional context to a later endeavor, hopefully one you'll see tomorrow evening.

[^2]:	I actually used to be a huge IB fanboy. Oh, how the turntables…

[^3]:	Are you sensing a theme in names yet?

[^4]:	Or [Objective-C](https://github.com/github/gitignore/blob/master/Objective-C.gitignore), if you used that.

[^5]:	I actually never use the `-m` flag when committing code, but I use it for brevity here. Instead, you should use an editor, set up with defaults for good commit messages. [This blog post](https://chris.beams.io/posts/git-commit/) has a set of rules for good commit messages that I wish I could force all developers to use.