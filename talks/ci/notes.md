# Continuous Integration for iOS
## Introduction
- iOS Developer
- Work with Mark at L4 Digital
	- The company soon to be known as the company formerly known as L4 Digital
- Also have several apps in the store individually
### What is Continuous Integration?
- Ask about who already has a continuous integration setup
- Making sure your code is always in a state that is stable for development.
	- Other things such as continuous delivery and continuous deployment, those aren’t being discussed here.
- Automated building
- Systematic building
- Makes sure you always have the same build every time.
	- Given stable code, you should always be able to make the same build without having to mess around with your environment.
### Benefits
#### For Teams
- Make sure everyone can build
	- Nothing is locked on any person’s machine
	- Can continue to build even if you lose people
	- Signing!
- First-pass review
	- Linting
	- Tests
	- Block failing builds!
- QA/stakeholders get regular releases
- Give walkthrough of what we do for L4 releases
	- On merge request
		- Run the tests
		- Update status on GitLab
	- On master branch
		- Builds app three times
			- Signs app for App Store, Enterprise, and Ad-Hoc
			- Puts build artifacts on Dropbox
		- Generates documentation
		- Sends a Slack message to a set of stakeholders
#### For Individuals
- Automate release
	- Submission to iTunes Connect
	- TestFlight
- Give walkthrough of what I do for Scrawl Notes
	- Run Carthage
	- Run tests
	- Download signing credentials (cert, profiles)
	- Sets the build number
	- Builds the app for App Store
	- Uploads to iTunes Connect
## Concepts
### Pipeline
- A set of tasks you want run in order to accomplish a goal.
	- e.g., build app, run tests, deploy
- Multiple pipelines can be run per trigger, for composable sets of recurring tasks
	- Perhaps you always want to run tests, but only deploy `master`
### Runner
- The machine/process that is executing the pipelines.
	- This basically has to be a Mac for any Xcode work.
- For self-hosted solutions, usually involves installing some kind of software on your machine.
- Can be a physical machine or just a virtual one.
### Host
- The system that manages all of the continuous integration tasks that are available.
- Does not necessarily need to be a Mac (my GitLab CI host is a Linux server).
- Communicates with the outside world (Slack, SCM, etc.)
## Available Solutions
### On-Site
- Pros
	- Privacy/security (not uploading source to third party)
	- Cost (most on-site are free)
	- Avoiding lock-in
#### Xcode Server
- Built into Xcode.
- Can easily run on every Mac.
- Managed through Xcode
	- In app, under the reports area
- Limited
	- One machine per bot, can’t distribute across machines
	- Limited non-Xcode scripting
#### Jenkins
- Oracle
- Tons of integrations
	- So many integrations
- Works with basically everything
### GitLab CI
- Single-file setup
	- YAML defines pipelines, artifacts, etc.
- Pretty dependent on already being in the GitLab ecosystem
### Fastlane.ci
- Recently announced
- Not too much information yet
- Mobile-focused
### Hosted
- Pros
	- Less fiddling, more handled for you
	- Don’t have to use machines you might otherwise have use for
	- Easier to scale upward as needed
#### Buddybuild
- So good.
	- …that it was bought by Apple.
- No longer available. 😭
#### Circle
- One of the most well-known hosted setups.
- Good documentation, big community
- Handles everything
- Not much hand holding
#### Bitrise
- Powerful.
- Confusing.
#### AppCenter
- Microsoft owned.
- Very nice!
- Limited.
## Conclusion
- Link to information available
	- Recording(?)
	- Slides
	- Contact Information
	- Links to solutions