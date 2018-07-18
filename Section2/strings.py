"{variable_name:format_description}"
print('{a:<10}|{a:^10}|{a:>10}'.format(a='test'))
print('{a:~<10}|{a:~^10}|{a:~>10}'.format(a='test'))

person = {"first":"Joran","last":"Beasley"}
print("{p[first]} {p[last]}".format(p=person))
data = range(100)
print("{d[0]}...{d[99]}".format(d=data))

print("normal:{num:d}".format(num=33))
print("normal:{num:f}".format(num=33))
print("binary:{num:b}".format(num=33))
print("binary:{num:08b}".format(num=33))
print("hex:{num:x}".format(num=33))
print("hex:0x{num:0<4x}".format(num=33))
print("octal:{num:o}".format(num=33))

print("{num:f}".format(num=22/7))
print("${num:0.2f}".format(num=22/7))

print("{num:.2e}".format(num=22/7))
print("{num:.1%}".format(num=22/7))

print("{num:g}".format(num=5.1200001))

variable=27
print(f"{variable}")


