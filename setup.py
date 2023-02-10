import encryptPassword.api as api

f = open('password.txt','w')
write = api.crypte_key("TEST") + '\n' + '\n'
f.write(write)
f.close()
