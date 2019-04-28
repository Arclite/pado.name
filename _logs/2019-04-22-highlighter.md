---
layout: log
highlight: logs
date: 2019-04-22
app: "Black Highlighter"
title: "Mirror World Geometry"
---

In this session, I figured out how to take the data representation of the text rectangles that were detected last time and represent them visually. A number of issues made this more difficult than first anticipated, though.

First, the coordinates that `VNTextObservation` contains aren't pixel-based coordinates; they're percentages of the total image size. This is pretty easy to fix, we just multiply each point by the image size. However, it's also in a "flipped" coordinate system. Instead of the top-left origin point used by UIKit, these coordinates use a lower-left origin point. We have to appropriately translate vertical positions before converting them to pixel coordinates.

The other issue that I ran into is that the image view we display the image in scales the image down to fit on screen. However, the visualization view I created doesn't do the same scaling (yet). As such, the rectangles that the view draws to show detected text doesn't quite line up with the text in the image. I'll have to make the visualization view draw at the same scale as the image view if I want things to look right.

## Commits Made

- [Translate text observations to rectangles in image coordinates](https://git.pado.name/highlighter/app/commit/fd2255c266b1af922094f9241cb9f44afcd3185d)
- [Create visualization view to draw detected text](https://git.pado.name/highlighter/app/commit/2bf5cce386e736fba71f35725a3bfa8e3f1f3f2b)

## Tickets Closed

- [Detect areas where text is visible](https://git.pado.name/highlighter/app/issues/5)

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>8</dd>
    <dt>Days Since Start</dt>
    <dd>22</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>9</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>24</dd>
    <dt>Percent Complete</dt>
    <dd>27.2%</dd>
</dl>

## Replay

Coming soon.
