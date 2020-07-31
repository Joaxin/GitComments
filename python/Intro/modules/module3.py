import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def foo():
    print("This is a running module")

def bar():
    print("This is an imported module")

## __name__是Python中一个隐含的变量，代表了模块的名字
if __name__ == '__main__':
  print('call foo()')
  foo()
else:
  print('call bar()')
  bar()