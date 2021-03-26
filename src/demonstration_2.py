"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    # Iterate over the alpha_order to populate the dictionary.. key, value = letter, index
    alpha_dict = {}
    for i in range(len(alpha_order)):
        alpha_dict[alpha_order[i]] = i

    # Compare each word with the word in front of it--except for the last word of the list
    for i in range(len(words)-1):
        # Compare each letter
        word1 = words[i]
        word2 = words[i+1]

        for j in range(min(len(word1), len(word2))):
            letter1 = alpha_dict[word1[j]]
            letter2 = alpha_dict[word2[j]]

            if letter1 > letter2:
                return False
            elif letter1 < letter2:
                break

        # If we've made it to this point without returning False, the letters must be the same. We now need to check that the first word is shorter in length than the second word
        if len(word1) > len(word2):
            return False

    return True

words = ["lambda","school"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(are_words_sorted(words, order))

words = ["were","where","yellow"]
order = "habcdefgijklmnopqrstuvwxyz"
print(are_words_sorted(words, order))

words = ["lambda","lamb"]
order = "abcdefghijklmnopqrstuvwxyz"
print(are_words_sorted(words, order))