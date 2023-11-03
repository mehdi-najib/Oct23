def greet(first_name):
    print(f'hi {first_name} ')

def get_greeting(first_name):
    return f'hi {first_name}'

message = get_greeting('mahdi')

print(message)

file = open('content.txt', 'w')
file.write(message)
