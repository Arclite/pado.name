---
layout: post
title: Detecting Pets with the iOS Vision Framework
date: 2019-07-19
excerpt: Apple’s WWDC has recently come and gone, leaving a trail of new technologies in its wake. With so many big announcements from Apple this year, it’s no surprise that some of the smaller features Apple announced went unnoticed for a while. One of these, however, Rover found and started working with shortly after the conference ended&#58; animal detectors.
---
*This post originally appeared on the [Rover Engineering blog](https://www.rover.com/blog/engineering/post/detecting-pets-with-the-ios-vision-framework/).*

It’s early summer here in Seattle, which means one thing for iOS developers: Apple’s WWDC has recently come and gone, leaving a trail of new technologies in its wake. This year brought a huge number of game-changing new things to play with: SwiftUI, Catalyst, Sign In with Apple, etc. With so many big announcements from Apple this year, it’s no surprise that some of the smaller features Apple announced went unnoticed for a while. One of these, however, Rover found and started working with shortly after the conference ended: animal detectors.

Animal detectors are a new addition to Apple’s Vision framework, which allows developers to enhance their apps by quickly detecting or recognizing certain objects in images. In past years, the Vision framework has allowed you to look for [rectangles](https://developer.apple.com/documentation/vision/vndetectrectanglesrequest), [faces](https://developer.apple.com/documentation/vision/vndetectfacerectanglesrequest), [text](https://developer.apple.com/documentation/vision/vndetecttextrectanglesrequest), etc. As of iOS 13, however, the Vision framework now includes a way to detect either cats or dogs in an arbitrary photo. The API returns a rectangle representing where an animal is located in a given image, a confidence level, and the type of animal it is: `"cat"` or `"dog"`.

<figure>
	<img src="/images/detected-doggo.jpg" alt="Dog lying down in a larger photo, with dog highlighted.">
	<figcaption>A sample result from the Vision framework</figcaption>
</figure>

This is cool and all, but what can we actually use this for in our app? Highlighting the location of a dog in a photo is an interesting tech demo, but it’s not really useful to any of our customers or sitters. After some brainstorming, though, we discovered there **is** a place where knowing the location of a pet in a photo was useful. In many places in the Rover iOS app, we show a picture of a pet cropped to a square or circle shape; a kind of “avatar” for that pet. However, it turns out that in the real world, pets don’t always sit still in the center of the frame when they’re having their picture taken. This leads to cases where we often show only part of the pet—or cut them out of the photo altogether!

<figure>
	<img src="/images/PetFocus.png" alt="A screenshot of an Apple event with the University of Missouri's Swift class called out.">
	<figcaption>Before and after results with <code>PetFocusedImageView</code>.</figcaption>
</figure>

Enter `PetFocusedImageView`: a drop-in replacement for `UIImageView` that centers the cropping of a photo on any and all cats or dogs that are detected in the image. Using `PetFocusedImageView`, we’re able to always show the best part of any photo: the one with a cat or dog in-frame.

`PetFocusedImageView` uses the new animal detector API to find all dogs and cats in a given image. If there aren’t any pets in the image (or the animal detector just doesn’t detect any), it falls back to a standard centering. It then combines all of the discovered areas together to get the entire area that contains any pets; we call this the “pet rectangle”. Combining all the discovered rectangles together handles cases where multiple pets are in an image—we wouldn’t want to leave anyone out! Next, the image view creates a “cropping rectangle” that’s the appropriate size to fit inside the original image, but has the same aspect ratio as the final image. This cropping rectangle is centered on the center of the pet rectangle from earlier, to make sure that the pet is in frame. If the cropping rectangle now sits outside of the bounds of the original image, we then shift the cropping rectangle until it’s entirely within the image bounds. While this means the pet isn’t perfectly centered within the final image, it’s as close to ideal as we can get without clipping the original image. Finally, we render the part of the original image inside the cropping rectangle, and set that render as the image view’s image.

`PetFocusedImageView` is open-source and [available on GitHub](https://github.com/roverdotcom/pet-focus). You can add it your project using CocoaPods, Carthage, or even the new Xcode support for Swift Package Manager. It can even be added to projects supporting as far back as iOS 10; when running on iOS versions older than iOS 13, it’ll behave as a normal `UIImageView`.
