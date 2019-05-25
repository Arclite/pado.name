---
layout: log
highlight: logs
date: 2019-04-27 04:30:00 -0700
app: "Black Highlighter"
title: "UIScrollView Lost Hours"
slug: "9"
---

This session is all about struggling with the weird behaviors of `UIScrollView` and Auto Layout. At the end of [the previous session](/logs/2019-04-22-highlighter), I had displayed the text observations, but they weren't scaled appropriately with the image that they were associated with. To make this work, I needed to put both the image view and the visualization view inside a scroll view, which would zoom out and display the whole image at a time.

This didn't go as easily as planned, though; while I was able to pretty quickly determine the scale which I needed to zoom the image to, setting the zoom scale didn't actually appear to be doing anything. Eventually, I discovered that I needed to implement the scroll view delegate method `viewForZooming(in:)`, which returns the editing view.

However, after implementing this, the view no longer scrolled. After some digging with the view debugger, I discovered that the editing view was completely zero-sized: 0 width, 0 height. After several attempts to fix that behavior, I remembered the obvious fix: the editing view needed `translatesAutoresizingMaskIntoConstraints` set to `false`.

That's the way developing apps is sometimes: bang your head against a seemingly-intractable problem for a long period of time, then realize it only requires a simple fix. 🤦‍♂️

## Commits Made

- [Zoom image view to correct scale to match observations](https://git.pado.name/highlighter/app/commit/3022739e0df14d2d6fabebf0e912eda3f5a58b6d)

## Tickets Closed

- [Display text rectangles](https://git.pado.name/highlighter/app/issues/6)

## Tickets Created

- [Center image in editing view](https://git.pado.name/highlighter/app/issues/39)

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>9</dd>
    <dt>Days Since Start</dt>
    <dd>27</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>10</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>24</dd>
    <dt>Percent Complete</dt>
    <dd>29.4%</dd>
</dl>

## Replay

{% include replay.html %}
