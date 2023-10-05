import sys

#try:
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("You forgot something")

if len(sys.argv) < 2:
    sys.exit("Too  few arguments")

    
for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg)
