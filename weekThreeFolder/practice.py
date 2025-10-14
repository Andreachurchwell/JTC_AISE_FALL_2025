# sent = ['Hello', 'my', 'NamE','is', 'andreA']
# def howmanycaps(sent):
#     count = 0
#     caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for word in sent:
#         print('word=', word)
#         for letter in word:

#             if letter in caps:
#                 count += 1
#                 print('count=', count)
           
#     return count
# print(howmanycaps(['Hello', 'my', 'NamE','is', 'andreA']))

# def howmanylows(sent):
#     lows = 'abcdefghijklmnopqrstuvwxys'
#     count = 0
#     for word in sent:
#         for letter in word:
#             if letter in lows:
#                 count += 1
#     return count
# print(howmanylows(['andrea', 'is', 'mY', "NAME"]))

# def countDig(strs):
#     dig = '1234567890'
#     count = 0
#     for word in strs:
#         for letter in word:
#             if letter  in dig:
#                 count +=1
#     return count
# print(countDig(['AISE2026', 'Week3', 'Python', '123abc']
# ))

# def whitesp(strs):
#     count = 0
#     wsp = ' '
#     for word in strs:
#         for letter in word:
#             if letter == ' ':
#                 count += 1
#     return count
# print(whitesp(["Hello world", "AISE 2026", "Andrea Churchwell"]))

# def startsWithCap(strs):
#     count = 0

#     for word in strs:
#         if word[0].isupper():
#             count += 1
#     return count
# print(startsWithCap(["Hello", "my", "Name", "is", "Andrea"]))

# def endWithV(strs):
#     vs = 'aeiouAEIOU'
#     count = 0
#     for word in strs:
#         if word[-1] in vs:
#             count += 1
    
#     return count
# print(endWithV(["Hello", "my", "Name", "is", "Andrea"]))

# def ticketPrice(age):
#     if age >= 60:
#         price = 12
#     elif 13 <= age < 60:
#         price = 15
#     elif 3 <= age <= 12:
#         price = 10
#     else:
#         price = 0
#     return price
# print(ticketPrice(21))
    

# def tempConverter(value, unit):
#     if unit == "F":
#         result = (value - 32) * 5/9
#         return round(result, 1)
#     elif unit == "C":
#         result = (value * 9/5) + 32
#         return round(result, 1)
    
# print(tempConverter(100, "F"))  # → 37.8
# print(tempConverter(0, "C"))    # → 32.0

# def getGrade(score):
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#     return grade
# print(getGrade(54))  # "F"
# print(getGrade(72))  # "C"
# print(getGrade(88))  # "B"
# print(getGrade(93))  # "A"
    
        
        