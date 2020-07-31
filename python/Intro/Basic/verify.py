import getpass

while True:
    print('请输入用户名(Enter your username):')
    age = input()
    if age.isdecimal():
        break
    print('Please enter your username.')

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

# from getpass import getpass
# from getpass import *

username = input(': ')
password = input('请输入口令: ')
# 输入口令的时候终端中没有回显
# password = getpass.getpass('请输入口令: ')

if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
