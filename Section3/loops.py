a_list = []
a_dict = {}
a_set = set()

for letter in "Hello World!":
    a_list.append(letter)
    a_set.add(letter)
    a_dict[letter] = len(a_list)

print("List:",a_list)

list2 = [letter for letter in "Hello World!"]
set2 = {letter for letter in "Hello World!"}
dict2 = {letter:i for i,letter in enumerate("Hello World!",1)}

print("L2,S2,D2",list2,set2,dict2,sep="\n")

print(list2==a_list,dict2==a_dict,set2==a_set)


print("Set:",a_set)
print("Dict:",a_dict)

a_list2 = []
for letter in "Hello":
    for letter2 in "world":
        a_list2.append((letter,letter2))

print(a_list2)

new_list = []
data = [[1,2],[4,5],[6,7],[9,8]]
for row in data:
    for value in row:
        new_list.append(value)

flattened = [value for row in data for value in row]

multidim = [[value for value in row] for row in data]

print(flattened)
print(multidim)

new_list = [[word.upper(),word,len(word)]for word in "the quick brown fox jumps over the lazy dog".split()]
print(new_list)


