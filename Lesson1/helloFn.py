def main():
    # call with default value
    hello()

    name = input("What's your name? ")

    # pass variable into hello
    hello(name)

# define a function with a default parameter value
def hello(to="world"):
    print("hello,", to)

main()