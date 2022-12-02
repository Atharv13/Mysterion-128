inp='SHA 69 is best'

#String To Hex
message="".join(["{:02x}".format(ord(c)) for c in inp])
#Padding
if len(message)<32:
  message=message+'0'*(32-len(message))
if len(message)>32:
  message=message[:32]

message=message.upper()

key='0205060752F3E1F2132435465B6C7D88'
r=12
debug=False
rounds=True
ciphertext= encrypt(message,key,r)
