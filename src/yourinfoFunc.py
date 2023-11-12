def yourinfo(name,age,gender):
    profile = "name: {}\nage: {}\ngender: {}".format(name,age,gender)
    return profile

myinfo = yourinfo("May","20","female")
print(myinfo)