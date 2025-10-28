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


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# for num in matrix:
#     print(num, end=' ')
for row in matrix:
    for num in row:
        print(num, end=" ")
