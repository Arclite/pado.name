---
layout: log
highlight: logs
date: 2019-05-13
app: "Black Highlighter"
title: "Saving Photos to the Photo Library"
---

A fully working app at last! The app can now handle saving an edited photo to the photo library. This completes the full app workflow from asking for photo permissions, to selecting an image to edit, to actually editing the image, and finally saving the finished image.

Getting this final bit of basic functionality involved a little bit of cheating, however. Rather than rewrite our drawing code to draw just a single image, we create copies of our app's views, and use `UIView` snapshotting to capture an image of those views. This is done by creating a graphics context the size of our image, and using the method [`drawHierarchy(in:afterScreenUpdates:)`](https://developer.apple.com/documentation/uikit/uiview/1622589-drawhierarchy) to draw both our image view and redaction view (in that order!) into the graphics context. Then we grab an image from the graphics context, and that's the final product—drawn exactly like the view before.

Once we have the final, redacted image, we need a way to get it out of the app. Fortunately, there's an easy solution for this: `UIActivityViewController`. This class is the "share sheet" that's used throughout iOS. We simply create a new activity view controller, pass it our image, and it gives us a bunch of different options for what to do with it—including saving it to the photo library. It doesn't handle saving in place, and we may want a way to save with fewer steps involved than the share sheet, but this accomplishes our main goal for now.

To protect anyone using the app from accidentally throwing away all their work, tapping the "Done" button when there are unsaved changes now pops up an alert asking if you **really** want to exit. I'm not super happy with the wording on that alert, but that's [an issue for a bug bash stream](https://git.pado.name/highlighter/app/issues/21).

## Commits Made

- [Save edited photo in place](https://git.pado.name/highlighter/app/commit/6b8aa76a83854971fe26e69a45554b5994c09fdc)  
(this commit message is wrong; the photo is saved as a copy, not in place)

## Tickets Closed

- [Share photo](https://git.pado.name/highlighter/app/issues/14)
- [Save photo copy](https://git.pado.name/highlighter/app/issues/13)
- [Prompt for saving on exit](https://git.pado.name/highlighter/app/issues/11)

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>17</dd>
    <dt>Days Since Start</dt>
    <dd>43</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>23</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>13</dd>
    <dt>Percent Complete</dt>
    <dd>63.9%</dd>
</dl>

## Replay

{% include replay.html %}
