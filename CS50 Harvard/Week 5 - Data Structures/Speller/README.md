# [Speller](https://cs50.harvard.edu/x/2020/psets/5/speller/#speller)

**Be sure to read this specification in its entirety before starting so
you know what to do and how to do it!**

Implement a program that spell-checks a file, a la the below, using a
hash table.

```{.highlight}
$ ./speller texts/lalaland.txt
MISSPELLED WORDS

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]

WORDS MISSPELLED:
WORDS IN DICTIONARY:
WORDS IN TEXT:
TIME IN load:
TIME IN check:
TIME IN size:
TIME IN unload:
TIME IN TOTAL:
```

## [Distribution](https://cs50.harvard.edu/x/2020/psets/5/speller/#distribution)

### [Downloading](https://cs50.harvard.edu/x/2020/psets/5/speller/#downloading)

Log into [CS50 IDE](https://ide.cs50.io/) and then, in a terminal
window, execute each of the below.

1.  Execute `cd`{.highlighter-rouge} to ensure that you’re in
    `~/`{.highlighter-rouge} (i.e., your home directory).
2.  Execute `mkdir pset5`{.highlighter-rouge} to make (i.e., create) a
    directory called `pset5`{.highlighter-rouge} in your home directory.
3.  Execute `cd pset5`{.highlighter-rouge} to change into (i.e., open)
    that directory.
4.  Execute
    `wget https://cdn.cs50.net/2019/fall/psets/5/speller/speller.zip`{.highlighter-rouge}
    to download a (compressed) ZIP file with this problem’s
    distribution.
5.  Execute `unzip speller.zip`{.highlighter-rouge} to uncompress that
    file.
6.  Execute `rm speller.zip`{.highlighter-rouge} followed by
    `yes`{.highlighter-rouge} or `y`{.highlighter-rouge} to delete that
    ZIP file.
7.  Execute `ls`{.highlighter-rouge}. You should see a directory called
    `speller`{.highlighter-rouge}, which was inside of that ZIP file.
8.  Execute `cd speller`{.highlighter-rouge} to change into that
    directory.
9.  Execute `ls`{.highlighter-rouge}. You should see this problem’s
    distribution:

```{.highlight}
dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  speller.c  texts/
```

### [Understanding](https://cs50.harvard.edu/x/2020/psets/5/speller/#understanding)

Theoretically, on input of size _n_, an algorithm with a running time of
_n_ is “asymptotically equivalent,” in terms of _O_, to an algorithm
with a running time of _2n_. Indeed, when describing the running time of
an algorithm, we typically focus on the dominant (i.e., most impactful)
term (i.e., _n_ in this case, since _n_ could be much larger than 2). In
the real world, though, the fact of the matter is that _2n_ feels twice
as slow as _n_.

The challenge ahead of you is to implement the fastest spell checker you
can! By “fastest,” though, we’re talking actual “wall-clock,” not
asymptotic, time.

In `speller.c`{.highlighter-rouge}, we’ve put together a program that’s
designed to spell-check a file after loading a dictionary of words from
disk into memory. That dictionary, meanwhile, is implemented in a file
called `dictionary.c`{.highlighter-rouge}. (It could just be implemented
in `speller.c`{.highlighter-rouge}, but as programs get more complex,
it’s often convenient to break them into multiple files.) The prototypes
for the functions therein, meanwhile, are defined not in
`dictionary.c`{.highlighter-rouge} itself but in
`dictionary.h`{.highlighter-rouge} instead. That way, both
`speller.c`{.highlighter-rouge} and `dictionary.c`{.highlighter-rouge}
can `#include`{.highlighter-rouge} the file. Unfortunately, we didn’t
quite get around to implementing the loading part. Or the checking part.
Both (and a bit more) we leave to you! But first, a tour.

#### [`dictionary.h`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/5/speller/#dictionaryh) {#dictionaryh}

Open up `dictionary.h`{.highlighter-rouge}, and you’ll see some new
syntax, including a few lines that mention
`DICTIONARY_H`{.highlighter-rouge}. No need to worry about those, but,
if curious, those lines just ensure that, even though
`dictionary.c`{.highlighter-rouge} and `speller.c`{.highlighter-rouge}
(which you’ll see in a moment) `#include`{.highlighter-rouge} this file,
`clang`{.highlighter-rouge} will only compile it once.

Next notice how we `#include`{.highlighter-rouge} a file called
`stdbool.h`{.highlighter-rouge}. That’s the file in which
`bool`{.highlighter-rouge} itself is defined. You’ve not needed it
before, since the CS50 Library used to `#include`{.highlighter-rouge}
that for you.

Also notice our use of `#define`{.highlighter-rouge}, a “preprocessor
directive” that defines a “constant” called `LENGTH`{.highlighter-rouge}
that has a value of `45`{.highlighter-rouge}. It’s a constant in the
sense that you can’t (accidentally) change it in your own code. In fact,
`clang`{.highlighter-rouge} will replace any mentions of
`LENGTH`{.highlighter-rouge} in your own code with, literally,
`45`{.highlighter-rouge}. In other words, it’s not a variable, just a
find-and-replace trick.

Finally, notice the prototypes for five functions:
`check`{.highlighter-rouge}, `hash`{.highlighter-rouge},
`load`{.highlighter-rouge}, `size`{.highlighter-rouge}, and
`unload`{.highlighter-rouge}. Notice how three of those take a pointer
as an argument, per the `*`{.highlighter-rouge}:

```{.highlight}
bool check(const char *word);
unsigned int hash(const char *word);
bool load(const char *dictionary);
```

Recall that `char *`{.highlighter-rouge} is what we used to call
`string`{.highlighter-rouge}. So those three prototypes are essentially
just:

```{.highlight}
bool check(const string word);
unsigned int hash(const string word);
bool load(const string dictionary);
```

And `const`{.highlighter-rouge}, meanwhile, just says that those
strings, when passed in as arguments, must remain constant; you won’t be
able to change them, accidentally or otherwise!

#### [`dictionary.c`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/5/speller/#dictionaryc) {#dictionaryc}

Now open up `dictionary.c`{.highlighter-rouge}. Notice how, atop the
file, we’ve defined a `struct`{.highlighter-rouge} called
`node`{.highlighter-rouge} that represents a node in a hash table. And
we’ve declared a global pointer array, `table`{.highlighter-rouge},
which will (soon) represent the hash table you will use to keep track of
words in the dictionary. The array contains `N`{.highlighter-rouge} node
pointers, and we’ve set `N`{.highlighter-rouge} equal to
`1`{.highlighter-rouge} for now, meaning this hash table has just 1
bucket right now. You’ll likely want to increase the number of buckets,
as by changing `N`{.highlighter-rouge}, to something larger!

Next, notice that we’ve implemented `load`{.highlighter-rouge},
`hash`{.highlighter-rouge}, `check`{.highlighter-rouge},
`size`{.highlighter-rouge}, and `unload`{.highlighter-rouge}, but only
barely, just enough for the code to compile. Your job, ultimately, is to
re-implement those functions as cleverly as possible so that this spell
checker works as advertised. And fast!

#### [`speller.c`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/5/speller/#spellerc) {#spellerc}

Okay, next open up `speller.c`{.highlighter-rouge} and spend some time
looking over the code and comments therein. You won’t need to change
anything in this file, and you don’t need to understand its entirety,
but do try to get a sense of its functionality nonetheless. Notice how,
by way of a function called `getrusage`{.highlighter-rouge}, we’ll be
“benchmarking” (i.e., timing the execution of) your implementations of
`check`{.highlighter-rouge}, `load`{.highlighter-rouge},
`size`{.highlighter-rouge}, and `unload`{.highlighter-rouge}. Also
notice how we go about passing `check`{.highlighter-rouge}, word by
word, the contents of some file to be spell-checked. Ultimately, we
report each misspelling in that file along with a bunch of statistics.

Notice, incidentally, that we have defined the usage of
`speller`{.highlighter-rouge} to be

```{.highlight}
Usage: speller [dictionary] text
```

where `dictionary`{.highlighter-rouge} is assumed to be a file
containing a list of lowercase words, one per line, and
`text`{.highlighter-rouge} is a file to be spell-checked. As the
brackets suggest, provision of `dictionary`{.highlighter-rouge} is
optional; if this argument is omitted, `speller`{.highlighter-rouge}
will use `dictionaries/large`{.highlighter-rouge} by default. In other
words, running

```{.highlight}
$ ./speller text
```

will be equivalent to running

```{.highlight}
$ ./speller dictionaries/large text
```

where `text`{.highlighter-rouge} is the file you wish to spell-check.
Suffice it to say, the former is easier to type! (Of course,
`speller`{.highlighter-rouge} will not be able to load any dictionaries
until you implement `load`{.highlighter-rouge} in
`dictionary.c`{.highlighter-rouge}! Until then, you’ll see
`Could not load`{.highlighter-rouge}.)

Within the default dictionary, mind you, are 143,091 words, all of which
must be loaded into memory! In fact, take a peek at that file to get a
sense of its structure and size. Notice that every word in that file
appears in lowercase (even, for simplicity, proper nouns and acronyms).
From top to bottom, the file is sorted lexicographically, with only one
word per line (each of which ends with `\n`{.highlighter-rouge}). No
word is longer than 45 characters, and no word appears more than once.
During development, you may find it helpful to provide
`speller`{.highlighter-rouge} with a `dictionary`{.highlighter-rouge} of
your own that contains far fewer words, lest you struggle to debug an
otherwise enormous structure in memory. In
`dictionaries/small`{.highlighter-rouge} is one such dictionary. To use
it, execute

```{.highlight}
$ ./speller dictionaries/small text
```

where `text`{.highlighter-rouge} is the file you wish to spell-check.
Don’t move on until you’re sure you understand how
`speller`{.highlighter-rouge} itself works!

Odds are, you didn’t spend enough time looking over
`speller.c`{.highlighter-rouge}. Go back one square and walk yourself
through it again!

#### [`texts/`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/5/speller/#texts)

So that you can test your implementation of
`speller`{.highlighter-rouge}, we’ve also provided you with a whole
bunch of texts, among them the script from _La La Land_, the text of the
Affordable Care Act, three million bytes from Tolstoy, some excerpts
from _The Federalist Papers_ and Shakespeare, the entirety of the King
James V Bible and the Koran, and more. So that you know what to expect,
open and skim each of those files, all of which are in a directory
called `texts`{.highlighter-rouge} within your
`pset5`{.highlighter-rouge} directory.

Now, as you should know from having read over
`speller.c`{.highlighter-rouge} carefully, the output of
`speller`{.highlighter-rouge}, if executed with, say,

```{.highlight}
$ ./speller texts/lalaland.txt
```

will eventually resemble the below. For now, try the staff’s solution
(using the default dictionary) by executing

```{.highlight}
$ ~cs50/2019/fall/pset5/speller texts/lalaland.txt
```

Below’s some of the output you’ll see. For information’s sake, we’ve
excerpted some examples of “misspellings.” And lest we spoil the fun,
we’ve omitted our own statistics for now.

```{.highlight}
MISSPELLED WORDS

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]

WORDS MISSPELLED:
WORDS IN DICTIONARY:
WORDS IN TEXT:
TIME IN load:
TIME IN check:
TIME IN size:
TIME IN unload:
TIME IN TOTAL:
```

`TIME IN load`{.highlighter-rouge} represents the number of seconds that
`speller`{.highlighter-rouge} spends executing your implementation of
`load`{.highlighter-rouge}. `TIME IN check`{.highlighter-rouge}
represents the number of seconds that `speller`{.highlighter-rouge}
spends, in total, executing your implementation of
`check`{.highlighter-rouge}. `TIME IN size`{.highlighter-rouge}
represents the number of seconds that `speller`{.highlighter-rouge}
spends executing your implementation of `size`{.highlighter-rouge}.
`TIME IN unload`{.highlighter-rouge} represents the number of seconds
that `speller`{.highlighter-rouge} spends executing your implementation
of `unload`{.highlighter-rouge}. `TIME IN TOTAL`{.highlighter-rouge} is
the sum of those four measurements.

**Note that these times may vary somewhat across executions of
`speller`{.highlighter-rouge}, depending on what else CS50 IDE is doing,
even if you don’t change your code.**

Incidentally, to be clear, by “misspelled” we simply mean that some word
is not in the `dictionary`{.highlighter-rouge} provided.

#### [`Makefile`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/5/speller/#makefile)

And, lastly, recall that `make`{.highlighter-rouge} automates
compilation of your code so that you don’t have to execute
`clang`{.highlighter-rouge} manually along with a whole bunch of
switches. However, as your programs grow in size,
`make`{.highlighter-rouge} won’t be able to infer from context anymore
how to compile your code; you’ll need to start telling
`make`{.highlighter-rouge} how to compile your program, particularly
when they involve multiple source (i.e., `.c`{.highlighter-rouge})
files, as in the case of this problem. And so we’ll utilize a
`Makefile`{.highlighter-rouge}, a configuration file that tells
`make`{.highlighter-rouge} exactly what to do. Open up
`Makefile`{.highlighter-rouge}, and you should see four lines:

1.  The first line tells `make`{.highlighter-rouge} to execute the
    subsequent lines whenever you yourself execute
    `make speller`{.highlighter-rouge} (or just
    `make`{.highlighter-rouge}).
2.  The second line tells `make`{.highlighter-rouge} how to compile
    `speller.c`{.highlighter-rouge} into machine code (i.e.,
    `speller.o`{.highlighter-rouge}).
3.  The third line tells `make`{.highlighter-rouge} how to compile
    `dictionary.c`{.highlighter-rouge} into machine code (i.e.,
    `dictionary.o`{.highlighter-rouge}).
4.  The fourth line tells `make`{.highlighter-rouge} to link
    `speller.o`{.highlighter-rouge} and
    `dictionary.o`{.highlighter-rouge} in a file called
    `speller`{.highlighter-rouge}.

**Be sure to compile `speller`{.highlighter-rouge} by executing
`make speller`{.highlighter-rouge} (or just `make`{.highlighter-rouge}).
Executing `make dictionary`{.highlighter-rouge} won’t work!**

## [Specification](https://cs50.harvard.edu/x/2020/psets/5/speller/#specification)

Alright, the challenge now before you is to implement, in order,
`load`{.highlighter-rouge}, `hash`{.highlighter-rouge},
`size`{.highlighter-rouge}, `check`{.highlighter-rouge}, and
`unload`{.highlighter-rouge} as efficiently as possible using a hash
table in such a way that `TIME IN load`{.highlighter-rouge},
`TIME IN check`{.highlighter-rouge}, `TIME IN size`{.highlighter-rouge},
and `TIME IN unload`{.highlighter-rouge} are all minimized. To be sure,
it’s not obvious what it even means to be minimized, inasmuch as these
benchmarks will certainly vary as you feed `speller`{.highlighter-rouge}
different values for `dictionary`{.highlighter-rouge} and for
`text`{.highlighter-rouge}. But therein lies the challenge, if not the
fun, of this problem. This problem is your chance to design. Although we
invite you to minimize space, your ultimate enemy is time. But before
you dive in, some specifications from us.

- \*\*You may not alter `speller.c`{.highlighter-rouge} or
  `Makefile`{.highlighter-rouge}.
- \*\*You may alter `dictionary.c`{.highlighter-rouge} (and, in fact,
  must in order to complete the implementations of
  `load`{.highlighter-rouge}, `hash`{.highlighter-rouge},
  `size`{.highlighter-rouge}, `check`{.highlighter-rouge}, and
  `unload`{.highlighter-rouge}), but you may not alter the
  declarations (i.e., prototypes) of `load`{.highlighter-rouge},
  `hash`{.highlighter-rouge}, `size`{.highlighter-rouge},
  `check`{.highlighter-rouge}, or `unload`{.highlighter-rouge}. You
  may, though, add new functions and (local or global) variables to
  `dictionary.c`{.highlighter-rouge}.
- \*\*You may change the value of `N`{.highlighter-rouge} in
  `dictionary.c`{.highlighter-rouge}, so that your hash table can have
  more buckets.
- \*\*You may alter `dictionary.h`{.highlighter-rouge}, but you may not
  alter the declarations of `load`{.highlighter-rouge},
  `hash`{.highlighter-rouge}, `size`{.highlighter-rouge},
  `check`{.highlighter-rouge}, or `unload`{.highlighter-rouge}.
- \*\*Your implementation of `check`{.highlighter-rouge} must be
  case-insensitive. In other words, if `foo`{.highlighter-rouge} is in
  dictionary, then `check`{.highlighter-rouge} should return true
  given any capitalization thereof; none of `foo`{.highlighter-rouge},
  `foO`{.highlighter-rouge}, `fOo`{.highlighter-rouge},
  `fOO`{.highlighter-rouge}, `fOO`{.highlighter-rouge},
  `Foo`{.highlighter-rouge}, `FoO`{.highlighter-rouge},
  `FOo`{.highlighter-rouge}, and `FOO`{.highlighter-rouge} should be
  considered misspelled.
- \*\*Capitalization aside, your implementation of
  `check`{.highlighter-rouge} should only return
  `true`{.highlighter-rouge} for words actually in
  `dictionary`{.highlighter-rouge}. Beware hard-coding common words
  (e.g., `the`{.highlighter-rouge}), lest we pass your implementation
  a `dictionary`{.highlighter-rouge} without those same words.
  Moreover, the only possessives allowed are those actually in
  `dictionary`{.highlighter-rouge}. In other words, even if
  `foo`{.highlighter-rouge} is in `dictionary`{.highlighter-rouge},
  `check`{.highlighter-rouge} should return
  `false`{.highlighter-rouge} given `foo's`{.highlighter-rouge} if
  `foo's`{.highlighter-rouge} is not also in
  `dictionary`{.highlighter-rouge}.
- \*\*You may assume that any `dictionary`{.highlighter-rouge} passed to
  your program will be structured exactly like ours, alphabetically
  sorted from top to bottom with one word per line, each of which ends
  with `\n`{.highlighter-rouge}. You may also assume that
  `dictionary`{.highlighter-rouge} will contain at least one word,
  that no word will be longer than `LENGTH`{.highlighter-rouge} (a
  constant defined in `dictionary.h`{.highlighter-rouge}) characters,
  that no word will appear more than once, that each word will contain
  only lowercase alphabetical characters and possibly apostrophes, and
  that no word will start with an apostrophe.
- \*\*You may assume that `check`{.highlighter-rouge} will only be
  passed words that contain (uppercase or lowercase) alphabetical
  characters and possibly apostrophes.
- \*\*Your spell checker may only take `text`{.highlighter-rouge} and,
  optionally, `dictionary`{.highlighter-rouge} as input. Although you
  might be inclined (particularly if among those more comfortable) to
  “pre-process” our default dictionary in order to derive an “ideal
  hash function” for it, you may not save the output of any such
  pre-processing to disk in order to load it back into memory on
  subsequent runs of your spell checker in order to gain an advantage.
- \*\*Your spell checker must not leak any memory. Be sure to check for
  leaks with `valgrind`{.highlighter-rouge}.
- \*\*You may search for (good) hash functions online, so long as you
  cite the origin of any hash function you integrate into your own
  code.

Alright, ready to go?

- \*\*Implement `load`{.highlighter-rouge}.
- \*\*Implement `hash`{.highlighter-rouge}.
- \*\*Implement `size`{.highlighter-rouge}.
- \*\*Implement `check`{.highlighter-rouge}.
- \*\*Implement `unload`{.highlighter-rouge}.

## [Walkthroughs](https://cs50.harvard.edu/x/2020/psets/5/speller/#walkthroughs)

**Please note that there are 6 videos in this playlist.**

## [Hints](https://cs50.harvard.edu/x/2020/psets/5/speller/#hints)

To compare two strings case-insensitively, you may find
[`strcasecmp`{.highlighter-rouge}](https://man.cs50.io/3/strcasecmp)
(declared in `strings.h`{.highlighter-rouge}) useful!

Ultimately, be sure to `free`{.highlighter-rouge} in
`unload`{.highlighter-rouge} any memory that you allocated in
`load`{.highlighter-rouge}! Recall that `valgrind`{.highlighter-rouge}
is your newest best friend. Know that `valgrind`{.highlighter-rouge}
watches for leaks while your program is actually running, so be sure to
provide command-line arguments if you want
`valgrind`{.highlighter-rouge} to analyze `speller`{.highlighter-rouge}
while you use a particular `dictionary`{.highlighter-rouge} and/or text,
as in the below. Best to use a small text, though, else
`valgrind`{.highlighter-rouge} could take quite a while to run.

```{.highlight}
$ valgrind ./speller texts/cat.txt
```

If you run `valgrind`{.highlighter-rouge} without specifying a
`text`{.highlighter-rouge} for `speller`{.highlighter-rouge}, your
implementations of `load`{.highlighter-rouge} and
`unload`{.highlighter-rouge} won’t actually get called (and thus
analyzed).

If unsure how to interpret the output of `valgrind`{.highlighter-rouge},
do just ask `help50`{.highlighter-rouge} for help:

```{.highlight}
$ help50 valgrind ./speller texts/cat.txt
```

## [Testing](https://cs50.harvard.edu/x/2020/psets/5/speller/#testing)

How to check whether your program is outting the right misspelled words?
Well, you’re welcome to consult the “answer keys” that are inside of the
`keys`{.highlighter-rouge} directory that’s inside of your
`speller`{.highlighter-rouge} directory. For instance, inside of
`keys/lalaland.txt`{.highlighter-rouge} are all of the words that your
program _should_ think are misspelled.

You could therefore run your program on some text in one window, as with
the below.

```{.highlight}
$ ./speller texts/lalaland.txt
```

And you could then run the staff’s solution on the same text in another
window, as with the below.

```{.highlight}
$ ~cs50/2019/fall/pset5/speller texts/lalaland.txt
```

And you could then compare the windows visually side by side. That could
get tedious quickly, though. So you might instead want to “redirect”
your program’s output to a file, as with the below.

```{.highlight}
$ ./speller texts/lalaland.txt > student.txt
$ ~cs50/2019/fall/pset5/speller texts/lalaland.txt > staff.txt
```

You can then compare both files side by side in the same window with a
program like `diff`{.highlighter-rouge}, as with the below.

```{.highlight}
$ diff -y student.txt staff.txt
```

Alternatively, to save time, you could just compare your program’s
output (assuming you redirected it to, e.g.,
`student.txt`{.highlighter-rouge}) against one of the answer keys
without running the staff’s solution, as with the below.

```{.highlight}
$ diff -y student.txt keys/lalaland.txt
```

If your program’s output matches the staff’s, `diff`{.highlighter-rouge}
will output two columns that should be identical except for, perhaps,
the running times at the bottom. If the columns differ, though, you’ll
see a `>`{.highlighter-rouge} or `|`{.highlighter-rouge} where they
differ. For instance, if you see

```{.highlight}
MISSPELLED WORDS                                                MISSPELLED WORDS

TECHNO                                                          TECHNO
L                                                               L
                                                              > Thelonious
Prius                                                           Prius
                                                              > MIA
L                                                               L
```

that means your program (whose output is on the left) does not think
that `Thelonious`{.highlighter-rouge} or `MIA`{.highlighter-rouge} is
misspelled, even though the staff’s output (on the right) does, as is
implied by the absence of, say, `Thelonious`{.highlighter-rouge} in the
lefthand column and the presence of `Thelonious`{.highlighter-rouge} in
the righthand column.

### [`check50`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/5/speller/#check50)

To test your code less manually (though still not exhaustively), you may
also execute the below.

```{.highlight}
$ check50 cs50/problems/2020/x/speller
```

Note that `check50`{.highlighter-rouge} will also check for memory
leaks, so be sure you’ve run `valgrind`{.highlighter-rouge} as well.

## [Staff’s Solution](https://cs50.harvard.edu/x/2020/psets/5/speller/#staffs-solution)

How to assess just how fast (and correct) your code is? Well, as always,
feel free to play with the staff’s solution, as with the below, and
compare its numbers against yours.

```{.highlight}
$ ~cs50/2019/fall/pset5/speller texts/lalaland.txt
```

## [Big Board](https://cs50.harvard.edu/x/2020/psets/5/speller/#big-board)

And if you’d like to put your code to the test against classmates’ code
(just for fun), execute the command below to challenge the Big Board
before or after you submit.

Submit to Big Board

```{.highlight}
$ submit50 cs50/problems/2020/x/challenges/speller
```

Then visit the URL that `submit50`{.highlighter-rouge} outputs to see
where you rank!

**Important Note: Submitting to the Big Board is not the same thing as
submitting the problem set itself. To submit the problem set, complete
the How to Submit instructions in the next section.**

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/5/speller/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
$ submit50 cs50/problems/2020/x/speller
```
