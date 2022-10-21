from sense_emu import SenseHat
sense=SenseHat()

# sense.show_message("Yamazaki")

print("input your age")

x=input("value:")
x_=int(x)

if x_ >= 20:
    print("you are adult")
else:
    print("you are young")