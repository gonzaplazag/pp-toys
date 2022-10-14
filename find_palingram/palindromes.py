""" Find palindromes in a dictionary"""
import load_dict
word_list = load_dict.load('dictionary.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f"\nNumber of palindromes found: {len(pali_list)}\n")
print(*pali_list, sep="\n")