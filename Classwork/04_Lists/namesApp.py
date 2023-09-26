names = []
print("\nEnter the names of your group, type done to finish\n")
while True:
    name = input("Enter a name, or type done to quit: ")
    if "done" in name.lower():
        break
    names.append(name)
for n in names:
    print("\n",n)
print("")