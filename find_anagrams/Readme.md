# Find Anagrams

In this projects, you'll find all the anagrams from a given word or phrase.

## A. Find single words anagrams

Find all the anagramas given a single word.

### Strategy

Use a Python dict to find all the single words anagrams for a given english word.

Two words are anagrams of each other if and only if: 1. They has the same number of letters, 2. The has the same letters. The second condition can be checked sorting the words.

So, we can write a function that:

1. Accepts a word as input.
2. Loop on a dictionary to find all the words with the same letters and the same length.
3. Returns a list with the anagrams.

### Pseudocode

- Given a word, loops on a dictionary of words. For each word:
- Define container list_an = []
  - If sort(word_input) == word(word_dict):
    - list_an.append(word_dict)
  - Return list_an