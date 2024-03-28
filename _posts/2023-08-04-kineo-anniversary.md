---
layout: post
title: "Kineo's 15th Anniversary"
date: 2023-08-04
---

One of my personal apps hit a major milestone today: Kineo first launched on the App Store on this date 15 years ago. While it certainly didn’t spend all of that time under active development, it’s still shocking to me that it’s been around all that time. As such, I wanted to write a little bit about its history and the major changes an app like Kineo has seen in that time.

Kineo started as a joint project between me and designer [Oliver Wagner](https://twitter.com/olliewagner?lang=en). Originally called "Flipbook", we changed its name after a dispute with another developer of a similar app. We originally changed the name to Flickbook, and released it under that name. However, that wasn't enough of a change, and we went back to the drawing board after a formal cease and desist from the other developer. After a few rounds of back-and-forth, we decided on the name "Kineo", a shortening of “kineograph", the original name [given to flip books by their inventor](https://en.wikipedia.org/wiki/Flip_book). Evidence of these changes are still present in Kineo today; the bundle identifier for Kineo is still `com.flipbookapp.flickbook`.

The old-timey name wasn’t the only animation history reference in Kineo. Kineo’s original icon (which you can still use in the app today, via a toggle in the settings pane) was a man on a running horse. This image, also used in the App Store screenshots, is a reference to Eadweard Muybridge’s [*The Horse in Motion*](https://en.wikipedia.org/wiki/The_Horse_in_Motion), one of the earliest examples of sequenced photographs. This series of images is considered an important precursor to modern motion pictures.

<figure>
	<img src="/images/flickbook-ss1.jpg" alt="One of Kineo's original screenshots, displaying an animation of a running horse." style="width: 160px"/>
    <img src="/images/flickbook-ss2.jpg" alt="One of Kineo's original screenshots, displaying a list of animations." style="width: 160px"/>
	<img src="/images/flickbook-ss3.jpg" alt="One of Kineo's original screenshots, displaying a color picker." style="width: 160px"/>
	<figcaption>Kineo&apos;s original App Store screenshots</figcaption>
</figure>

Kineo was a surprise hit with the early App Store audience, and it became so much more popular than Oliver and I had expected. We’d worked on apps together before, but none of them had seen more than a few dozen purchases. Suddenly, Kineo was everywhere. Kineo was mentioned in all kinds of iPhone-centric websites, blogs, and podcasts. People were [posting clips of their animations to YouTube](https://www.youtube.com/watch?v=V1YijF_kd-Q), even though a “screen recording” in those days was literally recording your screen with a separate camera. Kineo even had a blink-and-you'll-miss-it cameo in one of Apple's famous "there's an app for that” ads.

<figure>
    <img src="/images/itchy.jpg" alt="A still from an Apple ad, showing Kineo's app icon." style="width: 100%"/>
	<figcaption>Kineo&apos;s icon appeared in an Apple television spot.</figcaption>
</figure>

Oliver and I continued working on Kineo for a few years, releasing several new updates with performance updates, new features, and bug fixes. However, around that time, both of us were finishing college, taking internships, and looking for our first jobs. As such, we weren’t able to spend as much time keeping up maintainenance, and the pipeline of new releases slowed down. The last major update of Kineo 1.x, released April 1st, 2010, added support for the soon-to-be-released iPad. The app continued to run fine, but fell behind in features (support for the Retina screens of the iPhone 4 being the worst offender), and was ultimately pulled from the App Store on July 5th, 2013.

Over the next several years, getting back to Kineo was something that was constantly at the back of my mind. The early years of working on it had been incredibly exciting, and I wanted to revisit a project that had been so much fun to work on. I made several attempts at recreating it, but building an app with the expectations of the modern App Store was a daunting task. The worst, of course, would be the drawing parts of the app. Slightly transparent single-width lines wouldn’t cut it any more. People would want different brushes and the ability to control line thickness and advanced effects. The thought of having to build all that from scratch prevented me from ever getting very far with a Kineo reboot.

At WWDC 2019, though, Apple announced [PencilKit](https://developer.apple.com/documentation/pencilkit). PencilKit is a framework that supports advanced drawing, with special focus on the Apple Pencil. This meant I could let Apple handle all of the drawing parts of Kineo, and I would be able to focus on everything else: user interface, sharing, modern features like iCloud syncing, etc. With the scariest part of a reboot out of the way, I finally had the motivation to actually tackle releasing a new version of Kineo.

I worked on it through the end of 2019 and into the early parts of 2020. Finally, the rebooted Kineo was released on April 1st, 2020: exactly ten years to the day after its last update. While it hasn’t made quite the splash with users it did in its heyday, I’m happy to be working on it again, and I’m quite excited about the future of it. I’d hoped to have something special to show off with this blog post, but it’s not **quite** ready yet. Keep an eye on the [@kineoapp](https://www.threads.net/@kineoapp) Threads account if you're interested in seeing what's in store.

As for the past: I’ve shared some of what remains of legacy Kineo above, in the form of old screenshots and YouTube videos. Two other bits remain, though. I’ve re-hosted the [original Kineo website](https://kineo.app/legacy/), so you can see what passed for app marketing in the early App Store. Some of the links are now broken, but the main page works exactly as it did in 2008. I've also [published the best source code](https://github.com/cocoatype/KineoLegacy/) that I was able to track down. It only seems to go as far as Kineo 1.2.1 (released February 3rd, 2010), and therefore doesn't have iPad support, but is otherwise a good demonstration of the original Kineo. It even builds and runs in modern Xcode!

It’s incredible to look back at how much the App Store has changed in the last 15 years, and how an app that’s existed for so long has changed along with it. I’m happy to have taken this app on that journey, and I hope I’m able to continue on that journey for another 15 years.
