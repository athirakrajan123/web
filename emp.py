class Employee:
    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
    # def display(self):
    #     print(self.id,self.name,self.desig,self.salary)
dic={}
f=open("data","r")
for i in f:
    d=i.rstrip("\n").split(",")
    id=d[0]
    name=d[1]
    desig=d[2]
    salary=d[3]
    e1=Employee(id,name,desig,salary)
    # e1.display()
    dic[id]=id,name,desig,salary
print(dic)
print(dic['1000'])
for id in dic:
    # name=input("enter property:")
    if name in dic['1000']:
        print(dic['1000'][name])
    else:
        print("invalid property")
# else:
#     print("not valid id")