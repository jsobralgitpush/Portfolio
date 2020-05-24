# [Filter](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#filter)

Implement a program that applies filters to BMPs, per the below.

```{.highlight}
$ ./filter -r image.bmp reflected.bmp
```

## [Background](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#background)

### [Bitmaps](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#bitmaps)

Perhaps the simplest way to represent an image is with a grid of pixels
(i.e., dots), each of which can be of a different color. For
black-and-white images, we thus need 1 bit per pixel, as 0 could
represent black and 1 could represent white, as in the below.

![a simple bitmap](./week%204%20Filter%20-%20CS50x_files/bitmap.png)

In this sense, then, is an image just a bitmap (i.e., a map of bits).
For more colorful images, you simply need more bits per pixel. A file
format (like [BMP](https://en.wikipedia.org/wiki/BMP_file_format),
[JPEG](https://en.wikipedia.org/wiki/JPEG), or
[PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) that
supports “24-bit color” uses 24 bits per pixel. (BMP actually supports
1-, 4-, 8-, 16-, 24-, and 32-bit color.)

A 24-bit BMP uses 8 bits to signify the amount of red in a pixel’s
color, 8 bits to signify the amount of green in a pixel’s color, and 8
bits to signify the amount of blue in a pixel’s color. If you’ve ever
heard of RGB color, well, there you have it: red, green, blue.

If the R, G, and B values of some pixel in a BMP are, say,
`0xff`{.highlighter-rouge}, `0x00`{.highlighter-rouge}, and
`0x00`{.highlighter-rouge} in hexadecimal, that pixel is purely red, as
`0xff`{.highlighter-rouge} (otherwise known as `255`{.highlighter-rouge}
in decimal) implies “a lot of red,” while `0x00`{.highlighter-rouge} and
`0x00`{.highlighter-rouge} imply “no green” and “no blue,” respectively.

### [A Bit(map) More Technical](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#a-bitmap-more-technical)

Recall that a file is just a sequence of bits, arranged in some fashion.
A 24-bit BMP file, then, is essentially just a sequence of bits,
(almost) every 24 of which happen to represent some pixel’s color. But a
BMP file also contains some “metadata,” information like an image’s
height and width. That metadata is stored at the beginning of the file
in the form of two data structures generally referred to as “headers,”
not to be confused with C’s header files. (Incidentally, these headers
have evolved over time. This problem uses the latest version of
Microsoft’s BMP format, 4.0, which debuted with Windows 95.)

The first of these headers, called
`BITMAPFILEHEADER`{.highlighter-rouge}, is 14 bytes long. (Recall that 1
byte equals 8 bits.) The second of these headers, called
`BITMAPINFOHEADER`{.highlighter-rouge}, is 40 bytes long. Immediately
following these headers is the actual bitmap: an array of bytes, triples
of which represent a pixel’s color. However, BMP stores these triples
backwards (i.e., as BGR), with 8 bits for blue, followed by 8 bits for
green, followed by 8 bits for red. (Some BMPs also store the entire
bitmap backwards, with an image’s top row at the end of the BMP file.
But we’ve stored this problem set’s BMPs as described herein, with each
bitmap’s top row first and bottom row last.) In other words, were we to
convert the 1-bit smiley above to a 24-bit smiley, substituting red for
black, a 24-bit BMP would store this bitmap as follows, where
`0000ff`{.highlighter-rouge} signifies red and
`ffffff`{.highlighter-rouge} signifies white; we’ve highlighted in red
all instances of `0000ff`{.highlighter-rouge}.

![red smile](./week%204%20Filter%20-%20CS50x_files/red_smile.png)

Because we’ve presented these bits from left to right, top to bottom, in
8 columns, you can actually see the red smiley if you take a step back.

To be clear, recall that a hexadecimal digit represents 4 bits.
Accordingly, `ffffff`{.highlighter-rouge} in hexadecimal actually
signifies `111111111111111111111111`{.highlighter-rouge} in binary.

Notice that you could represent a bitmap as a 2-dimensional array of
pixels: where the image is an array of rows, each row is an array of
pixels. Indeed, that’s how we’ve chosen to represent bitmap images in
this problem.

### [Image Filtering](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#image-filtering)

What does it even mean to filter an image? You can think of filtering an
image as taking the pixels of some original image, and modifying each
pixel in such a way that a particular effect is apparent in the
resulting image.

#### [Grayscale](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#grayscale)

One common filter is the “grayscale” filter, where we take an image and
want to convert it to black-and-white. How does that work?

Recall that if the red, green, and blue values are all set to
`0x00`{.highlighter-rouge} (hexadecimal for `0`{.highlighter-rouge}),
then the pixel is black. And if all values are set to
`0xff`{.highlighter-rouge} (hexadecimal for `255`{.highlighter-rouge}),
then the pixel is white. So long as the red, green, and blue values are
all equal, the result will be varying shades of gray along the
black-white spectrum, with higher values meaning lighter shades (closer
to white) and lower values meaning darker shades (closer to black).

So to convert a pixel to grayscale, we just need to make sure the red,
green, and blue values are all the same value. But how do we know what
value to make them? Well, it’s probably reasonable to expect that if the
original red, green, and blue values were all pretty high, then the new
value should also be pretty high. And if the original values were all
low, then the new value should also be low.

In fact, to ensure each pixel of the new image still has the same
general brightness or darkness as the old image, we can take the average
of the red, green, and blue values to determine what shade of grey to
make the new pixel.

If you apply that to each pixel in the image, the result will be an
image converted to grayscale.

#### [Sepia](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#sepia)

Most image editing programs support a “sepia” filter, which gives images
an old-timey feel by making the whole image look a bit reddish-brown.

An image can be converted to sepia by taking each pixel, and computing
new red, green, and blue values based on the original values of the
three.

There are a number of algorithms for converting an image to sepia, but
for this problem, we’ll ask you to use the following algorithm. For each
pixel, the sepia color values should be calculated based on the original
color values per the below.

```{.highlight}
  sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
  sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
  sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
```

Of course, the result of each of these formulas may not be an integer,
but each value could be rounded to the nearest integer. It’s also
possible that the result of the formula is a number greater than 255,
the maximum value for an 8-bit color value. In that case, the red,
green, and blue values should be capped at 255. As a result, we can
guarantee that the resulting red, green, and blue values will be whole
numbers between 0 and 255, inclusive.

#### [Reflection](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#reflection)

Some filters might also move pixels around. Reflecting an image, for
example, is a filter where the resulting image is what you would get by
placing the original image in front of a mirror. So any pixels on the
left side of the image should end up on the right, and vice versa.

Note that all of the original pixels of the original image will still be
present in the reflected image, it’s just that those pixels may have
rearranged to be in a different place in the image.

#### [Blur](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#blur)

There are a number of ways to create the effect of blurring or softening
an image. For this problem, we’ll use the “box blur,” which works by
taking each pixel and, for each color value, giving it a new value by
averaging the color values of neighboring pixels.

Consider the following grid of pixels, where we’ve numbered each pixel.

![a grid of pixels](./week%204%20Filter%20-%20CS50x_files/grid.png)

The new value of each pixel would be the average of the values of all of
the pixels that are within 1 row and column of the original pixel
(forming a 3x3 box). For example, each of the color values for pixel 6
would be obtained by averaging the original color values of pixels 1, 2,
3, 5, 6, 7, 9, 10, and 11 (note that pixel 6 itself is included in the
average). Likewise, the color values for pixel 11 would be be obtained
by averaging the color values of pixels 6, 7, 8, 10, 11, 12, 14, 15 and 16.

For a pixel along the edge or corner, like pixel 15, we would still look
for all pixels within 1 row and column: in this case, pixels 10, 11, 12,
14, 15, and 16.

## [Getting Started](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#getting-started)

Here’s how to download this problem’s “distribution code” (i.e., starter
code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io/)
and then, in a terminal window, execute each of the below.

- \*\*Execute `cd`{.highlighter-rouge} to ensure that you’re in
  `~/`{.highlighter-rouge} (i.e., your home directory).
- \*\*Execute `mkdir pset4`{.highlighter-rouge} to make (i.e., create) a
  directory called `pset4`{.highlighter-rouge} in your home directory.
- \*\*Execute `cd pset4`{.highlighter-rouge} to change into (i.e., open)
  that directory.
- \*\*Execute
  `wget https://cdn.cs50.net/2019/fall/psets/4/filter/less/filter.zip`{.highlighter-rouge}
  to download a (compressed) ZIP file with this problem’s
  distribution.
- \*\*Execute `unzip filter.zip`{.highlighter-rouge} to uncompress that
  file.
- \*\*Execute `rm filter.zip`{.highlighter-rouge} followed by
  `yes`{.highlighter-rouge} or `y`{.highlighter-rouge} to delete that
  ZIP file.
- \*\*Execute `ls`{.highlighter-rouge}. You should see a directory
  called `filter`{.highlighter-rouge}, which was inside of that ZIP
  file.
- \*\*Execute `cd filter`{.highlighter-rouge} to change into that
  directory.
- \*\*Execute `ls`{.highlighter-rouge}. You should see this problem’s
  distribution, including `bmp.h`{.highlighter-rouge},
  `filter.c`{.highlighter-rouge}, `helpers.h`{.highlighter-rouge},
  `helpers.c`{.highlighter-rouge}, and `Makefile`{.highlighter-rouge}.
  You’ll also see a directory called `images`{.highlighter-rouge},
  with some sample Bitmap images.

## [Understanding](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#understanding)

Let’s now take a look at some of the files provided to you as
distribution code to get an understanding for what’s inside of them.

### [`bmp.h`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#bmph) {#bmph}

Open up `bmp.h`{.highlighter-rouge} (as by double-clicking on it in the
file browser) and have a look.

You’ll see definitions of the headers we’ve mentioned
(`BITMAPINFOHEADER`{.highlighter-rouge} and
`BITMAPFILEHEADER`{.highlighter-rouge}). In addition, that file defines
`BYTE`{.highlighter-rouge}, `DWORD`{.highlighter-rouge},
`LONG`{.highlighter-rouge}, and `WORD`{.highlighter-rouge}, data types
normally found in the world of Windows programming. Notice how they’re
just aliases for primitives with which you are (hopefully) already
familiar. It appears that `BITMAPFILEHEADER`{.highlighter-rouge} and
`BITMAPINFOHEADER`{.highlighter-rouge} make use of these types.

Perhaps most importantly for you, this file also defines a
`struct`{.highlighter-rouge} called `RGBTRIPLE`{.highlighter-rouge}
that, quite simply, “encapsulates” three bytes: one blue, one green, and
one red (the order, recall, in which we expect to find RGB triples
actually on disk).

Why are these `struct`{.highlighter-rouge}s useful? Well, recall that a
file is just a sequence of bytes (or, ultimately, bits) on disk. But
those bytes are generally ordered in such a way that the first few
represent something, the next few represent something else, and so on.
“File formats” exist because the world has standardized what bytes mean
what. Now, we could just read a file from disk into RAM as one big array
of bytes. And we could just remember that the byte at
`array[i]`{.highlighter-rouge} represents one thing, while the byte at
`array[j]`{.highlighter-rouge} represents another. But why not give some
of those bytes names so that we can retrieve them from memory more
easily? That’s precisely what the structs in `bmp.h`{.highlighter-rouge}
allow us to do. Rather than think of some file as one long sequence of
bytes, we can instead think of it as a sequence of
`struct`{.highlighter-rouge}s.

### [`filter.c`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#filterc) {#filterc}

Now, let’s open up `filter.c`{.highlighter-rouge}. This file has been
written already for you, but there are a couple important points worth
noting here.

First, notice the definition of `filters`{.highlighter-rouge} on line

11. That string tells the program what the allowable command-line
    arguments to the program are: `b`{.highlighter-rouge},
    `g`{.highlighter-rouge}, `r`{.highlighter-rouge}, and
    `s`{.highlighter-rouge}. Each of them specifies a different filter that
    we might apply to our images: blur, grayscale, reflection, and sepia.

The next several lines open up an image file, make sure it’s indeed a
BMP file, and read all of the pixel information into a 2D array called
`image`{.highlighter-rouge}.

Scroll down to the `switch`{.highlighter-rouge} statement that begins on
line 102. Notice that, depending on what `filter`{.highlighter-rouge}
we’ve chosen, a different function is called: if the user chooses filter
`b`{.highlighter-rouge}, the program calls the
`blur`{.highlighter-rouge} function; if `g`{.highlighter-rouge}, then
`grayscale`{.highlighter-rouge} is called; if `r`{.highlighter-rouge},
then `reflect`{.highlighter-rouge} is called; and if
`s`{.highlighter-rouge}, then `sepia`{.highlighter-rouge} is called.
Notice, too, that each of these functions take as arguments the height
of the image, the width of the image, and the 2D array of pixels.

These are the functions you’ll (soon!) implement. As you might imagine,
the goal is for each of these functions to edit the 2D array of pixels
in such a way that the desired filter is applied to the image.

The remaining lines of the program take the resulting
`image`{.highlighter-rouge} and write them out to a new image file.

### [`helpers.h`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#helpersh) {#helpersh}

Next, take a look at `helpers.h`{.highlighter-rouge}. This file is quite
short, and just provides the function prototypes for the functions you
saw earlier.

Here, take note of the fact that each function takes a 2D array called
`image`{.highlighter-rouge} as an argument, where
`image`{.highlighter-rouge} is an array of `height`{.highlighter-rouge}
many rows, and each row is itself another array of
`width`{.highlighter-rouge} many `RGBTRIPLE`{.highlighter-rouge}s. So if
`image`{.highlighter-rouge} represents the whole picture, then
`image[0]`{.highlighter-rouge} represents the first row, and
`image[0][0]`{.highlighter-rouge} represents the pixel in the upper-left
corner of the image.

### [`helpers.c`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#helpersc) {#helpersc}

Now, open up `helpers.c`{.highlighter-rouge}. Here’s where the
implementation of the functions declared in
`helpers.h`{.highlighter-rouge} belong. But note that, right now, the
implementations are missing! This part is up to you.

### [`Makefile`{.highlighter-rouge}](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#makefile)

Finally, let’s look at `Makefile`{.highlighter-rouge}. This file
specifies what should happen when we run a terminal command like
`make filter`{.highlighter-rouge}. Whereas programs you may have written
before were confined to just one file, `filter`{.highlighter-rouge}
seems to use multiple files: `filter.c`{.highlighter-rouge},
`bmp.h`{.highlighter-rouge}, `helpers.h`{.highlighter-rouge}, and
`helpers.c`{.highlighter-rouge}. So we’ll need to tell
`make`{.highlighter-rouge} how to compile this file.

Try compiling `filter`{.highlighter-rouge} for yourself by going to your
terminal and running

```{.highlight}
$ make filter
```

Then, you can run the program by running:

```{.highlight}
$ ./filter -g images/yard.bmp out.bmp
```

which takes the image at `images/yard.bmp`{.highlighter-rouge}, and
generates a new image called `out.bmp`{.highlighter-rouge} after running
the pixels through the `grayscale`{.highlighter-rouge} function.
`grayscale`{.highlighter-rouge} doesn’t do anything just yet, though, so
the output image should look the same as the original yard.

## [Specification](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#specification)

Implement the functions in `helpers.c`{.highlighter-rouge} such that a
user can apply grayscale, sepia, reflection, or blur filters to their
images.

- \*\*The function `grayscale`{.highlighter-rouge} should take an image
  and turn it into a black-and-white version of the same image.
- \*\*The function `sepia`{.highlighter-rouge} should take an image and
  turn it into a sepia version of the same image.
- \*\*The `reflect`{.highlighter-rouge} function should take an image
  and reflect it horizontally.
- \*\*Finally, the `blur`{.highlighter-rouge} function should take an
  image and turn it into a box-blurred version of the same image.

You should not modify any of the function signatures, nor should you
modify any other files other than `helpers.c`{.highlighter-rouge}.

## [Walkthrough](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#walkthrough)

## [Usage](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#usage)

Your program should behave per the examples below.

```{.highlight}
$ ./filter -g infile.bmp outfile.bmp
```

```{.highlight}
$ ./filter -s infile.bmp outfile.bmp
```

```{.highlight}
$ ./filter -r infile.bmp outfile.bmp
```

```{.highlight}
$ ./filter -b infile.bmp outfile.bmp
```

## [Hints](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#hints)

- \*\*The values of a pixel’s `rgbtRed`{.highlighter-rouge},
  `rgbtGreen`{.highlighter-rouge}, and `rgbtBlue`{.highlighter-rouge}
  components are all integers, so be sure to round any floating-point
  numbers to the nearest integer when assigning them to a pixel value!

## [Testing](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#testing)

Be sure to test all of your filters on the sample bitmap files provided!

Execute the below to evaluate the correctness of your code using
`check50`{.highlighter-rouge}. But be sure to compile and test it
yourself as well!

```{.highlight}
check50 cs50/problems/2020/x/filter/less
```

Execute the below to evaluate the style of your code using
`style50`{.highlighter-rouge}.

```{.highlight}
style50 helpers.c
```

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/4/filter/less/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/filter/less
```
