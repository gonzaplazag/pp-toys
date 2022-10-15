"""Find all palingrams in a dict"""
import load_dict
import time
start_time = time.time()

word_list = load_dict.load('dictionary.txt')
load_time = time.time()


def find_palingrams():
    """Find dict palingrams."""
    pali_list =[]
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()
find_pal_time = time.time()
palingrams_sorted = sorted(palingrams)

print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    pass
    #print("{} {}".format(first, second))

end_time = time.time()

print(f'Runtime read list. {load_time - start_time}')
print(f'Runtime find pals: {find_pal_time - start_time}')
print(f'Runtime total: {end_time - start_time}')