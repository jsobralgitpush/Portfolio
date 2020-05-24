# [Credit](https://cs50.harvard.edu/x/2020/psets/6/credit/#credit)

Implement a program that determines whether a provided credit card
number is valid according to Luhn’s algorithm.

```{.highlight}
$ python credit.py
Number: 378282246310005
AMEX
```

## [Specification](https://cs50.harvard.edu/x/2020/psets/6/credit/#specification)

- \*\*In `credit.py`{.highlighter-rouge} in
  `~/pset6/credit/`{.highlighter-rouge}, write a program that prompts
  the user for a credit card number and then reports (via
  `print`{.highlighter-rouge}) whether it is a valid American Express,
  MasterCard, or Visa card number, exactly as you did in [Problem Set
  1](https://cs50.harvard.edu/x/2020/psets/1/), except that your
  program this time should be written (a) in Python and (b) in CS50
  IDE.
- \*\*So that we can automate some tests of your code, we ask that your
  program’s last line of output be `AMEX\n`{.highlighter-rouge} or
  `MASTERCARD\n`{.highlighter-rouge} or `VISA\n`{.highlighter-rouge}
  or `INVALID\n`{.highlighter-rouge}, nothing more, nothing less.
- \*\*For simplicity, you may assume that the user’s input will be
  entirely numeric (i.e., devoid of hyphens, as might be printed on an
  actual card).
- \*\*Best to use `get_int`{.highlighter-rouge} or
  `get_string`{.highlighter-rouge} from CS50’s library to get users’
  input, depending on how you to decide to implement this one.

## [Usage](https://cs50.harvard.edu/x/2020/psets/6/credit/#usage)

Your program should behave per the example below.

```{.highlight}
$ python credit.py
Number: 378282246310005
AMEX
```

## [Testing](https://cs50.harvard.edu/x/2020/psets/6/credit/#testing)

No `check50`{.highlighter-rouge} for this problem, but be sure to test
your code for each of the following.

- \*\*Run your program as `python credit.py`{.highlighter-rouge}, and
  wait for a prompt for input. Type in
  `378282246310005`{.highlighter-rouge} and press enter. Your program
  should output `AMEX`{.highlighter-rouge}.
- \*\*Run your program as `python credit.py`{.highlighter-rouge}, and
  wait for a prompt for input. Type in
  `371449635398431`{.highlighter-rouge} and press enter. Your program
  should output `AMEX`{.highlighter-rouge}.
- \*\*Run your program as `python credit.py`{.highlighter-rouge}, and
  wait for a prompt for input. Type in
  `5555555555554444`{.highlighter-rouge} and press enter. Your program
  should output `MASTERCARD`{.highlighter-rouge}.
- \*\*Run your program as `python credit.py`{.highlighter-rouge}, and
  wait for a prompt for input. Type in
  `5105105105105100`{.highlighter-rouge} and press enter. Your program
  should output `MASTERCARD`{.highlighter-rouge}.
- \*\*Run your program as `python credit.py`{.highlighter-rouge}, and
  wait for a prompt for input. Type in
  `4111111111111111`{.highlighter-rouge} and press enter. Your program
  should output `VISA`{.highlighter-rouge}.
- \*\*Run your program as `python credit.py`{.highlighter-rouge}, and
  wait for a prompt for input. Type in
  `4012888888881881`{.highlighter-rouge} and press enter. Your program
  should output `VISA`{.highlighter-rouge}.
- \*\*Run your program as `python credit.py`{.highlighter-rouge}, and
  wait for a prompt for input. Type in
  `1234567890`{.highlighter-rouge} and press enter. Your program
  should output `INVALID`{.highlighter-rouge}.

## [How to Submit](https://cs50.harvard.edu/x/2020/psets/6/credit/#how-to-submit)

Execute the below, logging in with your GitHub username and password
when prompted. For security, you’ll see asterisks
(`*`{.highlighter-rouge}) instead of the actual characters in your
password.

```{.highlight}
submit50 cs50/problems/2020/x/sentimental/credit
```
