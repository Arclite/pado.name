---
layout: post
title: Seriously, What is Happening with PencilKit?
date: 2019-08-27
excerpt: Apple "resolved" the PencilKit issue… by making it even harder to support it.
---

This is a direct continuation of [this post](/blog/2019/08/what-happened-to-pencilkit/). Please read it first.

Apple dropped a new beta of iOS/iPadOS 13.1 today, surprising developers who were still expecting 13.0 releases. Included in the release notes for this release was a "Resolved Issue" referencing my PencilKit problem:

>If your app links PencilKit, and its deployment target is iOS 13.1 or later, you can now submit it to the App Store. (53811027)

Uh… what? Apple is now saying that your app's deployment target has to be 13.1 to link PencilKit at all? Even if you cordon it off with `#available` checks? Will there be a public 13.0 at release? Will this mean that developers can't support **that** release, either?

I'm going to continue using my hack until I get rejected otherwise, but, yikes. This doesn't make me feel good about supporting this new framework in my apps…
