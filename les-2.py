name_and_lastname = "ilya" + "kamardin"
print(name_and_lastname[-1])
print(name_and_lastname[0:4])
print(name_and_lastname[:4])
print(name_and_lastname[4:])
print(name_and_lastname[::-1]) #if we need to write some word in revers we can use this [::-1]
# [from : to(not include) : step]

# if we need for example check if we have a email we need confirm we have a @ we can use this
email = "ilya.ccnp@gmail.com"
index = email.find("@")
print(index)
print(email[:index])
print(email[index+1:]) # if ew need to tack the word until @




