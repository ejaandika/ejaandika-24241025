# operasi komperasi / perbandingan

# hasil operasi sesalu bertipe boolean (TRUE/FALSE)

# >,<,==,!=,>=,<=,is, dan is not

a = 4
b = 2

# lebih besar dari >
print("====Lebih Besar dari (>)====")
hasil = a > 3 # TRUE
print(a,">", 3, "=", hasil)
hasil = b > 3 # FALSE
print(b,">", 3, "=", hasil)
hasil = b > 2 # FALSE
print(b, ">", 2, "=", hasil)

# kurang dari <
print("====Kurang dari (<)====")
hasil = a < 3 # FALSE
print(a,"<", 3, "=", hasil)
hasil = b < 3 # TRUE
print(b,"<", 3, "=", hasil)
hasil = b < 2 # FALSE
print(b, "<", 2, "=", hasil)

# lebih dari sama dengan >=
print("====lebih dari sama dengan(>=)====")
hasil = a >= 3 # TRUE
print(a,">=", 3, "=", hasil)
hasil = b >= 3 # FALSE
print(b,">=", 3, "=", hasil)
hasil = b >= 2 # TRUE
print(b, ">=", 2, "=", hasil)

# kurang dari sama dengan <=
print("====kurang dari sama dengan(<=)====")
hasil = a <= 3 # TRUE
print(a,"<=", 3, "=", hasil)
hasil = b <= 3 # FALSE
print(b,"<=", 3, "=", hasil)
hasil = b <= 2 # TRUE
print(b, "<=", 2, "=", hasil)

# sama dengan ==
print("====sama dengan(==)====")
hasil = a == 3 # FALSE
print(a,"==", 3, "=", hasil)
hasil = a == 3 # TRUE
print (a,"==", 3, "=", hasil)

# tidak dengan !=
print("====tidak sama dengan(!=)====")
hasil = a != 3 # TRUE
print(a,"!=", 3, "=", hasil)
hasil = a != 3 # FALSE
print (a,"!=", 3, "=", hasil)

# is sebagai komparasi
print("====objek identity")
x = 5
y = 5
hasil = x is y # TRUE
print(x, "is", y,"=", hasil)
print("nilai x =", x, "id= ",hex(id(x))
print("nilai y =", y, "id= ",hex(id(y))

# is not sebagai komparasi
print ("====objek identity")
x=5
y=
hasil=x is y #FLASE
print(x,"is",y,"=",hasil)
print("nilai x=",X,"id =",hex(id(x))
print("nilai y=",y,"id =",hex(id(y))