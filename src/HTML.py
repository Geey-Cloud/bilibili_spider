import random


def get_ua(uafile):
    """
    随机获取用户UA
    @param uafile: UA地址
    @return: UA
    """
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[:-1])
    random.shuffle(uas)
    return random.choice(uas)


def get_header(user_mid):
    """
    根据提供的user_mid返回网页的头部
    @param user_mid: 用户id
    @return: 请求头部
    """
    header = {
        'Referer': 'https://space.bilibili.com/' + str(user_mid) + '?from=search&seid=' + str(random.randint(10000, 50000)),
        # 没Cookie 请求不到用户视频、专栏信息
        'Cookie': 'buvid3=438655DA-8273-8C15-1B4D-256E070CA1BE54014infoc; i-wanna-go-back=-1; _uuid=C7C1DEAA-9BCA-2'
                  '648-E582-810BC7EC57E9455418infoc; buvid4=DE0FB238-F9A8-27FE-C8D9-801979590C7F62928-022032214-fpU'
                  'O3AI/PtyNaAFhngFwpQ==; CURRENT_BLACKGAP=0; fingerprint=fbaccd801ff8ee9923fa3168d25ca1ac; buvid_f'
                  'p_plain=undefined; SESSDATA=8965e01a,1663570468,ea3fa*31; bili_jct=09231190afc2929a755a672ad1ba7'
                  '2df; DedeUserID=257257414; DedeUserID__ckMd5=b876868b4576e7c2; sid=lap3pkmw; b_ut=5; buvid_fp=fb'
                  'accd801ff8ee9923fa3168d25ca1ac; fingerprint3=fd9760232aef1488de08a5f8668f2442; bp_video_offset_2'
                  '57257414=641094903479140400; PVID=2; bsource=search_bing; b_lsid=8610BD5610_17FC58DE536; innersi'
                  'gn=1; blackside_state=0; CURRENT_FNVAL=80',
        'User-Agent': get_ua('user_agents.txt')
    }
    # print(header['Referer'], header['User-Agent'])
    return header


# if __name__ == '__main__':
#     get_header(1002)
