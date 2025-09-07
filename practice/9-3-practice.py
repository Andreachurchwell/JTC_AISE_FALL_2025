"""
9-3-practice.py

9-3-25 — First AISE onboarding session.

We were supposed to start PY4E/PYFEB, but since I’ve already gone through that, 
I’m focusing on reps of Python basics to get sharper before the 22nd. 

Today I practiced:
- Strings (slicing, reversing, upper/lower, capitalize)
- Lists (counting, collecting, reversing, summing)
- Loops + conditionals (if/else patterns)
- Dictionaries (word count, evens/odds separation)

Goal: build fluency and confidence in fundamentals through clean reps.
"""



# 1. Slice the string to print only "Columbia"
school = "Columbia University"
print(school.split(' ')[0])


# 2. Reverse this word
word = "justice"
print(word[::-1])

# 3. Find the longest word in this list
words = ["python", "data", "visualization", "AI", "learning"]
 
def longest(words):
    longest_so_far = ''
    for word in words:
        if len(word) > len(longest_so_far):
            longest_so_far = word
    return longest_so_far
    
print(longest(words))       

# 4. Highest number in a list
numbers = [12, 7, 34, 56, 89, 23, 89, 1]

def find_max(numbers):
    max_so_far = numbers[0]
    for num in numbers:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
print(find_max(numbers))


# 5. Count vowels in a string

text = 'Justice Through Code'

def count_vowels(s):
    vowels = 'AEIOUaeiou'
    count = 0
    for item in s:
        if item in vowels:
            count +=1
     
    return count
print(count_vowels(text))



def how_many(s):
    vowels = 'AEIOUaeiou'
    result = {}
    for char in s:
        if char in vowels:
            if char in result:
                result[char] +=1
            else:
                result[char] = 1
    return result
print(how_many(text))


numbers = [3, 10, 7, 4, 12, 15, 8]

def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count    

print(count_evens(numbers))


numbers = [3, 10, 7, 4, 12, 15, 8]

def collect_evens(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result
    

print(collect_evens(numbers))  
# should print [10, 4, 12, 8]


text = "justice through code justice through learning"

def word_count(s):
    result = {}
    words = s.split(' ')
    for item in words:
        # print('looking at: ', item)
        print("looking at:", item, "current dict:", result)
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
            # print('so far: ', result)
            print("looking at else:", item, "current dict:", result)
    return result

print(word_count(text))
# expected: {'justice': 2, 'through': 2, 'code': 1, 'learning': 1}



text = "justice through code justice through learning"

def long_words(s):
    result = []
    words = s.split(' ')
    for word in words:
        if len(word) > 4:
            result.append(word)
    return result

print(long_words(text))
# expected: ['justice', 'through', 'justice', 'through', 'learning']


numbers = [-5, 10, -3, 7, 0, -2, 8]

def sum_positive(nums):
    total = 0
    for num in nums:
        if num > 0:
            total += num
    return total

print(sum_positive(numbers))
# expected: 25   (10 + 7 + 8)     


numbers = [42, 17, 8, 99, 23, 5, 61]

def find_min(nums):
    min_so_far = nums[0]
    for num in nums:
        if num < min_so_far:
            min_so_far = num
    return min_so_far

print(find_min(numbers))
# expected: 5


# 📝 Challenge 1: Count Odd Numbers
numbers = [3, 10, 7, 4, 12, 15, 8]

def count_odds(nums):
    count = 0
    for num in nums:
        if num % 2 != 0:
            count += 1
    return count

print(count_odds(numbers))
# expected: 3  (3, 7, 15)


# 📝 Challenge 2: Reverse a List
items = [1, 2, 3, 4, 5]

def reverse_list(lst):
    return lst[::-1]

print(reverse_list(items))
# expected: [5, 4, 3, 2, 1]


# 📝 Challenge 3: Uppercase All Words
text = "justice through code"

def upper_words(s):
    result = []
    words = s.split(' ')
    for word in words:
        result.append(word.upper())
    return result
print(upper_words(text))   


text = "justice through code"

def cap_words(s):
    result = []
    words = s.split(' ')
    for word in words:
        result.append(word.title())
    return result

print(cap_words(text))
# expected: ['Justice', 'Through', 'Code']



numbers = [3, 10, 7, 4, 12, 15, 8]

def separate(nums):
    result = {'evens': [], 'odds': []}
    for num in nums:
        if num % 2 == 0:
            result["evens"].append(num)
        else:
            result["odds"].append(num)
    return result

print(separate(numbers))
# expected: {"evens": [10, 4, 12, 8], "odds": [3, 7, 15]}



