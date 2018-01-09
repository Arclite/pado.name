---
layout: post
title: Exploring Alternatives to buddybuild
date: 2018-01-09
---
Last week, the amazing mobile continuous integration service [buddybuild](http://buddybuild.com) was [acquired by Apple](https://www.buddybuild.com/blog/buddybuild-is-now-part-of-apple). I’ve been using buddybuild for nearly a year now to build all of my personal side projects such as [Scrawl Notes](https://notes.scrawlapp.com) and [Scrawl Pouch](https://pouch.scrawlapp.com). Their ease of setup and level of service and support far outstrips anything else I’ve seen, and it’s easy to understand why Apple snapped them up.

I was using buddybuild’s free service plan, which allowed for a single build at a time that got put in line behind paying customers. It usually took about an hour before a build would run, but that was perfect for my needs and the amount I was able to spend[^1]. Unfortunately, as part of the acquisition, buddybuild will be shutting down the free service plan on March 1st, so I have to go looking for a new continuous integration system.

This post is **not** intended to pick a specific “winner”, but to give insight into my own personal decision process. The choice I ended up making is almost certainly the wrong one for your specific needs. Rather, this post aims to be a guide as to what solutions are out there, and what pros and cons I personally saw for each one.

## My Needs
I don’t have a particularly demanding set of needs for my continuous integration system; this setup will be for my pet personal projects. However, there is some baseline functionality that I need just to be able to use it.

- Can build iOS, watchOS, and tvOS projects.
- Can pull code from self-hosted Git repositories[^2].
- Will build code on pushes to a specific Git branch.
- Will deploy the built apps to iTunes Connect, to publish on the App Store or TestFlight.
- Low-cost or free tiers (\<$20/month).

Other “nice-to-haves” are:
- Ease of setup/maintenance.
- Good documentation.
- Integration with Slack[^3].
- Support for non-iOS platforms without compromising ease of setup.

## Alternatives Considered
With those needs/wants in mind, what did I look into?

### CircleCI
Circle (along with non-considered alternative Travis) are the 800-pound gorillas of the industry; I basically lump these two together in my head. I evaluated Circle and not Travis because the later’s lowest-cost tier is $69/month, **well** out of my price range.

Circle has a more-reasonable $39/month low tier, which is still out of my price range, but might be a good next step up if my apps start making any real money. There’s also no quick setup flow for iOS projects, something that other CI services have, and something I’d like to have if I’m paying that higher cost. There’s some [great documentation](https://circleci.com/docs/2.0/testing-ios/) around building and deploying iOS apps, but it’s still very much a hands-on process.

### Microsoft App Center
Microsoft’s [Visual Studio App Center](https://appcenter.ms) is a recently-released upgrade of [HockeyApp](https://www.hockeyapp.net), and is intended to be a full-service set of tools for mobile developers. It includes not only CI, but also beta testing, analytics, crash reports, and more. It’s got easy setup for a bunch of different mobile app configurations, a good free tier, and a decent upgrade path (the next step up is only $40/month, still under buddybuild or Travis).

App Center looks like an amazing tool, and I’d really love to use it… but it’s missing a few key features. Foremost among these for my needs is support for arbitrary Git repositories. App Center only supports pulling from three places: [GitHub](https://github.com), [Bitbucket](https://bitbucket.org), and [Visual Studio Team Services](https://www.visualstudio.com/team-services/). I self-host all of my Git repositories, and even if I were to host elsewhere, it’d be on Gitlab.com, not any of those three. As such, I have to pass up on App Center for now, but I might look back at them in the near future.

### Bitrise
I really thought [Bitrise](https://www.bitrise.io) was going to be the service I ended up with. Their setup and interface seemed very similar to buddybuild’s, they supported everything I needed, and the cost was right. The initial setup experience with Bitrise was simple: add your repository, your workflow gets created, and your first build runs right away. It’s **after** that great first-run experience that things went off the rails.

After getting your first build running, the setup assistant offers to help set up deploying your built app (to TestFlight, Hockey, or similar). I followed this setup, downloaded a tool to upload my signing credentials, followed all the instructions… and ended up with a broken build. Nothing worked, the error messages weren’t particularly useful, and the helpful setup assistant had disappeared. Attempting to figure it out myself led me down a rat’s nest of poorly-documented and confusing workflow steps. I eventually just gave up.

I feel really bad about this one; it seems like a missed opportunity for something that could have been a good solution. 😢 

### BuildKite
I didn’t spend long evaluating [BuildKite](https://buildkite.com) (for reasons I’ll get into later), but I’m including it for completeness sake. It’s quite different from other services. BuildKite **only** provides the management part of your CI system; you provide the “agents” that actually run your builds. Pricing is a flat $15/month ($12/month if paying annually), and it seems to handle most of what I’d need easily. There’s no special setup for mobile apps, but it doesn’t look any more complicated than Circle or my final choice. This seems like a great solution for anyone willing to host their own agents.

## Alternatives Not Considered
There are a few other alternatives that were dismissed before I had a chance to really dig into them. I’m listing them here in case people are interested, but I’m not going to go into detail as to why there weren’t chosen:

- [Jenkins/Hudson](https://jenkins.io)
- [Xcode Server](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/xcode_guide-continuous_integration/adopt_continuous_integration.html)
- [Travis](https://travis-ci.com)
- [TeamCity](https://www.jetbrains.com/teamcity/)

## Chosen Solution
In the end, I chose to go with [GitLab CI](https://about.gitlab.com/gitlab-ci/). GitLab CI works very similarly to BuildKite: it merely coordinates a set of agents (“runners” in GitLab parlance), who are responsible for the actual building of the project. I’m already running a GitLab server to host my Git repositories, so using it for CI didn’t require any new installation or setup for my existing repositories. I installed the GitLab runner on a desktop machine I have at home, setup a build configuration, and let it run. 

I’ll likely go into more detail about my exact GitLab CI setup in a later post, but it’s a fairly straightforward one: 

- There are two build stages, `test` and `beta`.
- `test` does a debug build, runs all my unit tests. `beta` is run on all pushes to the repository.
- `beta` is only run on pushes to my master branch. It builds with the Release configuration, signs for the App Store, and uploads the build to iTunes Connect.
- Both build stages run a [Fastlane](https://fastlane.tools) script to handle all the gritty details of building and deploying, rather than attempting to deal with `xcodebuild` directly.

As I said above, GitLab CI is almost certainly **not** the right solution for your case. It’s the right solution for me, because *a)* it’s cheap, *b)* I was already running a GitLab server, and *c)* none of the other alternatives fit my needs quite as well. Please check out the other alternatives for yourself. App Center seems great if you’re hosted on GitHub, Circle is probably a good solution if you’ve got non-mobile platforms and an actual budget, Bitrise and BuildKite both have their own niches as well, and even the alternatives I tossed out entirely likely have their audiences. 

[^1]:	None of my side projects make enough to justify the lowest $71/month paid tier on buddybuild, no matter how awesome of a platform it is.

[^2]:	Specifically, self-hosted GitLab.

[^3]:	As a poor-man’s notification system. I have a Slack team with myself as the single user for this reason.