# [Mario](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#mario)

If you already started to work on Problem Set 1 in CS50 Lab, you may
[continue working on
it](https://lab.cs50.io/cs50/labs/2020/x/mario/less/) there. If you’re
just now starting to work in this problem, be sure to use CS50 IDE
instead by following the instructions below!

## [World 1-1](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#world-1-1)

Toward the end of World 1-1 in Nintendo’s Super Mario Brothers, Mario
must ascend right-aligned pyramid of blocks, a la the below.

![screenshot of Mario jumping up a right-aligned
pyramid](./week%201%20-%20Mario%20-%20CS50x_files/pyramid.png)

Let’s recreate that pyramid in C, albeit in text, using hashes
(`#`{.highlighter-rouge}) for bricks, a la the below. Each hash is a bit
taller than it is wide, so the pyramid itself is also be taller than it
is wide.

```{.highlight}
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

The program we’ll write will be called `mario`{.highlighter-rouge}. And
let’s allow the user to decide just how tall the pyramid should be by
first prompting them for a positive integer between, say, 1 and 8,
inclusive.

Here’s how the program might work if the user inputs
`8`{.highlighter-rouge} when prompted:

```{.highlight}
$ ./mario
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Here’s how the program might work if the user inputs
`4`{.highlighter-rouge} when prompted:

```{.highlight}
$ ./mario
Height: 4
   #
  ##
 ###
####
```

Here’s how the program might work if the user inputs
`2`{.highlighter-rouge} when prompted:

```{.highlight}
$ ./mario
Height: 2
 #
##
```

And here’s how the program might work if the user inputs
`1`{.highlighter-rouge} when prompted:

```{.highlight}
$ ./mario
Height: 1
#
```

If the user doesn’t, in fact, input a positive integer between 1 and 8,
inclusive, when prompted, the program should re-prompt the user until
they cooperate:

```{.highlight}
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
####
```

How to begin? Let’s approach this problem one step at a time.

## [Pseudocode](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#pseudocode)

First, create a new directory (i.e., folder) called
`mario`{.highlighter-rouge} inside of your `pset1`{.highlighter-rouge}
directory by executing

```{.highlight}
~/ $ mkdir ~/pset1/mario
```

Add a new file called `pseudocode.txt`{.highlighter-rouge} inside of
your `mario`{.highlighter-rouge} directory.

Write in `pseudocode.txt`{.highlighter-rouge} some pseudocode that
implements this program, even if not (yet!) sure how to write it in
code. There’s no one right way to write pseudocode, but short English
sentences suffice. Recall how we wrote pseudocode for [finding Mike
Smith](https://docs.google.com/presentation/d/17wRd8ksO6QkUq906SUgm17AqcI-Jan42jkY-EmufxnE/edit?usp=sharing).
Odds are your pseudocode will use (or imply using!) one or more
functions, conditions, Boolean expressions, loops, and/or variables.

Spoiler

There’s more than one way to do this, so here’s just one!

1.  Prompt user for height
2.  If height is less than 1 or greater than 8 (or not an integer at
    all), go back one step
3.  Iterate from 1 through height:
    1.  On iteration _i_, print _i_ hashes and then a newline

It’s okay to edit your own after seeing this pseudocode here, but don’t
simply copy/paste ours into your own!

## [Prompting for Input](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#prompting-for-input)

Whatever your pseudocode, let’s first write only the C code that prompts
(and re-prompts, as needed) the user for input. Create a new file called
`mario.c`{.highlighter-rouge} inside of your `mario`{.highlighter-rouge}
directory.

Now, modify `mario.c`{.highlighter-rouge} in such a way that it prompts
the user for the pyramid’s height, storing their input in a variable,
re-prompting the user again and again as needed if their input is not a
positive integer between 1 and 8, inclusive. Then, simply print the
value of that variable, thereby confirming (for yourself) that you’ve
indeed stored the user’s input successfully, a la the below.

```{.highlight}
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
Stored: 4
```

Hints

- \*\*Recall that you can compile your program with
  `make`{.highlighter-rouge}.
- \*\*Recall that you can print an `int`{.highlighter-rouge} with
  `printf`{.highlighter-rouge} using `%i`{.highlighter-rouge}.
- \*\*Recall that you can get an integer from the user with
  `get_int`{.highlighter-rouge}.
- \*\*Recall that `get_int`{.highlighter-rouge} is declared in
  `cs50.h`{.highlighter-rouge}.
- \*\*Recall that we prompted the user for a positive integer in class
  via `positive.c`{.highlighter-rouge}.

## [Building the Opposite](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#building-the-opposite)

Now that your program is (hopefully!) accepting input as prescribed,
it’s time for another step.

It turns out it’s a bit easier to build a left-aligned pyramid than
right-, a la the below.

```{.highlight}
#
##
###
####
#####
######
#######
########
```

So let’s build a left-aligned pyramid first and then, once that’s
working, right-align it instead!

Modify `mario.c`{.highlighter-rouge} at right such that it no longer
simply prints the user’s input but instead prints a left-aligned pyramid
of that height.

Hints

- \*\*Keep in mind that a hash is just a character like any other, so
  you can print it with `printf`{.highlighter-rouge}.
- \**Just as Scratch has a
  [Repeat](https://docs.google.com/presentation/d/17wRd8ksO6QkUq906SUgm17AqcI-Jan42jkY-EmufxnE/edit?usp=sharing)
  block, so does C have a
  [`for`{.highlighter-rouge}](https://docs.google.com/presentation/d/191XW0DHWlW6WmAhYuFUYnZKUlDx0N4u4Fp81AeW-uNs/edit?usp=sharing)
  loop, via which you can iterate some number times. Perhaps on each
  iteration, *i\*, you could print that many hashes?
- \*\*

  You can actually “nest” loops, iterating with one variable (e.g.,
  `i`{.highlighter-rouge}) in the “outer” loop and another (e.g.,
  `j`{.highlighter-rouge}) in the “inner” loop. For instance, here’s
  how you might print a square of height and width
  `n`{.highlighter-rouge}, below. Of course, it’s not a square that
  you want to print!

  ```{.highlight}
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
  ```

## [Right-Aligning with Dots](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#right-aligning-with-dots)

Let’s now right-align that pyramid by pushing its hashes to the right by
prefixing them with dots (i.e., periods), a la the below.

```{.highlight}
.......#
......##
.....###
....####
...#####
..######
.#######
########
```

Modify `mario.c`{.highlighter-rouge} in such a way that it does exactly
that!

Hint

Notice how the number of dots needed on each line is the “opposite” of
the number of that line’s hashes. For a pyramid of height 8, like the
above, the first line has but 1 hash and thus 7 dots. The bottom line,
meanwhile, has 8 hashes and thus 0 dots. Via what formula (or
arithmetic, really) could you print that many dots?

### [How to Test Your Code](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#how-to-test-your-code)

Does your code work as prescribed when you input

- \*\*`-1`{.highlighter-rouge} (or other negative numbers)?
- \*\*`0`{.highlighter-rouge}?
- \*\*`1`{.highlighter-rouge} through `8`{.highlighter-rouge}?
- \*\*`9`{.highlighter-rouge} or other positive numbers?
- \*\*letters or words?
- \*\*no input at all, when you only hit Enter?

## [Removing the Dots](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#removing-the-dots)

All that remains now is a finishing flourish! Modify
`mario.c`{.highlighter-rouge} in such a way that it prints spaces
instead of those dots!

### [How to Test Your Code](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#how-to-test-your-code-1)

Execute the below to evaluate the correctness of your code using
`check50`{.highlighter-rouge}. But be sure to compile and test it
yourself as well!

```{.highlight}
check50 cs50/problems/2020/x/mario/less
```

Execute the below to evaluate the style of your code using
`style50`{.highlighter-rouge}.

```{.highlight}
style50 mario.c
```

Hint

A space is just a press of your space bar, just as a period is just a
press of its key! Just remember that `printf`{.highlighter-rouge}
requires that you surround both with double quotes!

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/1/mario/less/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/mario/less
```
