while True:
    try:
        x = int(input("please enter a number : "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again....")

if x >18:
    print("you are eligible to get a  driving license")
else:
    print("you gotta wait till 18")
