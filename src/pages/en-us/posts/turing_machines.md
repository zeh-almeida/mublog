---
title: Turing Machines
description: The most basic definition of a computer
date: 2023-08-01
modified: 2023-08-01
tags: turing,machine,computer,definition,instruction,algorithm,tape,head,alphabet,general,purpose
---
# <i class="fa-solid fa-computer"></i> Turing Machines - The Most Basic Definition of a Computer

## <i class="fa-solid fa-triangle-exclamation"></i> Disclaimer

> Most of the things I've written are in free form. Of course, I researched and have my sources linked in the text as it goes but take my writing with a grain of salt: I am not a computer scientist nor a great researcher.
**When in doubt, always check the sources**. Thanks and on with the show!

## <i class="fa-solid fa-list-ul"></i> Index
- [First of all, who is Turing?](#first-of-all-who-is-turing)
- [What are those things?](#what-are-those-things)
    - [Algorithms](#algorithms)
    - [General-purpose Computing](#general-purpose-computing)
    - [Turing Machine](#turing-machine)
        - [What is the machine](#what-is-the-machine)
        - [The Alphabet](#the-alphabet)
        - [The Tape](#the-tape)
        - [The Head](#the-head)
- [Ok but why should I care?](#ok-but-why-should-i-care)
    - [Why does it matter?](#why-does-it-matter)
    - [Is this really important for a programmer?](#is-this-really-important-for-a-programmer)

___
## <i class="fa-solid fa-person-circle-question"></i> First of all, who is Turing?
> Our dead are never dead to us, until we have forgotten them. - [George Elliot](https://www.brainyquote.com/quotes/george_eliot_148896)

**Alan Mathison Turing** was a [British mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist](https://en.wikipedia.org/wiki/Alan_Turing).

He was one of the responsible for the creation and development of computer science because he defined the concepts of **algorithms** and the **general-purpose computer** with the **Turing Machine**.

Really, much of the modern society we live in is still based on things Turing thought of almost a century ago.

## <i class="fa-regular fa-circle-question"></i> What are those things?

### <i class="fa-solid fa-code-branch"></i> Algorithms

#### <i class="fa-solid fa-shuffle"></i> **[TL;DR](https://www.urbandictionary.com/define.php?term=tl%3Bdr)**

`Algorithms` are the definition, step-by-step, of how to solve a problem.

A good way to think about it is like a recipe: if you follow the steps correctly in the order they are presented using the same ingredients and measurements, you will get a repeatable result, every time.

#### <i class="fa-solid fa-scroll"></i> The long version

An `Algorithm` is a set of very specific instructions which must be followed in their entirety in order to solve a problem.

Such instructions may include conditions and even interact with other `Algorithms`, as long as they are defined in a way in which they are expected to have a final state, i.e., they will eventually stop, either successfully or not.

If you use `Facebook`, `TikTok`, `YouTube` or any other social media, you are probably aware of the existence of the `Recommendation Algorithms`. Those are proprietary sets of `algorithms` and can be considered part of the brain of those applications

I think the International Institute in Geneva has a better explanation I could ever give about `algorithms` [here](https://www.iig.ch/en-en/blog/computer-science/algorithm-computer-science-definition-and-understanding).

### <i class="fa-solid fa-server"></i> General-purpose Computing

In the past, computing was used as a way to perform calculations faster than a human could. However, those computers had very specific logic, meaning they could not be programmed to calculate things other than the one they were originally programmed for.

This limitation, as well as their gigantic size and complexity, made them very expensive, hard to use and maintain, as explained in the [history of the first general computer, ENIAC](https://penntoday.upenn.edu/news/worlds-first-general-purpose-computer-turns-75).

What this all meant was that you had to write very specific `algorithms` for very specific machines. You could not simply update your logic and re-run. You would probably have to re-align parts of the computer or even have to use a completely different machine, which could be impossible.

The idea to have the same computing machine be able to execute different `algorithms` without having to change it's overall structure is what we call `General-purpose computing` and as linked in the article above, ENIAC was the first machine that was capable of this feat.

### <i class="fa-solid fa-cash-register"></i> Turing Machine

It was clear at that point in history we needed general-purpose computers but how do we define one? Ah, that's where Alan Turing and his Machine come for the rescue!

Turing was able to define, in very simple terms, what a general-purpose machine is and how it operates. Of course, his definition is of an abstract machine, not a physical one.

This machine is capable of running any and all computer `algorithms`, as long as they follow the rule in which they have a finite state.

#### <i class="fa-solid fa-satellite"></i> What is the machine?

The `Turing Machine` is comprised of a few, shall we say, parts: the `Head`, the `Tape` and the `Alphabet`.

#### <i class="fa-solid fa-braille"></i> The Alphabet

In order for the machine to work, an `Alphabet` must be defined in which the machine takes an action based on a specific symbol.

This is analogous to what we call [`computer instructions`](https://pclt.sites.yale.edu/cpu-instructions) today.

#### <i class="fa-solid fa-tape"></i> The Tape

`The Tape` of the machine is analogous to what we call `memory` in today's computers.

In this abstract machine, it is a `infinite tape` divided into cells, all of the same size. Each cell may contain a symbol from the `Alphabet` or simply be empty.

#### <i class="fa-solid fa-thumbtack"></i> The Head

`The Head` of the machine is able to move between each and every cell of the `Tape`, in any direction but only once cell at a time.

Once the `head` enters a cell, it scans its content and based on the `Alphabet` definition it will move itself to another cell or write another symbol in the current cell.

This is analogous to how modern-day [CPUs work](https://en.wikipedia.org/wiki/Instruction_cycle).

## <i class="fa-regular fa-star"></i> Ok but why should I care?

As mentioned many times before in this article, pretty much all computers since the invention of the `Turing Machine` use this model.

Understanding this model could help you have a better time with any technology as well, since you will probably understand how to better "communicate" with the machines.

It doesn't matter if you have a Original IBM PC from 1980 or the newest fictional (for now) iPhone 99x Pro: they both have a CPU that is modeled after the `Turing Machine`.

And yes, even those "[cheapo](https://www.pinterest.com/pin/102105116538007472/)" games are `Turing Machines` in a way or another.

Let's list some of the objects which are also `Turing Machines`:

- Smart TVs
- Tablets
- Vehicles
- Any of those "_smart_" appliances

The list goes on and on...

### <i class="fa-solid fa-terminal"></i> Is this important for a programmer?

In a word? Yes. In another word? **absolutely**. The whole existence of a programmer is to create `Algorithms` for the `Turing Machines` to process.

> In  my opinion, nothing is more important in today's world than a well-defined, well-documented `algorithm`, regardless of it's application.

Even if you use programming languages such as `Python`, `Javascript`, `Java`, `C#`, `Rust` or `C/C++` the code will eventually turn into `assembly`, either directly by compilation such as `Rust` and `C/C++` or by interpretation such as the other examples.

Every computer architecture has it's own `assembly alphabet` and here are some of the architectures I can remember on the top of my head:

- [x86/x64](https://en.wikipedia.org/wiki/X86-64) - Pretty much every Windows computer, since ever. Granted, there is the whole `16`, `32` and `64-bit` eras but this is topic for another discussion.
- [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family) - Pretty much all appliances you have, such as TVs, Cellphones, etc.
- [MIPS](https://en.wikipedia.org/wiki/MIPS_architecture) - Ah the good old N64 and PlayStation...
- [RISC V](https://en.wikipedia.org/wiki/RISC-V) - New player, comparable to ARM chips but it is a different architecture.
- [POWER](https://en.wikipedia.org/wiki/IBM_POWER_architecture) - IBM architecture. used mainly in mainframes and other industrial applications.
- [6502](https://en.wikipedia.org/wiki/MOS_Technology_6502) - used in the Nintendo Entertainment System, Apple II and many others.

___