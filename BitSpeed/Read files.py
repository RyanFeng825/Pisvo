while True:
 try:
  dn = raw_input('data name:')
  if dn == 'exit':break
  try:
    ffile = open(dn,'r')
  except IOError:
      print('The system cannot find this data')
      continue
  while True:
      for (num,value)in enumerate(ffile):
        num += 1
        num = str(num)
        string = str(value)
        print(num)
        print(value)
 except EOFError:
     print('Accidental withdraw')
     break
print('Thank you')

