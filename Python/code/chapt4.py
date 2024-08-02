users = {
    'aeinstein':{
        'first' : 'albert'
        'last'  : 'einstein'
        'location': 'prinston'
    }
    'mcuri':{
        'first' : 'meri'
        'last' : 'curi'
        'location':'paris'
    }
}

for username,user_info in users.items():
    print(f'username : {username}')
    print(f'Full name : {user_info['first'] } {user_info['last']}')
    print(f"location : {user_info['location']}\n")