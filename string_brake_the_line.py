# if we need for example check if we have a email we need confirm we have a @ we can use this
email = "ilya.ccnp@gmail.com"
index = email.find("@")
print(index)  # 9
print(email[:index])  # ilya.ccnp
print(email[index + 1:])  # if ew need to tack the word until @   #gmail.com

print(email.split('@'))  # ['ilya.ccnp', 'gmail.com']

# need to check about the functions .ljust()  & .rjust()


# old option
name = "ilya"
age = 32
mony = 30.3
# print("hello %s your age is %i and you have %f mony" % (name, age, mony))
# midle option
# print("hello {} your age is {} and you have {} mony".format(name,age,mony))

# new option
print(f"hello {name} your age is {age} and you have {mony} mony") # need to remember we need put f before our string