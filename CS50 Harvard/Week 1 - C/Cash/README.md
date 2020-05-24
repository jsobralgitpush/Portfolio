# [Cash](https://cs50.harvard.edu/x/2020/psets/1/cash/#cash)

If you already started to work on Problem Set 1 in CS50 Lab, you may
[continue working on it](https://lab.cs50.io/cs50/labs/2020/x/cash/)
there. If you’re just now starting to work in this problem, be sure to
use CS50 IDE instead by following the instructions below!

## [Greedy Algorithms](https://cs50.harvard.edu/x/2020/psets/1/cash/#greedy-algorithms)

![US coins](./week%201%20Cash%20-%20CS50x_files/coins.jpg)

When making change, odds are you want to minimize the number of coins
you’re dispensing for each customer, lest you run out (or annoy the
customer!). Fortunately, computer science has given cashiers everywhere
ways to minimize numbers of coins due: greedy algorithms.

According to the National Institute of Standards and Technology (NIST),
a greedy algorithm is one “that always takes the best immediate, or
local, solution while finding an answer. Greedy algorithms find the
overall, or globally, optimal solution for some optimization problems,
but may find less-than-optimal solutions for some instances of other
problems.”

What’s all that mean? Well, suppose that a cashier owes a customer some
change and in that cashier’s drawer are quarters (25¢), dimes (10¢),
nickels (5¢), and pennies (1¢). The problem to be solved is to decide
which coins and how many of each to hand to the customer. Think of a
“greedy” cashier as one who wants to take the biggest bite out of this
problem as possible with each coin they take out of the drawer. For
instance, if some customer is owed 41¢, the biggest first (i.e., best
immediate, or local) bite that can be taken is 25¢. (That bite is “best”
inasmuch as it gets us closer to 0¢ faster than any other coin would.)
Note that a bite of this size would whittle what was a 41¢ problem down
to a 16¢ problem, since 41 - 25 = 16. That is, the remainder is a
similar but smaller problem. Needless to say, another 25¢ bite would be
too big (assuming the cashier prefers not to lose money), and so our
greedy cashier would move on to a bite of size 10¢, leaving him or her
with a 6¢ problem. At that point, greed calls for one 5¢ bite followed
by one 1¢ bite, at which point the problem is solved. The customer
receives one quarter, one dime, one nickel, and one penny: four coins in
total.

It turns out that this greedy approach (i.e., algorithm) is not only
locally optimal but also globally so for America’s currency (and also
the European Union’s). That is, so long as a cashier has enough of each
coin, this largest-to-smallest approach will yield the fewest coins
possible. How few? Well, you tell us!

## [Implementation Details](https://cs50.harvard.edu/x/2020/psets/1/cash/#implementation-details)

Implement, in a file called `cash.c`{.highlighter-rouge} in a
`~/pset1/cash`{.highlighter-rouge} directory, a program that first asks
the user how much change is owed and then prints the minimum number of
coins with which that change can be made.

- \*\*Use `get_float`{.highlighter-rouge} to get the user’s input and
  `printf`{.highlighter-rouge} to output your answer. Assume that the
  only coins available are quarters (25¢), dimes (10¢), nickels (5¢),
  and pennies (1¢).
  - \*\*We ask that you use `get_float`{.highlighter-rouge} so that
    you can handle dollars and cents, albeit sans dollar sign. In
    other words, if some customer is owed \$9.75 (as in the case
    where a newspaper costs 25¢ but the customer pays with a \$10
    bill), assume that your program’s input will be
    `9.75`{.highlighter-rouge} and not `$9.75`{.highlighter-rouge}
    or `975`{.highlighter-rouge}. However, if some customer is owed
    \$9 exactly, assume that your program’s input will be
    `9.00`{.highlighter-rouge} or just `9`{.highlighter-rouge} but,
    again, not `$9`{.highlighter-rouge} or
    `900`{.highlighter-rouge}. Of course, by nature of
    floating-point values, your program will likely work with inputs
    like `9.0`{.highlighter-rouge} and `9.000`{.highlighter-rouge}
    as well; you need not worry about checking whether the user’s
    input is “formatted” like money should be.
- \*\*You need not try to check whether a user’s input is too large to
  fit in a `float`{.highlighter-rouge}. Using
  `get_float`{.highlighter-rouge} alone will ensure that the user’s
  input is indeed a floating-point (or integral) value but not that it
  is non-negative.
- \*\*If the user fails to provide a non-negative value, your program
  should re-prompt the user for a valid amount again and again until
  the user complies.
- \*\*So that we can automate some tests of your code, be sure that your
  program’s last line of output is only the minimum number of coins
  possible: an integer followed by `\n`{.highlighter-rouge}.
- \*\*Beware the inherent imprecision of floating-point values. Recall
  `floats.c`{.highlighter-rouge} from class, wherein, if
  `x`{.highlighter-rouge} is `2`{.highlighter-rouge}, and
  `y`{.highlighter-rouge} is `10`{.highlighter-rouge},
  `x / y`{.highlighter-rouge} is not precisely two tenths! And so,
  before making change, you’ll probably want to convert the user’s
  inputted dollars to cents (i.e., from a `float`{.highlighter-rouge}
  to an `int`{.highlighter-rouge}) to avoid tiny errors that might
  otherwise add up!
- \*\*

  Take care to round your cents to the nearest penny, as with
  `round`{.highlighter-rouge}, which is declared in
  `math.h`{.highlighter-rouge}. For instance, if
  `dollars`{.highlighter-rouge} is a `float`{.highlighter-rouge} with
  the user’s input (e.g., `0.20`{.highlighter-rouge}), then code like

  ```{.highlight}
  int cents = round(dollars * 100);
  ```

  will safely convert `0.20`{.highlighter-rouge} (or even
  `0.200000002980232238769531250`{.highlighter-rouge}) to
  `20`{.highlighter-rouge}.

Your program should behave per the examples below.

```{.highlight}
$ ./cash
Change owed: 0.41
4
```

```{.highlight}
$ ./cash
Change owed: -0.41
Change owed: foo
Change owed: 0.41
4
```

### [Walkthrough](https://cs50.harvard.edu/x/2020/psets/1/cash/#walkthrough)

### [How to Test Your Code](https://cs50.harvard.edu/x/2020/psets/1/cash/#how-to-test-your-code)

Does your code work as prescribed when you input

- \*\*`-1.00`{.highlighter-rouge} (or other negative numbers)?
- \*\*`0.00`{.highlighter-rouge}?
- \*\*`0.01`{.highlighter-rouge} (or other positive numbers)?
- \*\*letters or words?
- \*\*no input at all, when you only hit Enter?

You can also execute the below to evaluate the correctness of your code
using `check50`{.highlighter-rouge}. But be sure to compile and test it
yourself as well!

```{.highlight}
check50 cs50/problems/2020/x/cash
```

Execute the below to evaluate the style of your code using
`style50`{.highlighter-rouge}.

```{.highlight}
style50 cash.c
```

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/1/cash/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/cash
```
