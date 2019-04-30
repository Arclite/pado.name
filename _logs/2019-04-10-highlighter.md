---
layout: log
highlight: logs
date: 2019-04-10
app: "Black Highlighter"
title: "Loading Thumbnails From the Photo Library"
---

In this session, I continued work on the photo picker from last session. Where that session left off, the app would display a set of squares for all of the images in the photo library. Now, the app loads a thumbnail of each photo and displays that in the cell instead. I also handle a potential pitfall when scrolling the photo picker; ensuring that the asset a cell currently represents matches the thumbnail before displaying it.

At the last minute, I decided to try cleaning up the design of the photo picker by tweaking the size of cells. Unfortunately, this didn't go as smoothly as hoped. First, the cell's image views drew outside the bounds of the cell, which was easily fixed. But ultimately, the design just didn't look very good. I'll have to go back to the drawing board on this one eventually.

## Commits Made

- [Display photos in photo picker](https://git.pado.name/highlighter/app/commit/e57f8e1e818138014966557e4be5160c0525489a)

## Tickets Closed

- [Show collection of photos](https://git.pado.name/highlighter/app/issues/2)

## Tickets Created

- [Improve design of photo picker](https://git.pado.name/highlighter/app/issues/36)

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>4</dd>
    <dt>Days Since Start</dt>
    <dd>10</dd>
    <dt>Issues Closed</dt>
    <dd>3</dd>
    <dt>Issues Open</dt>
    <dd>29</dd>
    <dt>Percent Complete</dt>
    <dd>9.4%</dd>
</dl>

## Replay

{% include replay.html video="WWKRpsOrf70" %}
