# Usage
GUI: `python3 pyqueens` 
CLI: `python3 pyqueens/cli.py [-h] [-p | -q] [-c] size`

# CLI Usage
```
usage: cli.py [-h] [-w WEAKNESS] [-p | -q] [-c] size

positional arguments:
  size                  Size of board to use

optional arguments:
  -h, --help            show this help message and exit
  -w WEAKNESS, --weakness WEAKNESS
  -p, --pretty          print board in a visual format
  -q, --quiet           do not print solutions
  -c, --count           display the count with each solution
```
Weakness is a way to support the Weak Queens problem, where up to W queens can be colinear without
that particular board failing.