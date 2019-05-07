---
layout: log
highlight: logs
date: 2019-05-06
app: "Black Highlighter"
title: "Drawing Redactions… Kinda"
---

Building on the excitement of last session, in this session, I started drawing lines through areas you select for redaction! Well… kinda. I draw thin green lines, not the real marker lines that users of the original Black Highlighter know and love.

To accomplish this required a lot of the base setup we'll need for the real deal, namely, creating structs to represent redactions, and generating paths to draw them. This involved one of the bigger chain of map/reduce calls I've ever written, and it somehow all worked in the end.

Oh, and I finally renamed `DetectedTextObservation` so I can stop fumbling its pronunciation.

## Commits Made

- [Generate paths where text is redacted.](https://git.pado.name/highlighter/app/commit/6ff8e9dad1a49d91841b5972653822d7495f5d13)

## Tickets Closed

None.

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>14</dd>
    <dt>Days Since Start</dt>
    <dd>36</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>15</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>20</dd>
    <dt>Percent Complete</dt>
    <dd>42.9%</dd>
</dl>

## Replay

{% include replay.html video="2d_D2Tp0s6I" %}
