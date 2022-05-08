import random
import requests
import time
from HTML import get_header
import mysql


def get_user_info(user_mid, url):
    """
    获得用户的信息
    @param url:
    @param user_mid: 用户id
    @return:
    """
    header = get_header(user_mid)
    # url = 'https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp' % user_mid
    try:
        data = requests.get(url=url, headers=header)
        if data.status_code == 200:
            # print("成功")
            return data.json()['data']
        # print(data['data'])
        else:
            return
    except Exception as e:
        print("请求失败")


# if __name__ == '__main__':
#     urls = ['https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp' % 2000,
#             'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % 2000,
#             'https://api.bilibili.com/x/space/upstat?mid=%s&jsonp=jsonp' % 2000]
#     for url in urls:
#         get_user_info(2000, url)


# def get_user_fans(user_mid, url):
#     """
#     获得用户的粉丝数据
#     @param url:
#     @param user_mid: 用户id
#     """
#     header = get_header(user_mid)
#     # url = 'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % user_mid
#     data = requests.get(url=url, headers=header).json()
#     print(data['data'])  # {'mid': 257257414, 'following': 185, 'whisper': 0, 'black': 4, 'follower': 3}
#     time.sleep(0.5)
#
#
# def get_user_video(user_mid, url):
#     """
#     获取用户的专栏、视频信息
#     @param url:
#     @param user_mid: 用户id
#     """
#     header = get_header(user_mid)
#     # url = 'https://api.bilibili.com/x/space/upstat?mid=%s&jsonp=jsonp' % user_mid
#     data = requests.get(url=url, headers=header).json()
#     print(data['data'])  # {'archive': {'view': 0}, 'article': {'view': 0}, 'likes': 16}
#     time.sleep(0.5)

def spider_user(user_mid):
    """
    获取用户信息
    @param user_mid: B站用户id
    @return: 用户信息
    """
    urls = ['https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp' % user_mid,
            'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % user_mid,
            'https://api.bilibili.com/x/space/upstat?mid=%s&jsonp=jsonp' % user_mid]
    # print(urls)
    # for url in urls.values():
    #     get_user_info(user_mid, url)
    #     get_user_fans(user_mid, url)
    #     get_user_video(user_mid, url)
    user_info = {}
    for url in urls:
        data = get_user_info(user_mid, url)
        user_info.update(data)  # 把一个人的信息整合在一个dict里
        # print(user_info)
    return user_info


def save_data(user_mid):
    user_info = spider_user(user_mid)
    # print(user_info)
    new_user_info = (user_info['mid'], user_info['name'], user_info['sex'],
                     user_info['level'], user_info['follower'], user_info['vip']['label']['text'])
    # {'mid': 1, 'name': 'bishi', 'sex': '保密',
    #  'face': 'http://i1.hdslb.com/bfs/face/34c5b30a990c7ce4a809626d8153fa7895ec7b63.gif', 'level': 4,
    #  'follower': 167947}
    print(new_user_info)
    sql = 'insert into user_info values(%s,%s,%s,%s,%s,%s)'
    mysql.execute_sql(sql, new_user_info)
    time.sleep(random.randint(3, 19) / 10)

# if __name__ == '__main__':
#     user_info = spider_user(257257414)
#     print(user_info['vip']['label']['text'])
#     # {'mid': 257257414, 'name': 'The丶雲', 'sex': '男',
#     #  'face': 'http://i1.hdslb.com/bfs/face/8515eda55a2477f43297e9c7074cfd4055fd2741.jpg', 'face_nft': 0, 'sign': '',
#     #  'rank': 10000, 'level': 6, 'jointime': 0, 'moral': 0, 'silence': 0, 'coins': 12, 'fans_badge': False,
#     #  'fans_medal': {'show': True, 'wear': True,
#     #                 'medal': {'uid': 257257414, 'target_id': 63231, 'medal_id': 2226, 'level': 1, 'medal_name': '泛团',
#     #                           'medal_color': 6067854, 'intimacy': 134, 'next_intimacy': 201, 'day_limit': 1500,
#     #                           'medal_color_start': 6067854, 'medal_color_end': 6067854, 'medal_color_border': 6067854,
#     #                           'is_lighted': 1, 'light_status': 1, 'wearing_status': 1, 'score': 134}},
#     #  'official': {'role': 0, 'title': '', 'desc': '', 'type': -1},
#     #  'vip': {'type': 2, 'status': 1, 'due_date': 1653840000000, 'vip_pay_type': 0, 'theme_type': 0,
#     #          'label': {'path': '', 'text': '年度大会员', 'label_theme': 'annual_vip', 'text_color': '#FFFFFF', 'bg_style': 1,
#     #                    'bg_color': '#FB7299', 'border_color': ''}, 'avatar_subscript': 1, 'nickname_color': '#FB7299',
#     #          'role': 3, 'avatar_subscript_url': 'http://i0.hdslb.com/bfs/vip/icon_Certification_big_member_22_3x.png'},
#     #  'pendant': {'pid': 451, 'name': '汉化日记',
#     #              'image': 'http://i1.hdslb.com/bfs/face/0f1f8ec045abd1fc572f537a6652207bcbf70a40.png', 'expire': 0,
#     #              'image_enhance': 'http://i1.hdslb.com/bfs/face/0f1f8ec045abd1fc572f537a6652207bcbf70a40.png',
#     #              'image_enhance_frame': ''}, 'nameplate': {'nid': 57, 'name': '收集萌新',
#     #                                                        'image': 'http://i2.hdslb.com/bfs/face/7767275600ea63d351b22fa87ec15a79aa24e5e5.png',
#     #                                                        'image_small': 'http://i0.hdslb.com/bfs/face/6589d992655595bf51543f268040eaeaed372fae.png',
#     #                                                        'level': '普通勋章', 'condition': '同时拥有粉丝勋章>=5个'},
#     #  'user_honour_info': {'mid': 0, 'colour': None, 'tags': []}, 'is_followed': False,
#     #  'top_photo': 'http://i1.hdslb.com/bfs/space/cb1c3ef50e22b6096fde67febe863494caefebad.png', 'theme': {},
#     #  'sys_notice': {}, 'live_room': None, 'birthday': '07-14', 'school': {'name': ''},
#     #  'profession': {'name': '', 'department': '', 'title': '', 'is_show': 0}, 'tags': None,
#     #  'series': {'user_upgrade_status': 3, 'show_upgrade_window': False}, 'is_senior_member': 1, 'following': 185,
#     #  'whisper': 0, 'black': 4, 'follower': 3, 'archive': {'view': 0}, 'article': {'view': 0}, 'likes': 16}
