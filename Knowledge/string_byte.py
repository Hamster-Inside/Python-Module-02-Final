text = 'szynszylka'

text_in_bytes = text.encode()
print (type(text_in_bytes))
print(text_in_bytes)
text_in_str = text_in_bytes.decode()
print(type(text_in_str))
print(text_in_str)