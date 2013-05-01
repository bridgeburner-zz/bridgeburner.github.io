---
layout: post
title: "My Blog Setup"
date: 2013-04-30 23:36
comments: true
categories: [ruby, octopress, blog]
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
  of use and design) was preferable.

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


### Octopress is awesome

I picked [Jekyll](https://github.com/mojombo/jekyll) initially, which
is more blog generator than blog engine. It takes a configuration
file, your posts and pages written in markdown and uses them to
generate (people also call it baking) an almost entirely static blog.

Eventually though, I settled with
[Octopress](http://octopress.org/)---an extra layer over Jeyll that
manages to add just enough to hit that sweet spot between features and
ease of use. It integrates easily with Twitter, Google Analytics and
other useful services, it also integrates with comment systems like
Disqus (which to be fair, Jekyll does too), and has options to easily
deploy to [Github Pages](http://pages.github.com/),
[Heroku](https://www.heroku.com/) or any rsync enabled hosting
service. I really like how well Octopress manages to cover every
single point in my checklist -

1. Octopress allows me to write my posts locally using my editor of
   choice (\**cough*\*Emacs\**cough*\*), and makes it trivial to save,
   generate and deploy the generated site.

2. Jekyll (and consequently Octopress) uses git to manage both the
   markdown source and the generated site, making it easy to work
   across mulitple machines and still keep things synchronized.

3. You can't get more secure than an entirely (almost) static
   site. Well, technically you could not have a site at all and be
   more secure. But practically, a baked blog is about as exploit free
   as you could get.

4. Assuming you have Git and Ruby installed on your machine already,
   you can have a blog up and running in literally a few minutes. The
   Octopress site does a great job of explaining how to [install and
   configure](http://octopress.org/docs/setup/) it to your liking.

   I switched my theme to
   [Fabric](http://panks.me/blog/2013/01/new-octopress-theme-fabric/)---which
   I'm using as is simply because of how much I love it---but it
   wasn't because of any shortcomings with the default theme, which
   looks just great.

5. The source for both Jekyll and Octopress is simple, well-written,
   and easy to read. It certainly doesn't hurt that they're both
   implemented in Ruby.


I'm currently hosting the blog on Github Pages, which seemed like a
good starting point. I don't have comments enabled at the moment,
which might seem like a controversial choice. I happened to read through
[Matt Gemmel's](http://mattgemmell.com/) excellent chronicling of his
decision to disable comments recently, (you can read his first post on it
[here](http://mattgemmell.com/2011/11/29/comments-off/), and the
bottom of that page contains links to his follow-ups) and agree more
or less with what he has to say.

As it stands I don't really expect a vast readership, but if you have
something to say about anything I post, I'd be glad for you to give me
a shout out on [Twitter](https://twitter.com/vishwath) or by
[mail](mailto:vishwath.mohan@gmail.com), both of which seem like more
natural mediums to carry out a discussion.
