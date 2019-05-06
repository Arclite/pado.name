---
layout: log
highlight: logs
date: 2019-04-29
app: "Black Highlighter"
title: "Character Boxes and Path Intersection"
---

We're getting closer and closer to a real app every day now. During this session, I built up the last of the pieces needed to start actually redacting text in images: detecting individual characters, and identifying which characters have been selected for redaction.

Detecting individual characters is an important part of providing an actually-useful experience. Only being able to redact whole text objects at a time means that you can't hide single words in a line of text, for example. Fortunately, the Vision framework already did the heavy lifting for us; we just needed to store and visualize that content.

Identifying which characters have been selected was a little trickier. We can't just check which text boxes are intersected by the path we draw. For one, a path is just a series of points; it's entirely possible for a line to contain points on either side of a text box without containing any point in the box itself. For another, the path object vailable to us is effectively zero width. We draw a much wider path to make it easier to select what you want. To accomplish the selection, we create a new path that encloses the shape of our drawn path, and then we find all the character boxes whose centers lie within that path. This isn't a **perfect** solution; it's possible to miss a character in a line because you didn't quite hit the center, but it's performant and quick to implement. I'll probably experiment with other solutions in future versions.

## Commits Made

- [Detect individual character observations](https://git.pado.name/highlighter/app/commit/19e1888250101b23cc587b1a01479cd36615b036)
- [Detect and visualize redacted character observations](https://git.pado.name/highlighter/app/commit/634ce038be6e254cfccf55d665a0275f11f59408)

## Tickets Closed

- [Detect subfeatures in text observations](https://git.pado.name/highlighter/app/issues/40)

## Tickets Created

- [Detect subfeatures in text observations](https://git.pado.name/highlighter/app/issues/40)

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>13</dd>
    <dt>Days Since Start</dt>
    <dd>31</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>15</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>20</dd>
    <dt>Percent Complete</dt>
    <dd>42.9%</dd>
</dl>

## Replay

{% include replay.html video="_cytr26zrpA" %}
