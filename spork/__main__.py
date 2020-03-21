from spork.hello import hello_to

def main():
    name = input("What is your name?")
    print(hello_to(name))


if __name__ == "__main__":
    main()
