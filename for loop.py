#For Loop

#iterating over sequence, (list, tuple, dict, a set, or string)

variable = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)


#loop through letters of "banana":
for x in "banana":
    print(x)

#exit loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
#continue function
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
