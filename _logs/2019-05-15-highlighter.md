---
layout: log
highlight: logs
date: 2019-05-15
app: "Black Highlighter"
title: "Toolbars and Lightning: Manual Redactions"
---

After all of the excitement of the last few sessions, it's time to slow things down a bit. During this session, I added a different way to redact items in text: the manual highlighter. Unlike the "magic" highlighter which uses the Vision framework to detect text, the manual highlighter just draws brush strokes everywhere that's been selected.

Doing that feature was pretty easy; the tricky part was exposing a UI for it! First, I had to add a toolbar, which involved rewriting part of our `NavigationController` class to set custom navigation and toolbar classes. Inside these classes, I was able to set styling. Setting the toolbar to opaque was required to get it to stop covering the bottom part of the editing view. After creating the toolbar class, it was pretty easy to put a toolbar item in it—just text at that point. 

To get the toolbar button to have any effect, I needed to represent the current tool selection state. To do this, I created a new enum: `HighlighterTool`, with two cases: `magic` and `manual`. A property on `PhotoEditingView` let it know what tool was current. From there, it was easy to create two different versions of the `handleBrushStroke` method, based on the current tool. 

Lastly, the actual redaction. This was pretty easy: just pass the raw path in `init`, and return that from the `paths` property.

## Commits Made

- [Add toolbar with highlighter tool toggle button](https://git.pado.name/highlighter/app/commit/53ecedb6a63aea70f06d64d792b17726721faa38)
- [Toggle button for current highlighter tool](https://git.pado.name/highlighter/app/commit/81e7b2d52ebae99dc96a5f52de396ba8bb5e2b9e)
- [Draw manual brush strokes](https://git.pado.name/highlighter/app/commit/3caee14e62247f36fa4972d5e5027e09209279ee)

## Tickets Closed

- [Add button to toggle redaction type](https://git.pado.name/highlighter/app/issues/8)
- [Redact manual strokes](https://git.pado.name/highlighter/app/issues/9)

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>18</dd>
    <dt>Days Since Start</dt>
    <dd>45</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>25</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>13</dd>
    <dt>Percent Complete</dt>
    <dd>69.4%</dd>
</dl>

## Replay

{% include replay.html %}
