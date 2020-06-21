import fileinput
import linecache
while True:
 ln = 1
 try:
  dn = raw_input('data name:')
  if dn == 'exit':break
  try:
    a = open(dn,'r')
  except IOError:
    print('The system cannot find this data.')
    continue
  te = raw_input('type:')
  if te == 'exit':break
  tn = raw_input('type:'+str(te)+',name:')
  if tn == 'exit':break
  sm = str(te)+':'+str(tn)+'\n'
  b = len(a.readlines())
  ga = 0
  s = 0
  print('reading')
  for line in fileinput.input(dn):
      if ga == b:break
      if sm == line:
        s += 1
        ga += 1
        print('in line '+str(ln))
        ln += 1
        while True:
          lgn = raw_input('How many lines do you want to print:')
          if lgn.isdigit()is False or lgn.count('.') == 1:
            print('error')
            continue
          else:break
        ES = 0
        lns = ln
        while True:
          if int(lgn) == 0:
            print('non-print')
            break
          if ES == int(lgn):break
          if lns > b:
            print("error:can't find more lines")
            break
          print('next:')
          print(linecache.getline(dn,lns))
          ES += 1
          lns += 1
        ES = 0
        lns = ln-2
        while True:
          if int(lgn) == 0:
            print('non-print')
            break
          if ES == int(lgn):break
          if lns < 0:
            print("error:can't find more lines")
            break
          print('last:')
          print(linecache.getline(dn,lns))
          lns -= 1
          ES += 1
      else:
          ga += 1
          ln += 1
  if s > 1:print(str(s)+' results')
  elif s == 1:print(str(s)+' result')
  else:print('no result')
 except EOFError:break
print('Thank you')

