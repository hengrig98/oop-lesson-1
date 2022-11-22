# takes either argument, or standard...

def say_hello(name = 'Guest'):
    print(f'Hello {name}')

say_hello('Mike')
say_hello()
say_hello()