---
title: Monte Carlo Integration
teaching: 15
exercises: 10
questions:
- "How do computers create random numbers?"
- "How can we use those to do integrals?"
- "What is the first assignment?"
objectives:
- "Create some pseudorandom numbers"
- "Understand good and bad random number generators"
keypoints:
- "The assignment is now available."
- "Some hints are shown above"
---


## Random numbers

See the screen for a short talk.

> ## Plot $$x_i$$ against $$x_{i-1}$$
> Use the linear congruential generator,
> $$x_i = (ax_{i-1} + b) \mod c$$,
> to recreate the plots shown in the slide deck,
> for:
> 
> * $$a=121, b=0, c=6133$$
> * $$a=135121, b=0, c=61331237$$
{: .challenge}

## Monte Carlo integration and assignment

See the screen for a short talk.

## Assignment topics

You will need to look up:

* How to loop over sequential numbers in a bash script. (Hint: `{}`)
* How to use the output of one command (e.g. a Python program) within another
  (e.g. `echo`). (Hint: backticks)
* How to generate a random vector, and how to calculate its magnitude.
  (I recommend using `numpy` for this.)

Everything else has been covered either last year or this year.
However, if anything is unclear and your pilot/co-pilot doesn't know either 
then please ask!


## A suggested workflow

* Decide on a feature to implement
* Prototype it in Jupyter
* Test it
* Transfer it to a raw Python program
* Test it
* Fix it if necessary
* Commit
* Push
* Move on to the next feature

Swap between pilot and co-pilot at regular intervals! I should see
commits from all members of your pair in `git log`.