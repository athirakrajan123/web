f=open("data","r")
emp={}
for line in f:
    #print(line)
    eid,name,desig,sal,exp=line.rstrip("\n").split(",")
    emp[int(eid)]={"eid":eid,"name":name,"desig":desig,"sal":sal,"exp":exp}
print(emp)
def printval(id=None,**kwargs):
    if id in emp:
        print(emp[id]["name"])
    else:
        print("invalid id")
    if "prop" in kwargs:
        print(emp[id][kwargs["prop"]])


id=int(input("enter id:"))
printval(id)
printval(id,prop="desig")
