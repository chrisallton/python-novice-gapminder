---
title: Hubble's Law experiment in Python
teaching: 15
exercises: 0
questions:
- "How can I practice using Pandas instead of Origin or Excel?"
- "How is using Pandas more convenient than using Origin or Excel?"
objectives:
- "Download a data file"
- "Load it into Pandas"
- "Plot it"
- "Fit it"
keypoints:
- "Refer to function reference to see what keyword arguments are available"
---

You may recall doing an experiment at level 2 on Hubble's Law. The second section of that involved
downloading some data from the Internet and trying to fit it to find a value for Hubble's constant.
Let's try and do that now with Pandas, as an exercise.

Firstly, we'll need that data. Use `wget` to download the file:

~~~
$ wget http://pyweb.swan.ac.uk/~perkins/PPC/prac/hubble.data
~~~
{: .bash}

## Loading the data in Pandas

Try loading the data into a Pandas DataFrame called `data`. Look at `data[2]` --
we see two columns in one. Because the file doesn't have commas, Pandas has assumed
the entire file is a single column.

We can supply additional arguments to `pandas.read_csv()` to make it use spaces as delimiters,
and to give the columns more helpful names (for example, `m` and `ln(v)`).

Use `help(pandas.read_csv)` to get look up the following keyword arguments:

* `delim_whitespace`
* `skiprows`
* `names`

Re-import the data using these arguments to give the DataTable a meaningful shape.

## Calculations

We can add new columns to the table, calculated from the existing ones.
You may recall that we need the distance, calculated from the magnitude $m$
as $D=10^{\frac{27 + m}{5}}$ (ie. assuming that the galaxies all have absolute magnitude 
$M=-22$). We can do that as

~~~
data["D"] = 10 ** ((27 + data["m"]) / 5)
~~~
{: .python}

However, this gives us the distance in parsecs! We need it in megaparsecs,
as $$H_0$$ has units $$\mathrm{km}/\mathrm{s}/\mathrm{Mpc}$$.
Adjust the code so that it gives $$D$$ in $$\mathrm{Mpc}$$.

Do the same to calculate $$v$$ from the second column, $$\ln (v)$$.
You'll need `exp()` from `numpy`.

## Plots

Plot the data, with $$D$$ on the horizontal axis and $v$ on the vertical axis.
Make this a scatter plot. To do this, replace the `-` with an `o` or a `.`
in the third parameter you pass to `plt.plot()`.

## Fits

Create a function `Hubble(D, H0, v0)`, that gives a straight line fit form,
$$v = H_0 D + v_0$$.

Use this with `curve_fit` (imported from `scipy.optimize`) to find the Hubble constant
$$H_0$$ from these data.

> ## Fitting the leading edge
> 
> You may recall that in fact the assumptions we made meant that $$D$$ is in fact
> an upper bound on distance---galaxies may be closer than they seem, so
> appear too far to the right on the plot. This clearly results in a value for $$H_0$$
> which is too small.
> 
> To remedy this, we fitted the leading edge of the plot.
> 
> Can we do this automatically? Yes:
>
> * Divide the $$v$$ axis into intervals of a fixed width.
> * Create a set of counts, one for each interval. A dictionary is good for this.
>   (A `defaultdict` is even better, if you want to look up how to use them.)
> * For each point, determine which interval it falls into
> * If the current point's $$D$$ value is lower than the value currently held in the dict,
>   then replace it. Otherwise, continue to the next point.
> * Fit the resulting dict. You can either use the centre of the bin
>   for the $$v$$ value, or the value associated with the point used.
>
> This is related to the idea of histogramming.
{: .challenge}
