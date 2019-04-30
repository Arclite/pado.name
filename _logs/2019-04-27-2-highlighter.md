---
layout: log
highlight: logs
date: 2019-04-27 05:45:00 -0700
app: "Black Highlighter"
title: "Bug Bash: App Icon, Scroll Views, and Settings"
---

In this bug bash session, an immediate follow-up to [the previous session](/logs/2019-04-27-highlighter), I tried tackling three smaller tickets. However, I only succeeded with two.

The [first ticket](https://git.pado.name/highlighter/app/issues/38) was a simple addition of an app icon so App Store Connect would stop sending me automated e-mails about how my app didn't have an icon. Since I was just re-using the Black Highlighter 1.x icon, it was pretty easy to just drag over the old assets.

The [second ticket](https://git.pado.name/highlighter/app/issues/39) didn't go as smoothly as I'd hoped. In the immediately-prior session, I got a scroll view up and running that showed the editing view zoomed out. However, it's currently top-left-aligned, rather than properly centered. I thought this was going to be an easy fix, but it wasn't. After a couple of attempts, I threw it back on the backlog to tackle another day.

The [third ticket](https://git.pado.name/highlighter/app/issues/22) was more straightforward, but took longer than I expected. I wanted to add a settings pane to the app for users to find Black Highlighter's about page, other apps by me, the privacy policy, etc. I copied a lot of this from one of my other apps.

## Commits Made

- [Add app icon](https://git.pado.name/highlighter/app/commit/a4248f67c9b1e044146fa11eb34e67632296bdfc)
- [Display settings page when button is clicked](https://git.pado.name/highlighter/app/commit/5427dd89a915692a33058a09b2a43f5b062bcf5c)
- [Fix settings button accessibility label](https://git.pado.name/highlighter/app/commit/eefe8d4ca73e25af6862020c2216ca6bd99608b1)
- [Add content to settings page](https://git.pado.name/highlighter/app/commit/bd7f5e5b7e87f5053b306b38762809036f277007)
- [Add title and accessory to settings items](https://git.pado.name/highlighter/app/commit/87eea15128c30f96928d619d58d9441eef8b859e)
- [Add button for dismissing settings view controller](https://git.pado.name/highlighter/app/commit/8824cec6438f6e908ff537ff29bbe39d071eebe0)
- [Clean up settings view controller classes](https://git.pado.name/highlighter/app/commit/99faaa357df37f7f24e28025aac5320c3181fa0e)

## Tickets Closed

- [Add app icon](https://git.pado.name/highlighter/app/issues/38)
- [Settings pane](https://git.pado.name/highlighter/app/issues/22)

## Tickets Created

- [Add app icon](https://git.pado.name/highlighter/app/issues/38)

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>10</dd>
    <dt>Days Since Start</dt>
    <dd>27</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=closed&milestone_title=2.0">Issues Closed</a></dt>
    <dd>12</dd>
    <dt><a href="https://git.pado.name/highlighter/app/issues?scope=all&utf8=✓&state=opened&milestone_title=2.0">Issues Open</a></dt>
    <dd>23</dd>
    <dt>Percent Complete</dt>
    <dd>34.3%</dd>
</dl>

## Replay

{% include replay.html %}
