msg = "Hello World!"
print(msg)
for x in range(10):
    print (msg+str(x))

msg1 = "it is a simple code of"+" "+msg
print(msg1.title())

msg.lstrip()
msg1.lstrip()

fullmsg = f"Test: {msg}{msg1}"

for y in range(18):
    print(fullmsg.rstrip()+str(y))



