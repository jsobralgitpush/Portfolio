# [Readability](https://cs50.harvard.edu/x/2020/psets/2/readability/#readability)

Implement a program that computes the approximate grade level needed to
comprehend some text, per the below.

```{.highlight}
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

## [Reading Levels](https://cs50.harvard.edu/x/2020/psets/2/readability/#reading-levels)

According to
[Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html),
E.B. White’s “Charlotte’s Web” is between a second and fourth grade
reading level, and Lois Lowry’s “The Giver” is between an eighth grade
reading level and a twelfth grade reading level. What does it mean,
though, for a book to be at a “fourth grade reading level”?

Well, in many cases, a human expert might read a book and make a
decision on the grade for which they think the book is most appropriate.
But you could also imagine an algorithm attempting to figure out what
the reading level of a text is.

So what sorts of traits are characteristic of higher reading levels?
Well, longer words probably correlate with higher reading levels.
Likewise, longer sentences probably correlate with higher reading
levels, too. A number of “readability tests” have been developed over
the years, to give a formulaic process for computing the reading level
of a text.

One such readability test is the Coleman-Liau index. The Coleman-Liau
index of a text is designed to output what (U.S.) grade level is needed
to understand the text. The formula is:

```{.highlight}
index = 0.0588 * L - 0.296 * S - 15.8
```

Here, `L`{.highlighter-rouge} is the average number of letters per 100
words in the text, and `S`{.highlighter-rouge} is the average number of
sentences per 100 words in the text.

Let’s write a program called `readability`{.highlighter-rouge} that
takes a text and determines its reading level. For example, if user
types in a line from Dr. Seuss:

```{.highlight}
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

The text the user inputted has 65 letters, 4 sentences, and 14 words. 65
letters per 14 words is an average of about 464.29 letters per 100
words. And 4 sentences per 14 words is an average of about 28.57
sentences per 100 words. Plugged into the Coleman-Liau formula, and
rounded to the nearest whole number, we get an answer of 3: so this
passage is at a third grade reading level.

Let’s try another one:

```{.highlight}
$ ./readability
Text: Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.
Grade 5
```

This text has 214 letters, 4 sentences, and 56 words. That comes out to
about 382.14 letters per 100 words, and 7.14 sentences per 100 words.
Plugged into the Coleman-Liau formula, we get a fifth grade reading
level.

As the average number of letters and words per sentence increases, the
Coleman-Liau index gives the text a higher reading level. If you were to
take this paragraph, for instance, which has longer words and sentences
than either of the prior two examples, the formula would give the text
an eleventh grade reading level.

```{.highlight}
$ ./readability
Text: As the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level. If you were to take this paragraph, for instance, which has longer words and sentences than either of the prior two examples, the formula would give the text an eleventh grade reading level.
Grade 11
```

## [Specification](https://cs50.harvard.edu/x/2020/psets/2/readability/#specification)

Design and implement a program, `readability`{.highlighter-rouge}, that
computes the Coleman-Liau index of the text.

- \*\*Implement your program in a file called
  `readability.c`{.highlighter-rouge} in a directory called
  `readability`{.highlighter-rouge}.
- \*\*Your program must prompt the user for a
  `string`{.highlighter-rouge} of text (using
  `get_string`{.highlighter-rouge}).
- \*\*Your program should count the number of letters, words, and
  sentences in the text. You may assume that a letter is any lowercase
  character from `a`{.highlighter-rouge} to `z`{.highlighter-rouge} or
  any uppercase character from `A`{.highlighter-rouge} to
  `Z`{.highlighter-rouge}, any sequence of characters separated by
  spaces should count as a word, and that any occurrence of a period,
  exclamation point, or question mark indicates the end of a sentence.
- \*\*Your program should print as output
  `"Grade X"`{.highlighter-rouge} where `X`{.highlighter-rouge} is the
  grade level computed by the Coleman-Liau formula, rounded to the
  nearest integer.
- \*\*If the resulting index number is 16 or higher (equivalent to or
  greater than a senior undergraduate reading level), your program
  should output `"Grade 16+"`{.highlighter-rouge} instead of giving
  the exact index number. If the index number is less than 1, your
  program should output `"Before Grade 1"`{.highlighter-rouge}.

### [Getting Started](https://cs50.harvard.edu/x/2020/psets/2/readability/#getting-started)

Log into [CS50 IDE](https://ide.cs50.io/) and then, in a terminal
window, execute each of the below.

- \*\*Execute `cd`{.highlighter-rouge} to ensure that you’re in
  `~/`{.highlighter-rouge} (i.e., your home directory).
- \*\*Execute `mkdir readability`{.highlighter-rouge} to make (i.e.,
  create) a directory called `readability`{.highlighter-rouge} in your
  home directory.
- \*\*Execute `cd readability`{.highlighter-rouge} to change into (i.e.,
  open) your new `readability`{.highlighter-rouge} directory.
- \*\*Execute `open readability.c`{.highlighter-rouge} to create and
  open in the editor an empty file called
  `readability.c`{.highlighter-rouge} in your
  `readability`{.highlighter-rouge} directory.

### [Getting User Input](https://cs50.harvard.edu/x/2020/psets/2/readability/#getting-user-input)

Let’s first write some C code that just gets some text input from the
user, and prints it back out. Specifically, write code in
`readability.c`{.highlighter-rouge} such that when the user runs the
program, they are prompted with `"Text: "`{.highlighter-rouge} to enter
some text.

The behavior of the resulting program should be like the below.

```{.highlight}
$ ./readability
Text: In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
```

### [Letters](https://cs50.harvard.edu/x/2020/psets/2/readability/#letters)

Now that you’ve collected input from the user, let’s begin to analyze
that input by first counting the number of letters that show up in the
text. Modify `readability.c`{.highlighter-rouge} so that, instead of
printing out the literal text itself, it instead prints out a count of
the number of letters in the text.

The behavior of the resulting program should be like the below.

```{.highlight}
$ ./readability
Text: Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"
235 letter(s)
```

Letters can be any uppercase or lowercase alphabetic characters, but
shouldn’t include any punctuation, digits, or other symbols.

You can reference [https://man.cs50.io/](https://man.cs50.io/) for
standard library functions that may help you here! You may also find
that writing a separate function, like
`count_letters`{.highlighter-rouge}, may be useful to keep your code
organized.

### [Words](https://cs50.harvard.edu/x/2020/psets/2/readability/#words)

The Coleman-Liau index cares not only about the number of letters, but
also the number of words in a sentence. For the purpose of this problem,
we’ll consider any sequence of characters separated by a space to be a
word (so a hyphenated word like `"sister-in-law"`{.highlighter-rouge}
should be considered one word, not three).

Modify `readability.c`{.highlighter-rouge} so that, in addition to
printing out the number of letters in the text, also prints out the
number of words in the text.

You may assume that a sentence will not start or end with a space, and
you may assume that a sentence will not have multiple spaces in a row.

The behavior of the resulting program should be like the below.

```{.highlight}
$ ./readability
Text: It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.
250 letter(s)
55 word(s)
```

### [Sentences](https://cs50.harvard.edu/x/2020/psets/2/readability/#sentences)

The last piece of information that the Coleman-Liau formula cares about,
in addition to the number of letters and words, is the number of
sentences. Determining the number of sentences can be surprisingly
trickly. You might first imagine that a sentence is just any sequence of
characters that ends with a period, but of course sentences could end
with an exclamation point or a question mark as well. But of course, not
all periods necessarily mean the sentence is over. For instance,
consider the sentence below.

```{.highlight}
Mr. and Mrs. Dursley, of number four Privet Drive, were proud to say that they were perfectly normal, thank you very much.
```

This is just a single sentence, but there are three periods! For this
problem, we’ll ask you to ignore that subtlety: you should consider any
sequence of characters that ends with a `.`{.highlighter-rouge} or a
`!`{.highlighter-rouge} or a `?`{.highlighter-rouge} to be a sentence
(so for the above “sentence”, you may count that as three sentences). In
practice, sentence boundary detection needs to be a little more
intelligent to handle these cases, but we’ll not worry about that for
now.

Modify `readability.c`{.highlighter-rouge} so that it also now prints
out the number of sentences in the text.

The behavior of the resulting program should be like the below.

```{.highlight}
$ ./readability
Text: When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.
295 letter(s)
70 word(s)
3 sentence(s)
```

### [Putting it All Together](https://cs50.harvard.edu/x/2020/psets/2/readability/#putting-it-all-together)

Now it’s time to put all the pieces together! Recall that the
Coleman-Liau index is computed using the formula:

```{.highlight}
index = 0.0588 * L - 0.296 * S - 15.8
```

where `L`{.highlighter-rouge} is the average number of letters per 100
words in the text, and `S`{.highlighter-rouge} is the average number of
sentences per 100 words in the text.

Modify `readability.c`{.highlighter-rouge} so that instead of outputting
the number of letters, words, and sentences, it instead outputs the
grade level as given by the Coleman-Liau index (e.g.
`"Grade 2"`{.highlighter-rouge} or `"Grade 8"`{.highlighter-rouge}). Be
sure to round the resulting index number to the nearest whole number!

If the resulting index number is 16 or higher (equivalent to or greater
than a senior undergraduate reading level), your program should output
`"Grade 16+"`{.highlighter-rouge} instead of giving the exact index
number. If the index number is less than 1, your program should output
`"Before Grade 1"`{.highlighter-rouge}.

Hints

- \*\*

  Recall that `math.h`{.highlighter-rouge} declares a function called
  `round`{.highlighter-rouge} that might be useful here.

- \*\*

  Recall that, when dividing values of type `int`{.highlighter-rouge}
  in C, the result will also be an `int`{.highlighter-rouge}, with any
  remainder (i.e., digits after the decimal point) discarded. Put
  another way, the result will be “truncated.” You might want to cast
  your one or more values to `float`{.highlighter-rouge} before
  performing division when calculating `L`{.highlighter-rouge} and
  `S`{.highlighter-rouge}!

## [Walkthrough](https://cs50.harvard.edu/x/2020/psets/2/readability/#walkthrough)

Note that while the walkthrough illustrates that words may be separated
by more than one space, you may assume, per the specifications above,
that no sentences will contain more than one space in a row.

## [How to Test Your Code](https://cs50.harvard.edu/x/2020/psets/2/readability/#how-to-test-your-code)

Try running your program on the following texts.

- \*\*`One fish. Two fish. Red fish. Blue fish.`{.highlighter-rouge}
  (Before Grade 1)
- \*\*`Would you like them here or there? I would not like them here or there. I would not like them anywhere.`{.highlighter-rouge}
  (Grade 2)
- \*\*`Congratulations! Today is your day. You're off to Great Places! You're off and away!`{.highlighter-rouge}
  (Grade 3)
- \*\*`Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.`{.highlighter-rouge}
  (Grade 5)
- \*\*`In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.`{.highlighter-rouge}
  (Grade 7)
- \*\*`Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"`{.highlighter-rouge}
  (Grade 8)
- \*\*`When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.`{.highlighter-rouge}
  (Grade 8)
- \*\*`There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.`{.highlighter-rouge}
  (Grade 9)
- \*\*`It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.`{.highlighter-rouge}
  (Grade 10)
- \*\*`A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.`{.highlighter-rouge}
  (Grade 16+)

Execute the below to evaluate the correctness of your code using
`check50`{.highlighter-rouge}. But be sure to compile and test it
yourself as well!

```{.highlight}
check50 cs50/problems/2020/x/readability
```

Execute the below to evaluate the style of your code using
`style50`{.highlighter-rouge}.

```{.highlight}
style50 readability.c
```

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/2/readability/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/readability
```
