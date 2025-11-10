# nums = [10, 20, 30, 40, 50]
# nums.remove(30)
# nums.insert(2,99)

# nums.remove(10)
# nums.append(60)
# print(nums)

# print(nums[0:3])

# nums = [5, 10, 15, 20, 25]
# nums.remove(15)
# nums.insert(2,99)
# nums.append(30)
# nums.append(35)
# nums.remove(5)
# print(nums)


# temps = [72, 65, 81, 60, 90, 75]
# temps.sort()
# print(temps)

# print(temps[0:3])
# temps.reverse()
# print(temps)


# mix = ["apple", 10, "banana", 20, "apple", 30]
# def appleCnt(mix):
#     count = 0
#     for item in mix:
#         if item == 'apple':
#             count += 1
#     return count
# print(appleCnt(mix))

# def remove20(mix):
#     result = []
#     for item in mix:
#         if item != 20:
#             result.append(item)
#     return result
# print(remove20(mix))

# groceries = ["milk", "eggs", "bread", "milk", "apples", "juice"]
# print(groceries.count('milk'))
# groceries.remove('milk')
# groceries.append('cheese')
# groceries.append('yogurt')
# print(groceries)


# playlist = ["song1", "song2", "song3", "song2", "song4"]
# print(playlist.count('song2'))
# playlist.remove('song2')
# playlist.append('song5')
# print(playlist)

# nums = [4, 8, 12, 8, 20, 4, 16]
# print(nums.count(8))
# nums.remove(8)
# nums.append(24)
# nums.append(28)
# nums.sort()
# print(nums)



# nums = [1, 2, 3]
# copy_nums = nums
# copy_nums.append(4)

# print("nums:", nums)
# print("copy_nums:", copy_nums)


# nums = [1, 2, 3]
# copy_nums = nums.copy()
# copy_nums.append(4)

# print("nums:", nums)
# print("copy_nums:", copy_nums)


# squares = []
# for n in [1, 2, 3, 4]:
#     squares.append(n**2)
# squares = [n**2 for n in [1, 2, 3, 4]]
# print(squares)

# evens = []
# for n in [1,2,3,4,5,6,7,8,9,10]:
#     if n % 2 == 0:
#         evens.append(n)
# evens = [n for n in [1,2,3,4,5,6,7,8,9,10] if n % 2 == 0]
# print(evens)

# result = []
# nums = [3, 7, 2, 8, 6, 1]
# for num in nums:
#     if num > 5:
#         result.append(num)

# print(result)

# greater5 = [n for n in [3,7,2,8,6,1]if n > 5]
# print(greater5)

# nums = [2, 4, 6, 8]

# doubled = [n*2 for n in nums]
# print(doubled)

# nums = [3, 9, 12, 4, 7, 2]
# double5 = [n * 2 for n in nums if n > 5]
# print(double5)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # for num in matrix:
# #     print(num, end=' ')
# for row in matrix:
#     for num in row:
#         print(num, end=" ")


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     print("row is:", row)          # show the whole inner list
#     for num in row:
#         print("   num is:", num)   # show each value inside that row

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = []
# # your nested loops here

# for row in matrix:
#     for num in row:
#         if num > 4:
#             result.append(num)
# print(result)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# doubled = [n * 2 for row in matrix for n in row if n > 4]
# print(doubled)



# nums = [10, 20, 30, 40, 50]
# nums = nums[:2] + [999] + nums[3]

# nums = [10, 20, 30, 40, 50]

# print(nums[:2])   # everything before index 2
# print(nums[3:])   # everything from index 3 onward
# nums = nums[:2] + [999] + nums[3:]
# print(nums)


# nums = [10, 20, 30, 40, 50]
# nums = nums[2:] + nums[:2]
# print(nums)

# nums = [10, 20, 30, 40, 50, 60]
# nums[2] = 333
# nums[3] = 444
# nums = nums[:3] + [555] + nums[-2:]
# print(nums)

# nums = [10, 20, 30, 40, 50, 60]
# nums[2:4] = [333, 444, 555]
# print(nums)

# nums = [5, 10, 15, 20, 25, 30]
# print(nums[1:3])
# print(nums[:2])
# print(nums[1:])

# nums = nums[:2] + nums[4:]
# print(nums)


groceries = ["milk", "eggs", "bread", "milk", "apples", "juice"]

# print(groceries.count('milk'))
# groceries.remove('milk')
# print(groceries)
# groceries.append('cheese')
# groceries.append('yogurt')
# print(groceries)

# def deletemilk(groceries):
#     result = []
#     for item in groceries:
#         if item != 'milk':
#             result.append(item)
#     return result
# print(deletemilk(groceries))

# groceries = [item for item in groceries if item != 'milk']
# print('listcomp=', groceries)


# nums = [3, 9, 12, 4, 7, 2]
# nums = [num for num in nums if num > 5]
# print(nums)

# nums = [2, 4, 6, 8, 10]
# nums = [num * 2 for num in nums if num > 5]
# print(nums)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# def flatlist(matrix):
#     result = []
#     for row in matrix:
#         for item in row:
#             if item > 4:
#                 result.append(item)
#     return result
# print(flatlist(matrix))
# matrix = [item for row in matrix for item in row if item > 4]
# print(matrix)

# mylist =["a", "b", "a", "c", "a"]
# def howmany(mylist):
#     result = 'a'
#     count = 0
#     for letter in mylist:
#         if letter == 'a':
#             count += 1
#     return count
# print(howmany(mylist))

# nums = [3, 10, 4, 8, 12, 5]
# def howmany(nums):
#     count = 0
#     for num in nums:
#         if num > 7:
#             count += 1
#     return count
# print(howmany(nums))

# letters = ["a", "bb", "ccc", "dd", "e", "ffff"]
# def exacttwo(letters):
#     count = 0
#     for letter in letters:
#         if len(letter) == 2:
#             count += 1
#     return count
# print(exacttwo(letters))

# values = [2, 5, 0, -3, 8, -1, 7]
# def whichneg(values):
#     count = 0
#     for val in values:
#         if val < 0:
#             count += 1
#     return count
# print(whichneg(values))

# words = ["sun", "car", "apple", "dog", "desk", "hi"]
# def startd(words):
#     count = 0
#     for word in words:
#         # print('word==', word)
#         if word[0] == 'd':
#             count += 1
#     return count

# print(startd(words))

# items = ["hi", 5, "cat", 12, "sun", 3]
# def hmst(items):
#     count = 0
#     for i in items:
#         if type(i) == str:
#             count += 1
#     return count
# print(hmst(items))


pairs = [(1, 2), (5, 1), (3, 8), (9, 0)]
def tup(pairs):
    count = 0
    for pair in pairs:
        print('pair==', pair)
        if pair[0] > pair[1]:
            count += 1
    return count

print(tup(pairs))