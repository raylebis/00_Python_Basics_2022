print()
print("*** Looping Demo #2 ***")
print()

# Quick for loop
for item in range(0, 5):
    print(item)

    # ask the user if they want to keep going.....
    keep_going = input("<enter> to keep looping, or any key")

    # end loop if user presses <enter>'
    if keep_going != "":
        break

print()
print("We are done")
print()