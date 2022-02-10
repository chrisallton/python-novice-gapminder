---
title: "Pair programming"
teaching: 10
exercises: 0
questions:
- "How can we use pair programming to learn and program better?"
objectives:
- "Pair up"
- "Establish logistics of working together as a pair"
keypoints:
- "Pair programming will improve productivity, understanding, and learning"
- "Both members of the pair must be engaged, and must switch roles regularly"
- "The co-pilot must keep a close watch for mistakes"
- "We will change pairings for the second assignment"
---

## Pair programming

As we discussed last week, Pair Programming (a variant of an older method
known as "Extreme Programming" (XP)) is a technique used in various contexts,
with the aim of

* Increasing productivity/decreasing amount of time to implement
a particular feature
* Reducing number of errors made in development
  * Reducing the time spend debugging
  * Reducing the chance of obtaining false results in production
* Increasing understanding and learning

At any one time, one person (the "Pilot" or "Driver") should have their hands
on a keyboard, making low-level technical decisions while the other (the
"Co-pilot" or  "Navigator") observes and makes higher-level strategic
decisions. It is important that the co-pilot carefully watches the code that
is being written, so as to spot mistakes as they are introduced.


## Pair up

Your allocated pairings were shown on the Canvas page. Find your
counterpart and set yourselves up on adjacent computers. Decide who is going
to act as the pilot first.


## Setting up

You will need to use git and GitLab to communicate your work between your two
computers. We also want git to be able to work with Jupyter notebooks
efficiently. The **pilot** should now:

* Set up a new repository on [GitLab](https://py-ph353.swan.ac.uk/)
* Clone it to your home directory
* Add the co-pilot as a Master
* Download the file [python-novice-gapminder-data.zip]({{page.root}}/files/python-novice-gapminder-data.zip)
and extract it to the new repository
* Add the new data folder to the staging area, commit it, and push to GitLab

{% comment %}
* Run the following two commands to enable git to be able to diff and merge 
Jupyter notebooks:

~~~
$ git-nbdiffdriver config --enable --global
$ git-nbmergedriver config --enable --global
~~~
{: .bash}
{% endcomment %}

The **co-pilot** should then:

* Clone the repository to your home directory
{% comment %}
* Run the above two commands to enable git to deal with Jupyter notebooks
{% endcomment %}

For the remainder of the session, the pilot should primarily have their eyes 
on the Juypter Notebook or Python program, while the co-pilot should have 
the tutorial open to work from.
