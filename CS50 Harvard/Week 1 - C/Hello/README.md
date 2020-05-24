[This is CS50x](https://cs50.harvard.edu/x/2020/) {data-id="this-is-cs50x"}
=================================================

OpenCourseWare

[David J. Malan](https://cs.harvard.edu/malan/)\
 [malan@harvard.edu](mailto:malan@harvard.edu)\
 [**](https://www.facebook.com/dmalan) [**](https://github.com/dmalan)
[**](https://www.instagram.com/davidjmalan/)
[**](https://www.linkedin.com/in/malan/)
[**](https://www.quora.com/profile/David-J-Malan)
[**](https://twitter.com/davidjmalan)

Menu

* * * * *

-   **[CS50x Puzzle Day 2020](https://cs50.harvard.edu/x/2020/puzzles/)
    **

* * * * *

-   **[Week 0](https://cs50.harvard.edu/x/2020/weeks/0/) Scratch **😺**
-   **[Week 1](https://cs50.harvard.edu/x/2020/weeks/1/) C
-   **[Week 2](https://cs50.harvard.edu/x/2020/weeks/2/) Arrays
-   **[Week 3](https://cs50.harvard.edu/x/2020/weeks/3/) Algorithms
-   **[Week 4](https://cs50.harvard.edu/x/2020/weeks/4/) Memory
-   **[Week 5](https://cs50.harvard.edu/x/2020/weeks/5/) Data Structures
-   **[Week 6](https://cs50.harvard.edu/x/2020/weeks/6/) Python **🐍**
-   **[Week 7](https://cs50.harvard.edu/x/2020/weeks/7/) SQL
-   **

    [Week 8](https://cs50.harvard.edu/x/2020/weeks/8/) Information

-   **[Tracks](https://cs50.harvard.edu/x/2020/tracks/)
-   **[Android](https://cs50.harvard.edu/x/2020/tracks/mobile/android/)
-   **[Games](https://cs50.harvard.edu/x/2020/tracks/games/)
-   **[iOS](https://cs50.harvard.edu/x/2020/tracks/mobile/ios/)
-   **

    [Web](https://cs50.harvard.edu/x/2020/tracks/web/)

-   **[Final Project](https://cs50.harvard.edu/x/2020/project/)

* * * * *

[CS50 Certificate](https://cs50.harvard.edu/x/2020/certificate/)

* * * * *

-   **[Ed Discussion](https://cs50.harvard.edu/x/ed) for Q&A
-   **[Quick Start
    Guide](https://cs50.harvard.edu/x/2020/quickstart.pdf)
-   **[FAQs](https://cs50.harvard.edu/x/2020/faqs/)
-   **[Staff](https://cs50.harvard.edu/x/2020/staff/)

* * * * *

-   **[edX](https://cs50.edx.org/)
-   **[iTunes U](https://cs50.harvard.edu/x/2020/psets/1/hello/#)
-   **[YouTube](https://www.youtube.com/playlist?list=PLhQjrBD2T381L3iZyDTxRwOBuUt6m1FnW)

* * * * *

-   **[CS50 IDE](https://ide.cs50.io/)
-   **[Gradebook](https://cs50.me/cs50x)
-   **[Manual Pages](https://man.cs50.io/)
-   **[Python Documentation](https://docs.python.org/3.7/search.html)
-   **[Style Guide](https://cs50.readthedocs.io/style/c/)
-   **[Syllabus](https://cs50.harvard.edu/x/2020/syllabus/)

* * * * *

-   **[Discord](https://discord.gg/T8QZqRx)
-   **[Facebook Group](https://www.facebook.com/groups/cs50/)
-   **[Facebook Page](https://www.facebook.com/cs50/)
-   **[GitHub](https://github.com/cs50)
-   **[Gitter](https://gitter.im/cs50/x)
-   **[Instagram](https://instagram.com/cs50)
-   **[LinkedIn Group](https://www.linkedin.com/groups/7437240/)
-   **[LinkedIn Page](https://www.linkedin.com/school/cs50/)
-   **[Quora](https://www.quora.com/topic/CS50)
-   **[Slack](https://cs50.edx.org/slack)
-   **[Snapchat](https://www.snapchat.com/add/cs50)
-   **[Twitter](https://twitter.com/cs50)
-   **[YouTube](http://www.youtube.com/subscription_center?add_user=cs50tv)

* * * * *

[![Harvard
Shop](./Hello%20-%20CS50x_files/GGMdcKt.png)](https://cs50.harvardshop.com/)

* * * * *

[CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/)

[Hello](https://cs50.harvard.edu/x/2020/psets/1/hello/#hello)
=============================================================

If you already started to work on Problem Set 1 in CS50 Lab, you may
[continue working on it](https://lab.cs50.io/cs50/labs/2020/x/hello/)
there. If you’re just now starting to work in this problem, be sure to
use CS50 IDE instead by following the instructions below!

[Getting Started](https://cs50.harvard.edu/x/2020/psets/1/hello/#getting-started)
---------------------------------------------------------------------------------

CS50 IDE is a web-based “integrated development environment” that allows
you to program “in the cloud,” without installing any software locally.
Indeed, CS50 IDE provides you with your very own “workspace” (i.e.,
storage space) in which you can save your own files and folders (aka
directories).

### [Logging In](https://cs50.harvard.edu/x/2020/psets/1/hello/#logging-in)

Head to [ide.cs50.io](https://ide.cs50.io/) and click “Sign in with
GitHub” to access your CS50 IDE. Once your IDE loads, you should see
that (by default) it’s divided into three parts. Toward the top of CS50
IDE is your “text editor”, where you’ll write all of your programs.
Toward the bottom of is a “terminal window” (light blue, by default), a
command-line interface (CLI) that allows you to explore your workspace’s
files and directories, compile code, run programs, and even install new
software. And on the left is your “file browser”, which shows you all of
the files and folders currently in your IDE.

Start by clicking inside your terminal window. You should find that its
“prompt” resembles the below.

``` {.highlight}
~/ $
```

Click inside of that terminal window and then type

``` {.highlight}
mkdir ~/pset1/
```

followed by Enter in order to make a directory (i.e., folder) called
`pset1`{.highlighter-rouge} in your home directory. Take care not to
overlook the space between `mkdir`{.highlighter-rouge} and
`~/pset1`{.highlighter-rouge} or any other character for that matter!
Keep in mind that `~`{.highlighter-rouge} denotes your home directory
and `~/pset1`{.highlighter-rouge} denotes a directory called
`pset1`{.highlighter-rouge} within `~`{.highlighter-rouge}.

Here on out, to execute (i.e., run) a command means to type it into a
terminal window and then hit Enter. Commands are “case-sensitive,” so be
sure not to type in uppercase when you mean lowercase or vice versa.

Now execute

``` {.highlight}
cd ~/pset1/
```

to move yourself into (i.e., open) that directory. Your prompt should
now resemble the below.

``` {.highlight}
~/pset1/ $
```

If not, retrace your steps and see if you can determine where you went
wrong.

Now execute

``` {.highlight}
mkdir ~/pset1/hello
```

to create a new directory called `hello`{.highlighter-rouge} inside of
your `pset1`{.highlighter-rouge} directory. Then execute

``` {.highlight}
cd ~/pset1/hello
```

to move yourself into that directory.

Shall we have you write your first program? From the *File* menu, click
*New File*, and save it (as via the *Save* option in the *File* menu) as
`hello.c`{.highlighter-rouge} inside of your
`~/pset1/hello`{.highlighter-rouge} directory. Proceed to write your
first program by typing precisely these lines into the file:

``` {.highlight}
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

Notice how CS50 IDE adds “syntax highlighting” (i.e., color) as you
type, though CS50 IDE’s choice of colors might differ from this problem
set’s. Those colors aren’t actually saved inside of the file itself;
they’re just added by CS50 IDE to make certain syntax stand out. Had you
not saved the file as `hello.c`{.highlighter-rouge} from the start, CS50
IDE wouldn’t know (per the filename’s extension) that you’re writing C
code, in which case those colors would be absent.

[Listing Files](https://cs50.harvard.edu/x/2020/psets/1/hello/#listing-files)
-----------------------------------------------------------------------------

Next, in your terminal window, immediately to the right of the prompt
(`~/pset1/hello/ $`{.highlighter-rouge}), execute

``` {.highlight}
ls
```

You should see just `hello.c`{.highlighter-rouge}? That’s because you’ve
just listed the files in your `hello`{.highlighter-rouge} folder. In
particular, you *executed* (i.e., ran) a command called
`ls`{.highlighter-rouge}, which is shorthand for “list.” (It’s such a
frequently used command that its authors called it just
`ls`{.highlighter-rouge} to save keystrokes.) Make sense?

[Compiling Programs](https://cs50.harvard.edu/x/2020/psets/1/hello/#compiling-programs)
---------------------------------------------------------------------------------------

Now, before we can execute the `hello.c`{.highlighter-rouge} program,
recall that we must *compile* it with a *compiler* (e.g.,
`clang`{.highlighter-rouge}), translating it from *source code* into
*machine code* (i.e., zeroes and ones). Execute the command below to do
just that:

``` {.highlight}
clang hello.c
```

And then execute this one again:

``` {.highlight}
ls
```

This time, you should see not only `hello.c`{.highlighter-rouge} but
`a.out`{.highlighter-rouge} listed as well? (You can see the same
graphically if you click that folder icon again.) That’s because
`clang`{.highlighter-rouge} has translated the source code in
`hello.c`{.highlighter-rouge} into machine code in
`a.out`{.highlighter-rouge}, which happens to stand for “assembler
output,” but more on that another time.

Now run the program by executing the below.

``` {.highlight}
./a.out
```

Hello, world, indeed!

[Naming Programs](https://cs50.harvard.edu/x/2020/psets/1/hello/#naming-programs)
---------------------------------------------------------------------------------

Now, `a.out`{.highlighter-rouge} isn’t the most user-friendly name for a
program. Let’s compile `hello.c`{.highlighter-rouge} again, this time
saving the machine code in a file called, more aptly,
`hello`{.highlighter-rouge}. Execute the below.

``` {.highlight}
clang -o hello hello.c
```

Take care not to overlook any of those spaces therein! Then execute this
one again:

``` {.highlight}
ls
```

You should now see not only `hello.c`{.highlighter-rouge} (and
`a.out`{.highlighter-rouge} from before) but also
`hello`{.highlighter-rouge} listed as well? That’s because
`-o`{.highlighter-rouge} is a *command-line argument*, sometimes known
as a *flag* or a *switch*, that tells `clang`{.highlighter-rouge} to
output (hence the `o`{.highlighter-rouge}) a file called
`hello`{.highlighter-rouge}. Execute the below to try out the newly
named program.

``` {.highlight}
./hello
```

Hello there again!

[Making Things Easier](https://cs50.harvard.edu/x/2020/psets/1/hello/#making-things-easier)
-------------------------------------------------------------------------------------------

Recall that we can automate the process of executing
`clang`{.highlighter-rouge}, letting `make`{.highlighter-rouge} figure
out how to do so for us, thereby saving us some keystrokes. Execute the
below to compile this program one last time.

``` {.highlight}
make hello
```

You should see that `make`{.highlighter-rouge} executes
`clang`{.highlighter-rouge} with even more command-line arguments for
you? More on those, too, another time!

Now execute the program itself one last time by executing the below.

``` {.highlight}
./hello
```

Phew!

[Getting User Input](https://cs50.harvard.edu/x/2020/psets/1/hello/#getting-user-input)
---------------------------------------------------------------------------------------

Suffice it to say, no matter how you compile or execute this program, it
only ever prints `hello, world`{.highlighter-rouge}. Let’s personalize
it a bit, just as we did in class.

Modify this program in such a way that it first prompts the user for
their name and then prints `hello, so-and-so`{.highlighter-rouge}, where
`so-and-so`{.highlighter-rouge} is their actual name.

As before, be sure to compile your program with:

``` {.highlight}
make hello
```

And be sure to execute your program, testing it a few times with
different inputs, with:

``` {.highlight}
./hello
```

### [Walkthrough](https://cs50.harvard.edu/x/2020/psets/1/hello/#walkthrough)

### [Hints](https://cs50.harvard.edu/x/2020/psets/1/hello/#hints)

#### [Don’t recall how to prompt the user for their name?](https://cs50.harvard.edu/x/2020/psets/1/hello/#dont-recall-how-to-prompt-the-user-for-their-name)

Recall that you can use `get_string`{.highlighter-rouge} as follows,
storing its *return value* in a variable called
`name`{.highlighter-rouge} of type `string`{.highlighter-rouge}.

``` {.highlight}
string name = get_string("What is your name?\n");
```

#### [Don’t recall how to format a string?](https://cs50.harvard.edu/x/2020/psets/1/hello/#dont-recall-how-to-format-a-string)

Don’t recall how to join (i.e., concatenate) the user’s name with a
greeting? Recall that you can use `printf`{.highlighter-rouge} not only
to print but to format a string (hence, the `f`{.highlighter-rouge} in
`printf`{.highlighter-rouge}), a la the below, wherein
`name`{.highlighter-rouge} is a `string`{.highlighter-rouge}.

``` {.highlight}
printf("hello, %s\n", name);
```

#### [Use of undeclared identifier?](https://cs50.harvard.edu/x/2020/psets/1/hello/#use-of-undeclared-identifier)

Seeing the below, perhaps atop other errors?

``` {.highlight}
error: use of undeclared identifier 'string'; did you mean 'stdin'?
```

Recall that, to use `get_string`{.highlighter-rouge}, you need to
include `cs50.h`{.highlighter-rouge} (in which
`get_string`{.highlighter-rouge} is *declared*) atop a file, as with:

``` {.highlight}
#include <cs50.h>
```

### [How to Test Your Code](https://cs50.harvard.edu/x/2020/psets/1/hello/#how-to-test-your-code)

Execute the below to evaluate the correctness of your code using
`check50`{.highlighter-rouge}. But be sure to compile and test it
yourself as well!

``` {.highlight}
check50 cs50/problems/2020/x/hello
```

Execute the below to evaluate the style of your code using
`style50`{.highlighter-rouge}.

``` {.highlight}
style50 hello.c
```

[How to Submit](https://cs50.harvard.edu/x/2020/psets/1/hello/#how-to-submit)
-----------------------------------------------------------------------------

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

``` {.highlight}
submit50 cs50/problems/2020/x/hello
```
