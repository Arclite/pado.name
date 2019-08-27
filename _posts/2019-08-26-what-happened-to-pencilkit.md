---
layout: post
title: What Happened to PencilKit?
date: 2019-08-26
excerpt: Apple's latest release notes ask developers to refrain from attempting to submit apps linking PencilKit to the App Store. What’s the story here? Why are developers asked not to submit apps linking PencilKit?
---

Between me making this post and actually telling anyone about it, Apple flipped the script on me again with the new iOS 13.1 release notes. Please see [this post](/blog/2019/08/seriously-what-is-happening-with-pencilkit/) for more details.

-----

> If your app links PencilKit, please refrain from attempting to submit it to the App Store until further notice. (53811027)

That’s the message included in the release notes for iOS beta 8, released last Wednesday[^1]. What’s the story here? Why are developers asked not to submit apps linking PencilKit?

Well, I’ve got a little bit of insight into this. Prior to this new beta release, I’d been trying to submit my app Black Highlighter for TestFlight testing for several weeks to no avail. Every time I’d upload a build[^2], it’d be immediately rejected, and I’d receive the following message by e-mail:

> Dear Developer,
>
> We identified one or more issues with a recent delivery for your app, "Black Highlighter" 19.4 (191). Please correct the following issues, then upload again.
>
> ITMS-90338: Non-public API usage - The app links to non-public libraries in Frameworks/Editing.framework/Editing: /System/Library/PrivateFrameworks/PencilKit.framework/PencilKit. If method names in your source code match the private Apple APIs listed above, altering your method names will help prevent this app from being flagged in future submissions. In addition, note that one or more of the above APIs may be located in a static library that was included with your app. If so, they must be removed. If you think this message was sent in error and that you have only used Apple-published APIs in accordance with the guidelines, send the app's Apple ID, along with detailed information about why you believe the above APIs were incorrectly flagged, to appreview@apple.com. For further information, visit the Technical Support Information at http://developer.apple.com/support/technical/

Well… that’s weird. PencilKit isn’t a private framework, Apple got on stage at WWDC and showed it off to everyone. They had several sessions! A lab! Surely I didn’t imagine all this! Clearly this is a case of mistaken identity! So I went ahead and e-mailed a plea to that App Review e-mail. I got an e-mail a few days later with a Radar number, then… radio silence for about two weeks. Eventually, I got another e-mail. I’m not going to risk upsetting Apple by including the actual text of the e-mail, but it essentially boiled down to “this is expected behavior, please use the public version of PencilKit”.

## Debugging

Okay, Apple says I’m using the private version of PencilKit. I don’t think I’ve done anything weird. I’ve just added it using the standard frameworks UI in Xcode. In fact, if I take a look at my project’s `pbxproj` file, it references the correct (non-private) path:

<script src="https://gist.github.com/Arclite/acf5576135fcebd8d6fdaeb6fbdc326f.js"></script>

So, everything’s fine with what I’m telling Xcode to build. Maybe there’s something wrong with the final product? There’s a tool built into macOS to check what libraries a given binary links: `otool`. Let’s use it to check on one of the builds I tried uploading to App Store Connect, using the path that Apple kept sending in their automated e-mails.

<script src="https://gist.github.com/Arclite/f8ee032de31807f0ce19fa071d96b85b.js"></script>

Sure enough, we’re linking against the `PrivateFrameworks` version of PencilKit. Something’s going wrong in between what we control and the final built product. Somewhere in the build process, the linker is choosing the wrong version of the framework, using the `PrivateFrameworks` version of PencilKit instead of the public version. But what is causing that incorrect path? It turns out that the answer is… PencilKit itself!

It turns out that Xcode doesn’t actually link against frameworks. Not directly, anyway. Xcode actually references stub libraries, in the form of `.tdb` files. Here’s the `.tdb` file for PencilKit[^3]:

<script src="https://gist.github.com/Arclite/d7562e1eb876c22411aa2aec064449d4.js"></script>

The culprit here is lines 9&ndash;13; the ones that reference the `PrivateFrameworks` path. These lines are telling the linker to link against the private version of PencilKit… if the deployment target is less than iOS 13.0. Which Black Highlighter is. So we’re out of luck, right? No way to use PencilKit without dropping support for iOS 12? 😭

## Fixing
**NOTE:** I did all this work fixing my app before Apple posted the new beta release notes. I don’t recommend duplicating this fix.

Let’s think this through. The deployment target is set to iOS 12. But deployment targets are set on a per… well, target… basis. Our PencilKit code technically isn't in the app project, it’s in a separate framework[^4]. Can we create yet another framework, containing **only** the PencilKit code, and set that framework’s deployment target to iOS 13?

<figure>
	<img src="/images/actually-no.jpg" alt="Well yes, but actually no.">
</figure>

Sure, we **can** make that framework. Actually using that framework is another story altogether. Trying to import the framework (which I called `Canvas`) in our app gives us an error: `Compiling for iOS 12.0, but module 'Canvas' has a minimum deployment target of iOS 13.0`.

So we can’t import the framework at compile time. Can we access the code in the framework at runtime? Searching for solutions to the issue, I stumbled across [this blog post describing how to create a plug-in system in Swift](https://blog.pendowski.com/plugin-architecture-in-swift-ish/)… by loading frameworks at runtime. I adapted the code in that post to my project, like so:

<script src="https://gist.github.com/Arclite/6a7d7daf0abc9c05d0b4dca546fae79a.js"></script>

And… boom! It builds, at least. Let’s check it with `otool`:

<script src="https://gist.github.com/Arclite/4038d9e7bb04563007499ffe96ca7825.js"></script>

Even App Store Connect is happy with this change. I’m not sure if it’d pass muster with an actual App Store release, or if Apple is planning on changing their checks to work around this, so now that Apple has officially recommended against doing this, I’m just hoping I can continue to test my app until they fix the root issue and allow people to link against PencilKit without having to jump through these hoops.

But hey, at least I’m not getting any more automated rejections. 😇

[^1]:	August 21st, 2019, for those of you in The Future™

[^2]:	Which happened on every merge to my release branch. See [My First 20 Minutes in an iOS Project](https://pado.name/blog/2019/03/my-first-20-minutes-in-an-ios-project/).

[^3]:	Which you can find yourself at **deep breath** Xcode.app/Contents/Developer/Platforms/ iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/System/ Library/Frameworks/PencilKit.framework/PencilKit.tbd.<br><br>Spaces added to break up that path because my blog apparently doesn't like lines that long.

[^4]:	This way, we can re-use the code in an action extension to bring parts of the Black Highlighter editing experience into other apps.
