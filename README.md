# Anagrams

Tool to assist in finding anagrams with certain minimum set of letters and optional set of letters. The results may be further refined using a regular expression.

## Author

Cyndi Cavanaugh
* [youtube.com/@cyndicorinne](https://www.youtube.com/@cyndicorinne)
* [github.com/cyndi5](https://github.com/cyndi5)

## Algorithm Explanation & Walkthrough Videos

* [Cynthia Computes Anagrams](https://youtu.be/b95GXI25u28)
* [Algorithms Python Code Walkthrough](https://youtu.be/SW1VT4__KJ4)

## Requirements

Python 3.11 (It should work on later Python 3 versions; it may work on earlier Python 3 versions as well.)

## Running the Program

All arguments except for `--minimum` are optional and have default values, as shown in the help message.

### `--help`

```
% python3 anagrams.py --help
usage: anagrams.py [-h] --minimum MINIMUM [--optional OPTIONAL]
                   [--regex REGEX] [--wordfile WORDFILE]

options:
  -h, --help           show this help message and exit
  --minimum MINIMUM    minimum string of characters which must be present (required)
  --optional OPTIONAL  optional string of characters to try (default: '')
  --regex REGEX        regex that has to match (default: '')
  --wordfile WORDFILE  word file (default: /usr/share/dict/words)
```

### `--minimum MINIMUM`

`MINIMUM` is the minimum string of characters which must be present in the word, in any order; e.g. 'de' == 'ed'. This argument is required.

```
% python3 anagrams.py --minimum dear
minimum=dear; optional=; wordfile=/usr/share/dict/words; regex=
dear:
  ['ared', 'daer', 'dare', 'dear', 'read']
```

### `--optional OPTIONAL`

`OPTIONAL` is the string of characters whose presence is optional in conjunction with the minimum string of characters. The search algorithm will try combining the minimum string with all optional characters and smaller subsets of them.

```
% python3 anagrams.py --minimum de --optional aer
minimum=de; optional=aer; wordfile=/usr/share/dict/words; regex=
deaer:
  ['eared', 'erade']
deer:
  ['deer', 'dere', 'dree', 'rede', 'reed']
dear:
  ['ared', 'daer', 'dare', 'dear', 'read']
deae:
  ['edea']
der:
  ['erd', 'red']
dee:
  ['dee']
dea:
  ['ade', 'dae']
de:
  ['de']
```

### `--wordfile WORDFILE`

`WORDFILE` is the path to a file containing newline-separated words to search. The default path `/usr/share/dict/words` corresponds to a word list that may come on a Linux or macOS system. Specifying `--wordfile /path/to/another/word_list.txt` will search the `/path/to/another/word_list.txt` file instead. 

```
% python3 anagrams.py --minimum de --optional aer --wordfile=/Users/cyndi/Documents/words_alpha.txt
minimum=de; optional=aer; wordfile=/Users/cyndi/Documents/words_alpha.txt; regex=
deaer:
  ['deare', 'eared', 'erade']
deer:
  ['deer', 'dere', 'dree', 'rede', 'reed']
dear:
  ['ared', 'daer', 'dare', 'dear', 'read']
deae:
  ['edea']
der:
  ['der', 'erd', 'red']
dee:
  ['dee']
dea:
  ['ade', 'dae', 'dea', 'ead']
de:
  ['de', 'ed']
```

### `--regex 'REGEX'`

`REGEX` is a regular expression compatible with the Python regular expressions. I typically place single quotation marks around the regular expression to avoid unwanted parameter expansion by the shell, as in `'REGEX'`. Refine the search results by adding the `--regex` option, specifying the regular expression that any result must match, before outputting the list of possible anagrams. This is helpful if you know the word must start with a certain letter, or contain a certain letter in a certain position, anything that can be searched with a regular expression.

### Starters:

* `.` matches a single character
* `^` indicates the start of a string
* `$` indicates the end of a string

### Example: word must be three letters and end with `de`

```
% python3 anagrams.py --minimum de --optional aer --regex='^.de$'                                 
minimum=de; optional=aer; wordfile=/usr/share/dict/words; regex=^.de$
dea:
  ['ade']
```

### Example: word must start with `d` and end with `r` and have two characters in between

```
% python3 anagrams.py --minimum de --optional aer --regex='^d..r$'
minimum=de; optional=aer; wordfile=/usr/share/dict/words; regex=^d..r$
deer:
  ['deer']
dear:
  ['daer', 'dear']
```

## Version History

* 0.1
    * Initial Release
* 0.2
    * Added regex results refinement option

## License

MIT License
