fruit = "banana"
colour = str(input("Enter fruit colour?.. ")).lower()
if colour == "green":
    print("Unripe")
elif colour == "yellow":
    print("Ripe")
elif colour == "brown":
    print("Overripe")
else:
    print("Invalid colour, so no idea")
