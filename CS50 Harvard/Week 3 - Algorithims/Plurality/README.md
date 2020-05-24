# [Plurality](https://cs50.harvard.edu/x/2020/psets/3/plurality/#plurality)

Implement a program that runs a plurality election, per the below.

```{.highlight}
$ ./plurality Alice Bob Charlie
Number of voters: 4
Vote: Alice
Vote: Bob
Vote: Charlie
Vote: Alice
Alice
```

## [Background](https://cs50.harvard.edu/x/2020/psets/3/plurality/#background)

Elections come in all shapes and sizes. In the UK, the [Prime
Minister](https://www.parliament.uk/education/about-your-parliament/general-elections/)
is officially appointed by the monarch, who generally chooses the leader
of the political party that wins the most seats in the House of Commons.
The United States uses a multi-step [Electoral
College](https://www.archives.gov/federal-register/electoral-college/about.html)
process where citizens vote on how each state should allocate Electors
who then elect the President.

Perhaps the simplest way to hold an election, though, is via a method
commonly known as the “plurality vote” (also known as
“first-past-the-post” or “winner take all”). In the plurality vote,
every voter gets to vote for one candidate. At the end of the election,
whichever candidate has the greatest number of votes is declared the
winner of the election.

## [Getting Started](https://cs50.harvard.edu/x/2020/psets/3/plurality/#getting-started)

Here’s how to download this problem’s “distribution code” (i.e., starter
code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io/)
and then, in a terminal window, execute each of the below.

- \*\*Execute `cd`{.highlighter-rouge} to ensure that you’re in
  `~/`{.highlighter-rouge} (i.e., your home directory).
- \*\*Execute `mkdir pset3`{.highlighter-rouge} to make (i.e., create) a
  directory called `pset3`{.highlighter-rouge} in your home directory.
- \*\*Execute `cd pset3`{.highlighter-rouge} to change into (i.e., open)
  that directory.
- \*\*Execute `mkdir plurality`{.highlighter-rouge} to make (i.e.,
  create) a directory called `plurality`{.highlighter-rouge} in your
  `pset3`{.highlighter-rouge} directory.
- \*\*Execute `cd plurality`{.highlighter-rouge} to change into (i.e.,
  open) that directory.
- \*\*Execute
  `wget https://cdn.cs50.net/2019/fall/psets/3/plurality/plurality.c`{.highlighter-rouge}
  to download this problem’s distribution code.
- \*\*Execute `ls`{.highlighter-rouge}. You should see this problem’s
  distribution code, in a file called
  `plurality.c`{.highlighter-rouge}.

## [Understanding](https://cs50.harvard.edu/x/2020/psets/3/plurality/#understanding)

Let’s now take a look at `plurality.c`{.highlighter-rouge} and read
through the distribution code that’s been provided to you.

The line `#define MAX 9`{.highlighter-rouge} is some syntax used here to
mean that `MAX`{.highlighter-rouge} is a constant (equal to
`9`{.highlighter-rouge}) that can be used throughout the program. Here,
it represents the maximum number of candidates an election can have.

The file then defines a `struct`{.highlighter-rouge} called a
`candidate`{.highlighter-rouge}. Each `candidate`{.highlighter-rouge}
has two fields: a `string`{.highlighter-rouge} called
`name`{.highlighter-rouge} representing the candidate’s name, and an
`int`{.highlighter-rouge} called `votes`{.highlighter-rouge}
representing the number of votes the candidate has. Next, the file
defines a global array of `candidates`{.highlighter-rouge}, where each
element is itself a `candidate`{.highlighter-rouge}.

Now, take a look at the `main`{.highlighter-rouge} function itself. See
if you can find where the program sets a global variable
`candidate_count`{.highlighter-rouge} representing the number of
candidates in the election, copies command-line arguments into the array
`candidates`{.highlighter-rouge}, and asks the user to type in the
number of voters. Then, the program lets every voter type in a vote (see
how?), calling the `vote`{.highlighter-rouge} function on each candidate
voted for. Finally, `main`{.highlighter-rouge} makes a call to the
`print_winner`{.highlighter-rouge} function to print out the winner (or
winners) of the election.

If you look further down in the file, though, you’ll notice that the
`vote`{.highlighter-rouge} and `print_winner`{.highlighter-rouge}
functions have been left blank. This part is up to you to complete!

## [Specification](https://cs50.harvard.edu/x/2020/psets/3/plurality/#specification)

Complete the implementation of `plurality.c`{.highlighter-rouge} in such
a way that the program simulates a plurality vote election.

- \*\*Complete the `vote`{.highlighter-rouge} function.
  - \*\*`vote`{.highlighter-rouge} takes a single argument, a
    `string`{.highlighter-rouge} called `name`{.highlighter-rouge},
    representing the name of the candidate who was voted for.
  - \*\*If `name`{.highlighter-rouge} matches one of the names of the
    candidates in the election, then update that candidate’s vote
    total to account for the new vote. The
    `vote`{.highlighter-rouge} function in this case should return
    `true`{.highlighter-rouge} to indicate a successful ballot.
  - \*\*If `name`{.highlighter-rouge} does not match the name of any
    of the candidates in the election, no vote totals should change,
    and the `vote`{.highlighter-rouge} function should return
    `false`{.highlighter-rouge} to indicate an invalid ballot.
  - \*\*You may assume that no two candidates will have the same name.
- \*\*Complete the `print_winner`{.highlighter-rouge} function.
  - \*\*The function should print out the name of the candidate who
    received the most votes in the election, and then print a
    newline.
  - \*\*It is possible that the election could end in a tie if
    multiple candidates each have the maximum number of votes. In
    that case, you should output the names of each of the winning
    candidates, each on a separate line.

You should not modify anything else in `plurality.c`{.highlighter-rouge}
other than the implementations of the `vote`{.highlighter-rouge} and
`print_winner`{.highlighter-rouge} functions (and the inclusion of
additional header files, if you’d like).

## [Usage](https://cs50.harvard.edu/x/2020/psets/3/plurality/#usage)

Your program should behave per the examples below.

```{.highlight}
$ ./plurality Alice Bob
Number of voters: 3
Vote: Alice
Vote: Bob
Vote: Alice
Alice
```

```{.highlight}
$ ./plurality Alice Bob
Number of voters: 3
Vote: Alice
Vote: Charlie
Invalid vote.
Vote: Alice
Alice
```

```{.highlight}
$ ./plurality Alice Bob Charlie
Number of voters: 5
Vote: Alice
Vote: Charlie
Vote: Bob
Vote: Bob
Vote: Alice
Alice
Bob
```

## [Walkthrough](https://cs50.harvard.edu/x/2020/psets/3/plurality/#walkthrough)

## [Testing](https://cs50.harvard.edu/x/2020/psets/3/plurality/#testing)

Be sure to test your code to make sure it handles…

- \*\*An election with any number of candidate (up to the
  `MAX`{.highlighter-rouge} of `9`{.highlighter-rouge})
- \*\*Voting for a candidate by name
- \*\*Invalid votes for candidates who are not on the ballot
- \*\*Printing the winner of the election if there is only one
- \*\*Printing the winner of the election if there are multiple winners

Execute the below to evaluate the correctness of your code using
`check50`{.highlighter-rouge}. But be sure to compile and test it
yourself as well!

```{.highlight}
check50 cs50/problems/2020/x/plurality
```

Execute the below to evaluate the style of your code using
`style50`{.highlighter-rouge}.

```{.highlight}
style50 plurality.c
```

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/3/plurality/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/plurality
```
