import pathlib
import itertools
import argparse
import sys
import pprint
import re


def count_letters(word):
    """
    Counts the number of each letter in a word.
    """

    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts


def search_strings(frequencies, strings):
    """
    Searches an array of strings for only those words that have the same character frequencies in the given frequencies.
    """

    results = []
    for string in strings:
        frequency = count_letters(string)
        if frequency == frequencies:
            results.append(string)
    return results


def get_all_subsets_of_string(string):
    """
    Returns all subsets of a string.
    """

    result = []
    for i in range(len(string) + 1):
        for combination in itertools.combinations(string, i):
            result.append(''.join(combination))

    return reversed(result)


def refine_results(results, regex):
    """
    Refines search results by only returning ones matching a regex
    """

    return list(filter(lambda word: re.match(regex, word), results))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--minimum',
        required=True,
        help='minimum string of characters which must be present (required)')
    parser.add_argument(
        '--optional',
        help='optional string of characters to try (default: \'\')',
        default='')
    parser.add_argument(
        '--regex',
        help='regex that has to match (default: \'\')',
        default='')
    parser.add_argument(
        '--wordfile',
        help='word file (default: /usr/share/dict/words)',
        default='/usr/share/dict/words')
    args = parser.parse_args()
    minimum = args.minimum
    optional = args.optional
    wordfile = args.wordfile
    regex = args.regex
    print(f"minimum={minimum}; optional={optional}; wordfile={wordfile}; regex={regex}")
    words = pathlib.Path(wordfile).read_text().split('\n')
    optional_combos = get_all_subsets_of_string(optional)
    for combo in optional_combos:
        target = minimum + combo
        results = search_strings(count_letters(target), words)
        if regex:
            results = refine_results(results, regex)
        if len(results) > 0:
            print(f"{target}:")
            print(f"  {results}")
