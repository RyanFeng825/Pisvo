#coding=gb18030
cache=[]
jc_list=[]
pd_list=[]
import time as t
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import datetime
import timedelta

waitNumber=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def demicalSystemToOthers(Number,System):

 intergerList=[]

 decimalList=[]

 result=""

 decimal=Number-int(Number)

 interger=int(Number)

 while interger>=System:

  intergerList.append(waitNumber[interger%System])

  interger=interger//System

 intergerList.append(waitNumber[interger])


 start=t.clock()

 while decimal!=0:

  decimal*=System

  decimalList.append(waitNumber[int(decimal//1)])

  decimal-=decimal//1

  if t.clock()-start>=0.001:

   break

 for k in range(len(intergerList)):

  result+=str(intergerList.pop(-1))

 if decimalList!=[]:

  result+="."

 for k in decimalList:

  result+=str(k)

 return result

def othersToDemicalSystem(NumberandSystem,System):



 result=0

 interger=NumberandSystem[0].split(".")[0]


 try:

  decimal=NumberandSystem[0].split(".")[1]

 except:

  decimal="0"


 for i in range(len(interger)):

  result+=waitNumber.index(interger[i])*(System**(len(interger)-i-1))

 for j in range(len(decimal)):

  result+=waitNumber.index(decimal[j])*(System**(-j-1))

 return result

def main(cs1,cs2):
 print("Welcome to use SystemChangingMode-1.0.2-r2d5g1")

 numberAndPreviousSystem=cs1.split(" ")

 LaterSystem=int(cs2)

 num=cs1.split(" ")[0]
 s=len(cache)
 c=0
 cs=""
 for q in cache:
     if s==c:break
     left=q.split("=")[0]
     right=q.split("=")[1]
     if left==num:
         result=right
         cs="ok"
 if cs=="ok":
     print(result)
     return

 symbol=""

 if numberAndPreviousSystem[0][0]=="-":

  numberAndPreviousSystem[0]=numberAndPreviousSystem[0][1:]

  symbol+="-"

 previousSystem=int(numberAndPreviousSystem[1])

 intermediateNumber=othersToDemicalSystem(numberAndPreviousSystem,previousSystem)

 resultNumber=demicalSystemToOthers(intermediateNumber ,LaterSystem)


 try:

  print(symbol+resultNumber[:resultNumber.index(".")+11]+"("+str(LaterSystem)+")")
  global cv
  cv=resultNumber[:resultNumber.index(".")+11]
  try:
   cv=int(cv)
  except ValueError:
      pass
  cache.append("("+cs1.split(" ")[0]+")"+cs1.split(" ")[1]+"="+symbol+resultNumber[:resultNumber.index(".")+11]+"("+str(LaterSystem)+")")
 except:
  print(symbol+resultNumber+"("+str(LaterSystem)+")")
  global cv
  cv=resultNumber
  try:
   cv=int(cv)
  except ValueError:
      pass
  cache.append("("+cs1.split(" ")[0]+")"+cs1.split(" ")[1]+"="+symbol+resultNumber+"("+str(LaterSystem)+")")
def pint(num1):
        if int(num1)==num1:
            global result
            result=int(num1)
        else:
            global result
            result=num1
def ys(ysf):
            global n1,n2
            n1=ysbds.split(ysf)[0]
            n2=ysbds.split(ysf)[1]
def ysb():
    global n1,n2,n3
    try:
        n1=float(n1)
        n2=float(n2)
        n3="no"
    except ValueError:
        print("A number can't be a string!")
        n3="ok"
def basic():
    global result
    print('welcome to use BasicMode-1.0.6')
    while True:
      try:
          global ysbds
          ysbds=raw_input('input:')
      except EOFError:
          break
      if ysbds=="finish":
          break
      s=0
      q=len(cache)
      for cr in cache:
          if s==q:
              break
          com=cr.split("=")[0]
          re=cr.split("=")[1]
          if com==ysbds:
              print re
              a=0
              break
          s+=1
      try:
          if a==0:continue
      except NameError:
          pass
      if "+" in ysbds:
            ys("+")
            ysb()
            if n3=="ok":continue
            result=float(n1)+float(n2)
            pint(result)
            print(result)
      elif "-" in ysbds:
            ys("-")
            ysb()
            if n3=="ok":continue
            result=float(n1)-float(n2)
            pint(result)
            print(result)
      elif "*" in ysbds:
            ys("*")
            ysb()
            if n3=="ok":continue
            result=float(n1)*int(n2)
            pint(result)
            print(result)
      elif "/" in ysbds:
            ys("/")
            ysb()
            if n3=="ok":continue
            try:
                result=float(n1)/float(n2)
            except ZeroDivisionError:
                print("ZeroDivisionError:integer division or modulo by zero")
                continue
            pint(result)
            print(result)
      elif "^" in ysbds:
            ys("^")
            ysb()
            if n3=="ok":continue
            result=float(n1)**float(n2)
            pint(result)
            print(result)
      else:
            print("invalid")
      try:
          cache.append(ysbds+"="+str(result))
      except NameError:continue
      while q>=100:
          del cache[0]
      else:continue
def dm():
    global result
    print("welcome to use MoreMode-2.0.23")
    while True:
        try:
            zt=raw_input("input:")
        except EOFError:
            break
        if zt=="exit":break
        n1=raw_input("number1:")
        n2=raw_input("number2:")
        result=0
        try:
            n1=int(n1)
            n2=int(n2)
        except ValueError:
            print("You only can input two integers")
            continue
        if n1==1 or n2==1:
            result=1
            print(result)
            continue
        if n1==0 or n2==0:
            print("error")
            continue
        zh=zt+" "+str(n1)+" "+str(n2)
        q=len(cache)
        s=0
        for zha in cache:
          if s==q:
              break
          com=zha.split("=")[0]
          re=zha.split("=")[1]
          if com==zh:
              print re
              a=0
              break
          s+=1
        try:
            if a==0:continue
        except NameError:
            pass
        if n1<n2:
                min=n1
                max=n2
        else:
                min=n2
                max=n1
        if zt=="maxin":
          if n1<n2:
                min=n1
                max=n2
          else:
                min=n2
                max=n1
          a=2
          while a<=min:
                if n1%a==0 and n2%a==0:
                    result=a
                    a+=1
                else:
                    a+=1
          else:
              if result==0:
                  print("none result")
                  cache.append("maxin "+str(n1)+" "+str(n2)+"="+"none")
              else:
                  print(result)
                  cache.append("maxin "+str(n1)+" "+str(n2)+"="+str(result))
        elif zt=="minout":
            if n1<n2:
                min=n1
                max=n2
            else:
                min=n2
                max=n1
            an=max
            maxn=max*min
            while an<maxn:
                if an%n1==0 and an%n2==0:
                    result=an
                    break
                else:an+=1
            if result==0:
                  result=maxn
                  print(result)
            else:
                  print(result)
            cache.append("minout "+str(n1)+" "+str(n2)+"="+str(result))
        else:print("invalid")
        try:
            if last!=result:
                cache.append(zt+" "+str(n1)+" "+str(n2)+"="+str(result))
            else:continue
        except NameError:
            continue
        while q>=100:
          del cache[0]
        else:continue
def fl(num1,num2):
  while 1:
    global qw,bds1,bds2
    qw="none"
    try:
        BdsCache1=num1.split(")")[0]
        BdsCache2=num1.split(")")[1]
        BdsCache3=num2.split(")")[0]
        BdsCache4=num2.split(")")[1]
    except:
        qw="ok"
        break
    if BdsCache2>10:
        bds1=str(BdsCache1.split("(")[1])+" "+BdsCache2
    elif BdsCache2<=10:
        try:
            bds1=str(int(BdsCache1.split("(")[1]))+" "+BdsCache2
        except:
            qw="ok"
    if BdsCache4>10:
        bds2=str(BdsCache3.split("(")[1])+" "+BdsCache4
    elif BdsCache4<=10:
        try:
            bds2=str(int(BdsCache3.split("(")[1]))+" "+BdsCache4
        except:
            qw="ok"
    break
def nss():
  global result
  print("Welcome to use NotSameSystemMode-1.0.0")
  print("ImportantWarning:Please input with this(must be)\n\
           (Number1)System +-*/^ (Number2)System")
  while True:
    try:
        global ysbds
        ysbds=raw_input("input:")
    except EOFError:
        break
    global label
    label=""
    for q in cache:
        left=q.split("=")[0]
        right=q.split("=")[1]
        if left==ysbds:
            result=right
            label="ok"
    if label=="ok":
        print(result)
        continue
    if "+" in ysbds:
        ys("+")
        q="+"
        fl(n1,n2)
        if qw=="ok":continue
        main(bds1,"10")
        a1=cv
        main(bds2,"10")
        a2=cv
        result=a1+a2
    elif "-" in ysbds:
        ys("-")
        q="-"
        fl(n1,n2)
        if qw=="ok":continue
        main(bds1,"10")
        a1=cv
        main(bds2,"10")
        a2=cv
        result=a1-a2
    elif "*" in ysbds:
        ys("*")
        q="*"
        fl(n1,n2)
        if qw=="ok":continue
        main(bds1,"10")
        a1=cv
        main(bds2,"10")
        a2=cv
        result=a1*a2
    elif "/" in ysbds:
        ys("/")
        q="/"
        fl(n1,n2)
        if qw=="ok":continue
        main(bds1,"10")
        a1=cv
        main(bds2,"10")
        a2=cv
        if a2==0:
            print("ZeroDivisionError:integer division or modulo by zero")
            continue
        result=a1/a2
    elif "^" in ysbds:
        ys("^")
        q="^"
        fl(n1,n2)
        if qw=="ok":continue
        main(bds1,"10")
        a1=cv
        main(bds2,"10")
        a2=cv
        result=a1**a2
    elif ysbds=="finish":break
    else:
        print("invalid")
        continue
    while True:
        try:
            ls=int(raw_input("Later system:"))
            main(str(result)+" "+"10",str(ls))
            result=cv
            print(result)
            break
        except:
            print("invalid")
            continue
    cache.append(str(n1)+q+str(n2)+"="+"("+str(result)+")"+str(ls))
def mn():
  while 1:
    print("Welcome to use MoreNumberMode-1.0.0")
    global result
    result=0
    try:
        try:
            result=input("input:")
        except EOFError:
            break
        if result=="finish":break
        print(str(result))
    except:
        print("invalid")
def draw2d(bds):
    print("Welcome to use Draw2dMode-1.0.0-rc12")
    low=lambda x:10000 if x>10000 else -10000 if x<-10000 else x
    try:
        f=lambda x:bds
    except:
        print("No modele named "+bds)
        return

    start=-10 
    stop=10 
    step=0.01


    num=(stop-start)/step
    x = np.linspace(start,stop,num)
    y = f(x)

    for i in range(len(y)):
        y[i]=low(y[i])
    z=y

    fig=plt.figure(figsize=(6,6))

    plt.plot(x, y,label='First Curve')

    plt.grid(True)

    plt.axis("equal")
    plt.xlim((-10, 10))
    plt.ylim((-10, 10))

    plt.plot([2*min(x),2*max(x)], [0,0],label='x-axis')
    plt.plot([0,0],[2*min(y),2*max(y)],label='y-axis')
    plt.legend()
    plt.show(fig)
def draw3d():
    pass
def nssmn():
    while 1:
     print("Welcome to use NotSameSystemMoreNumberMode-1.0.0")
     print("ImportantWarning:\
     	you must write follow this:\
     	Binary numbers:0b+number\n\
     	October numbers:0+number\n\
     	Hexagon numbers:0x+number\n\
     	Integer numbers:number\n\
      Other systems' numbers:\
      now isn't support")
     try:
       try:
           result=input("input:") 
           if result=="finish":break
       except EOFError:
           break
       print(str(result))
     except:
         print("invalid")
while True:
    try:
        if i==False:break
    except NameError:
        pass
    try:
        zt=raw_input('please input the mode:')
    except EOFError:
        break
    if zt=='basic':
        basic()
        continue
    elif zt=='dm':
        dm()
        continue
    elif zt=='exit':
        break
    elif zt=="cache":
        s=len(cache)
        if s==0:
            print("None")
            continue
        else:
            print(str(cache))
    elif zt=="clear":
        if jczt==True:
            cache=[]
            print("finish")
        else:
            print("The program is not currently activated and cannot be executed")
            continue
    elif zt=="sys":
        while True:
            try:
                zta=raw_input("Go on:")
            except EOFError:
                print("invalid")
                continue
            if zta=="yes":
                pass
            elif zta=="no":
                break
            else:
                print("invalid")
            try:
                numberAndPreviousSystem=raw_input("请输入要转换的数及其进制（用空格分开）：")
            except EOFError:
                print("invalid")
                continue
            if numberAndPreviousSystem.count(" ")==1:
                l=numberAndPreviousSystem.split(" ")[0]
                r=numberAndPreviousSystem.split(" ")[1]
                try:
                    l=int(l)
                    r=int(r)
                except:
                    print("Input Error")
                    continue
            else:
                print("Input Error")
                continue
            try:
                LaterSystem=raw_input("请输入转换后的数的进制：")
            except EOFError:
                print("invalid")
                continue
            try:
                Later=int(LaterSystem)
            except:
                print("Input Error")
            main(numberAndPreviousSystem,LaterSystem)
    elif zt=="nss":
        nss()
    elif zt=="mn":
        mn()
    elif zt=="nssmn":
        nssmn()
    elif zt=="draw2d":
        try:
            a=raw_input("Enter a relationship between X and Y \
(where x is an independent variable and Y is a dependent variable):")
        except EOFError:
            break
        try:
            l=a.split("=")[0]
            r=a.split("=")[1]
            if l=="" or " "in l or r=="" or " "in r:
                print("invalid")
                continue
            else:
                draw2d(r)
        except:
            print("invalid")
            continue
    elif zt=="draw3d":
        draw3d()
    else:
        print('invalid')
        continue
print('thanks')