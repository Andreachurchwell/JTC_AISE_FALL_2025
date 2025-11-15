w = int(input("Enter the watermelon weight: "))

if w % 2 == 0 and w > 2:
    print("YES")
    print(f"{w} can be split into two even parts, such as {w//2} + {w//2}.")
else:
    print("NO")
    if w == 2:
        print("2 is even, but it cannot be split into two positive even numbers.")
    elif w % 2 != 0:
        print(f"{w} is odd, so it cannot be split into two even parts.")
    else:
        print("This weight cannot be divided into two even-weight pieces.")
