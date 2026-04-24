i = input("Enter a number: ")

if i == 1997:
    print("You are right!")
elif type(i) == int:
    print("A number!")
else:
    print("Not a number!")
    match i:
        case "yxd":
            print("YXD")
        case "yxd2":
            print("YXD2")
        case _:
            print("Not YXD")
