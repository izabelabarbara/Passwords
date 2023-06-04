print ('''\033[35mMY LOGIN SYSTEM\033[0m

👾👾👾👾👾👾👾
''')
username = input('\033[36mUsername > \033[0m')
password = input('\033[36mPassword > \033[0m')
print()

if username == 'iza' and password == 'password':
  print (f'\033[34mWelcome, {username}!')
  
elif username == 'iza' and password != 'password':
  print (f'\033[31mWrong password, {username}!')
  password = input('\033[36mGive it another try > \n')
  if password == 'password':
    print (f'''\033[32;1mYou did it!!\n
    Welcome to the site, {username}!''')
  else:
    print (f'\033[31mSorry, {username}, please try again in 5 minutes...')

elif username == 'suzanne' and password == '5uzann3':
  print (f'\033[35mOh, hi there {username}!')
elif username == 'suzanne' and password != '5uzann3':
  print (f'\033[31mWrong password, {username}!')
  password = input('\033[36mGive it another try > \n')
  if password == '5uzann3':
    print (f'''\033[32;1mYou did it!!\n
    Welcome to the site, {username}!''')
  else:
    print (f'\033[31mSorry, {username}, please try again in 5 minutes...')

elif username == 'zul' and password == '':
  print (f'\033[35mOh, hi there {username}!')
elif username == 'zul' and password != '':
  print (f'\033[31mWrong password, {username}!')
  password = input('\033[36mGive it another try > \n')
  if password == '':
    print (f'''\033[32;1mYou did it!!
    \033[0;0mWelcome to the site, {username}!''')
  else:
    print (f'\033[31mSorry, {username}, please try again in 5 minutes...')

else:
  print (f'\033[31mSorry, {username}, you\'re not welcome...')