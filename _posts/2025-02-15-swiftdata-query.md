---
layout: post
title: "Separating Concerns in SwiftData Models, or: @Query Considered Harmful"
date: 2025-02-15
---

Over the year-and-change since its release, I've watched several developer friends abandon SwiftData in frustration, finding it buggy and unreliable. Meanwhile, I've found it to be a key part of my app's architecture, and I can't imagine going back. Am I just a 10x developer and everyone else needs to git gud? 🤔 No, of course not. But I think my experience, compared to others’, comes down to one key difference: I completely avoided using `@Query`, and everyone else should, too.

### Separation of Concerns

A long-standing principle of software design is "[separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)”: the idea that a given chunk of code, such as a Swift type, should only be **concern**ed with a single concept. If a type has to handle multiple responsibilties, it becomes fragile. For every change you make, you have to be sure that you aren’t interfering with any of the type's other responsibilities. Separating concerns (also known as "encapsulation”) gives code a smaller surface area, which makes it easier to understand, reuse, and test.

`@Query`'s core issue is that it takes this principle and chucks it right out the window. In case you're not familiar, `@Query` is a property wrapper that lets you directly access and monitor data stored with SwiftData as a computed property. You define the data you want (the actual "query" of `@Query`), add it to a SwiftUI view, and SwiftData handles fetching that data and keeping it up to date. In Apple's sample code and WWDC videos, this sounds super convenient! Underneath, though, there's a hidden issue. Your view now has two concerns: displaying your interface **and** managing your persistent storage.

### Not Just Academic

Okay, so it violates some ancient “best practice”. Who cares? Let’s check out a example where this actually helps. Say you’re building a task app. For the first version, you just provide a simple list for people to add items to:

```swift
@Model
class Task {
    var title: String
    var dueDate: Date
}

struct TasksList: View {
    @Query private var tasks: [Task]

    var body: some View {
        List(tasks) { task in
            Text(task.title)
        }
    }
}
```

You release it, and users quickly demand a way to categorize tasks. So you add a category property. Wanting to avoid a migration, you make it an optional value[^default_value]:

```swift
@Model
class Task {
    var title: String
    var dueDate: Date
    var category: String?
}

struct TasksList: View {
    @Query private var tasks: [Task]

    var body: some View {
        List(tasks) { task in
            Text(task.title)
            Text(task.category ?? "Uncategorized")
        }
    }
}
```

Ick. That optional handling doesn't look great, and you're going to have to do it everywhere you need to display a category. Decisions you made about how you **store** the data are affecting how you write your views. Let's try making it a computed property on `Task` instead.

```swift
@Model
class Task {
    var title: String
    var dueDate: Date
    var category: String?

    var displayCategory: String {
        category ?? "Uncategorized"
    }
}

struct TasksLists: View {
    @Query private var tasks: [Task]

    var body: some View {
        List(tasks) { task in
            Text(task.title)
            Text(task.displayCategory)
        }
    }
}
```

This is fine… for now. But as your app’s UI gets more complex, so too will your `Task` class. You'll have a bunch of computed properties and extensions, all of which you have to understand and keep track of. You'll be tempted to do things like filter on them… only to find that that crashes at runtime because `@Query` can't filter on computed properties. What should be a simple store of data is now a myriad of different things, just based on all the places it can be shown.

### So… What Now?

How can we clean this up? The answer is a term that you’ve likely heard before, and may even already use in SwiftUI: view models[^domain_model]. Create a new type that handles translating your data for display, and create it from the storage model.

```swift
struct TasksListViewModel {
    var title: String
    var category: String

    init(_ task: Task) {
        self.title = task.title
        self.category = task.category ?? "Uncategorized"
    }
}
```

Yeah, that’ll do it! And now we just need to get our list to display it!

```swift
struct TasksList: View {
    @Query private var tasks: [Task]
    @State private var taskViewModels: [TasksListViewModel]

    init() {
        let viewModels = _tasks.wrappedValue
            .map(TasksListViewModel.init)
        _taskViewModels = State(initialValue: viewModels)
    }

    var body: some View {
        List(taskViewModels) { task in
            Text(task.title)
            Text(task.category)
        }.onChange(of: tasks) {
            taskViewModels = tasks.map(.init)
        }
    }
}
```

Oh, jeez. We’re right back where we started with having a whole bunch of extra handling in all of our views, just to support how we save data.

So, what do we do instead? Step one: **Build your view around the view model.** It simplifies your views dramatically to take in the view model instead, and not worry about how we get the data:

```swift
struct TasksList: View {
    let taskViewModels: [TasksListViewModel]

    var body: some View {
        List(taskViewModels) { task in
            Text(task.title)
            Text(task.category)
        }
    }
}
```

Step two: **Have a dedicated type for managing storage.** This one varies a bit, depending on your exact needs. I recommend reading up on the [repository pattern](https://martinfowler.com/eaaCatalog/repository.html), which sounds fancy but is actually pretty simple. Here's an example one for our needs:

```swift
@MainActor
struct TasksRepository {
    private let modelContainer: ModelContainer
    init() {
        self.modelContainer = try! ModelContainer(
            for: Task.self
        )
    }

    var tasks: [TasksListViewModel] {
        do {
            return try modelContainer.mainContext
                .fetch(FetchDescriptor())
                .map(TasksListViewModel.init)
        } catch { return [] }
    }
}
```

### Other Benefits

Having a type for this gives you much more flexibility with your data access than `@Query` does. You can manage concurrency better (this type could be an actor instead of the example struct), you can pre-sort all your results instead of having to sort them in each view, you can provide functions with simple parameters to ease the creation of complex filters… the sky's the limit!

When you’re using your own types instead of `@Query`, you also gain a lot of simplicity in setting up your views for various circumstances. Building SwiftUI previews becomes easier, as you can either pass in your view models directly, or create stub versions of your manager that you can pass in instead of creating empty model contexts. You can swap in those stubs for unit or snapshot tests of your views, which makes those tests more stable. You can have a build flag that swaps out your storage manager for one with a bunch of example data that is known to cause a bug you're debugging, or example data you use to create App Store screenshots.

Heck, if after all this, you finally just decide you still hate SwiftData, you can even replace the whole thing with something else, and avoid having to rewrite all your views.

### Just Say No

`@Query` makes your views fragile. It makes your views inflexible. It ties your views permanently to SwiftData. It adds friction to every step of development. It looks shiny and convenient in WWDC slides, but that luster wears off quickly.

Using view models and a single type for managing SwiftData[^rest_api] avoids all that for a small upfront cost. It’s worth it.

### Footnotes

[^default_value]: Yes, you can use a default value. That’s still a migration, and it still runs into the issue of view decisions affecting how you structure your data model. Keep reading.

[^domain_model]: Personally, I prefer the generic term “domain model”, as you can use these standardized forms in business logic that isn’t just views. You can even use a domain model as an intermediate step between a storage model and a view model! But this post is long enough already.

[^rest_api]: In case you hadn’t picked up on it, there’s nothing **truly** SwiftData-specific about any of these problems or solutions. You should do the same thing with **any** data transfer, be that SwiftData, a SQL database, or a REST API. The problem of using data models in views is just as prevalent, just without the convenient property wrapper tempting you.
