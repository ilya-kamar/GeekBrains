import re

pattern = '([\.a-zA-Z0-9_]+@[a-z]+\.(ru|org|com))'
# email = 'ilya.ccnp1988@gmail.com'
# print(f"match => {re.match(pattern, email)}" )
# print(f"search => {re.search(pattern, email)}")

text = 'dsilya.ccnp1988@gmail.comkfds ilya.ccnp1988@gmail.com kfjdskfdj ilya.ccnp1988@gmail.comdfjksd fk kdsf dskfs kdf ilya.ccnp1988@gmail.com'
print(re.findall(pattern, text))
