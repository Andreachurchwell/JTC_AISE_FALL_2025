# 📝 Challenge 1:
# Take this string:
text = "columbia university aise program"
# Write code that:
# Splits it into words
words = text.split(" ")
cap_words = []
# Makes the first letter of each word uppercase
for word in words:
    cap_words.append(word.title())
# Joins it back into a single string with spaces
result = " ".join(cap_words)
print(result)



# 📝 Challenge 2

# You’ve got a list of numbers:

numbers = [12, 7, 5, 18, 21, 4, 9]


# 👉 Your task:
evens_and_odds = {'evens': [], 
                  'odds': []}
# Loop through the list
for num in numbers:
    if num % 2 == 0:
# Put the even numbers into one list
        evens_and_odds["evens"].append(num)
# Put the odd numbers into another list
    else:
        evens_and_odds["odds"].append(num)
# Print both lists at the end
print(evens_and_odds)


# 📝 Challenge 3

# You’ve got a string:

word = "justice"
# 👉 Your task:
vowel = 0
vowels = 'aeiou'
consts = 0
# Loop through each letter in the word
for item in word:
# Count how many vowels (a, e, i, o, u) are in it
    if item in vowels:
        vowel += 1
# Count how many consonants are in it
    
    else:
        consts += 1
# Print both counts at the end
print('vowel count = ', vowel, 'const count = ', consts)



# 📝 Challenge 4

# You’ve got a list of words:

words = ["code", "justice", "through", "program", "python"]
vs = 'aieou'

result = {}
# 👉 Your task:

# Loop through the list of words
for word in words:
    count = 0
# For each word, count how many vowels it has
    for ch in word:
        if ch in vs:
            count += 1
    result[word] = count
# Store the results in a dictionary, where the key is the word and the value is the vowel count
print(result)
# Print the dictionary at the end


# 📝 Challenge 5

# You’ve got a list of words again:

words = ["justice", "through", "code", "python", "program"]
filtered = []
vowels = 'aeiou'
# 👉 Your task:

# Loop through the list
for word in words:
# Only keep the words that have more than 2 vowels
    count = 0
# Store those words in a new list called filtered
    for ch in word:
        if ch in vowels:
            count += 1
    if count > 2:
        filtered.append(word)
print(filtered)
        
# Print that list at the end

# 💡 Nudge:
# You already know how to count vowels per word (from Challenge 4).
# This time, instead of saving counts in a dictionary, you’ll check:

# if count > 2:
    # keep the word



# 📝 Challenge 6

# You’ve got the same list:

words = ["justice", "through", "code", "python", "program"]
vowels = "aeiou"
# One for the highest count so far (max_count = 0)
max_count = 0
# One for the word that matches it (max_word = "")
max_word = ""

# 👉 Your task:
# Loop through the list
for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    if count > max_count:
# Figure out which word has the highest number of vowels
# Then as you loop, if the current word’s vowel count is bigger than max_count, you update both trackers.
        max_count = count
        max_word = word
print('max word == ', max_word, 'max count == ', max_count)
# Count the vowels in each word


# 📝 Challenge 7: Palindrome Checker

# A palindrome is a word that reads the same forward and backward (like "level" or "racecar").

# 👉 Your task:

# Take a string like

word = "racecar"
def isPal(word):
    if word[::-1] == word:
        return "YES"
# Check if it’s a palindrome

# Print "yes" if it is, "no" if it isn’t
    else:
        return "NO"
print(isPal(word))
    

# 📝 Challenge 7.5: Palindrome (Sentence Edition)

# This time, instead of just one word, you’ll handle full sentences.

# 👉 Example:

# "Never odd or even" → palindrome ✅

# "Justice Through Code" → not palindrome ❌

# Your Task:

# Take a sentence (string with spaces, maybe mixed case)
def isPal(sentence):
    cleaned = sentence.lower().replace(" ", "")
    if cleaned == cleaned[::-1]:
        return "YES"
    else:
        return "NO"

print(isPal("Never odd or even"))
print(isPal("JUstice THru COde"))



           

    



