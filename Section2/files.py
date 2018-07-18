filename="settings.dat"
with open(filename,"wb") as f:
    f.write(b"some string")

my_file = open(filename,"wb")
user_input = input("enter your name:")
try:
    my_file.write(user_input.encode('utf8'))
except Exception as e:
    import traceback
    traceback.print_exc()
    raise
    print("not shown")
finally:
    my_file.close()
    print("OK ALL DONE")

with open(filename,"rb") as f_in:
    print(f_in.read().decode('utf8'))


with open("lorum.txt","rb") as f_in:
    print(f_in.read(1))
    print(f_in.readline())
    for line in f_in:
        print ("Line:",line)
