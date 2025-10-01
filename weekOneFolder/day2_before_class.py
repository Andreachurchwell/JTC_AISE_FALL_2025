for value in [0,1,[],[0],'','text',None]:
    if value:
        print(value, 'is Truthy')
    else:
        print(value, 'is Falsy')


squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# LIST COMPREHENSION FOR CODE ABOVE WILL BE
squares = [x**2 for x in range(10)if x%2==0]

def run_command(command):
    match command:
        case ['move', x, y]:
            print(
                f'Moving to {x}, {y}'
            )
        case ['quit']:
            print('EXITING PROGRAM')
        case _:
            print('UNKNOWN COMMAND')

commands = [['move',2,3], ['quit'], ['dance']]
for cmd in commands:
    run_command(cmd)

while(cmd := input('Enter command: ')) != 'quit':
    print('You entered:', cmd)