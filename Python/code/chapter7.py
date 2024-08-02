message = input("Tell me something and i will repeat it to you : ")
print(message)

age = input("what is your age : ")
age = int(age)
print(age>=18)

current_number = 1
while current_number<=10:
    print(current_number)
    current_number+=1

prompt = 'tell me something and i will repeat it to you'
prompt+='\n enter quit if you dont want to continue'
message = ''
while message !='quite':
    message = input("write")
    print(message)

current_number=1
while current_number<=10:
    current_number+=1
    if current_number % 2 == 0:
        continue
    print(current_number)

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
