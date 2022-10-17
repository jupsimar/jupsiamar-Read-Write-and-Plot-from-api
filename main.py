

choice = input("Do you want to Read, Write, or Plot? ")
if choice.lower() == 'w':
    import write
elif choice.lower() == "r":
    import read
else:
    import plot    