# if we need for example check if we have a email we need confirm we have a @ we can use this
email = "ilya.ccnp@gmail.com"
index = email.find("@")
print(index)
print(email[:index])
print(email[index+1:]) # if ew need to tack the word until @
