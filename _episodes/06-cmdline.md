---
title: Command-Line Programs
teaching: 15
exercises: 0
questions:
- "How can I write Python programs that will work like Unix command-line tools?"
objectives:
- "Use the values of command-line arguments in a program."
- "Handle flags and files separately in a command-line program."
- "Read data from standard input in a program so that it can be used in a pipeline."
keypoints:
- "The `sys` library connects a Python program to the system it is running on."
- "The list `sys.argv` contains the command-line arguments that a program was run with."
- "Avoid silent failures."
- "The pseudo-file `sys.stdin` connects to a program's standard input."
- "The pseudo-file `sys.stdout` connects to a program's standard output."
---

The Jupyter Notebook and other interactive tools are great for prototyping code and exploring data,
but sooner or later we will want to use our program in a pipeline
or run it in a shell script to process thousands of data files.
In order to do that,
we need to make our programs work like other Unix command-line tools.
For example,
we may want a program that reads a dataset
and prints the average GDP per country

> ## Switching to Shell Commands
>
> In this lesson we are switching from typing commands in a Python interpreter to typing
> commands in a shell terminal window (such as bash). When you see a `$` in front of a
> command that tells you to run that command in the shell rather than the Python interpreter.
{: .callout}

> ## emacs
> 
> `emacs` is a powerful text editor, usable both at the command-line and in a graphical
> mouse-driven interface. Unlike `nano`, it assists you significantly with preparing
> high-quality code; it automatically indents for you (use the `Tab` key for this)
> and highlights your code in colours depending on the meaning.
> It also is aware what language you are writing and adjuts accordingly.
{: .callout}

## Command-Line Arguments

Open a new file, `sys_version.py`, in emacs:

~~~
$ emacs sys_version.py
~~~
{: .bash}

~~~
import sys
print('version is', sys.version)
~~~
{: .python}

The first line imports a library called `sys`,
which is short for "system".
It defines values such as `sys.version`,
which describes which version of Python we are running.
We can run this script from the command line like this:

~~~
$ python sys_version.py
~~~
{: .bash}

~~~
3.5.2 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:53:06)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]
~~~
{: .output}

Create another file called `argv_list.py` and save the following text to it.

~~~
import sys
print('sys.argv is', sys.argv)
~~~
{: .python}

The strange name `argv` stands for "argument values".
Whenever Python runs a program,
it takes all of the values given on the command line
and puts them in the list `sys.argv`
so that the program can determine what they were.
If we run this program with no arguments:

~~~
$ python argv_list.py
~~~
{: .bash}

~~~
sys.argv is ['argv_list.py']
~~~
{: .output}

the only thing in the list is the full path to our script,
which is always `sys.argv[0]`.
If we run it with a few arguments, however:

~~~
$ python argv_list.py first second third
~~~
{: .bash}

~~~
sys.argv is ['argv_list.py', 'first', 'second', 'third']
~~~
{: .output}

then Python adds each of those arguments to that magic list.

With this in hand,
let's build a program, `per_country_means.py`
that always prints the per-country mean GDPs of a single data file.
The first step is to write a function that outlines our implementation,
and a placeholder for the function that does the actual work.
By convention this function is usually called `main`,
though we can call it whatever we want:

~~~
import sys
import pandas

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = pandas.read_csv(filename)
    for m in data.mean(axis=1):
        print(m)
~~~
{: .python}

This function gets the name of the script from `sys.argv[0]`,
because that's where it's always put,
and the name of the file to process from `sys.argv[1]`.
Here's a simple test:

~~~
$ python per_country_means.py data/gapminder_gdp_africa.csv
~~~
{: .bash}

There is no output because we have defined a function,
but haven't actually called it.
Let's add a call to `main`:

~~~
if __name__ == '__main__':
   main()
~~~
{: .python}

and run it again:

~~~
4426.02597317
3607.10052883
1155.39510738
...
810.383787908
1358.199409
635.858042292
~~~
{: .output}

> ## Running Versus Importing
>
> Running a Python script in bash is very similar to
> importing that file in Python.
> The biggest difference is that we don't expect anything
> to happen when we import a file,
> whereas when running a script, we expect to see some
> output printed to the console.
>
> In order for a Python script to work as expected
> when imported or when run as a script,
> we typically put the part of the script
> that produces output in the following if statement:
>
> ~~~
> if __name__ == '__main__':
>     main()  # Or whatever function produces output
> ~~~
> {: .python}
>
> When you import a Python file, `__name__` is the name
> of that file (e.g., when importing `readings.py`,
> `__name__` is `'readings'`). However, when running a
> script in bash, `__name__` is always set to `'__main__'`
> in that script so that you can determine if the file
> is being imported or run as a script.
>
> To clarify this point, create two python scripts, the first called `adder.py`:
>
> ~~~
> import sys
> 
> def doit():
>     i = 0
>     for m in range(int(sys.argv[1])):
>         i += 1
>         print(i)
> 
> if __name__ == '__main__':
>    doit()
> ~~~
> {: .python}
> 
> and the second `wrapper.py`
> 
> ~~~
> import adder
> adder.doit()
> ~~~
> {: .python}
> 
> You should then verify that, e.g.
>
> ~~~
> $ python adder.py 5
> ~~~
> {: .bash}
> 
> and
> 
> ~~~
> $ python wrapper.py 5
> ~~~
> {: .bash}
>
> yield identical outputs.
{: .callout}

> ## The Right Way to Do It
>
> If our programs can take complex parameters or multiple filenames,
> we shouldn't handle `sys.argv` directly.
> Instead,
> we should use Python's `argparse` library,
> which handles common cases in a systematic way,
> and also makes it easy for us to provide sensible error messages for our users.
> We will not cover this module in this lesson
> but you can go to Tshepang Lekhonkhobe's [Argparse tutorial](http://docs.python.org/dev/howto/argparse.html)
> that is part of Python's Official Documentation.
{: .callout}

## Plotting at the command-line
Let's recreate a plot from the previous episode, in program that we can call from a shell script:

~~~
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')
data.loc['Australia'].plot()
plt.xticks(rotation=90)
~~~
{: .python}

If we run this, nothing happens. Why not? Because we have not explicitly told `pyplot` to
output the plot, so it doesn't. (We see it in the Jupyter notebook because that
always presents the output of the last line, which with `pyplot` is the current plot state.)

Add a line to the end of the program:

~~~
plt.show()
~~~
{: .python}

and re-run it. Now we see the plot on the screen, and the program waits for us to close the plot
window before exiting.

What if we wanted to create a PDF file instead, so that we could include the plot in a report
(without resorting to screen shots)?

Replace the call to `plt.show()` with one to `plt.savefig("australia.pdf")`, and re-run it.

## Subplots

What if we want to have two plots side-by-side? For that, `pyplot` gives us "subplots".
Try the following:

~~~
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('data/gapminder_gdp_africa.csv', index_col='country')

years = []
for col in data.columns:
    year = col[-4:]
    years.append(year)

plt.suptitle("Africa GDPs")

plt.subplot(221)
plt.title("Gabon")
plt.plot(years, data.loc["Gabon"])

plt.subplot(222)
plt.title("Djibouti")
plt.plot(years, data.loc['Djibouti'])

plt.subplot(223)
plt.title("Burkina Faso")
plt.plot(years, data.loc['Burkina Faso'])

plt.subplot(224)
plt.title("Eritrea")
plt.plot(years, data.loc['Eritrea'])

plt.savefig("africa_gdps.pdf")
~~~
{: .python}

If we open this file, we see that the axes have crashed a bit close together. To fix this
add a call to `plt.tight_layout()` immediately before the final line of the program.
(I.e. once all elements are in place, then tighten then up.)

> ## Arithmetic on the Command Line
>
> Write a command-line program that does addition and subtraction:
>
> ~~~
> $ python arith.py add 1 2
> ~~~
> {: .python}
>
> ~~~
> 3
> ~~~
> {: .output}
>
> ~~~
> $ python arith.py subtract 3 4
> ~~~
> {: .python}
>
> ~~~
> -1
> ~~~
> {: .output}
>
> > ## Solution
> > ~~~
> > import sys
> >
> > def main():
> >     assert len(sys.argv) == 4, 'Need exactly 3 arguments'
> >
> >     operator = sys.argv[1]
> >     assert operator in ['add', 'subtract', 'multiply', 'divide'], \
> >         'Operator is not one of add, subtract, multiply, or divide: bailing out'
> >     try:
> >         operand1, operand2 = float(sys.argv[2]), float(sys.argv[3])
> >     except ValueError:
> >         print('cannot convert input to a number: bailing out')
> >         return
> >
> >     do_arithmetic(operand1, operator, operand2)
> >
> > def do_arithmetic(operand1, operator, operand2):
> >
> >     if operator == 'add':
> >         value = operand1 + operand2
> >     elif operator == 'subtract':
> >         value = operand1 - operand2
> >     elif operator == 'multiply':
> >         value = operand1 * operand2
> >     elif operator == 'divide':
> >         value = operand1 / operand2
> >     print(value)
> >
> > main()
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Generate an Error Message
>
> Write a program called `check_arguments.py` that prints usage
> then exits the program if no arguments are provided.
> (Hint) You can use `sys.exit()` to exit the program.
>
> ~~~
> $ python check_arguments.py
> ~~~
> {: .bash}
>
> ~~~
> usage: python check_argument.py filename.txt
> ~~~
> {: .output}
>
> ~~~
> $ python check_arguments.py filename.txt
> ~~~
> {: .bash}
>
> ~~~
> Thanks for specifying arguments!
> ~~~
> {: .output}
{: .challenge}
