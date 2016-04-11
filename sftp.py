import pysftp
#from passlib.hash import sha256_crypt
import getpass

print("### sftp transfer ###")


def transfer(server,user,rsakey,rsakeypass):
    sftp = pysftp.Connection(server,username=user,private_key=rsakey,private_key_pass=rsakeypass)
    sftp.listdir(remotepath='.')
    #sftp.put("localfile", "remotefile")
    sftp.close()

##server = raw_input("enter server: ")
##user = raw_input("enter username: ")
rsakp_input = getpass.getpass(prompt="enter keypass: ", stream=None)

transfer("","","", rsakp_input)

print("done. bye.")
