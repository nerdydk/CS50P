#def = define
# here def means defining my own function called hello and providing it with a parameter called "x" which has a default value "world".
# this means if anywhere the hello function doesn't get any parameter it will print "Hello World" by default


def hello(x='World'):
    print("Hello,", x)

hello()

name = input("Hey there, what's your name ? ").strip().capitalize()

hello(name)
