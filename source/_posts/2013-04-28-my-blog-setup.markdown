---
layout: post
title: "My Blog Setup"
date: 2013-04-28 23:36
comments: true
categories: [ruby, octopress, blog]
published: false
---

I'm obsessive to a fault when it comes to researching the right tool
for a job. I could (and do) spend days sifting through article
after article comparing different languages, libraries, programming
paradigms, every little thing you could imagine every time I start a
new project. It's actually one of the reasons I have so many
incomplete projects on my hands.

### The Search

Naturally, picking a blog engine to use was no exception. I used a
small checklist of features for comparison as I looked around. Here
they are in no particular order -

* As a programmer I was looking for something that didn't deviate too
  far from a coding workflow (which is a fancy way of saying "me want
  emacs").

* As a security researcher I obviously prefered a solution that was as
  secure as possible.

* As a lazy person, I wanted something that would be both functional
  and aesthetically sensible out of the box (or with minimal setup).

* I didn't need an overwhelming set of features, so simplicity (both
  of use and design) was desirable.

* I wanted to be able to go under the hood to make my own
  customizations if I wanted to. But more than that, I wanted to be
  able to look at the source and really understand what was going
  on. This is obviously harder that larger the code base gets, and so
  is somewhat related to the previous point. It's also related to the
  next two points.

* If it catered to my irrational dislike and ignorance of PHP, then
  all the better (I really need to sit down and go beyond the hello
  world stuff with PHP at some point. Hopefully that point is very,
  very far away).

* If it catered to my irrational (it's not irrational really, I only
  say this out of a sense of fairness to the point above) love and
  appreciation of Python, Ruby, or Lisp then all the better.


### My choice (or why Octopress is awesome)

I ended up picking Jekyll initially, but eventually settled with
Octopress which is an extra layer over Jeyll that manages to add just
enough to hit that sweet spot between features and ease of use. Jekyll
(and consequently Octopress) is a blog generator more than blog
engine. It takes a configuration file, posts and pages written in
markdown, and converts them into a static set of pages with all your
content. This static content can then be served easily for cheap or
even for free using options like Github Pages or Heroku.
