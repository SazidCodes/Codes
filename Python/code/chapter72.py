unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    user_shift = unconfirmed_users.pop()
    confirmed_users.append(user_shift)
confirmed_users.reverse()
print(confirmed_users)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
pets.remove('cat')
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input('what is your name : ')
    response = input('which place do you want to visit:')
    responses[name] = response
    repeat = input('do you want to allow others to participate(yes/no) : ')
    if repeat == 'no':
        polling_active = False
print(responses)
