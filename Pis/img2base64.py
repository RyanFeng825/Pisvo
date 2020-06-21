import base64
way=raw_input("Please input the path:")
f=open(way,"rb")
ls_f=base64.b64encode(f.read())
f.close()
c=open("0.txt","w")
c.write(ls_f)
c.close()
print("Finished")
