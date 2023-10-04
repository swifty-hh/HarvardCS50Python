def main():
    x = get_int()
    print(f"x is {x}.")

def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            print("That is not an integer.") # 'pass' for same function but no guide
            

main()
