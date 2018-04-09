---
layout: post
title: Finding your iPhone with HomePod
date: 2018-04-09
---

On Friday night, I did something I’ve done hundreds of times before: misplaced my iPhone. Not in any concerning way; it was somewhere in my house, just… I didn’t know where. Almost as a joke, I decided to ask my HomePod: “Hey Siri, where’s my iPhone?” Of course, I got a disappointing answer: “Sorry, I can’t find phones here.”

Lame. The more I thought about it, the more this seemed like a killer feature. It’s something I use my Apple Watch for fairly frequently, and it’d be a great addition to the HomePod. So, like a good little developer, I did what little I could: I filed a Radar ([rdar://39257448](rdar://39257448)).

But wait… **is** that all I can do? HomePod has limited SiriKit support; can I build this feature myself?

Yes. Yes, I can:
<div class="video-wrapper"><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/a9PQZbwb7hc?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>

(For the impatient: go ahead and grab the source code [here](https://github.com/Arclite/Finder).)

How did I go about building this? First I had to determine if it was even possible.
1. Is there a suitable SiriKit intent for this purpose?
2. Can I trigger a Find my iPhone alert from a third-party API?

To answer the first question, I headed to Apple’s developer site for more information. It turns out the full extent of Apple’s documentation regarding SiriKit on HomePod is a [single news post](https://developer.apple.com/news/?id=10302017a), only a paragraph long. Fortunately, it still actually had the information I needed: HomePod supports two intent domains: [ Lists & Notes](https://developer.apple.com/documentation/sirikit/lists_and_notes), and [Messaging](https://developer.apple.com/documentation/sirikit/messaging). I’d implemented the Lists & Notes SiriKit intents before, for my app [Scrawl Notes](https://notes.scrawlapp.com). It didn’t seem like a great fit. But Messaging seemed promising; I could make each device connected to an iCloud account a different “contact”, and you’d “message” those contacts in order to play a sound on them.

On to the next question. This seemed less likely; Apple was unlikely to have a public API for Find my iPhone. Fortunately, it seems like there’s a community of people reverse-engineering the web APIs out there. I found open-source projects like [pyicloud](https://github.com/picklepete/pyicloud) and [find-my-iphone](https://github.com/matt-kruse/find-my-iphone) that had ways of interacting with iCloud, and specifically the Find my iPhone API. I downloaded and played with a few of them, enough to prove that, yes, it was totally possible to trigger an alert from third-party sources.

The rest of the build is pretty boring from there, so I’ll just give the high-level overview:

1. Build an app with no UI that just takes an Apple ID, password, and device name as environment variables. It only works when run from Xcode, but it proves that I can play an alert from an iOS app.
2. Use the code from the above with a Siri intent. Still requires being tethered to Xcode, and therefore doesn’t work from HomePod, but it proves that the messaging intent is going to fit.
3. Create a simple UI for getting the Apple ID and password. Store it in the keychain. This allows me to drop the Xcode tethering requirement and test it out from HomePod… and realize that Siri isn’t great at discerning the kinds of words that are in my device’s names.
4. Add support for finding the current device if you don’t specify a recipient at all. For example, using the request “Hey Siri, send a message using Finder”. This gets around trying to decipher what device a user wants from their request.
5. Implement a feature to save the device list as contacts for Siri purposes. This dramatically improves the support for finding which device a user wants to trigger an alert for, and allows me to bring back triggering **any** device, not just the current one.

So, that’s where we are now. There’s still some issues (using the app pops up a two-factor authentication dialog on every device you own), and the UI is still extremely barebones, but it works! I can now find my iPhone using only my voice, and I didn’t have to wait for Apple to do it.  
  
As linked above, the source for this project is [available on Github](https://github.com/Arclite/Finder). Issues and such are [available on my GitLab](https://git.pado.name/pado/Finder). I’m not going to even **try** to put this on the App Store, so this is the only way to get this functionality if you want it. If you’re brave (and lucky) enough to get this through App Review, please send me a copy. 🙂