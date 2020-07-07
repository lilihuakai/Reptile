from my_db import RedisClient

conn = RedisClient('accounts', 'weibo')

def set(username, passwrod):
    result = conn.set(username, passwrod)
    print("账号", username, "密码", passwrod)
    print("录入成功" if result else "录入失败")

def scan():
    print('请输入账号密码组, 输入exit退出读入')
    while True:
        username = input("账号:")
        if username == 'exit':
            break
        passwrod = input("密码:")
        set(username, passwrod)

if __name__ == '__main__':
    scan()
