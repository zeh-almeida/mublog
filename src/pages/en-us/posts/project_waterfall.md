---
title: Project Lifecycle - The Waterfall
description: What is the Waterfall Model, also known as "Project Management 101"
date: 2023-08-10
modified: 2023-08-10
tags: project,management,agile,waterfall,requirement,business rule,analysis,problem,statement
---
# <i class="fa-solid fa-water"></i> Project Lifecycle - The Waterfall

## <i class="fa-solid fa-triangle-exclamation"></i> Disclaimer

> Most of the things I've written are in free form. Of course, I researched and have my sources linked in the text as it goes but take my writing with a grain of salt: I am not a computer scientist nor a great researcher.
**When in doubt, always check the sources**. Thanks and on with the show!

## <i class="fa-solid fa-list-ul"></i> Index

- [First Things First: What is a Project Lifecycle?](#first-things-first-what-is-a-project-lifecycle)
- [Navigating Through the Waterfall](#navigating-through-the-waterfall)
- [Having the Boat In the Water](#having-the-boat-in-the-water)
    - [Make Sure the Water is Deep Enough](#make-sure-the-water-is-deep-enough)
- [All the Fools Sailed Away](#all-the-fools-sailed-away)
    - [Rule of Thumb](#rule-of-thumb)
- [Navigate the Sea Charts](#navigate-the-sea-charts)
    - [Uncharted Territory](#uncharted-territory)
- [Still Under Construction](#still-under-construction)

___
## [>](#index) <i class="fa-solid fa-chart-line"></i> First Things First: What is a Project Lifecycle?

Let's say you got yourself a problem. Not that hard to imagine, is it?

Now, you're a bright person, so you want to take the necessary steps to make this problem, let's say, disappear.
Let's call this collection of steps a `project`, to make the example clearer.

Now that you have yourself a project, are you ready to solve the problem? Well, not really.
You first got to understand this problem, make sure you're not treating the symptoms but the disease itself.

Well, if you know how to do that, you wouldn't have a problem, right? That's what `project's lifecycles` are all about.

They are a `collection of steps, phases and operations you execute in order to have your project end with a good result`.

## [>](#index) <i class="fa-solid fa-clipboard-question"></i> Navigating Through the Waterfall

The Waterfall lifecycle is actually one of the oldest and probably the first method of lifecycle management for software projects, [according to Wikipedia](https://en.wikipedia.org/wiki/Waterfall_model).

It is called a `Waterfall` because it starts from the top and goes to the bottom, no chance of going back.

Of course, the results of the current phase should be validated and accepted by the team before going to the next phase.

## [>](#index) <i class="fa-solid fa-sailboat"></i> Having the Boat In the Water

> In order to reach the `Waterfall`, one must first procure a boat.

Everything starts with the `problem statement`:
 - What needs to be done
 - Why it needs to be done this way

This is regularly called `requirements` and, in my personal opinion `are the most common thing to get wrong in any project`.

`Requirements` are the things the project **MUST** accomplish, no questions asked: either the project fulfills the `requirements` or it fails. Therefore, it is imperative the `requirements` are clear. Otherwise you might as well require the software to [solve the halting problem](https://en.wikipedia.org/wiki/Halting_problem).

There is no limit for the number of `requirements`. Of course, the longer the list, the harder it will be to maintain and develop for.

> While this is very opinionated, I believe the success of the project lies in having a small but carefully selected `requirements`, separated in distinct phases.

### <i class="fa-solid fa-water-ladder"></i> Make Sure the Water is Deep Enough

The `requirement gathering stage` **must** result in a single yet very detailed artifact: The [`Requirement Document`](https://en.wikipedia.org/wiki/Product_requirements_document).

This document should be very clear and specific on `what the problem requires`, not `how the problem will be solved`. This question will be answered in following phases.

Let's say you have a very simple `requirement` of having a wall built. The `statement` could be as simple as saying something like:

 ```
 In order to have the rooms of the construction clearly defined, the rooms must be separated by walls.
 ```

 In this `statement` there is nothing like the dimension of the wall, the materials to use, whatever. The `statement` is very simple: it `tells in simple text what the problem is and what is expected to be done`.

## [>](#index) <i class="fa-solid fa-wind"></i> [All the Fools Sailed Away](https://open.spotify.com/track/0SYF0IKXsDZI0XR7TM2Kxr?si=f571b8fc704a4fe0 "Ronnie James Dio, The Man on the Silver Mountain")

> Now that ou have your boat on the water, where are you going?

Using your `problem statement`, you have your `whats` and `whys` so you have to figure out the `hows`.

This part of the lifecycle is called `Analysis` and it is really straight-forward.
You have to make sure:
 - All the `requirements` are clear
 - All the `requirements` are achievable
 - The `requirements` do not cancel one another
 - The `requirements` can be tested in a straight-forward manner

At this stage of the trip, it may become impossible to keep sailing because one of those statements could not be answered in a satisfying manner because the `Waterfall` process you have to work with the results of the previous step as if they were the absolute truth.

What this means is if you find your `requirements` are not up to standard only during the `analysis` phase, the project _should_ be over, at least in theory.

> And it **really** should stop there. There is no way your project will be successful if you are not confident in those four bullet points there.

Once each and every `requirement` is analyzed thoroughly, they must be extensively documented in order to guarantee they are built correctly.

No matter how many `requirements` are correct: if only one of them could not be successfully analyzed and/or documented, please stop the project - it is doomed to fail.

### <i class="fa-solid fa-thumbs-up"></i> Rule of Thumb

The result of having gone through all the `requirements` and making sure they are valid is a more technical approach to the `how` of the `problem statement`.

One or more `business rule` may exist for a `requirement`. Such rules answer the `how` of each `requirement`, which may come in many steps.

Going back to the [wall example](#make-sure-the-water-is-deep-enough), we can derive some `rules`:

```
- Walls must not leave any space between each other saved by doors and windows;
- Door and window positions must be given before the construction of the walls;
- Walls must allow electric cables, heating and water pipes to go through and be concealed;
- Walls must always follow all the proper guidelines and building rules established;
```

Ok, this gives a much clearer idea of `how` that `requirement` will be fulfilled, though my example is clearly not a real one, it is just used to illustrate the situation.

Now that we have both the `list of requirements we must achieve` and `how each and every requirement should be implemented` we can finally move ahead.

## [>](#index) <i class="fa-regular fa-compass"></i> Navigate the Sea Charts

> Alright: we got ourselves a boat on the water with the destination set, great! How do we navigate there?

After the `requirements` became `business rules` we now have our `whats`, `whys` and `hows`, so what is missing?

In simple terms, we need to know in which way our `business rules` will interact with each other. We have already established those `rules` are connected but they do not cross over each other, so we must find a way to make them live together,

That's when the `design phase` comes in. Sure, it does look like it arrived late at the party but it really didn't. In order for the `design` to complete it's goals, said goals **MUST** be unequivocally clear and we just only reached that stage with our `business rules`.

Keeping with our `civil engineering theme` in the examples, this phase would be analogous to the `architecture design`: You know the limitations of `walls` and `rooms` so you have to `design` the `project` in such a way as to optimize the usage according to the `business rules`.

### <i class="fa-solid fa-compass-drafting"></i> Uncharted Territory

> It is possible your map does not have a route for the destination you desire.

While organizing the many `business rules` and their connections, it may be impossible to accomodate them all.

Imagine, if you will, that you need your first floor to have a certain amount of rooms and your `business rules` determined that rooms must have a specific size.

What would happen if there is physically no more space to fit all rooms according to the `rules`? Well, it means the `project is bust`.

Realistically, this problem _could_ and really, **should** have been caught during the `analysis` phase but sometimes the complexity and minute details of the `business requirements` take a little longer to creep up.

___
## [>](#index) <i class="fa-solid fa-person-digging"></i> Still Under Construction

Welp, you've reached this far already? Well, I haven't finished writing the whole article yet.

Probably sounds crazy to publish as-is but I want to gather feedback while I write.

Now that I think about it, it's very ironic to ask for feedback because I am writing about Waterfall, right? We will get to that, don't worry.

___