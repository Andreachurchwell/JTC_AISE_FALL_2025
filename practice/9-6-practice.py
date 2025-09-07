def reversed_words2(sentence):
    rev_word=[]
    for word in sentence.split():
        rev_word.append(word[::-1])
        print("current growing list: ", rev_word)
    return ' '.join(rev_word)
print(reversed_words2('LOuie is my kitty cat'))

def count_vs(text):
    count = 0 
    vs = 'AEIOUaeiou'
    for ch in text:
        if ch in vs:
            count += 1
            print('FOUND VOWEL: ', ch, "| count now: ", count)
    return count
print(count_vs('andrea elizabeth churchwell'))
    
def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
        print('checking: ', num, '| Largest so far:', largest)
    return largest
print(find_largest([4,6,1,7,9]))


def remove_duplicates(nums):
    new_list = []
    for num in nums:
        if num not in new_list:
            new_list.append(num)
        print('CHecking:', num, '| New list:', new_list)
    return new_list
print(remove_duplicates([1,2,2,3,4,4,5]))

def word_count(s):
    counts = {}
    for word in s.split():
        counts[word] = counts.get(word, 0) + 1
        print('After seeing:', word, '| counts so far:', counts)
    return counts
print(word_count('justice thru code thru justice'))


# Find the smallest number in a list.

def smallest(nums):
    small = nums[0]
    for num in nums:
        if num < small:
            small = num
    return small
print(smallest([4,7,9,3,1]))
print(smallest([2,7,9,3,4])) 


def largest(nums):
    big = nums[0]
    for num in nums:
        if num > big:
            big = num
    return big
print(largest([2,3,5,66,3,2,33,64]))


def minmax(nums):
    big = nums[0]
    small = nums[1]
    for num in nums:
        if num > big:
            big = num
        elif num < small:
            small = num
    return big, small
print(minmax([2,3,5,66,3,2,33,64]))


# def longest_word(sentence):


# print(longest_word("Louie is my cat"))      # "Louie"
# print(longest_word("Justice Through Code")) # "Justice"

