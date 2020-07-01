import time
from multiprocessing import Process
# 自定义
from getter import Getter
from server import app
from tester import Tester

API_ENABLED = True
API_HOST = '0.0.0.0'
API_PORT = 5055
API_THREADED = True
GETTER_CYCLE = 20
GETTER_ENABLED = True
TESTER_CYCLE = 20
TESTER_ENABLED = True


class Scheduler(object):
    """docstring for Scheduler"""
    def scheduler_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print("测试器开始运行")
            tester.run()
            time.sleep(cycle)

    def scheduler_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        while True:
            print("开始抓取代理")
            getter.run()
            time.sleep(cycle)

    def scheduler_api(self):
        """
        开启API
        """
        app.run(host=API_HOST, port=API_PORT, threaded=API_THREADED)

    def run(self):
        print("代理池开始运行")
        if TESTER_ENABLED:
            tester_process = Process(target=self.scheduler_tester)
            tester_process.start()
        if GETTER_ENABLED:
            getter_process = Process(target=self.scheduler_getter)
            getter_process.start()
        if API_ENABLED:
            api_process = Process(target=self.scheduler_api)
            api_process.start()


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
