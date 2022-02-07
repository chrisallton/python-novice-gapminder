---
title: "Setup"
teaching: 10
exercises: 0
questions:
- "How can I get Python working on the VM machines?"
objectives:
- "Download the data we'll be testing with"
---

The Anaconda Python distribution is installed and available on the
Linux VM machines. 

To test it now,  you type

~~~
$ python
~~~
{: .bash}

then a Python interpreter will start, and report the correct version of
Python (3.7.1):

~~~
$ python
Python 3.7.1 |Anaconda, Inc.| (default, Dec  14 2018, 19:28:38)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~
{: .output}

Press Ctrl+D to exit for now.


## The sample data

The data we will be using is taken from the [gapminder][gapminder] dataset.
To obtain it, download and unzip the file
[python-novice-gapminder-data.zip]({{page.root}}/files/python-novice-gapminder-data.zip).
In order to follow the presented material, you should launch a Jupyter
notebook in the root directory. Change directory to the root of the gapminder
data, and then run

~~~
$ jupyter notebook
~~~
{: .bash}

We're now ready to start.

[gapminder]: http://gapminder.org
