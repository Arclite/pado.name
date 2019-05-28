---
layout: log
highlight: logs
date: 2019-05-27
app: "Black Highlighter"
title: "Bug Bash: Finishing Other Apps and New Picker Features"
slug: "23"
---

This stream was all about the sparklies. An accidentally-appropriate demonstration of the major issue came right off the bat; the visualization view was always the size of the **image**, not the size of the screen. This led to a number of issues: sparks would shrink and be hard to see, performance was terrible on larger images, and some images were just too big and no sparks would appear at all. The first part of fixing this was to separate the visualization view from the rest of the editing view (renamed the "workspace" view).

After getting the visualization view displaying correctly all the time, it was time to work on the design of the sparks themselves. The first version we had from the Xcode template was… **fine**, but ultimately it looked like a bunch of floating spots more than actual sparks. A trip to Sketch created something that looked more like a tiny, glowing, plus symbol, and it looked significantly better in the actual app.

The next part was trying to get the sparkles to only appear where text was. This was… far harder than it should have been. Mostly because I did something stupid a while back and named the text observation's rectangle property "bounds" rather than "frame". I attempted to mask out the areas with text by creating a bunch of shape layers representing the observations, but because I set both the layer frame **and** its path to the same "frame" property, all of the positioning on these layers was effectively doubled (once for the layer position, and once for the path origin). Once this was fixed, getting the layout correct was fairly straightforward. 

## Commits Made

- [Move visualization view to not be a child of editing view](https://git.pado.name/highlighter/app/commit/16b2d2f3116c014289ba596e053f5439ff354073)
- [Update spark design](https://git.pado.name/highlighter/app/commit/f697c4545c4e60aa27017888d59ec2e0e99d1260)
- [Mask out sparks where text is detected](https://git.pado.name/highlighter/app/commit/47e1361ffa289092165145526fde2f930afd31ab)
- [Tweak sparks design](https://git.pado.name/highlighter/app/commit/08c8c199e593051286cb97a1e49e96186b0075de)

## Tickets Closed

None.

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>23</dd>
    <dt>Days Since Start</dt>
    <dd>57</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>34</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>6</dd>
    <dt>Percent Complete</dt>
    <dd>85.0%</dd>
</dl>

## Replay

{% include replay.html %}