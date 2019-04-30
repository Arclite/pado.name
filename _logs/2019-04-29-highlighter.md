---
layout: log
highlight: logs
date: 2019-04-29
app: "Black Highlighter"
title: "Brush Strokes with UIBezierPath"
---

Actual user interaction! In this session, I started drawing brush strokes based on touch feedback. This turned out to be significantly simpler than expected. I created a new view, which implemented all the touch-handling methods on `UIView`, to create and stroke a single `UIBezierPath` at a time.

With the extra time remaining, I built out part of the interface required to handle [actually redacting text](https://git.pado.name/highlighter/app/issues/7), by having the brush stroke view implement `UIControl` target-action behavior.

## Commits Made

- [Draw brush strokes in editing view](https://git.pado.name/highlighter/app/commit/18b17808069949693d9309f9fb0f55ac2cedd5c6)

## Tickets Closed

- [Draw brush strokes](https://git.pado.name/highlighter/app/issues/4)

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>12</dd>
    <dt>Days Since Start</dt>
    <dd>29</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>14</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>20</dd>
    <dt>Percent Complete</dt>
    <dd>41.2%</dd>
</dl>

## Replay

Coming soon.
