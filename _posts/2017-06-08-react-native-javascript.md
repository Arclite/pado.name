---
layout: post
title: React Native !== JavaScript
date: 2017-08-06
---
I've lately been working on a blog post for [my employer](https://l4digital.com) detailing the benefits and drawbacks of [React Native](https://facebook.github.io/react-native/) (found [here](https://l4digital.com/cross-compiled/)). One thing that keeps coming up in my discussions with co-workers is that [a major drawback to React Native is JavaScript](https://arielelkin.github.io/articles/why-im-not-a-react-native-developer.html#javascript). But that's **not** a drawback of React Native at all.

Don't get me wrong, I hate JavaScript just as much as the next person (unless the next person is my co-worker Rob. Hi, Rob! 👋). The reason JavaScript isn't a drawback of React Native is that _you don't have to write JavaScript to use React Native_. There are plenty of better languages out there that essentially use JavaScript as a virtual machine to run on, a la the JVM. You can use these languages to target React Native, and some have explicit support _for_ React Native.

## Languages
My favorite of these languages, which I've [mentioned on this blog before](http://pado.name/blog/2017/05/clojurescript-react-native/), is [ClojureScript](https://clojurescript.org). ClojureScript comes from the Lisp family of languages. As such, it's a highly functional language, and fits nicely with the reactive nature of React Native. Being able to use the full set of Clojure(Script) tooling in React Native development is a godsend. Popping open a REPL and being able to edit your code on the fly alongside React Native's hot reloading gives you a crazy fast development loop. You won't have time to get distracted and tab over to Hacker News while using ClojureScript.

Another such language is [Elm](http://elm-lang.org). Elm, like ClojureScript, is a functional language. It's not a Lisp, taking more inspiration from Haskell. Elm has a lot of nice features, including a complete lack of runtime exceptions and amazingly helpful compiler errors. Elm support for React Native is still in early stages, but the engineering team at [thoughtbot](https://robots.thoughtbot.com) have been doing some [pretty cool work](https://robots.thoughtbot.com/elm-native-ui-in-production) with it so far.

If you're looking for something more familiar to JavaScript developers, there's always [TypeScript](http://www.typescriptlang.org). TypeScript is basically just a strongly-typed compiled version of JavaScript. Most JavaScript code should just run in TypeScript, but you can annotate your code with type information and catch simple errors before they happen. TypeScript has a lot of community support and the best tools of any language on this list. [Visual Studio Code](https://code.visualstudio.com) by Microsoft has a lot of support for TypeScript, and many popular JavaScript libraries have type information for TypeScript available.

## Resources
Here are a few resources for getting started using React Native in each of the above languages:
* **ClojureScript**: [CLJSRN](http://cljsrn.org)
* **Elm**: [Elm Native UI](https://github.com/ohanhi/elm-native-ui)
* **TypeScript**: Microsoft's [React Native Starter](https://github.com/Microsoft/TypeScript-React-Native-Starter)