---
title: "How we came up with a way to use GitHub to write songs."
date: 2019-05-31 00:00:00 
permalink: /2019/05/how-we-came-up-with-way-to-use-github.html
thumbnail: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMvKx_63ZQKYGXgLDDonkm-6RHTvTpdt2Pt9HGss18xcpGXned6eWuuCFD4CIm0KSPT7dOXswwaOOyfsz7-E2dVSTCqS5Y26EABZ-SILzX-GGWujHNNwCJ-zfxhXrP7Fj_6yYT/s320/GitHub.png
excerpt: "How the open source band Lorenzo's Music came up with a concept to use GitHub as a way to write songs."
tags: ["github", "open source music", "linux", "blog"]
---

<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMvKx_63ZQKYGXgLDDonkm-6RHTvTpdt2Pt9HGss18xcpGXned6eWuuCFD4CIm0KSPT7dOXswwaOOyfsz7-E2dVSTCqS5Y26EABZ-SILzX-GGWujHNNwCJ-zfxhXrP7Fj_6yYT/s1600/GitHub.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img alt="Lorenzo's Music and GitHub Logo" border="0" data-original-height="1400" data-original-width="1400" height="320" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMvKx_63ZQKYGXgLDDonkm-6RHTvTpdt2Pt9HGss18xcpGXned6eWuuCFD4CIm0KSPT7dOXswwaOOyfsz7-E2dVSTCqS5Y26EABZ-SILzX-GGWujHNNwCJ-zfxhXrP7Fj_6yYT/s320/GitHub.png" title="Lorenzo's Music uses github to collaborate on music." width="320" /></a></div>
<br />
The idea to collaborate on songs and music online has always interested me. I've talked to people that say they've done it, but it was more of a track sharing concept. They would work on a track, share it with another person and they would add on top of it.<br />
<br />
That's when I first got the idea to use <a href="https://github.com/lorenzosmusic" target="_blank">GitHub</a> for that process.<br />
<br />
Recently I was talking on twitter to Jason from <a href="https://www.jupiterbroadcasting.com/show/choose/" target="_blank">The Choose Linux Podcast</a> about this concept and he had mentioned it on his show.<br />
<blockquote class="twitter-tweet">
<div dir="ltr" lang="en">
Check it out. <a href="https://twitter.com/killyourfm?ref_src=twsrc%5Etfw">@killyourfm</a> and the <a href="https://twitter.com/ChooseLinux?ref_src=twsrc%5Etfw">@ChooseLinux</a> podcast talk about how we figured out a way to use <a href="https://twitter.com/github?ref_src=twsrc%5Etfw">@github</a> for our songwriting collaboration. 😃 <a href="https://twitter.com/hashtag/opensource?src=hash&amp;ref_src=twsrc%5Etfw">#opensource</a> <a href="https://twitter.com/hashtag/music?src=hash&amp;ref_src=twsrc%5Etfw">#music</a> listen to the whole podcast here <a href="https://t.co/dNHXilQvTV">https://t.co/dNHXilQvTV</a> <a href="https://t.co/MgmVS9pd2V">pic.twitter.com/MgmVS9pd2V</a></div>
— Lorenzo's Music (@lorenzosmusic) <a href="https://twitter.com/lorenzosmusic/status/1133136362738110465?ref_src=twsrc%5Etfw">May 27, 2019</a></blockquote>
<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>I thought I would write down the concept of how we've been using GitHub for this just to see if anyone had any interest in it.<br />
<br />
There are two ways I've done this on <b>GitHub</b>. One is an easy version and the second is a more complex version.<br />
<br />
The first idea I tried was a similar kind of concept to sharing the song file but I exported all the individual tracks as "Stems" into a GitHub repository to use as individual tracks.<br />
<br />
<h2>
<b>
GitHub Music Collaboration (Easy Version)</b></h2>
To test out this idea, I set up a GitHub repository using a finished song for people to create remixes. <br />
<a href="https://github.com/lorenzosmusic/i-never-wanted-to-say-remix-stems">https://github.com/lorenzosmusic/i-never-wanted-to-say-remix-stems</a><br />
<br />
Here was the explanation for how it would work in this case.<br />
<div>
<br />
<h3>
<b>
GitHub Song Remix Instructions</b></h3>
<ol>
<li>Grab the audio stems to use in the stems folder.</li>
<li>Import them to the DAW (Digital Audio Workstation) of your choice like Protools, Cubase, Ardour, etc...</li>
<li>Remix the song in some awesome new way</li>
<li>Export the new remix you made</li>
<li>Send us the link to your new version at <a href="mailto:info@lorenzosmusic.com">info@lorenzosmusic.com</a></li>
<li>We email you back saying how much we like it.</li>
</ol>
<div>
Also, creating a <b>version tag for the GitHub Repository</b> turns the whole thing into a zip file people can download!</div>
</div>
<div>
<a href="https://github.com/lorenzosmusic/i-never-wanted-to-say-remix-stems/archive/v1.0.zip" target="_blank">i-never-wanted-to-say-remix-stems/archive/v1.0.zip</a></div>
<div>
<br /></div>
<h2>
<b>
GitHub Music Collaboration (Complex Version)</b></h2>
<div>
Because <a href="https://www.lorenzosmusic.com/2018/09/lorenzos-music-in-forbes-using-open.html">the whole band only uses open source software for writing and recording</a> I began to wonder if I could build out this concept even more? What if we had the ability for all of us to work on songs and build and change them in the original working file?&nbsp;</div>
<div>
<br /></div>
<div>
The end result: This would become the song we release.</div>
<h3>
<b>
GitHub Song Writing process</b></h3>
<div>
<ul>
<li>We are using the <a href="https://ardour.org/" target="_blank">multitracking software Ardour</a> to record songs.</li>
<li>Add the Ardour song folder to GitHub as a new repository</li>
<li>Add the <a href="https://git-lfs.github.com/" target="_blank">Git Large File Storage (LFS)</a> extension to the repository (Sometimes the audio files are too large. This fixes that.)</li>
<li>Create a new branch every time you work on the song. (I add the date to the branch title so everyone knows what the current one is.)</li>
<li>When the song is done, make that branch the default branch.</li>
<li>Create a release tag</li>
<li>Share the repository for remixing!</li>
</ul>
<div>
This isn't perfect but it's worked for us so far. Plus, you can now work on this anywhere. And if your computer crashes you'll always have the working file.</div>
<div>
<br /></div>
<div>
<b>Here are a few notes on this method:</b></div>
<div>
<ul>
<li>Before starting always pull the latest updates!</li>
<li>Always push your latest changes!</li>
<li>We try and make sure we all have the same plugins. Otherwise, the mixes won't sound the same.</li>
<li>Creating a new branch each time takes a good amount of communication. Let everyone know when you do it so they can switch to the new one.</li>
<li>Branching keeps everyone from losing the version they are working on.</li>
</ul>
<div>
This is just a basic rundown of the concept.<br />
<br />
I share live videos while working on songs and editing on our <b>YouTube channel</b> from time to time. For updates on that subscribe to -&nbsp;<a href="https://www.youtube.com/lorenzosmusic?sub_confirmation=1" target="_blank">https://www.youtube.com/lorenzosmusic</a></div>
</div>
</div>
<div>
<br /></div>
<div>
<div>
<br /></div>
<div>
<br /></div>
<div>
<br /></div>
</div>
