---
layout: log
highlight: logs
date: 2019-04-08
app: "Black Highlighter"
title: "Navigation, UICollectionView, and Size Classes"
---

In this session, I started building the photo picker for the app, where someone can choose which photo they want to edit. For now, we're just going to show all photos in a grid; eventually we'll want to provide some [additional browsing features](https://git.pado.name/highlighter/app/issues/34).

When the app has photo library access permission, it swaps out a child controller of its root view controller, providing a seamless transition between the "permission prompt" and "photo picker" states of the app without having to stuff both of those states in the same view controller class.

The picker itself is a collection view. In this session, I built up the full stack of items needed to display a collection view: the view itself, the data source, a cell class, and a layout. The custom layout determines which size the cells are when displayed; this is based on the collection view's trait collection to show differently-sized cells depending on how much space we have to display in.

## Commits Made

- [Display photo library picker with sample cells design](https://git.pado.name/highlighter/app/commit/c09a5ea0f03f2e21b1c41123b949a9248b673846)

## Tickets Closed

None.

## Tickets Created

- [Navigate albums in photo library](https://git.pado.name/highlighter/app/issues/34)

## Project Stats

<dl>
    <dt>Sessions Completed</dt>
    <dd>3</dd>
    <dt>Days Since Start</dt>
    <dd>8</dd>
    <dt>Issues Closed</dt>
    <dd>2</dd>
    <dt>Issues Open</dt>
    <dd>28</dd>
    <dt>Percent Complete</dt>
    <dd>7%</dd>
</dl>

## Replay

Coming soon.
