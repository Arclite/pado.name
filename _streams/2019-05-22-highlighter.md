---
layout: log
highlight: logs
date: 2019-05-22
app: "Black Highlighter"
title: "Fun with SpriteKit Particle Emitters"
slug: "21"
---

This session started with a quick fix to the issue we left open last time: the undo and redo buttons wouldn't disable appropriately when their respective stack was empty. This turned out to be a simple timing issue; reloading the buttons after the undo action rather than when the redactions changed made everything work correctly.

The rest of this session was a bit more fun: playing with SpriteKit particle emitters. I've dreamed of putting  particle effects in an otherwise serious app for a long time, and needing a way to show where "magic" highlighting could be done seemed like as good a place as any.

First, I had to get a particle effect that I liked. Fortunately, Xcode has a neat particle effect editor that allows you to tweak all the settings live, and save your emitter node out to a file. I started with the "Fireflies" particle template and tweaked colors, lifespan, birthrate, etc. until I had something that looked good.

After having a particle effect I liked, it was time to put it in the app. I took the existing visualization view and made it a SpriteKit view. Then, I created a scene with a single child node (the particle emitter) and presented that scene from the visualization view, and boom! sparkles everywhere!

There's still a lot of things left to fix with the particle effects (mostly their scale on larger images), but seeing it in action already looks pretty cool. I'm excited to see how this looks when it's finally complete.

## Commits Made

- [Fix undo/redo button disabling](https://git.pado.name/highlighter/app/commit/b52928b76b679b4c7a36c510a3710760b3e7b849)

## Tickets Closed

- [Undo/redo support](https://git.pado.name/highlighter/app/issues/10)

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>20</dd>
    <dt>Days Since Start</dt>
    <dd>52</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>29</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>10</dd>
    <dt>Percent Complete</dt>
    <dd>74.4%</dd>
</dl>

## Replay

{% include replay.html %}
