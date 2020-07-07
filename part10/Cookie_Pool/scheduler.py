from multiprocessing import Process
from server import app
from config import *


class Scheduler(object):
    """docstring for Scheduler"""
    @staticmethod
    def generate_cookie(cycle=CYCLE):
        while True:
            print("Cookies生成进程开始运行")
            try:
                for website, cls in GENERATOR_MAP.items():
                    generator = eval(cls + '(website="' + website + '")')
                    generator.run()
            except Exception as e:
                print(e.args)

    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print("Cookies检测进程开始运行")
            try:
                for website, cls in GENERATOR_MAP.items():
                    tester = eval(cls + '(website="' + website + '")')
                    tester.run()
            except Exception as e:
                print(e.args)
    @staticmethod
    def server():
        print("server接口开始运行")
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        if API_PROCESS:
            print(API_PROCESS)
            server_process = Process(target=Scheduler.server)
            server_process.start()
        if GENERATOR_PROCESS:
            print(GENERATOR_PROCESS)
            generate_process = Process(target=Scheduler.generate_cookie)
            generate_process.start()
        if VALID_PROCESS:
            print(VALID_PROCESS)
            valid_process = Process(target=Scheduler.valid_cookie)
            valid_process.start()


if __name__ == '__main__':
    s = Scheduler()
    s.run()