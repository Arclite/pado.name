---
layout: log
highlight: logs
date: 2019-05-25
app: "Black Highlighter"
title: "Bug Bash: Finishing Other Apps and New Picker Features"
slug: "22"
---

This session picked up where we left off at the [last weekend session](/streams/2019-05-18-highlighter.md), finishing the "other apps" list in the help section. When I last worked on it, I'd loaded the list of apps from the App Store lookup API and displayed the app name. However, trying to show the app icon led to a broken design; the app icon covered up the beginning of the app name! This was fixed by creating a new cell subclass that displayed an icon **and** a label, laying them out appropriately.

The next ticket on the chopping block was about fixing the layout of the photo picker. While I'd picked some item sizes that looked good on the few devices I was testing with, different devices and presentations (such as iPad split view) didn't look so great. Instead of sticking to a finite number of item sizes, I played with the iOS Photos app to determine a formula for figuring out an item size that looked good in most cases. Rather than trying to make sure that this worked out right on a bunch of different simulators, I wrote unit tests that prepared the layout and then make sure they fit the expected the results of the formula.

Next up, prompting the user for app reviews. I don't really love doing this, but Apple's new native dialog isn't so bad, and app reviews really do help. I tried to make it as unobtrusive as possible, showing the dialog directly after saving. I don't even try to ask for a review after the first save; the app will prompt for a review after the third, tenth, and thirtieth saves. However, this current method will stop trying to show reviews forever after those 30 saves. I [filed a ticket](https://git.pado.name/highlighter/app/issues/47) to fix this in the future, but it's probably not important to get finished for version 2.0.

Finally, I wrapped up by implementing support for dragging and dropping images into the photo picker to open an image that isn't necessarily in your photo library. This turned out to be way easier in theory than in practice, as the photo editor expected everything to be a `PHAsset` rather than a `UIImage`. I added a `UIImage` parameter to the photo editor, and this seems to work now. I suspect this area will need a refactor in the future.

## Commits Made

- [Add Carthage step to GitLab CI](https://git.pado.name/highlighter/app/commit/580641bc6b48f239e1bc01f31094bb3a0d9a8290)
- [Display app icons for other app entries](https://git.pado.name/highlighter/app/commit/503978317a1bb52c40e93dc693eb3b5e3bca374c)
- [Fix layout of photo album cells in photo picker](https://git.pado.name/highlighter/app/commit/4f38f4ae848b36f185bb5a0295164be18ebc8dcf)
- [Display app ratings prompt on save](https://git.pado.name/highlighter/app/commit/d53c20c36586cb02b3dffdb000b3d1034f2d0496)
- [Add drop support for photo picker](https://git.pado.name/highlighter/app/commit/c18bc945f3c7342d8fbdaa1ef11d5b0263c2badf)

## Tickets Closed

- [List other apps](https://git.pado.name/highlighter/app/issues/26)
- [Display icons for other apps](https://git.pado.name/highlighter/app/issues/45)
- [Style photo picker](https://git.pado.name/highlighter/app/issues/20)
- [Drag into photo picker](https://git.pado.name/highlighter/app/issues/15)

## Tickets Created

- [Drag into photo picker](https://git.pado.name/highlighter/app/issues/15)

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>22</dd>
    <dt>Days Since Start</dt>
    <dd>55</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>34</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>6</dd>
    <dt>Percent Complete</dt>
    <dd>85.0%</dd>
</dl>

## Replay

{% include replay.html %}