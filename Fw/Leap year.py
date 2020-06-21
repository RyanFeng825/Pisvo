while True:
  A = raw_input('Enter text:')
  if A == 'end':break
  try:
    B = int(A)
  except ValueError:
    print('input error')
    continue
  if B != 0:
    if B < 0:
      print('input error')
      continue
  if isinstance(B,int) is False:
      print('input error')
      continue
  Z = map(int,str(A))
  if str(Z[:1]) == str(map(int,str(0))):
      print('input error')
      continue
  if B%100 == 0:
      if B%400 == 0:
        print('It is a leap year')
      else:
        print('It is not a leap year')
  else:
      if B%4 == 0:
        print('It is a leap year')
      else:
        print('It is not a leap year')
print('thank you')
