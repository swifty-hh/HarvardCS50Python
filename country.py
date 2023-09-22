#city = input("Where are you from? ")
#if city == "Seoul":
#    print("Korea!")
#elif city == "Seattle":
#    print("USA!")
#elif city == "Kyoto":
#    print("Japan!")
#else:
#    print("I wanna go there!")

city = input("Where are you from? ")

match city:
    case "Seoul" | "Busan":
        print("Korea!")
    case "Seattle":
        print("USA!")
    case "Kyoto":
        print("Japan!")
    case _:
        print("I wanna go there!")