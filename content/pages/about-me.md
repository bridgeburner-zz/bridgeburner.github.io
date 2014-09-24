title: About Me
date: 2013-04-25 03:03
slug: about-me
author: vishwath mohan

<img style="float: right; margin: 20px 20px" src="{filename}../images/me.jpg" height=200px />

I'm a PhD candidate at the University of Texas at Dallas, working with
my advisor [Dr. Kevin W. Hamlen](http://www.utdallas.edu/~hamlen) in the
field of computer security. My research focuses mostly on malware
obfuscation, malware detection and automated program rewriting. Some
of that research has been featured in the
[Economist](http://www.economist.com/node/21560839),
[New Scientist](http://www.newscientist.com/article/mg21528785.600-frankenstein-virus-creates-malware-by-pilfering-code.html),
[Wired](http://www.wired.co.uk/news/archive/2012-08/21/frankenstein-virus)
and
[NBC News](http://www.nbcnews.com/technology/technolog/frankenstein-virus-could-assemble-itself-app-snippets-959004). I'm
also interested in artificial intelligence, philosophy, neuroscience,
and procrastinating (usually by playing on the guitar). You'll find a
smattering of these and other topics on my [blog here](/index.html).

A list of some projects I've been working on and their associated
publications are listed below.


### Projects

1. **Frankenstein** is a system that stitches together malware from benign
   binaries. Given a high-level description of what the malware should
   do, Frankenstein looks for semantically useful sequences of code
   (adding two values, moving a value from one location to another,
   etc) in the programs on a host system and finds combinations of
   these sequences that when executed, implement the malware
   description. It synthesizes a new binary for every combination it
   finds, creating malware mutants that are composed entirely of bytes
   from benign programs-making them much harder to detect using
   standard feature-based detectors.

3. **Stir** is an automated program rewriting tool that prevents
   ROP-attacks by self-randomizing all basic blocks within the program
   at run-time, on each invocation, without source code or debug
   information. If you don't know where the gadgets are, you can't use
   them.

4. **Reins** is also an automated rewriter that requires no source code or
   debug symbols, that can secure an untrusted program by enforcing
   (custom) security policies. Want to make sure Outlook can't attach
   any files from your c:\SuperSecretWork\ directory? Reins can
   rewrite it to do that. Or maybe you want to allow such an
   attachment to be sent only once a day, and only if the recipient
   happens to be you? Reins can do that too!

2. **Macgyver** is a malware propagation mechanism that works by
   generating transformation functions that can take a benign file
   (like Notepad) as input and produce the malware you want as
   output. The transformation function consists of simple mathematical
   operations and contains nothing that can be flagged as
   malicious. Its a kind of encryption, except you transmit the
   (harmless looking) encryption function, and the key happens to be a
   benign file on the target system.

*Note: Unfortunately many (read all) of these projects are either
on-going efforts, or are being expanded into better (meaner?) versions
of themselves. As a result I don't have any source code, or binaries
(but really you shouldn't be downloading any binaries from me :) ) to
share at the moment. This may change in the not-too-distant future
though.*


### Publications

1. [Securing Untrusted Code via Compiler-Agnostic Binary Rewriting.]({filename}../assets/reins_acsac.pdf)
   In Proceedings of the 28th Annual Computer Security Applications
   Conference (ACSAC), December 2012. Richard Wartell, Vishwath Mohan,
   Kevin W. Hamlen, and Zhiqiang Lin. *Awarded best student paper*

2. [Binary Stirring: Self-randomizing Instruction Addresses of Legacy x86 Binary Code.]({filename}../assets/stir_ccs.pdf)
   In Proceedings of the 19th ACM Conference on Computer and
   Communications Security (CCS), October 2012. Richard Wartell,
   Vishwath Mohan, Kevin W. Hamlen, and Zhiqiang Lin. *NYU Poly AT&T
   Best Applied Security Paper 2012 Runners-up*

3. [Frankenstein: Stitching Malware from Benign Binaries.]({filename}../assets/frankenstein_woot.pdf)
   In Proceedings of the 6th USENIX Workshop on Offensive Technologies
   (WOOT), August 2012. Vishwath Mohan and Kevin W. Hamlen.

4. [Reining In Windows API Abuses with In-lined Reference Monitors.]({filename}../assets/reins_tech_report.pdf)
   Technical Report UTDCS-18-10, Computer Science Department, The
   University of Texas at Dallas, Richardson, Texas, June 2010. Kevin
   W. Hamlen, Vishwath Mohan, and Richard Wartell.

5. [Exploiting an Antivirus Interface.]({filename}../assets/av_interface.pdf)
   Computer Standards & Interfaces Journal, 31(6):1182-1189,
   April 2009. Kevin W. Hamlen, Vishwath Mohan, Mohammad M. Masud,
   Latifur Khan, and Bhavani Thuraisingham.


### About this blog
<s>I'm using Brandon Mathis' excellent
[Octopress](https://octopress.org) framework for the blog, with the
unaltered version of the
[Fabric](http://panks.me/blog/2013/01/new-octopress-theme-fabric/)
theme in lieu of Octopress's default. The blog is hosted on
[Github Pages](https://pages.github.com). If you're interested, you
can also read a slightly more in depth [explanation]({% post_url
2013-04-30-my-blog-setup %}) of my blog setup and why I chose it.</s>

*I've since switched over to using
 [Pelican](http://blog.getpelican.com/) - a static site generator
 written in Python that is just awesome.*
