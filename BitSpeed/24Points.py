print('loading')
import random
import linecache
while True:
    try:
        gdr = open('gd.txt','r')
    except IOError:
        print('lose the game data,try to write a new data')
        gdw = open('gd.txt','w')
        gdw.close()
        gdr = open('gd.txt','r')
    try:
        glyd = open('administrator.txt')
        wdjc = len(glyd.readlines())
        if wdjc != 2:
            print("administrator.txt is broken,and can't use.Please input again.")
            xr = open('administrator.txt','w')
            adne = raw_input("input administrator's name:")
            adpd = raw_input("input administrator's password:")
            xr.write(adne+'\n')
            xr.write(adpd)
            xr.close()
    except IOError:
        print("The system can't find administrator's data.Try to write.")
        adne = raw_input("input administrator's name:")
        adpd = raw_input("input administrator's password:")
        xr = open('administrator.txt','w')
        xr.write(adne+'\n')
        xr.write(adpd)
        xr.close()
    zhs = len(gdr.readlines())
    zhsjc = str(linecache.getline('gd.txt',1))
    if zhs > 1:
        print('gd.txt is broken.Try to write a new data.')
        gdw = open('gd.txt','w')
        print('All right')
    while True:
        print('Hello')
        do = raw_input('what do you want to do:')
        if do == 'play':break
        elif do == 'admin':
            srn = raw_input("input the administrator's name:")
            srn += '\n'
            nameyz = linecache.getline('administrator.txt',1)
            if srn != nameyz:
                print('wrong!')
                break
            srp = raw_input("input the administrator's password:")
            srp += '\n'
            passwordyz = linecache.getline('administrator.txt',2)
            if srp != passwordyz:
                print('wrong!')
                break
            print('Hello!Administrator '+srn)
            while True:
                zhs = len(gdr.readlines())
                ado = raw_input('what do you want to do:')
                if ado == 'end':
                    st = 'break'
                    break
                elif ado == 'changenp':
                    nn = raw_input('input your new name:')
                    np = raw_input('input your new password:')
                    nc = open('administrator.txt','r+')
                    nc.seek(0)
                    nc.truncate()
                    nc.write(nn+'\n')
                    nc.write(np)
                    nc.close()
                    continue
                elif ado == 'score':
                    spd = raw_input('do:')
                    if spd == 'read':
                        if zhs == 0:
                            print('nothing')
                            continue
                        else:
                            print(str(linecache.getline('gd.txt',zhs)))
                            continue
                    elif spd == 'cscore':
                        xlh = raw_input('input your number:')
                        bzxlh = 'HJHGF-A4B90-CCV23-567YU-W2E3T-@(*%!'
                        if xlh == bzxlh:
                            news = raw_input('input the new number:')
                            with open('gd.txt','r+') as l:
                                l.seek(0)
                                l.truncate()
                                l.write(news)
                                l.close()
                            print('All right')
                            continue
                        else:
                            print('wrong number!')
                            continue
                    else:
                        print('invalid')
                        continue
                else:
                    print('invalid')
                    continue
        if st == 'break':break
    gdr = open('gd.txt','r')
    zhs = len(gdr.readlines())
    while True:
      if zhs == 0:
        print('welcome')
        df = 0
        break
      else:
        print('welcome')
        df = linecache.getline('gd.txt',zhs)
        df = int(df)
        print('your score is '+str(df))
        break
    while True:
        result = 0
        r1 = random.randint(1,13)
        r2 = random.randint(1,13)
        r3 = random.randint(1,13)
        r4 = random.randint(1,13)
        r5 = random.randint(1,13)
        r6 = random.randint(1,13)
        r7 = random.randint(1,13)
        r8 = random.randint(1,13)
        def jiafa(a,b):
            global result
            result = a+b
        def jianfa(a,b):
            global result
            result = a-b
        def chengfa(a,b):
            global result
            result = a*b
        def chufa(a,b):
            global result
            result = a/b
        def chengfang(a,b):
            global result
            result = pow(a,b)
        level = raw_input('level(1-3):')
        if level == '1':
            srjc = [str(r1),str(r2),str(r3),str(r4),str(r5),str(r6),str(r7),str(r8)]
            bs = 20
            print("You can ues "+str(srjc))
            print("You have "+str(bs)+" steps.")
        elif level == '2':
            srjc = [str(r1),str(r2),str(r3),str(r4),str(r5),str(r6)]
            bs = 14
            print("You can ues "+str(srjc))
            print("You have "+str(bs)+" steps.")
        elif level == '3':
            srjc = [str(r1),str(r2),str(r3),str(r4)]
            bs = 8
            print("You can ues "+str(srjc))
            print("You have "+str(bs)+" steps.")
        else:
            print('invalid level')
            continue
        while True:
            if bs == 0 or len(srjc) == 1:break
            if result == 24:break
            do = raw_input('do(number1(+-*/^)number2):')
            if do.count('+') == 1:
                fn = do.split('+')[0]
                sn = do.split('+')[1]
                if fn in srjc and sn in srjc:
                   jiafa(int(fn),int(sn))
                   bs -= 1
                   try:
                       srjc.remove(str(fn))
                       srjc.remove(str(sn))
                   except ValueError:
                       print('invalid')
                       srjc.append(str(sn))
                       print('you can use '+str(srjc))
                       print('you have '+str(bs)+' step')
                       continue
                   srjc.append(str(result))
                   print('you can use '+str(srjc))
                   print('you have '+str(bs)+' step')
                else:
                    print('invalid')
                    bs -= 1
                    print('you can use '+str(srjc))
                    print('you have '+str(bs)+' step')
                    continue
            elif do.count('-') == 1:
                fn = do.split('-')[0]
                sn = do.split('-')[1]
                if fn in srjc and sn in srjc:
                   jianfa(int(fn),int(sn))
                   bs -= 1
                   try:
                       srjc.remove(str(fn))
                       srjc.remove(str(sn))
                   except ValueError:
                       print('invalid')
                       srjc.append(str(sn))
                       print('you can use '+str(srjc))
                       print('you have '+str(bs)+' step')
                       continue
                   srjc.append(str(result))
                   print('you can use '+str(srjc))
                   print('you have '+str(bs)+' step')
                else:
                    print('invalid')
                    bs -= 1
                    print('you can use '+str(srjc))
                    print('you have '+str(bs)+' step')
                    continue
            elif do.count('*') == 1:
                fn = do.split('*')[0]
                sn = do.split('*')[1]
                if fn in srjc and sn in srjc:
                   chengfa(int(fn),int(sn))
                   bs -= 1
                   try:
                       srjc.remove(str(fn))
                       srjc.remove(str(sn))
                   except ValueError:
                       print('invalid')
                       srjc.append(str(sn))
                       print('you can use '+str(srjc))
                       print('you have '+str(bs)+' step')
                       continue
                   srjc.append(str(result))
                   print('you can use '+str(srjc))
                   print('you have '+str(bs)+' step')
                else:
                    print('invalid')
                    bs -= 1
                    print('you can use '+str(srjc))
                    print('you have '+str(bs)+' step')
                    continue
            elif do.count('/') == 1:
                fn = do.split('/')[0]
                sn = do.split('/')[1]
                if fn in srjc and sn in srjc and sn != '0':
                   chufa(int(fn),int(sn))
                   bs -= 1
                   try:
                       srjc.remove(str(fn))
                       srjc.remove(str(sn))
                   except ValueError:
                       print('invalid')
                       srjc.append(str(sn))
                       print('you can use '+str(srjc))
                       print('you have '+str(bs)+' step')
                       continue
                   srjc.append(str(result))
                   print('you can use '+str(srjc))
                   print('you have '+str(bs)+' step')
                else:
                    print('invalid')
                    bs -= 1
                    print('you can use '+str(srjc))
                    print('you have '+str(bs)+' step')
                    continue
            elif do.count('^') == 1:
                fn = do.split('^')[0]
                sn = do.split('^')[1]
                if fn in srjc and sn in srjc:
                   chengfang(int(fn),int(sn))
                   bs -= 1
                   try:
                       srjc.remove(str(fn))
                       srjc.remove(str(sn))
                   except ValueError:
                       print('invalid')
                       srjc.append(str(sn))
                       print('you can use '+str(srjc))
                       print('you have '+str(bs)+' step')
                       continue
                   srjc.append(str(result))
                   print('you can use '+str(srjc))
                   print('you have '+str(bs)+' step')
                else:
                    print('invalid')
                    bs -= 1
                    print('you can use '+str(srjc))
                    print('you have '+str(bs)+' step')
                    continue
            else:
                print('invaild')
                print('you can use '+str(srjc))
                bs -= 1
                print('you have '+str(bs)+' step')
                continue
        if result == 24:
            if level == '1':
                df += 15
                print('you win,you score is '+str(df))
                with open('gd.txt', 'w') as f:
                    f.write(str(df))
                    f.close()
                lpd = raw_input('play again:')
                if lpd == 'no':
                    itc = 'break'
                    break
                elif lpd == 'other':
                    itc = 'continue'
                    break
                else:continue
            elif level == '2':
                df += 25
                print('you win,you score is '+str(df))
                with open('gd.txt', 'w') as f:
                    f.write(str(df))
                    f.close()
                lpd = raw_input('play again:')
                if lpd == 'no':
                    itc = 'break'
                    break
                elif lpd == 'other':
                    itc = 'continue'
                    break
                else:continue
            else:
                df += 35
                print('you win,you score is '+str(df))
                with open('gd.txt', 'w') as f:
                    f.write(str(df))
                    f.close()
                lpd = raw_input('play again:')
                if lpd == 'no':
                    itc = 'break'
                    break
                elif lpd == 'other':
                    itc = 'continue'
                    break
                else:continue
        else:
            print('you lose,you score is '+str(df))
            with open('gd.txt', 'w') as f:
                f.write(str(df))
                f.close()
            lpd = raw_input('play again:')
            if lpd == 'no':
                itc = 'break'
                break
            elif lpd == 'other':
                itc = 'continue'
                break
            else:continue
    try:
        if itc == 'break':break
        elif itc == 'continue':
            itc = 'nothing'
            continue
        else:
            itc = 'error'
            continue
    except NameError:pass
print('thank you')
with open('gd.txt', 'r+') as f:
  f.seek(0)
  f.truncate()
  f.write(str(df))
  f.close()
try:
    gdw.close()
except NameError:pass
