# person = {
#     "name": "Andrea",
#     "city": "Selmer",
#     "pet": "Louie"
# }
# print(person['city'])
# person['city'] = 'Memphis'
# person['fav_color'] = 'blue'
# print(person)

# person = {
#     "name": "Andrea",
#     "city": "Memphis",
#     "pet": "Louie",
#     "fav_color": "blue"
# }
# for key in person:
#     print('key:', key)
# for val in person:
#     print('val', val)
# for key, value in person.items():
#     print(key, "→", value)

# fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
# def builddic(fruits):
#     result = {}
  
#     for fruit in fruits:
#         if fruit in result:
#             result[fruit] += 1
#         else:
#             result[fruit] = 1
#     return result
# print(builddic(fruits))
# result = {}
# for fruit in fruits:
#     result[fruit] = result.get(fruit, 0) + 1
# print(result)

# from collections import Counter
# fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
# counts= Counter(fruits)
# print(counts)



# scores = {"Ann": 91, "Bob": 77, "Cara": 88, "Dan": 72}
# def above80(scores):
#     count = 0
#     val = 80
#     for name in scores:
#         print('name--', name)
#         if scores[name] > val:
#             count += 1
#     return count
  

# print(above80(scores))


# scores = {"Ann": 91, "Bob": 77, "Cara": 88, "Dan": 72}
# def under75(scores):
#     val=75
#     count=0
#     for item in scores:
#         if scores[item] < 75:
#             count += 1
#     return count
# print(under75(scores))


# scores = {"Ann": 91, "Bob": 77, "Cara": 88, "Dan": 72}
# def swc(scores):
#     count = 0
#     for item in scores:
#         if item[0] == "C":
#             count += 1
#     return count
# print(swc(scores))

# sales = {"Mon": 120, "Tue": 90, "Wed": 150, "Thu": 70, "Fri": 200}
# def over100(sales):
#     count = 0
#     val = 100
#     for item in sales:
#         if sales[item] > val:
#             count += 1
#     return count
# print(over100(sales))

# temps = {"morning": 55, "noon": 72, "evening": 61, "night": 48}
# def below60(temps):
#     count = 0
#     val=60
#     for item in temps:
#         if temps[item] < 60:
#             count +=1
#     return count
# print(below60(temps))


# people = {
#     "Ann": 25,
#     "Bob": 17,
#     "Cara": 33,
#     "Dan": 14,
#     "Ella": 19
# }
# def older18(people):
#     count = 0
#     val = 18
#     for name,age in people.items():
#         if age >= val:
#             count +=1
#     return count
# print(older18(people))


# pets = {
#     "Ann": ["cat", "fish"],
#     "Bob": ["dog"],
#     "Cara": ["bird", "cat", "hamster"],
#     "Dan": [],
#     "Ella": ["dog", "dog"]
# }
# def onepet(pets):
#     count = 0
#     pet_list = []
#     for name, pet in pets.items():
#         print('name=', name, 
#               'pet=', pet)
#         if len(pet) > 0:
#             count += 1
#     return count
# print(onepet(pets))


# grades = {
#     "Ann": [91, 87, 95],
#     "Bob": [70, 82],
#     "Cara": [88, 90, 92, 85],
#     "Dan": [60],
#     "Ella": [100, 98]
# }
# def oneabove(grades):
#     count = 0
 
#     for name, gradelist in grades.items():
#         # print('name=', name, 
#         #       'grade=', grade)
#         foundone= False
#         for i in gradelist:
#             print('i=', i)
#             if i > 90:
#                 foundone=True
#                 break
#         if foundone:
#             count += 1
#     return count
               
# print(oneabove(grades))


# movies = {
#     "Avatar": 7.8,
#     "Up": 8.3,
#     "Cars": 7.1,
#     "Coco": 8.4,
#     "Jaws": 8.0
# }
# def good(movies):
#     count = 0
#     for name, rating in movies.items():
#         if rating >= 8.0:
#             count += 1
#     return count
# print(good(movies))


# products = {
#     "laptop": 999,
#     "mouse": 25,
#     "keyboard": 80,
#     "monitor": 150,
#     "desk": 200
# }
# def cheappro(products):
#     count = 0
#     for pro, price in products.items():
#         if price <= 100:
#             count+=1
#     return count
# print(cheappro(products))


# classes = {
#     "math": ["Ann", "Bob"],
#     "science": ["Cara"],
#     "history": ["Dan", "Ella", "Frank"],
#     "art": []
# }
# def morethan2(classes):
#     count = 0
#     for classname, students in classes.items():
#         # print('claname=', classname, 'stu-', students)
#         if len(students) >= 2:
#             count+=1
#     return count
# print(morethan2(classes))


# books = {
#     "Horror": ["IT", "The Shining"],
#     "Romance": ["Twilight"],
#     "SciFi": ["Dune", "Foundation", "Neuromancer"],
#     "Poetry": [],
# }
# def onebook(books):
#     count = 0
#     for g, name in books.items():
#         if len(name) > 0:
#             count += 1
#     return count
# print(onebook(books))


# meals = {
#     "breakfast": ["eggs", "toast"],
#     "lunch": ["salad"],
#     "dinner": ["pasta", "salmon", "bread"],
#     "snack": []
# }
# def howmany(meals):
#     count = 0
#     for meal, types in meals.items():
#         for foods in types:
#             # if len(foods)> 0:
#                 count += 1
#     return count
# print(howmany(meals))


orders = {
    "Ann": [12, 5, 20],
    "Bob": [3],
    "Cara": [15, 8],
    "Dan": [],
    "Ella": [2, 30, 1]
}
def over10(orders):
    count = 0
    
    for name, orderlist in orders.items():
        found=False
        for o in orderlist:
            if o > 10:
                found=True
                break
        if found:
            count +=1
    return count

print(over10(orders))