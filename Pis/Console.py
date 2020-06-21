#coding=gbk
try:
 import time
 import os
 import subprocess
 import platform
 dt = time.localtime()
 ft = "%Y-%m-%d %H:%M:%S"
 title1 = time.strftime(ft,dt)
 print("Welcome to use Pisvo Console!")
 print(title1)
 while True:
     sysinfo = platform.platform()
     sysname = sysinfo.split("-")[0]
     if sysname != "Windows":
         print("Warning:\n\
 Detecting that the current system is not Windows\n\
 may cause compatibility problems in subsequent operations.\n\
 These problems may cause the program to flash back.\n\
 If you solve this problem,\n\
 you can use the Windows system environment\n\
 or use the Windows virtual machine.")
         print("Your system is "+sysname)
         break
     else:
         bbhycl = sysinfo.split("-")[1]
         try:
             bbh = int(bbhycl.split(".")[0])
         except ValueError:
             print("Warning:\n\
Discovering that the current Windows version is smaller than\n\
Windows 7 may cause compatibility problems during running.\n\
To solve this problem, you can run in an environment\n\
above Windows 7 or install virtual machines.")
         if bbh < 7:
             print("Warning:\n\
Discovering that the current Windows version is smaller than\n\
Windows 7 may cause compatibility problems during running.\n\
To solve this problem, you can run in an environment\n\
above Windows 7 or install virtual machines.")
             break
         else:
             print("Your system is "+sysname)
             break
 while True:
    dqwz = os.getcwd()
    command = raw_input(dqwz+">")
    if command == 'exit':break
    elif command == 'date':
        dt = time.localtime()
        ft = "%Y-%m-%d %H:%M:%S"
        title1 = time.strftime(ft,dt)
        print(title1)
        continue
    elif command.startswith("cd"):
        jc1 = command.count(" ")
        if jc1 == 1:
            ml = command.split(" ")[1]
            if ":" in ml:
                try:
                    os.chdir(ml)
                    continue
                except WindowsError:
                    print("The system can't find the way")
                    continue
            else:
                try:
                    wzml = dqwz + "/" + ml
                    os.chdir(wzml)
                    continue
                except WindowsError:
                    print("The system can't find the way")
                    continue
        elif command == "cd..":
            if len(dqwz)==3:pass
            else:
                last = os.path.dirname(os.getcwd())
                os.chdir(last)
        elif command == "cd/":
            pf = str(dqwz[:1])
            wq = pf + ":/"
            os.chdir(wq)
        else:
            print("invalid command")
            continue
    elif command.startswith("md") or command.startswith("mkdir"):
      if command.count(" ")!=1:
          print("invalid command")
          continue
      try:
        wjjm = command.split(" ")[1]
      except ValueError:
        print("invalid command")
        continue
      if wjjm=="":
          print("invalid command")
          continue
      os.mkdir(wjjm)
    elif command.startswith("rd"):
        try:
            wjjm = command.split(" ")[1]
        except ValueError:
            print("invalid command")
            continue
        if wjjm == "":
            print("invalid command")
            continue
        try:
            os.rmdir(wjjm)
        except WindowsError:
            print("The system can't find it")
    elif command=="ldir":
        a = os.listdir(dqwz)
        jc = len(a)
        s=0
        for line in a:
            s+=1
            if s==jc:break
            print(line)
    elif command=="odir":
        wjjm = raw_input("please input the whole way:")
        if wjjm.count(":")==1 and wjjm.split(":")[0]!=""and wjjm.split(":")[1]!="":
            try:
                a = os.listdir(wjjm)
            except WindowsError:
                print("The system can't find the way")
                continue
            jc = len(a)
            s=0
            for line in a:
                s+=1
                if s==jc:break
                print(line)
        else:
            print("invalid command")
            continue
    elif command.startswith("remove"):
        if command.count(" ")!=1:
            print("invalid command")
            continue
        wjm = command.split(" ")[1]
        if wjm == "":
            print("invalid command")
            continue
        if os.path.isfile(dqwz+"/"+wjm) is False:
            print(wjm+" isn't a file")
            continue
        os.remove(dqwz+"/"+wjm)
    elif command=="ver":
        print(sysinfo)
    else:
        process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        process.wait()
        command_output = process.stdout.read().decode('gbk')
        print(command_output)
 print("Thank you for your using")
except EOFError:
    print('invalid command')
    dt = time.localtime()
    ft = "%Y-%m-%d %H:%M:%S"
    title1 = time.strftime(ft,dt)
    try:
        q1 = open('error.bst','r')
        q = open('error.bst','a')
        q.write(title1+"\n")
        q.write("invalid input\n")
        q.write("accident exit\n")
        q.close()
    except IOError:
        q = open('error.bst','w')
        q.write(title1+"\n")
        q.write("invalid input\n")
        q.write("accident exit\n")
        q.close
