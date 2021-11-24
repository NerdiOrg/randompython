print("\n\nTEST 1 START : \n")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
if a == b:
    print("a == b")
    # [1,2,3] == [1,2,3]
if b == c:
    print("b == c")
    # [1,2,3] = [1,2,3]
if c == a:
    print("c == a")
    # [1,2,3] = [1,2,3]
if a is not b:
    print("a is not b, (" + str(id(a)) + ", "+ str(id(b)) + ")")
    # id(a) != id(b)
if b is not c:
    print("b is not c, (" + str(id(b)) + ", "+ str(id(c)) + ")")
    # id(b) != id(c)
if c is a:
    print("c is a, (" + str(id(c)) + ", "+ str(id(a)) + ")")
    # id(c) == id(a)

   
# On the other hand, strings and integers are two types of immutable objects:
print("\n\nTEST 2 START : \n")
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


print("\n\nTEST 3 START : \n")
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
    
  
