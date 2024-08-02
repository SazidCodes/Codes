name = ['sazid','priom','antor']
message = f'here the student of madarasa is {name[-1].title()}'
print(message)
print(f'{name[0].title()} is the best in maths and {name[1].title()} bro is the best in law')
name[0] = "irina"
print(name)
cars = []
cars.append('toyota')
cars.append('marcidies')
print(cars)
cars.insert(0,"bmw")
cars.remove('toyota')
print(cars)
last_car = cars.pop()
print(last_car)
new =  ['bmw', 'audi', 'toyota', 'subaru']
new.sort()
print(new)
new.sort(reverse=True)
print(new)
new.reverse()
print(new)