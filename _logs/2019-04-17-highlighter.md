---
layout: log
highlight: logs
date: 2019-04-17
app: "Black Highlighter"
title: "Vision, Operations, and Logging, Oh My!"
---

In this session, I started digging into the actual functionality of the app. In order to start hiding stretches of text, we have to start by detecting stretches of text. The first version of Black Highlighter used `CIDetector` and `CITextFeature` to locate text in screenshots. Since that release, though, Apple has added new frameworks for detecting things in images: the Vision framework.

I decided to wrap interacting with the Vision framework in an Operation subclass. This allows us to put all the work of detecting text rectangles in a single class and not requiring other classes to import the Vision framework. It'll also help with pushing the work to detect text off of the main thread and into the background. Creating a new Operation subclass is pretty straightforward, but requires a bit of boilerplate.

One other thing I tackled this session is logging. Some unexpected errors can occur during text detection, and I thought it would be important to log when those errors happen. I'm mostly using the system `os_log`, with just a thin wrapper to make it a bit easier to use from Swift.

## Commits Made

- [Clean up photo editing view controller classes](https://git.pado.name/highlighter/app/commit/28ae17a31d628596bccd7fbc62da94c43682f670)
- [Find and log text rectangles](https://git.pado.name/highlighter/app/commit/053682f97c727b15f9feb2ff312a2e7030787aa5)

## Tickets Closed

None.

## Tickets Created

None.

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>7</dd>
    <dt>Days Since Start</dt>
    <dd>17</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>8</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>25</dd>
    <dt>Percent Complete</dt>
    <dd>24.2%</dd>
</dl>

## Replay

{% include replay.html video="U0gJTrb3aZI" %}
