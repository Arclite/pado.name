---
layout: post
title: Your App’s Other UI
date: 2016-12-15
---
Every iOS app has two user interfaces. These interfaces are equally important in delivering a quality product. Ignoring one for the sake of the other can lead to a horrible experience for many of your users. However, from tooling all the way through to testing, one of these interfaces is largely seen as second-class and mostly ignored.
 
The two interfaces every app has are a visible UI and an accessible UI. The visible UI is what is displayed on the screen, made up of visible elements such as icons, labels, and buttons. The accessible UI is made up of accessibility elements. Accessibility elements describe the interface of an app in a machine-readable way that iOS uses to provide standard accessibility features across all apps. Some of the important information an element provides are its label, hint, and traits.
 
* **Label:** a quick description of the element, such as a button's title.
* **Hint:** a description of what the element does in cases where it might not be obvious. For example, a table row with a phone number might explain that activating it will actually place the call.
* **Traits:** a set of values that describe how an element presents itself to the accessibility system. For example, text content is "static text", tappable links or table rows are "button", sliders are "adjustable", etc. Traits can be mixed and matched; there's no reason to pick just one.
 
Accessibility elements also provide hierarchy and connection to an app's visible UI through the use of containers and frames. For the most part, the standard iOS elements will handle this automatically, but some additional work may be needed in highly customized apps.
 
## Technologies
While anyone building apps for the iOS platform should strive to be familiar with a large range of Apple's accessibility technologies, there are a few that are more important to learn than others. These technologies are the ones that can be most affected by individual apps; while most accessibility technologies apply in a standard way across iOS, these three require input from the app the user is interacting with. An app that provides high-quality accessibility data will be more user-friendly than one that doesn't. Providing limited, incorrect, or badly-designed data can render an app entirely unusable.

### VoiceOver
VoiceOver provides screen reading and navigation for users who are unable to see the device screen. It uses a number of special gestures to navigate through an app’s accessible UI, reading element labels and hints. Other gestures control interaction with elements, such as activating a button, incrementing a slider, or dismissing a dialog.
 
### Switch Control
Switch Control allows users with physical and motor control issues to interact with iOS through means other than direct interaction with the device screen. Switch Control navigates sequentially or with a pointer through accessibility elements, and the user triggers an action, called a "switch", to choose their selection. A switch can be a physical switch or button (connected to a device over Bluetooth), or there are a number of software switches built into iOS.

Multiple switches can be configured to trigger different actions, helping a user to have their most-used actions available easily. You can see a demonstration of how powerful a Switch Control setup can be in [this YouTube video](https://m.youtube.com/watch?v=no12EfZUSQo&feature=youtu.be%20) , where a user uses Apple's Swift Playgrounds app to write code on iOS using only a small number of switches.
 
### Dynamic Type
Dynamic Type is a setting that changes the font size and weight in any app that supports it. This helps users with limited eyesight more easily read text content in an app by setting the font size to one that is easier for them (both larger and smaller), or by making otherwise-thin text bolder.
 
## Accessibility Inspector
With Xcode 8, Apple has dramatically improved the state of testing and debugging your app's accessible UI. Xcode 8 includes a completely redesigned version of an app called Accessibility Inspector. True to its name, Accessibility Inspector allows you to inspect all the important information about your app's accessible UI.
 
Accessibility Inspector works best with the iOS Simulator, not a physical device. The most powerful feature of Accessibility Inspector is an "inspection pointer" that allows you to highlight parts of your app's accessible interface and learn about the available information at that point. If you've ever used Chrome's DOM inspection tools, the inspection pointer will feel extremely familiar.
 
Another important feature of the new Accessibility Inspector is the Settings pane. This part of the app allows you to tweak accessibility settings in your app without having to back out to the home screen, open the Settings app, tweak your setting, and switch back. This is especially useful for checking how your app reflows at different Dynamic Type sizes.
 
## Common Pitfalls
### Text Reflow
When laying out text in an application, give it room to expand if necessary. Avoid trying to align multiple labels horizontally; space will start to become limited as font size increases. Don't limit text labels to a single line unless you're okay with it truncating in cases where the font size is larger than the app is designed for.

If an app is using fonts other than the iOS system font, it needs to specifically respond to content size changes by specifying the font size and weight that should be displayed. Special care should be used when using completely custom fonts; a font size that is perfectly legible with the system font may be unreadable with a highly stylized one.
 
### Unlabeled Buttons
If a button only has an icon in its visible UI, it's likely that it doesn't have a good label that can be read in the accessible UI. By default, any button that has only an icon and no title gets an accessibility label equal to the icon's asset name. If an app's icons are given development-friendly names, such as “icon_rooms”, this will be reflected in the accessible UI. Instead, replace them labels that reflect their usage (e.g. "conference rooms"). Accessibility labels can be set in code, or in their properties in Interface Builder. For good measure, these labels should be localizable strings, so that they are properly translated to languages other than the app's base development language.
 
In addition, custom-drawn buttons that have neither a title or icon get the supremely unhelpful name "button". Assigning an accessibility label is paramount in these cases to explain what a button is and does.
 
### Custom Controls
Many apps will implement custom controls that provide a unique experience to users in that app. It's important to make sure that that new control is equally usable via the accessible UI. Special attention should be paid to a control's traits (to ensure users are able to use it through the accessibility technology of their choice) and value (for controls that are editable by user action).
 
## Conclusion
If you'd like to learn more about improving your app's accessible UI, Apple has several links to help you. If you're mostly interested in taking a look at the available technologies from a user perspective, Apple's new [Accessibility portal](https://apple.com/accessibility) is the place to go. It has an overview of most of the technologies available on iOS (as well as macOS, watchOS, and tvOS), with quick summaries of how they're enabled and used.

---

This post originally appeared as [Two (Inter)faced](https://l4digital.com/ui/) on the [L4 Digital](https://l4digital.com) blog.