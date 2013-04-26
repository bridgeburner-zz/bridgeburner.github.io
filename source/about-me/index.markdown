---
layout: page
title: "About Me"
date: 2013-04-25 03:03
comments: true
sharing: true
footer: true
---

I'm a PhD candidate at the University of Texas at Dallas, working with
my advisor Dr. Kevin W. Hamlen in the field of computer security. My
research focuses mostly on malware obfuscation, malware detection and
automated program rewriting. Some of that research has been featured
in the Economist, New Scientist, Wired and NBC News. I'm also
interested in artificial intelligence, philosophy, neuroscience, and
procrastinating (usually by playing on the guitar).

A list of some projects I've been working on and their associated
publications are listed below. You can also find my (soon-to-be at
this point) [blog here]({{ root_url }}/index.html).


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

2. **Macgyver** is a mppalware propagation mechanism that works by
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

1. Securing Untrusted Code via Compiler-Agnostic Binary Rewriting. In
   Proceedings of the 28th Annual Computer Security Applications
   Conference (ACSAC), December 2012. Richard Wartell, Vishwath Mohan,
   Kevin W. Hamlen, and Zhiqiang Lin. *Awarded best student paper*

2. Binary Stirring: Self-randomizing Instruction Addresses of Legacy
   x86 Binary Code. In Proceedings of the 19th ACM Conference on
   Computer and Communications Security (CCS), October 2012. Richard
   Wartell, Vishwath Mohan, Kevin W. Hamlen, and Zhiqiang Lin. *NYU
   Poly AT&T Best Applied Security Paper 2012 Runners-up*

3. Frankenstein: Stitching Malware from Benign Binaries. In
   Proceedings of the 6th USENIX Workshop on Offensive Technologies
   (WOOT), August 2012. Vishwath Mohan and Kevin W. Hamlen.

4. Reining In Windows API Abuses with In-lined Reference
   Monitors. Technical Report UTDCS-18-10, Computer Science
   Department, The University of Texas at Dallas, Richardson, Texas,
   June 2010. Kevin W. Hamlen, Vishwath Mohan, and Richard Wartell.

5. Exploiting an Antivirus Interface. Computer Standards & Interfaces
   Journal, 31(6):1182-1189, April 2009. Kevin W. Hamlen, Vishwath
   Mohan, Mohammad M. Masud, Latifur Khan, and Bhavani Thuraisingham.
