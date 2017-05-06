---
layout: post
title: ClojureScript & React Native
date: 2017-05-06
---
I've mentioned [a like of ClojureScript on this blog](http://pado.name/blog/2014/11/om/) before, but in the few years since writing that post, I've mostly worked with its older brother, Clojure. The kinds of projects I've done in the interim just didn't lend themselves to ClojureScript.

On the other hand, [React Native](https://facebook.github.io/react-native/) has been around for a few years, providing a different paradigm for building the views of first iOS, and now also Android apps. React Native is based on React, a similar framework for the web. While I'd played with [React](https://facebook.github.io/react/) on the web before, I'd never even really looked at React Native. I already know how to build mobile apps, and React Native didn't seem to provide much if you were already an experienced mobile dev.

Recently, however, both of these technologies caught my eye again. The [State of Clojure 2016](http://blog.cognitect.com/blog/2017/1/31/state-of-clojure-2016-results) post included an interesting tidbit; a significant portion (18%) of ClojureScript deploys were for React Native work. It was this post that led me to looking into combining the two—the idea of building major parts of an iOS app in ClojureScript appealed to me.

My initial impressions of ClojureScript + React Native (the community calls this combination CLJSRN) have been quite positive. Developing with live reloading and the ClojureScript REPL is a magical experience. The unidirectional flow and stateless paradigms make both debugging and refactoring feel much more natural.

That's not to say that absolutely everything is perfect, though. The integrations between ClojureScript tools and the JavaScript-based React Native tools are nascent, and don't always work as simply as I'd like. For example, every time I add a new image to the app, I have to restart three different processes in the right order before the app can reference that image.

I haven't completed any projects in CLJSRN yet, but I've built quite a few prototypes both for myself and my employer. Sadly, we don't have any other ClojureScript fans at the office (yet 😉), so making that sell isn't easy.

More information about combining ClojureScript and React Native can be found at http://cljsrn.org.