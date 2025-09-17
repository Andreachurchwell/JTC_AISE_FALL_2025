def longest_word(sentence):
    # split sentence into words
    words = sentence.split()
    longest = ''
    for word in words:
   
        if len(word) > len(longest):
            longest = word
    return longest

    # TODO: find the longest word
    #  use len() to check word length
print(longest_word("Louie is my cat"))
print(longest_word("Justice Through Code"))
 


 
def longest_word(sentence):
    words = sentence.split()
    max_length = max(len(word)for word in words)
    longest_word = [word for word in words if len(word)==max_length]
    return longest_word
print(longest_word("Louie is my cat"))
print(longest_word("Justice Through Code"))
print(longest_word("AI rocks and JTC rules"))



# Exercise 1: Build Your Own Max Function

# Write a function my_max(nums) that takes a list of numbers and returns the largest number (without using Python’s max()).


def my_max(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest
        
print(my_max([2, 7, 3, 10, 5]))  # 10


# Exercise 2: Longest Word (Loop Only)

# Rewrite your longest word finder without using max() or list comprehensions.
# That means:
# Track the length manually.
# Collect longest words in a loop.
def longest_word_finder(sentence):
    words = sentence.split()
    long = []
    max_len = 0
    for word in words:
        if len(word)> max_len:
            max_len = len(word)
            long = [word]
        elif len(word) == max_len:
            long.append(word)
    return long

print(longest_word_finder("Louie is my cat"))          # ['Louie']
print(longest_word_finder("Justice Through Code"))     # ['Justice', 'Through']
print(longest_word_finder("AI rocks and JTC rules"))   # ['rocks', 'rules']


# New Challenge: Word Frequencies

# Take a sentence and return a dictionary with each word and how many times it appears.
def word_freq(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_freq("AI AI is amazing"))
print(word_freq("AI ai Ai"))


# Write a function that takes a list of numbers and returns both the smallest and largest number, using just one loop.
def minmax(nums):
    smallest = nums[0]
    largest = nums[0]
    
    for num in nums:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    
    return (smallest, largest)

print(minmax([3, 7, 1, 9, 4]))

def rev_string(text):
    result = ''
    for ch in text:
        result = ch + result
    return result
print(rev_string('andrea'))

def list_rev(listOfW):
    result = []
    for ch in listOfW:
        result = [ch] + result
    return result
print(list_rev(['andrea', 'is','my','name']))



def longest_word_reversed(sentence):
    words = sentence.split()
    max_length = 0
    longest_words = []

    for word in words:
        if len(word) > max_length:
            max_length = len(word)      #  update max length
            longest_words = [word]      # reset list with this word
        elif len(word) == max_length:
            longest_words.append(word)  # add ties

    # now reverse each longest word
    reversed_words = []
    for word in longest_words:
        rev = ""
        for ch in word:
            rev = ch + rev              
        reversed_words.append(rev)

    return reversed_words


print(longest_word_reversed("Justice Through Code"))
# ['ecitsuJ', 'hguorhT']


def word_count_from_file(filename):
    with open(filename, 'r') as f:
        text = f.read()

    words = text.lower().split()
    counts = {}

    for word in words:
        pkg = word.split('==')[0]
        if pkg in counts:
            counts[pkg] +=1
        else:
            counts[pkg] = 1
    
    # sorted_counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_counts
print(word_count_from_file('../requirements.txt'))