def greet_user():
    print('hello')
greet_user()

def greet_user(name):
    print(f'hi my name is {name}')
greet_user('jessica')

def build_person(first_name, last_name, age = None):
    person = {'first name' : first_name , 'last_name' : last_name}
    if age:
        person['age'] = age
    return person
coder = build_person('sazid', 'hasan', age = 22)
print(coder)
