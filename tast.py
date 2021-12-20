def get_users():
    users = {'user1': {'user_name': 'yuli', 'email' : 'yuli11@gmail.com'},
             'user2': {'user_name': 'yosik', 'email': 'yosik12@gmail.com'},
             'user3': {'user_name': 'erez', 'email': 'erezMaster@gmail.com'},
             'user4': {'user_name': 'amit', 'email': 'tuli@gmail.com'},
             'user5': {'user_name': 'guy', 'email': 'guyTheKing@gmail.com'},
             'user6': {'user_name': 'shahaf', 'email': 'shahafgros@gmail.com'},
             'user7': {'user_name': 'dor', 'email': 'dori100@gmail.com'},
             'user8': {'user_name': 'itamar', 'email': 'itamari@gmail.com'}, }
    return  users

print(get_users().values())