# Example of a CLOSURE
def outer():
    message = "Hello, Andrea"   # parent creates a message

    def inner():
        print(message)          # child remembers the parent's message

    return inner                # return the inner function

# Now call it
greet = outer()     # outer() runs and gives us back the inner() function
greet()             # prints: Hello, Andrea


# Example of a GENERATOR
# What it is: a function that can pause and resume
# How? It uses Yield (NOT RETURN)

# tiny example
def count_to_three():
    print('Starting')
    yield 1
    print('AFTER 1st YIELD')
    yield 2
    print('AFTER 2nd YIELD')
    yield 3
    print('AFTER 3rd YIELD and DONE')

for n in count_to_three():
    print('got:',n)

g = count_to_three() #creates a generator: nothing prints yet
print(next(g)) #runs until the first yield => prints "starting", then 1
print(next(g)) #resumes -> prints 'after 1st yield', then 2
print(next(g)) #resumes -> prints 'after 2nd yield', then 3
# next(g) now would raise StopIteration(it's done)
print(list(count_to_three()))

# Two key takeaways:

# yield makes a generator; it runs only when you iterate.

# Creating it (calling the function) returns a generator object but doesn’t execute the body yet.


def squares(n):
    for i in range(n):
        yield i*i
print(list(squares(5)))

def demo_gen_behavior():
    def g():
        print("open")
        yield "A"
        print("mid")
        yield "B"
        print("close")

    print("1) for-loop")
    for x in g():
        print(" ->", x)

    print("\n2) next()")
    it = g()
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration:
        print("StopIteration (done)")

    print("\n3) list()")
    print(list(g()))


# Context manager: setup -> use -> cleanup
class DemoCM:
    def __enter__(self):
        print("enter (setup)")
        return "RESOURCE"
    def __exit__(self, exc_type, exc, tb):
        print("exit (cleanup)")

print("\nContext manager demo:")
with DemoCM() as r:
    print("using:", r)


# Under the hood: __enter__ / __exit__.
with open("tmp.txt","w") as f:
    f.write("hi")

def make_adder(x):
    def add(y): return x+y
    return add
make_adder(5)(10)  # 15



# 4) Decorators (built on closures)

# Say this: “A decorator wraps a function to add behavior; @decorator applies it; functools.wraps keeps the name/doc.”

# Micro example:

from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] {func.__name__}{args}{kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b): return a+b

add(2,3)  # prints before, then returns 5


# 5) functools quick hits

# Say this: “lru_cache caches results; partial pre-fills arguments; wraps preserves metadata in decorators.”

# Micro examples:

from functools import lru_cache, partial

@lru_cache(maxsize=128)
def slow_double(x):
    # pretend expensive work here
    return x*2

square = partial(pow, exp=2)  # or partial(pow, 2) for base

