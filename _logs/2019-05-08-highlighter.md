---
layout: log
highlight: logs
date: 2019-05-08
app: "Black Highlighter"
title: "Drawing Redactions For Real"
---

Finally, some actual black highlighting! In this session, the app got upgraded from the thin green lines of the last stream to the marker lines we want to be seeing.

Drawing the marker lines is a pretty simple, straightforward solution that nonetheless required a bit of finagling. The drawing effect is accomplished by taking a single image of a marker stroke and stamping it a bunch of times along the path that was created. This involves taking the original path and create a dashed line from it, so that there are a bunch of points where the brush image can be stamped.

The next step is a bit more involved and required dealing with the fun that is pointer manipulation in Swift. The goal is to take the dashed line path and run a function against each of its points. `CGPath` exposes a method, `apply`, that provides this functionality. However, using it requires working with two types of pointers: the typed path element pointer, and the raw "info" pointer, which is used to pass the function that will actually be applied.
    
Once these two parts exist, it's a matter of just calling them with our brush stamp image. Unfortunately, the image is drawn from its top left, and at only a single size. Some quick redrawing later, and the app is able to scale the brush image to whatever size is needed.

## Commits Made

- [Draw the correct black streaks instead of green lines](https://git.pado.name/highlighter/app/commit/d039c4f589bc4f22176cf972c3fca8698fe0373c)

## Tickets Closed

- [Redact text rectangles](https://git.pado.name/highlighter/app/issues/7)

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>15</dd>
    <dt>Days Since Start</dt>
    <dd>38</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>16</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>19</dd>
    <dt>Percent Complete</dt>
    <dd>45.7%</dd>
</dl>

## Replay

{% include replay.html %}
