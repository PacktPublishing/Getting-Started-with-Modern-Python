s="hello"
print(list(s))

name = "Joran Beasley"
first,last = name.split()
print("{first} + {last}".format(first=first,last=last))

print("/path/to/a/folder".split("/"))

import os
print(os.environ['PATH'].split(os.pathsep))

print("Apples,Bananas,Chips,Bread,Fish".split(","))

print("Apples and Bananas".split(" and "))

print("Apples,Bananas,Chips,Bread,Fish".split(",", 2))

file_path = "/some/path/to/some_file.ext"
print(file_path.rsplit(".",1)[-1])
print(file_path.rsplit("/",1)[-1])
print(file_path.rsplit("/",1)[0])

parts = "Apples and Bananas".split(" and ")
print(" or ".join(parts))

print(" ".join([str(1),str(2),str(3)]))

if isinstance(name,str):
    # Do String Stuff
    pass

name.isprintable()
name.isalnum()

print(
    name[0].isdigit(),
    name[0].isspace(),
    name[0].islower(),
    name[0].isupper(),
    name[0].isalpha(),
)

# result = input("Play Again?")

"\r   a string    \n\r\t".strip() == "a string"
"&&a string !!&&".strip("&! ") == "a string"

"a string".upper() == "A STRING"
"A StrinG".lower() == "a string"
"A StrinG".swapcase() == "a sTRINg"

"yes".startswith("y")
"filename.exe".endswith(".exe")

"a s" in "a string"

print("a string".replace("ring","ar"))