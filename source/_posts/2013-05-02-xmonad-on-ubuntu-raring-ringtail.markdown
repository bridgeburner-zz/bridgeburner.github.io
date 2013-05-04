---
layout: post
title: "Configuring XMonad on Ubuntu 13.04"
date: 2013-05-02 21:01
comments: true
categories: [xmonad, ubuntu, setup]
keywords: xmonad, ubuntu, raring ringtail
description: How to setup XMonad on Ubuntu 13.04 Raring Ringtail
---

I first tried [XMonad](http://xmonad.org/) about a year ago, and its
since become an indispensable part of my standard Linux setup. It's an
incredible productivity booster, especially on dual monitor setups,
making it infinitely easier to rapidly switch between multiple
windows. It makes me weep a little inside each time I have to boot
back into Windows' single, non-tiling, keybinding devoid workspace (on
a side note, I've used both
[DisplayFusion](http://www.displayfusion.com/) and
[UltraMon](http://www.realtimesoft.com/ultramon/) with some success
for a more keyboard focused experience, so it isn't all
bad. Still...)

<!-- more -->

Now, I either lie in the segment of Ubuntu users for whom XMonad does
not work out of the box, or the segment of Ubuntu users for whom
XMonad does not work out of the box *and* who need to head to the
interwebs to figure it out. Since I also end up (re-)installing Linux
on VM's, or my laptop, or the lab computer once every 4-5 months, and
forgetting the solutions I'd arrived at previously with astonishing
punctuality, this is a less than ideal scenario.

So in the interest of documenting this for my future self (and anyone
else who might find this useful) here are the steps to get XMonad to
work on your latest Ubuntu install -

##### 1. Install gnome-panel

```
$ sudo apt-get install gnome-panel
```
<br>
##### 2. Install XMonad

```
$ sudo apt-get install xmonad
```
<br>
##### 3. Create your xmonad.hs

   This one tripped me up for a while, but I realized I suffer from
   [this bug](https://bugs.launchpad.net/ubuntu/+source/xmonad/+bug/1059358)
   every time. I haven't figured out why, but the fix is pretty
   simple. Just, create a (possibly empty) xmonad.hs like so -

```
$ mkdir ~/.xmonad
$ touch ~/.xmonad/xmonad.hs
```
<br>
##### 4. Replace your default mod key

   I like replacing the mod key from its default of *Alt* to *Super*
   (the Windows key). If that makes sense to you, you might want to
   edit your xmonad.hs with the minimal -

```haskell Replace the default mod key
import XMonad
import XMonad.Config.Gnome

main = xmonad gnomeConfig
       { modMask = mod4Mask
       }
```
<br>
##### 5. Reload your xsession

   Log out of your current session and log back in using the 'Gnome
   with XMonad' option.


And there you go. Five incredibly simple steps to a vastly improved
dual monitor experience. Happy hacking!
