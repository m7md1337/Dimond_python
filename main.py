def cheche(x,y): # x mean number of loop , y its static mean number your enter ex: 7 
  Center = round(y/2+0.5)
  diff = abs(Center-x) # abs function conver nigatave to positive
  space = abs((diff+diff+2)-y)
  if x == 1 or x == y:
    return " "*diff + "*" + " "*diff
  else:
    return " "*diff+"*"+" "*space+"*"+" "*diff
 
num = int(input("enter num: "))
for xx in range(1,num+1):
  print(cheche(xx,num))

