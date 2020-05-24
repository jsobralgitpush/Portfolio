# [Houses](https://cs50.harvard.edu/x/2020/psets/7/houses/#houses)

Implement a program to import student data into a database, and then
produce class rosters.

```{.highlight}
$ python import.py characters.csv
$ python roster.py Gryffindor

Lavender Brown, born 1979
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980
```

## [Getting Started](https://cs50.harvard.edu/x/2020/psets/7/houses/#getting-started)

Here’s how to download this problem into your own CS50 IDE. Log into
[CS50 IDE](https://ide.cs50.io/) and then, in a terminal window, execute
each of the below.

- \*\*Execute `cd`{.highlighter-rouge} to ensure that you’re in
  `~/`{.highlighter-rouge} (i.e., your home directory, aka
  `~`{.highlighter-rouge}).
- \*\*If you haven’t already, execute `mkdir pset7`{.highlighter-rouge}
  to make (i.e., create) a directory called
  `pset7`{.highlighter-rouge} in your home directory.
- \*\*Execute `cd pset7`{.highlighter-rouge} to change into (i.e., open)
  that directory.
- \*\*Execute
  `wget https://cdn.cs50.net/2019/fall/psets/7/houses/houses.zip`{.highlighter-rouge}
  to download a (compressed) ZIP file with this problem’s
  distribution.
- \*\*Execute `unzip houses.zip`{.highlighter-rouge} to uncompress that
  file.
- \*\*Execute `rm houses.zip`{.highlighter-rouge} followed by
  `yes`{.highlighter-rouge} or `y`{.highlighter-rouge} to delete that
  ZIP file.
- \*\*Execute `ls`{.highlighter-rouge}. You should see a directory
  called `houses`{.highlighter-rouge}, which was inside of that ZIP
  file.
- \*\*Execute `cd houses`{.highlighter-rouge} to change into that
  directory.
- \*\*Execute `ls`{.highlighter-rouge}. You should see a
  `characters.csv`{.highlighter-rouge} file and a
  `students.db`{.highlighter-rouge} database.

## [Background](https://cs50.harvard.edu/x/2020/psets/7/houses/#background)

Hogwarts is in need of a student database. For years, the professors
have been maintaing a CSV file containing all of the students’ names and
houses and years. But that file didn’t make it particularly easy to get
access to certain data, such as a roster of all the Ravenclaw students,
or an alphabetical listing of the students enrolled at the school.

The challenge ahead of you is to import all of the school’s data into a
SQLite database, and write a Python program to query that database to
get house rosters for each of the houses of Hogwarts.

## [Specification](https://cs50.harvard.edu/x/2020/psets/7/houses/#specification)

In `import.py`{.highlighter-rouge}, write a program that imports data
from a CSV spreadsheet.

- \*\*Your program should accept the name of a CSV file as a
  command-line argument.
  - \*\*If the incorrect number of command-line arguments are
    provided, your program should print an error and exit.
  - \*\*You may assume that the CSV file will exist, and will have
    columns `name`{.highlighter-rouge}, `house`{.highlighter-rouge},
    and `birth`{.highlighter-rouge}.
- \*\*For each student in the CSV file, insert the student into the
  `students`{.highlighter-rouge} table in the
  `students.db`{.highlighter-rouge} database.
  - \*\*While the CSV file provided to you has just a
    `name`{.highlighter-rouge} column, the database has separate
    columns for `first`{.highlighter-rouge},
    `middle`{.highlighter-rouge}, and `last`{.highlighter-rouge}
    names. You’ll thus want to first parse each name and separate it
    into first, middle, and last names. You may assume that each
    person’s name field will contain either two space-separated
    names (a first and last name) or three space-separated names (a
    first, middle, and last name). For students without a middle
    name, you should leave their `middle`{.highlighter-rouge} name
    field as `NULL`{.highlighter-rouge} in the table.

In `roster.py`{.highlighter-rouge}, write a program that prints a list
of students for a given house in alphabetical order.

- \*\*Your program should accept the name of a house as a command-line
  argument.
  - \*\*If the incorrect number of command-line arguments are
    provided, your program should print an error and exit.
- \*\*Your program should query the `students`{.highlighter-rouge} table
  in the `students.db`{.highlighter-rouge} database for all of the
  students in the specified house.
- \*\*Your program should then print out each student’s full name and
  birth year (formatted as, e.g.,
  `Harry James Potter, born 1980`{.highlighter-rouge} or
  `Luna Lovegood, born 1981`{.highlighter-rouge}).
  - \*\*Each student should be printed on their own line.
  - \*\*Students should be ordered by last name. For students with the
    same last name, they should be ordered by first name.

## [Walkthrough](https://cs50.harvard.edu/x/2020/psets/7/houses/#walkthrough)

## [Usage](https://cs50.harvard.edu/x/2020/psets/7/houses/#usage)

Your program should behave per the example below:

```{.highlight}
$ python import.py characters.csv
```

```{.highlight}
$ python roster.py Gryffindor
Hermione Jean Granger, born 1979
Harry James Potter, born 1980
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980
...
```

## [Hints](https://cs50.harvard.edu/x/2020/psets/7/houses/#hints)

- \*\*Recall that after you’ve imported `SQL`{.highlighter-rouge} from
  `cs50`{.highlighter-rouge}, you can set up a database connection
  using syntax like

```{.highlight}
db = SQL("sqlite:///students.db")
```

Then, you can use `db.execute`{.highlighter-rouge} to execute SQL
queries from inside of your Python script.

- \*\*Recall that when you call `db.execute`{.highlighter-rouge} and
  perform a `SELECT`{.highlighter-rouge} query, the return value will
  be a `list`{.highlighter-rouge} of rows that are returned, where
  each row is represented by a Python `dict`{.highlighter-rouge}.

## [Testing](https://cs50.harvard.edu/x/2020/psets/7/houses/#testing)

No `check50`{.highlighter-rouge} for this problem, but be sure to test
your code for each of the following.

```{.highlight}
$ python import.py characters.csv
$ python roster.py Gryffindor
Lavender Brown, born 1979
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980

$ python roster.py Hufflepuff
Hannah Abbott, born 1980
Susan Bones, born 1979
Cedric Diggory, born 1977
Justin Finch-Fletchley, born 1979
Ernest Macmillan, born 1980

$ python roster.py Ravenclaw
Terry Boot, born 1980
Mandy Brocklehurst, born 1979
Cho Chang, born 1979
Penelope Clearwater, born 1976
Michael Corner, born 1979
Roger Davies, born 1978
Marietta Edgecombe, born 1978
Anthony Goldstein, born 1980
Robert Hilliard, born 1974
Luna Lovegood, born 1981
Isobel MacDougal, born 1980
Padma Patil, born 1979
Lisa Turpin, born 1979

$ python roster.py Slytherin
Millicent Bulstrode, born 1979
Vincent Crabbe, born 1979
Tracey Davis, born 1980
Marcus Flint, born 1975
Gregory Goyle, born 1980
Terence Higgs, born 1979
Draco Lucius Malfoy, born 1980
Adelaide Murton, born 1982
Pansy Parkinson, born 1979
Adrian Pucey, born 1977
Blaise Zabini, born 1979
```

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/7/houses/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/houses
```
