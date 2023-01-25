import random
counter = 0

d = int(input('kuinka monta noppaa? '))

for i in range(d):
  dice=  random.randint(1,6)
  print(dice) 

  counter += dice

print(f'summa {counter}')




