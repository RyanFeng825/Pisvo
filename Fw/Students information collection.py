q = open('student score.txt','w')
while True:
  A = raw_input('Name:')
  if A == 'end':break
  a = str(A)
  if A.isdigit() is True:
      print('error:writing error:invalid name')
      continue
  else:
    if a.count('.')>0 or a.count('-')>0:
      print('error:writing error:invalid name')
      continue
  while True:
    B = raw_input('Score:')
    if B == 'end':
      B = ''
      break
    s = str(B)
    if s.count('.') == 1:
      left = s.split('.')[0]
      right = s.split('.')[1]
      if left.startswith('-') and left.count('-') == 1 and right.isdigit():
        lleft = left.split('-')[1]
        if lleft.isdigit():
          print('error:writing error:invalid score')
          continue
      elif left.startswith('-') is False and left.count('-') == 0 and right.isdigit() and left.split():break
      else:
        print('error:writing error:invalid score')
        continue
    elif s.count('.') == 0:
      if B == str(0):break
      elif s.startswith('-'):
        fhh = s.split('-')[1]
        if fhh.isdigit():
          print('error:writing error:invalid score')
          continue
        else:
          print('error:writing error:invalid score')
          continue
      elif s.startswith('-')is False and s.isdigit():
        Z = map(int,str(B))
        if str(Z[:1]) == str(map(int,str(0))):
          print('error:writing error:invalid score')
          continue
        else:break
  C = raw_input('what do you want:')
  if C == 'end':
    q.write('Name:'+str(A)+'\n')
    q.write('Score:'+str(B)+'\n')
    break
  if C == 'delete':
    D = raw_input('Do you really want to delete:')
    if D == 'yes':
      print('deleted:\n'+'Name:'+str(A)+'\n'+'Score:'+str(B)+'\n')
      continue
  print('Name:'+str(A))
  print('Score:'+str(B))
  q.write('Name:'+str(A)+'\n')
  q.write('Score:'+str(B)+'\n')
print('thank you')
q.close()
