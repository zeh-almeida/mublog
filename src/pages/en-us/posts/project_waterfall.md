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
- [Get Your Engine Rollin'](#get-your-engine-rollin)
    - [Trying to Stay Above the Weather!](#trying-to-stay-above-the-weather)
- [Check Your Engine and Mind the Fuel](#check-your-engine-and-mind-the-fuel)
    - [Well, There's Your Problem!](#well-theres-your-problem)
- [You Have Arrived! Customs is at Your Left](#you-have-arrived-customs-is-at-your-left)
    - [You Haven't Declared This Item](#you-havent-declared-this-item)
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

While organizing the many `business rules` and their connections, it may be impossible to accommodate them all.

Imagine, if you will, that you need your first floor to have a certain amount of rooms and your `business rules` determined that rooms must have a specific size.

What would happen if there is physically no more space to fit all rooms according to the `rules`? Well, it means the `project is bust`.

Realistically, this problem _could_ and really, **should** have been caught during the `analysis` phase but sometimes the complexity and minute details of the `business requirements` take a little longer to creep up.

## [>](#index) <i class="fa-solid fa-gauge-high"></i> Get Your Engine Rollin'

> We know how to go, where to go so let's just go, then!

We **finally** got to the part where "things get done". Not that the other steps weren't "doing" anything: they were all **extremely** necessary but they didn't deliver anything that solved the `problem` in the first place. All they did was `prepare the terrain`, so to speak, for the `real solution to the problem`.

Let's list all the things we've gathered so far:
- `Requirements`: what needs to be done
- `Business Rules`: how it must be done
- `Solution Design`: how it should be organized

Things look good, we have a good understanding of the situation we are undertaking. What's left now is to really do it, that's why this phase is called `the Construction` or, in software projects, `the Coding`.

This phase is where things start taking shape: you start `cleaning the terrain`, `making sure it is leveled`, `getting your bricks, sand and concrete` all lined up in the yard, looks amazing.

`Business Rules` are being worked on by the crew `as designed` and `following the rules`, maybe we will keep this trip right on schedule, right?

**Right?**

### <i class="fa-solid fa-cloud-showers-water"></i> Trying to Stay Above the Weather!

> No matter how detailed and planned your trip plan was: Nature is a harsh mistress and is prone to mood swings.

`The Construction phase` is when the `requirements` and `business rules` take shape "in reality". Up until this points they were ideals, things that had real importance but were still ethereal.

Once they reach this phase, however, `the materialization from ethereal to real may not be perfect`.

Sure, your `design` was extremely clear and precise on the measurements but `someone ordered the wrong bricks` and now `things don't line up`.

What did you say? Oh, the faucet `should have been on the other wall`? Can't you just, I don't know, `invert` the room?

Things like this are so much more common than what we would like, I believe everyone has some kind of story about situations like this. Being unpredictable is the flavor of life, I suppose.

Going for the same song and dance, `things like this are unacceptable in Waterfall` and instantly means the project failed.

## [>](#index) <i class="fa-solid fa-temperature-quarter"></i> Check Your Engine and Mind the Fuel

> The trip is proceeding smoothly, just as it should. Don't let the engine get hot nor thirsty, we are almost at our destination!

Can you believe `things got done` already? Wow, so much work has been accomplished up until this point and yet, there is some more to be done: we are now entering the `validation phase` of our trip.

If the very very **VERY** careful and detailed planning made was followed and the `construction phase` went on without a hitch, it is time to make sure things were done correctly and to the letter. Since `waterfall` is not really about `feedbacks`, this step _should_ be just a formality, simply a way to demonstrate things are as they should be.

But life is a box of surprises and [Murphy's Law](https://en.wikipedia.org/wiki/Murphy%27s_law) tends to show up anytime.

### <i class="fa-solid fa-temperature-high"></i> Well, There's Your Problem!

Because we are dealing with the `Waterfall`, problems tend to accumulate until they burst. The `validation phase` is known for picking on `bad interpretation of requirements`, `incompatible business rules` or simply, a `bad construction job`.

Didn't we review things before moving to the next step? Surely those things were fixed before, right? Well, they should have been but not always. 

In the case of `civil construction`, some people have so much experience and knowledge about the processes that they become second nature and don't deviate. In things like software, for example, where every solution is different because it is tailored for specific problems, it is quite common to catch stragglers.

Of course, I should be very clear: this does not mean the team is incompetent or rogue actors. Building things is **HARD** and **complicated**, doesn't matter if it's a `calculator app` or a `multi-platform, cloud-ready, do-it-all operating system`.

Make sure any defect is well documented: it **MUST** include what was expected, what was experienced and why this is wrong. This will help the `root cause analysis` and improve the team's `response time` for fixing things.

## [>](#index) <i class="fa-solid fa-building-shield"></i> You Have Arrived! Customs is at Your Left

> Finally, we have reached your destination! Great vacation, very relaxing. Oh, let's not forget to go through Customs before going back, we brought so many souvenirs!

Finally, our trip is over, we conquered the `Waterfall`. However before we go home, we got to go through the Customs processes.

It goes like that in our example of `civil construction` as well: once all inspections are done and green lit, all that's left is to let the client in. Maybe it's their `dream house` or event their new `office space`, surely they want to use the space as soon as possible.

This means, of course, `moving`: `Setting up furniture`, `putting up the paintings and photos`, `wiring up the equipments`... Oh, the joy of moving in, right?

But hey, once this process is done you're free to use it as you like because things are **finally** done!

### <i class="fa-solid fa-handcuffs"></i> You Haven't Declared This Item

Unfortunately for some, not everything ends well sometimes.

Maybe you have a `standup desk` that is just to big to enter the room and can't be disassembled, or maybe your new bed doesn't fit the room because you bought it _after_ the measurements were taken.

Things like this happen and they may `kill the project`. If you cannot deliver the project, can ou say it's finished?

___
## [>](#index) <i class="fa-solid fa-person-digging"></i> Still Under Construction

Welp, you've reached this far already? Well, I haven't finished writing the whole article yet.

Probably sounds crazy to publish as-is but I want to gather feedback while I write.

Now that I think about it, it's very ironic to ask for feedback because I am writing about Waterfall, right? We will get to that, don't worry.

___