import json
import time
import datetime
import requests
from client import HeyBoxClient


def send_result(content, skey):
    url = 'https://sc.ftqq.com/%s.send' % skey
    data = {
        'text': '小黑盒脚本',
        'desp': content
    }
    resp = requests.get(url, data)
    print('执行结束', resp.status_code, resp.json())


def load_settings():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def daily_task():
    settings = load_settings()
    heybox = HeyBoxClient(settings['account'])

    heybox.auto()  # 自动完成每日任务，自动动态点赞
    detail = heybox.get_task_detail()  # 获取任务详情
    my_data = heybox.get_my_data()

    result = ', '.join((detail, my_data))
    send_result(result, settings['ftqqskey'])


if __name__ == '__main__':
    daily_task()
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 30:
            daily_task()
        else:
            print(now)
            time.sleep(60)
