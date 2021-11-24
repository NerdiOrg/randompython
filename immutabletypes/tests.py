nums = [1,2,3]
numstwo = [1,2,3]
if nums == numstwo:
    # True, these are equal ==
    print("nums == numstwo")
    
if nums is numstwo: # False, nums is not numstwo
    print("nums is numstwo")
else:
    print("nums is not numstwo")
# This is because lists are "Mutable" and the "is / is not" in Python will not consider the two the same because their lists are stored as different objects in memory
# On the other hand, strings and integers are two types of immutable objects:
a = 1
b = 1
if a == b:
    # True, these are equal ==
    print("a == b (" + str(a) + ", " + str(b) + ")")
if a is b:
    # True, a is b
    print("a is b (" + str(a) + ", " + str(b) + ")")
id_a = id(a)
id_b = id(b)
if id_a == id_b:
    # True, same id in memory
    print("id_a == id_b (" + str(id_a) + ", " + str(id_b) + ")")
hex_a = hex(id_b)
hex_b = hex(id_b)
if hex_a == hex_b:
    # True, same id from memory in hexadecimal format
    print("hex_a == hex_b (" + hex_a + ", " + hex_b + ")")

c = "string"
d = "string"
if c == d:
    # True, these are equal ==
    print("c == d (" + c + ", " + d + ")")
if c is d:
    # True, c is d
    print("c is d (" + c + ", " + d + ")")
id_c = id(c)
id_d = id(d)
if id_c == id_d:
    # True, same id in memory
    print("id_c == id_d (" + str(id_c) + ", " + str(id_d) + ")")
hex_c = hex(id_c)
hex_d = hex(id_d)
if hex_c == hex_d:
    # True, same id from memory in hexadecimal format
    print("hex_c == hex_d (" + hex_c + ", " + hex_d + ")")
