# Description
These python scripts use the `mrjob` package to search the GDELT data set for particular patterns or words. It then returns the number of times that word occurs inside files contained within the specified directory. 
There are two scripts that return a slightly different count. These are:

### line_count.py
The `line_count.py` script returns the number of lines where the word occurs. If the word occurs more than once in a line it will only be counted once.

### word_count.py
The `word_count.py` script returns the total amount of times the word occurs. If the word occurs eight times in a line it will be counted eight times.
___

# Inputs
Both programs take two string inputs. These inputs should be typed directly after the script name separated by a single space in the command line in the following order (see examples section):
1. A directory to search (eg. `/home/path/to/gdelt`)
2. A word to search for (eg. `Africa`)
___

# Output
The output will be a string of the following format:
`"word-that-was-searched"    count`
___

# Examples
### Linux:
#### Comand:
`python line_count.py /home/path/to/gdelt Africa`

#### Output:
`"Africa"        13045`

### Windows:
#### Comand:
`python word_count.py "C:\\path\to\gdelt" Africa`

#### Output:
`"Africa"        27693`
