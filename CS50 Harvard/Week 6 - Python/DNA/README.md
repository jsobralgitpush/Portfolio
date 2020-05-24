# [DNA](https://cs50.harvard.edu/x/2020/psets/6/dna/#dna)

Implement a program that identifies a person based on their DNA, per the
below.

```{.highlight}
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```

## [Getting Started](https://cs50.harvard.edu/x/2020/psets/6/dna/#getting-started)

Here’s how to download this problem into your own CS50 IDE. Log into
[CS50 IDE](https://ide.cs50.io/) and then, in a terminal window, execute
each of the below.

- \*\*Execute `cd`{.highlighter-rouge} to ensure that you’re in
  `~/`{.highlighter-rouge} (i.e., your home directory, aka
  `~`{.highlighter-rouge}).
- \*\*If you haven’t already, execute `mkdir pset6`{.highlighter-rouge}
  to make (i.e., create) a directory called
  `pset6`{.highlighter-rouge} in your home directory.
- \*\*Execute `cd pset6`{.highlighter-rouge} to change into (i.e., open)
  that directory.
- \*\*Execute
  `wget https://cdn.cs50.net/2019/fall/psets/6/dna/dna.zip`{.highlighter-rouge}
  to download a (compressed) ZIP file with this problem’s
  distribution.
- \*\*Execute `unzip dna.zip`{.highlighter-rouge} to uncompress that
  file.
- \*\*Execute `rm dna.zip`{.highlighter-rouge} followed by
  `yes`{.highlighter-rouge} or `y`{.highlighter-rouge} to delete that
  ZIP file.
- \*\*Execute `ls`{.highlighter-rouge}. You should see a directory
  called `dna`{.highlighter-rouge}, which was inside of that ZIP file.
- \*\*Execute `cd dna`{.highlighter-rouge} to change into that
  directory.
- \*\*Execute `ls`{.highlighter-rouge}. You should see a directory of
  sample `databases`{.highlighter-rouge} and a directory of sample
  `sequences`{.highlighter-rouge}.

## [Background](https://cs50.harvard.edu/x/2020/psets/6/dna/#background)

DNA, the carrier of genetic information in living things, has been used
in criminal justice for decades. But how, exactly, does DNA profiling
work? Given a sequence of DNA, how can forensic investigators identify
to whom it belongs?

Well, DNA is really just a sequence of molecules called nucleotides,
arranged into a particular shape (a double helix). Each nucleotide of
DNA contains one of four different bases: adenine (A), cytosine (C),
guanine (G), or thymine (T). Every human cell has billions of these
nucleotides arranged in sequence. Some portions of this sequence (i.e.
genome) are the same, or at least very similar, across almost all
humans, but other portions of the sequence have a higher genetic
diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short
Tandem Repeats (STRs). An STR is a short sequence of DNA bases that
tends to repeat consecutively numerous times at specific locations
inside of a person’s DNA. The number of times any particular STR repeats
varies a lot among individuals. In the DNA samples below, for example,
Alice has the STR `AGAT`{.highlighter-rouge} repeated four times in her
DNA, while Bob has the same STR repeated five times.

![Sample STRs](./week%206%20DNA%20-%20CS50x_files/strs.png)

Using multiple STRs, rather than just one, can improve the accuracy of
DNA profiling. If the probability that two people have the same number
of repeats for a single STR is 5%, and the analyst looks at 10 different
STRs, then the probability that two DNA samples match purely by chance
is about 1 in 1 quadrillion (assuming all STRs are independent of each
other). So if two DNA samples match in the number of repeats for each of
the STRs, the analyst can be pretty confident they came from the same
person. CODIS, The FBI’s [DNA
database](https://www.fbi.gov/services/laboratory/biometric-analysis/codis/codis-and-ndis-fact-sheet),
uses 20 different STRs as part of its DNA profiling process.

What might such a DNA database look like? Well, in its simplest form,
you could imagine formatting a DNA database as a CSV file, wherein each
row corresponds to an individual, and each column corresponds to a
particular STR.

```{.highlight}
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

The data in the above file would suggest that Alice has the sequence
`AGAT`{.highlighter-rouge} repeated 28 times consecutively somewhere in
her DNA, the sequence `AATG`{.highlighter-rouge} repeated 42 times, and
`TATC`{.highlighter-rouge} repeated 14 times. Bob, meanwhile, has those
same three STRs repeated 17 times, 22 times, and 19 times, respectively.
And Charlie has those same three STRs repeated 36, 18, and 25 times,
respectively.

So given a sequence of DNA, how might you identify to whom it belongs?
Well, imagine that you looked through the DNA sequence for the longest
consecutive sequence of repeated `AGAT`{.highlighter-rouge}s and found
that the longest sequence was 17 repeats long. If you then found that
the longest sequence of `AATG`{.highlighter-rouge} is 22 repeats long,
and the longest sequence of `TATC`{.highlighter-rouge} is 19 repeats
long, that would provide pretty good evidence that the DNA was Bob’s. Of
course, it’s also possible that once you take the counts for each of the
STRs, it doesn’t match anyone in your DNA database, in which case you
have no match.

In practice, since analysts know on which chromosome and at which
location in the DNA an STR will be found, they can localize their search
to just a narrow section of DNA. But we’ll ignore that detail for this
problem.

Your task is to write a program that will take a sequence of DNA and a
CSV file containing STR counts for a list of individuals and then output
to whom the DNA (most likely) belongs.

## [Specification](https://cs50.harvard.edu/x/2020/psets/6/dna/#specification)

In a file called `dna.py`{.highlighter-rouge} in
`~/pset6/dna/`{.highlighter-rouge}, implement a program that identifies
to whom a sequence of DNA belongs.

- \*\*The program should require as its first command-line argument the
  name of a CSV file containing the STR counts for a list of
  individuals and should require as its second command-line argument
  the name of a text file containing the DNA sequence to identify.
  - \*\*If your program is executed with the incorrect number of
    command-line arguments, your program should print an error
    message of your choice (with `print`{.highlighter-rouge}). If
    the correct number of arguments are provided, you may assume
    that the first argument is indeed the filename of a valid CSV
    file, and that the second argument is the filename of a valid
    text file.
- \*\*Your program should open the CSV file and read its contents into
  memory.
  - \*\*You may assume that the first row of the CSV file will be the
    column names. The first column will be the word
    `name`{.highlighter-rouge} and the remaining columns will be the
    STR sequences themselves.
- \*\*Your program should open the DNA sequence and read its contents
  into memory.
- \*\*For each of the STRs (from the first line of the CSV file), your
  program should compute the longest run of consecutive repeats of the
  STR in the DNA sequence to identify.
- \*\*If the STR counts match exactly with any of the individuals in the
  CSV file, your program should print out the name of the matching
  individual.
  - \*\*You may assume that the STR counts will not match more than
    one individual.
  - \*\*If the STR counts do not match exactly with any of the
    individuals in the CSV file, your program should print
    `"No match"`{.highlighter-rouge}.

## [Walkthrough](https://cs50.harvard.edu/x/2020/psets/6/dna/#walkthrough)

## [Usage](https://cs50.harvard.edu/x/2020/psets/6/dna/#usage)

Your program should behave per the example below:

```{.highlight}
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```

```{.highlight}
$ python dna.py
Usage: python dna.py data.csv sequence.txt
```

```{.highlight}
$ python dna.py data.csv
Usage: python dna.py data.csv sequence.txt
```

## [Hints](https://cs50.harvard.edu/x/2020/psets/6/dna/#hints)

- \*\*You may find Python’s
  [`csv`{.highlighter-rouge}](https://docs.python.org/3/library/csv.html)
  module helpful for reading CSV files into memory. You may want to
  take advantage of either
  [`csv.reader`{.highlighter-rouge}](https://docs.python.org/3/library/csv.html#csv.reader)
  or
  [`csv.DictReader`{.highlighter-rouge}](https://docs.python.org/3/library/csv.html#csv.DictReader).
- \*\*The
  [`open`{.highlighter-rouge}](https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files)
  and
  [`read`{.highlighter-rouge}](https://docs.python.org/3.3/tutorial/inputoutput.html#methods-of-file-objects)
  functions may prove useful for reading text files into memory.
- \*\*Consider what data structures might be helpful for keeping
  tracking of information in your program. A
  [`list`{.highlighter-rouge}](https://docs.python.org/3/tutorial/introduction.html#lists)
  or a
  [`dict`{.highlighter-rouge}](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  may prove useful.

## [Testing](https://cs50.harvard.edu/x/2020/psets/6/dna/#testing)

No `check50`{.highlighter-rouge} for this problem, but be sure to test
your code for each of the following.

- \*\*Run your program as
  `python dna.py databases/small.csv sequences/1.txt`{.highlighter-rouge}.
  Your program should output `Bob`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/small.csv sequences/2.txt`{.highlighter-rouge}.
  Your program should output `No match`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/small.csv sequences/3.txt`{.highlighter-rouge}.
  Your program should output `No match`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/small.csv sequences/4.txt`{.highlighter-rouge}.
  Your program should output `Alice`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/5.txt`{.highlighter-rouge}.
  Your program should output `Lavender`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/6.txt`{.highlighter-rouge}.
  Your program should output `Luna`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/7.txt`{.highlighter-rouge}.
  Your program should output `Ron`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/8.txt`{.highlighter-rouge}.
  Your program should output `Ginny`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/9.txt`{.highlighter-rouge}.
  Your program should output `Draco`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/10.txt`{.highlighter-rouge}.
  Your program should output `Albus`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/11.txt`{.highlighter-rouge}.
  Your program should output `Hermione`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/12.txt`{.highlighter-rouge}.
  Your program should output `Lily`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/13.txt`{.highlighter-rouge}.
  Your program should output `No match`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/14.txt`{.highlighter-rouge}.
  Your program should output `Severus`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/15.txt`{.highlighter-rouge}.
  Your program should output `Sirius`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/16.txt`{.highlighter-rouge}.
  Your program should output `No match`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/17.txt`{.highlighter-rouge}.
  Your program should output `Harry`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/18.txt`{.highlighter-rouge}.
  Your program should output `No match`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/19.txt`{.highlighter-rouge}.
  Your program should output `Fred`{.highlighter-rouge}.
- \*\*Run your program as
  `python dna.py databases/large.csv sequences/20.txt`{.highlighter-rouge}.
  Your program should output `No match`{.highlighter-rouge}.

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/6/dna/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/dna
```
