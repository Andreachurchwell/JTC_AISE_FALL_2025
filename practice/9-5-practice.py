# 📝 Today’s Python Reps
# 1. Unique Characters Checker

# Write a function that takes a string and returns True if all characters are unique, otherwise False.
# 👉 Example: "abc" → True, "apple" → False.

def unique_chars(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True

print(unique_chars('andrea'))  
print(unique_chars('andre'))


# 🚀 Exercise: Second Largest Number
# Write a function that finds the second largest number in a list of integers.
# Example: [4, 9, 1, 7] → should return 7
def get_second(list_of_nums):
# so i need somewhere to hold the highest val, and i think somehwere to hold the second highest
    first = list_of_nums[0]
    second = list_of_nums[1]
# i also need to loop thru the list
    for num in list_of_nums:
        if num > first:
            first = num
        elif num > second and num != first:
            second = num
# i need to return the 2nd highest val
    return second
print(get_second([4,9,1,7]))



# Day 1 – Strings

# 1. Count Vowels
# Write a function count_vowels(text) that returns how many vowels (a, e, i, o, u) are in the string.
# need a counter and vowel str
def count_vowels(text):
    count = 0
    vs = "AEIOUaeiou"
    for ch in text:
        if ch in vs:
            count += 1
    return count
print(count_vowels('andrea'))
print(count_vowels('JUSTICE'))  
print(count_vowels('xyz'))


# 2. Reverse Each Word
# Write a function reverse_words(sentence) that reverses each word in the sentence but keeps the word order the same.
# i need to split at white space and return reversed
sentence = 'Louie is my cat'
def reverse_words(sentence):
    words = sentence.split()
    rev_words = []
    for word in words:
        rev_words.append(word[::-1])
    return ' '.join(rev_words)
print(reverse_words('Louie is my cat'))


s = 'Louie is my cat'
print(s.split()) 
words = ["Louie", "is", "my", "cat"]
print(
    ' '.join(words)
)

s = 'Andrea'
print(list(s))
chars = list(s)
print('-'.join(chars))

s = 'apples, bananas, cherries'
words = s.split(',')
print(words)
print(' '.join(words))


s = "Python is fun"
words = s.split()
print('-'.join(words))


sentence = 'Louie is my cat'

def reversed_words(sentence):
    rev_word = []
    rev = sentence.split()
    for word in rev:
        rev_word.append(word[::-1])
        print(rev_word)
    return ' '.join(rev_word)
print(reversed_words('Louie is my cat'))
        


