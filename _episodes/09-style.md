---
title: "Programming Style"
teaching: 15
exercises: 15
questions:
- "How can I make my programs more readable?"
- "How do most programmers format their code?"
- "How can programs check their own operation?"
objectives:
- "Provide sound justifications for basic rules of coding style."
- "Refactor one-page programs to make them more readable and justify the changes."
- "Use Python community coding standards (PEP-8)."
keypoints:
- "Follow standard Python style in your code."
- "Use docstrings to provide online help."
---
## Follow standard Python style in your code.

*   [PEP8](https://www.python.org/dev/peps/pep-0008):
    a style guide for Python that discusses topics such as how you should name variables,
    how you should use indentation in your code,
    how you should structure your `import` statements,
    etc.
    Adhering to PEP8 makes it easier for other Python developers to read and understand your code,
    and to understand what their contributions should look like.
    The [PEP8 application and Python library](https://pypi.python.org/pypi/pep8)
    can check your code for compliance with PEP8.

## Use assertions to check for internal errors.
The use of *assert* enables a helpful message to be displayed in the event that a runtime exception occurs triggered by a 
particular condition not being met. A classic 
example is an inadvertent division by zero, which could be caught by checking whether the denominator 
vanishes.  Introducing *assert*s can help debug complex code, and also  
make python scripts more portable. 

This illustrative example is taken from *Learning Scientific Programming with Python* by 
Christian Hill (see reading list on module Canvas page for further information). 

~~~
def cross_product(a,b):
    assert len(a) == len(b) == 3, 'Vectors a,b must be three-dimensional'
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]] 

cross_product([1,2,-1],[2,0,-1,3])    # Ooops...
~~~
{: .python}
~~~
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-8-cd8b29a450c3> in <module>()
----> 1 cross_product([1,2,-1],[2,0,-1,3])    # Ooops...

<ipython-input-7-7b7186ef1bd1> in cross_product(a, b)
      1 def cross_product(a,b):
----> 2     assert len(a) == len(b) == 3, 'Vectors a,b must be three-dimensional'
      3     return [a[1]*b[2] - a[2]*b[1],
      4             a[2]*b[0] - a[0]*b[2],
      5             a[0]*b[1] - a[1]*b[0]] 

AssertionError: Vectors a,b must be three-dimensional
~~~
{: .output}
~~~
cross_product([1,2,-1],[2,0,-1])    # That's better!
~~~
{: .python}
~~~
[-2, -1, -4]
~~~
{: .output}

## Use docstrings to provide online help.

*   If the first thing in a function is a character string
    that is not assigned to a variable,
    Python attaches it to the function as the online help.
*   Called a *docstring* (short for "documentation string").

~~~
def average(values):
    "Return average of values, or None if no values are supplied."

    if len(values) == 0:
        return None
    return sum(values) / len(values)

help(average)
~~~
{: .python}
~~~
Help on function average in module __main__:

average(values)
    Return average of values, or None if no values are supplied.
~~~
{: .output}

> ## Multiline Strings
>
> Often use *multiline strings* for documentation.
> These start and end with three quote characters (either single or double)
> and end with three matching characters.
>
> ~~~
> """This string spans
> multiple lines.
>
> Blank lines are allowed."""
> ~~~
> {: .python}
{: .callout}

> ## What Will Be Shown?
>
> Highlight the lines in the code below that will be available as online help.
> Are there lines that should be made available, but won't be?
> Will any lines produce a syntax error or a runtime error?
>
> ~~~
> "Find maximum edit distance between multiple sequences."
> # This finds the maximum distance between all sequences.
>
> def overall_max(sequences):
>     '''Determine overall maximum edit distance.'''
>
>     highest = 0
>     for left in sequences:
>         for right in sequences:
>             '''Avoid checking sequence against itself.'''
>             if left != right:
>                 this = edit_distance(left, right)
>                 highest = max(highest, this)
>
>     # Report.
>     return highest
> ~~~
> {: .python}
{: .challenge}

> ## Document This
>
> Turn the comment on the following function into a docstring
> and check that `help` displays it properly.
>
> ~~~
> def middle(a, b, c):
>     # Return the middle value of three.
>     # Assumes the values can actually be compared.
>     values = [a, b, c]
>     values.sort()
>     return values[1]
> ~~~
> {: .python}
{: .challenge}

> ## Clean Up This Code
>
> 1. Read this short program and try to predict what it does.
> 2. Run it: how accurate was your prediction?
> 3. Refactor the program to make it more readable.
>    Remember to run it after each change to ensure its behavior hasn't changed.
> 4. Compare your rewrite with your neighbor's.
>    What did you do the same?
>    What did you do differently, and why?
>
> ~~~
> import sys
> n = int(sys.argv[1])
> s = sys.argv[2]
> print(s)
> i = 0
> while i < n:
>     # print('at', j)
>     new = ''
>     for j in range(len(s)):
>         left = j-1
>         right = (j+1)%len(s)
>         if s[left]==s[right]: new += '-'
>         else: new += '*'
>     s=''.join(new)
>     print(s)
>     i += 1
> ~~~
> {: .python}
>
> > ## Solution
> >
> > Here's one solution.
> >
> > ~~~
> > def string_machine(input_string, iterations):
> >     """
> >     Takes input_string and generates a new string with -'s and *'s
> >     corresponding to characters that have identical adjacent characters
> >     or not, respectively.  Iterates through this procedure with the resultant
> >     strings for the supplied number of iterations.
> >     """
> >     print(input_string)
> >     old = input_string
> >     for i in range(iterations):
> >         new = ''
> >         # iterate through characters in previous string
> >         for j in range(len(s)):
> >             left = j-1
> >             right = (j+1)%len(s) # ensure right index wraps around
> >             if old[left]==old[right]:
> >                 new += '-'
> >             else:
> >                 new += '*'
> >         print(new)
> >         # store new string as old
> >         old = new
> >
> > string_machine('et cetera', 10)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}
