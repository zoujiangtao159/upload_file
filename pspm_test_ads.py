import json

import pickle
import requests
import time


def pmpm_video_cam_config():
    url = 'http://report.ads.newborntown.com/go_test/1'
    cookies = {"sessionid":"y8pw2h13dzcwqi1c6bdtftyyoengvijq"}
    print(cookies)
    s = requests.session()
    req = s.get(url,cookies = cookies)
    req_result =json.loads(req.content)

    timestamp = [time.time()]  # unix时间戳
    print(timestamp[0],len(timestamp))


pmpm_video_cam_config()