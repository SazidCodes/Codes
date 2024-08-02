name = ['sazid', 'rahat', 'tasin']
for x in name:
    print(f'{x.title()} is a good student')

digits = [1,4,3,2,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [ value ** 2 for value in range(1,11) ]
print(squares)

students = ['sazid', 'rahat', "tasin", 'antor', 'irina','priom']
print(students[0:3])

for student in students:
    if(student == 'sazid'):
        print(student.upper())
    else:
        print(student.title())

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if(requested_topping in available_toppings):
        print(f'{requested_topping.upper()} is added')
    else:
        print(f'{requested_topping}  is not available')

alien_0 = {'color': 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'you have just got {new_points} now')

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 6
print(alien_1)

alien_0['color'] = 'blue'
print(alien_0['color'])

alien_0['speed'] = 'medium'
print(alien_0)
if alien_0['speed'] == 'low':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] =  alien_0['x_position'] + x_increment
print(f"New position : {alien_0['x_position']}")

#removing key value pair
del alien_0['points']
print(alien_0)

alien_0.get('points', 'no point value assigned')
print(alien_0)
new_value = alien_0.get('points', 'no point value assigned')
print(new_value)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for  x,y in user_0.items():
    print(f'key = {x}')
    print(f'value = {y}')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language}")

for name in favorite_languages.keys():
    print(name)
for language in favorite_languages.values():
    print(language)

for name in sorted(favorite_languages.keys()):
    print(f"{name} , thank you for participating the poll")

aliens =[]
for x in range(30):
    new_alien =  {'color':'green', 'points':5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)

print(f"the number of aliens is {len(aliens)}")
print(aliens)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username,user_info in users.items():
    print(f'username : {username}')
    print(f'Full name : {user_info['first'] } {user_info['last']}')
    print(f"location : {user_info['location']}\n")

    