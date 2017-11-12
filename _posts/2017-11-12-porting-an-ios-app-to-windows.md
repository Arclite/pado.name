---
layout: post
title: Porting an iOS app to Windows
date: 2017-11-12
---
Over the last two weekends, I ported my iOS app [Scrawl Notes](https://notes.scrawlapp.com) to Windows. Specifically, to the [Universal Windows Platform](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide), which encompasses Windows desktop, Windows Phone (RIP), Xbox, HoloLens, and more.

Scrawl Notes only runs on some of these (primarily Windows desktop), but I’m of the understanding that it’d be fairly easy to add support for the remaining platforms with minimal effort.

## Why?
So, why port Scrawl Notes to Windows? Honestly, the answer is mostly “why not?”. Scrawl Notes is a fairly simple app, and it already has a port for macOS, so a port for Windows seemed like a no-brainer. Also, there was [a contest](https://developer.microsoft.com/en-us/windows/projects/campaigns/windows-developer-day-sweepstakes), and I really wanted to win a Surface Studio. 😛

## Porting
Porting the basic functionality of Scrawl Notes was a fairly straightforward task, once I wrapped my head around the various differences between the platforms.

In iOS and macOS, I store notes in [NSUserDefaults](https://developer.apple.com/reference/foundation/nsuserdefaults). In Windows, the equivalent is [ApplicationData.LocalSettings](https://docs.microsoft.com/en-us/uwp/api/Windows.Storage.ApplicationData#Windows_Storage_ApplicationData_LocalSettings). Most of the functionality for note storage is almost line-by-line translations of each other from Swift to C#. The only real difference is the use of C# event handlers rather than Swift (well, Foundation) notifications.

The primary feature of Scrawl Notes for iOS is putting your notes in a widget. In Windows, I add it to the app’s Start tile. Like the widget, the Start tile has to be explicitly added by the user before it’s visible. Unlike on iOS, however, I can give the user a button to do so inside of the app. In theory, I could also bug them on each app launch until they do so, but I chose to just put it behind a button rather than get in their face.

Another difference is in how this information is presented on the lock screen. In iOS, the same widget is used for the lock screen, Notification Center, and 3D Touch on the home screen. With Start tiles, you don’t get that same benefit. However, you can provide “detailed information” that a user can choose to display on their lock screen. I’ve chosen to send the first bits of a user’s note (3 lines of 60 characters each) to the lock screen, allowing them to put their most-needed information front and center.

## Problems
I mentioned above that there’s an existing macOS version of Scrawl Notes, and that was part of the reason it made sense to create a Windows version. That said… the main reason there’s a macOS port was to enter notes on your desktop that you’ll want to peek at later on your phone, but I haven’t yet ported the syncing capabilities. Scrawl Notes’s syncing capabilities are based on iCloud, specifically the [iCloud Key-Value Store](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore). As such, getting it to play nicely with Windows isn’t a simple task. Scrawl Notes for iOS is already getting an overhaul of its syncing system to [CloudKit](https://developer.apple.com/icloud/cloudkit/) in order to support some new features (background updates, watchOS, merging, etc.), and I’m hoping that will make adding syncing to the Windows app easier.

## Next Steps
There’s a few features I want to add to the Windows version in the near future that take advantage of the unique aspects of the Windows platform. [Ink](https://docs.microsoft.com/en-us/windows/uwp/input-and-devices/pen-and-stylus-interactions) support sounds like a fun feature that isn’t particularly easy on iOS _or_ macOS, allowing you to hand-write your notes instead of typing them. I’d also like to look into adding [Cortana](https://developer.microsoft.com/en-us/cortana) support to bring the Windows version up to snuff with the Siri support in the iOS app.

Scrawl Notes for Windows is currently in certification before going to the Window Store, and I’ll update this page when it’s released.