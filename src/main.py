from concurrent.futures import ThreadPoolExecutor
import spiderUser
import mysql


if __name__ == '__main__':
    mysql.clear()
    pool = ThreadPoolExecutor(max_workers=6)
    id_start = 1000
    id_end = 1600
    user_mid = []
    for i in range(id_start, id_end):
        user_mid.append(i)
    try:
        future_user = pool.map(spiderUser.save_data, user_mid)
        mysql.show()
    except Exception as e:
        print(e)
    pool.shutdown()
