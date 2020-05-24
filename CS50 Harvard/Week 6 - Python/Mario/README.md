# [Mario](https://cs50.harvard.edu/x/2020/psets/6/mario/more/#mario)

![screenshot of Mario jumping up
pyramid](./week%206%20Mario%20-%20CS50x_files/pyramids.png)

Implement a program that prints out a double half-pyramid of a specified
height, per the below.

```{.highlight}
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

## [Specification](https://cs50.harvard.edu/x/2020/psets/6/mario/more/#specification)

- \*\*Write, in a file called `mario.py`{.highlighter-rouge} in
  `~/pset6/mario/more/`{.highlighter-rouge}, a program that recreates
  these half-pyramids using hashes (`#`{.highlighter-rouge}) for
  blocks, exactly as you did in [Problem Set
  1](https://cs50.harvard.edu/x/2020/psets/1/), except that your
  program this time should be written (a) in Python and (b) in CS50
  IDE.
- \*\*To make things more interesting, first prompt the user with
  `get_int`{.highlighter-rouge} for the half-pyramid’s height, a
  positive integer between `1`{.highlighter-rouge} and
  `8`{.highlighter-rouge}, inclusive. (The height of the half-pyramids
  pictured above happens to be `4`{.highlighter-rouge}, the width of
  each half-pyramid `4`{.highlighter-rouge}, with a gap of size
  `2`{.highlighter-rouge} separating them).
- \*\*If the user fails to provide a positive integer no greater than
  `8`{.highlighter-rouge}, you should re-prompt for the same again.
- \*\*Then, generate (with the help of `print`{.highlighter-rouge} and
  one or more loops) the desired half-pyramids.
- \*\*Take care to align the bottom-left corner of your pyramid with the
  left-hand edge of your terminal window, and ensure that there are
  two spaces between the two pyramids, and that there are no
  additional spaces after the last set of hashes on each row.

## [Usage](https://cs50.harvard.edu/x/2020/psets/6/mario/more/#usage)

Your program should behave per the example below.

```{.highlight}
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

## [Testing](https://cs50.harvard.edu/x/2020/psets/6/mario/more/#testing)

No `check50`{.highlighter-rouge} for this problem, but be sure to test
your code for each of the following.

- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Type in `-1`{.highlighter-rouge} and press
  enter. Your program should reject this input as invalid, as by
  re-prompting the user to type in another number.
- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Type in `0`{.highlighter-rouge} and press
  enter. Your program should reject this input as invalid, as by
  re-prompting the user to type in another number.
- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Type in `1`{.highlighter-rouge} and press
  enter. Your program should generate the below output. Be sure that
  the pyramid is aligned to the bottom-left corner of your terminal,
  and that there are no extra spaces at the end of each line.

```{.highlight}
#  #
```

- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Type in `2`{.highlighter-rouge} and press
  enter. Your program should generate the below output. Be sure that
  the pyramid is aligned to the bottom-left corner of your terminal,
  and that there are no extra spaces at the end of each line.

```{.highlight}
 #  #
##  ##
```

- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Type in `8`{.highlighter-rouge} and press
  enter. Your program should generate the below output. Be sure that
  the pyramid is aligned to the bottom-left corner of your terminal,
  and that there are no extra spaces at the end of each line.

```{.highlight}
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Type in `9`{.highlighter-rouge} and press
  enter. Your program should reject this input as invalid, as by
  re-prompting the user to type in another number. Then, type in
  `2`{.highlighter-rouge} and press enter. Your program should
  generate the below output. Be sure that the pyramid is aligned to
  the bottom-left corner of your terminal, and that there are no extra
  spaces at the end of each line.

```{.highlight}
 #  #
##  ##
```

- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Type in `foo`{.highlighter-rouge} and press
  enter. Your program should reject this input as invalid, as by
  re-prompting the user to type in another number.
- \*\*Run your program as `python mario.py`{.highlighter-rouge} and wait
  for a prompt for input. Do not type anything, and press enter. Your
  program should reject this input as invalid, as by re-prompting the
  user to type in another number.

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/6/mario/more/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/sentimental/mario/more
```
