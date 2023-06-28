# Anagrams

## Author

Cyndi Cavanaugh

## Requirements

Python 3.11 (It should work on later Python 3 versions; it may work on earlier Python 3 versions as well.)

## Running the Program

All arguments are optional and have default values, as shown in the help message. Providing an argument will only override the corresponding default value for that argument.

### Display help message

```
$ python3 anagrams.py --help
usage: anagrams.py [-h] [--minimum MINIMUM] [--optional OPTIONAL]
                   [--wordfile WORDFILE]

options:
  -h, --help           show this help message and exit
  --minimum MINIMUM    minimum string of characters which must be present
                       (default: de)
  --optional OPTIONAL  optional string of characters to try (default: aer)
  --wordfile WORDFILE  word file (default: /usr/share/dict/words)
```

### Default arguments

```
$ python3 anagrams.py       
minimum=de; optional=aer; wordfile=/usr/share/dict/words
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

### `--minimum MINIMUM`

`MINIMUM` is the minimum string of characters which must be present in the word, in any order; e.g. 'de' == 'ed'.

```
$ python3 anagrams.py --minimum me  
minimum=me; optional=aer; wordfile=/usr/share/dict/words
meer:
  ['mere', 'reem']
mear:
  ['mare', 'rame', 'ream']
mee:
  ['eme']
mea:
  ['ame', 'mae']
me:
  ['em', 'me']
```

### `--optional OPTIONAL`

`OPTIONAL` is the string of characters whose presence is optional in conjunction with the minimum string of characters. The search algorithm will try combining the minimum string with all optional characters and smaller subsets of them.

```
$ python3 anagrams.py --optional vle
minimum=de; optional=vle; wordfile=/usr/share/dict/words
devle:
  ['delve']
dele:
  ['dele', 'lede', 'leed']
dee:
  ['dee']
del:
  ['eld', 'led']
dev:
  ['dev']
de:
  ['de']
```

### `--wordfile WORDFILE`

`WORDFILE` is the path to a file containing newline-separated words to search. The default path `/usr/share/dict/words` corresponds to a word list that may come on a Linux or macOS system. Specifying `--wordfile /path/to/another/word_list.txt` will search the `/path/to/another/word_list.txt` file instead. 

```
$ python3 anagrams.py --minimum me --optional vle --wordfile=/Users/cyndi/Documents/words_alpha.txt
minimum=me; optional=vle; wordfile=/Users/cyndi/Documents/words_alpha.txt
mele:
  ['elem', 'leme', 'mele']
mee:
  ['eme', 'mee']
mel:
  ['elm', 'mel']
mev:
  ['mev']
me:
  ['em', 'me']
```

### `--regex 'REGEX'`

`REGEX` is a regular expression compatible with the Python regular expressions. I typically place single quotation marks around the regular expression to avoid unwanted parameter expansion by the shell, as in `'REGEX'`. Refine the search results by adding the `--regex` option, specifying the regular expression that any result must match, before outputting the list of possible anagrams. This is helpful if you know the word must start with a certain letter, or contain a certain letter in a certain position, anything that can be searched with a regular expression.

### Starters:

* `.` matches a single character
* `^` indicates the start of a string
* `$` indicates the end of a string

### Example: word must be three letters and end with `de`

```
% python3 anagrams.py --regex '^.de$' 
minimum=de; optional=aer; wordfile=/usr/share/dict/words; regex=^.de$
dea:
  ['ade']
```

### Example: word must start with `d` and end with `r` and have two characters in between

```
% python3 anagrams.py --regex '^d..r$'
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
