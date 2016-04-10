import pysftp
#from passlib.hash import sha256_crypt
import getpass

print("### sftp transfer ###")


def transfer(server,user,pw):
    sftp = pysftp.Connection(server,username=user,password=pw)
    sftp.put("/tmp/hello.txt", "/home/grob/hello1.txt")
    sftp.close()

##server = raw_input("enter server: ")
##user = raw_input("enter username: ")
pw = getpass.getpass(prompt="enter pass: ", stream=None)

transfer("localhost","grob",pw)

print("done. bye.")

