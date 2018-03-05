#Dictionary practice

dic1 = {"Age" : 20, "Class" : 1}
print(dic1["Age"])


name = input("Give your name: ")
age = input("Give your age: ")

dic2 = {"Name" : name, "Age" : age}

print("Name: " + dic2["Name"] + "\n" + "Age: " + dic2["Age"])

print(dic2.items())