# nums = [1,2,3,4,5,6,7,8,9,10]
# # even list comp
# my_list= [n for n in nums if n%2 ==0]
# # odd list comp
# my_list= [n for n in nums if n%2 !=0]


# # letter numb pair for abcd in each number in 0123
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)
from typing import List, Dict
# 🥦 1. Healthy Groceries
def healthy_items(cart: List[Dict]) -> List[str]:
    """
    Return the names of grocery items that are in stock
    AND have fewer than 200 calories.
    Must use a single list comprehension.
    """
    # return []
    # result = []
    # for item in cart:
    #     # print('item:', item)
    #     if item['in_stock'] and item['calories'] <= 200 and item['category'] == 'grocery':
    #         result.append(item['name'])
    # return result
    return [item['name'] for item in cart if item['in_stock'] and item['calories'] <= 200 and item['category'] == 'grocery']





# # 💸 2. Expensive Electronics
def expensive_electronics(cart: List[Dict], min_price: float) -> List[str]:
    """
    Return the names of items in the 'electronics' category
    that are in stock AND cost at least min_price each.
    Must use a single list comprehension.
    """
    # return []
    # result = []
    # for item in cart:
    #     if item['category'] == 'electronics' and item["in_stock"] and item['price']>= min_price:
    #         result.append(item['name'])
    # return result
    return [item['name'] for item in cart if item['category'] == 'electronics' and item['in_stock'] and item['price'] >= min_price]


# # 🧾 3. Discounted Totals
def discounted_totals(cart: List[Dict], discount: float) -> List[float]:
    """
    Return the *discounted total price* (price * qty * (1-discount))
    for every item that is in stock.
    Must use a single list comprehension.
    """
    # return []
    # result = []
    # for item in cart:
    #     if item['in_stock']:
    #         total = item['price'] * item['qty'] * (1-discount)
    #         result.append(round(total,2))
    # return result
    return[(item['name'],round(item['price'] * item['qty'] * (1 - discount),2))for item in cart if item['in_stock']]






if __name__ == "__main__":
    cart = [
        {"name": "Apples", "price": 1.50, "qty": 4, "in_stock": True,  "category": "grocery", "calories": 95},
        {"name": "Banana", "price": 0.99, "qty": 6, "in_stock": True,  "category": "grocery", "calories": 105},
        {"name": "Salad",  "price": 4.99, "qty": 2, "in_stock": False, "category": "grocery", "calories": 150},
        {"name": "Energy Drink", "price": 2.50, "qty": 1, "in_stock": True, "category": "grocery", "calories": 250},
        {"name": "USB Cable", "price": 7.99, "qty": 3, "in_stock": True,  "category": "electronics", "calories": 0},
        {"name": "Laptop",    "price": 899.99, "qty": 1, "in_stock": False, "category": "electronics", "calories": 0},
        {"name": "Headphones","price": 199.99, "qty": 1, "in_stock": True,  "category": "electronics", "calories": 0}
    ]

    # Test Healthy Items
    print("Healthy Items (<200 cal):", healthy_items(cart))

    # # Test Expensive Electronics
    print("Expensive Electronics (>=50):", expensive_electronics(cart, 50))

    # # Test Discounted Totals
    print("Discounted Totals (20% off):", discounted_totals(cart, 0.20))