---
layout: log
highlight: logs
date: 2019-04-13
app: "Black Highlighter"
title: "Bug Bash: Unit Testing with Photo Permissions"
slug: "5"
---

In this session, I tried out something new: a bug bash session. In this kind of session, I'll tackle as many smaller tickets as I can in a short period. The tickets that I've tagged for hitting in bug bashes can be seen [on GitLab](https://git.pado.name/highlighter/app/issues?label_name%5B%5D=Bug+Bash). I'm planning on doing these on a fairly regular basis, but I haven't decided what cadence yet. It'll probably either be every fifth session, or every weekend session (if I only stream every other weekend, these are effectively the same).

Two of the tickets I took on during this session had to do with different photo library permission states. Since it's not necessarily simple to get a device in these states, I wrote the first sets of unit tests for this app to tackle these. I extracted the photo library permission behaviors from the intro view controller into its own class, and was able to mock that class to provide different authorization statuses when running under test.

## Commits Made

- [Display alert when photo library permission is denied](https://git.pado.name/highlighter/app/commit/586ae6e4eda911001b2401c20debad8b8f909685)
- [Handle photo permissions restricted state](https://git.pado.name/highlighter/app/commit/aa52cef5211491180866daebe80fb708784a8a1c)
- [Add underline to prompt button](https://git.pado.name/highlighter/app/commit/e9777a93d364f01300599d46b1f880e290e0a358)
- [Automatically open photo picker on launch when authorized](https://git.pado.name/highlighter/app/commit/0bb7799caa267817e557a307c2d04a1a9efc959d)

## Tickets Closed

- [Handle failure states for permissions prompt](https://git.pado.name/highlighter/app/issues/31)
- [Figure out Dynamic Type for navigation titles](https://git.pado.name/highlighter/app/issues/33)
- [Add underline to prompt button](https://git.pado.name/highlighter/app/issues/32)
- [Automatically open photo picker when permission is authorized](https://git.pado.name/highlighter/app/issues/37)

## Tickets Created

- [Automatically open photo picker when permission is authorized](https://git.pado.name/highlighter/app/issues/37)

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>5</dd>
    <dt>Days Since Start</dt>
    <dd>13</dd>
    <dt>Issues Closed</dt>
    <dd>7</dd>
    <dt>Issues Open</dt>
    <dd>26</dd>
    <dt>Percent Complete</dt>
    <dd>21.2%</dd>
</dl>

## Replay

{% include replay.html video="qYvm9xq1SsQ" %}
