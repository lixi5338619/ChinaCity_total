import re
import requests
import time

save_route = './2018chengzhen.txt'
results2 = []
results3 = []
results4 = []
results5 = []
Dates1 = []
kv = {'user-agent': 'Mozilla/5.0'}
n = 0
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html'
r = requests.get(url, headers=kv)
r.raise_for_status()
r.encoding = r.apparent_encoding
pattern = re.compile("<a href='(.*?)'>(.*?)<")  # 正则表达式
result1 = list(set(re.findall(pattern, r.text)))  # 从主页面获取子页面的html
# print('result1')
# print(result1)
i2 = 0
for i2 in range(len(result1)):
    try:
        url2a = result1[i2][0]
        address1 = result1[i2][1]  # 一级地址
        i2 += 1
        url2 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/' + url2a
        # http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/44.html
        # print(url2)
        # print(address1)
        r2 = requests.get(url2, headers=kv)
        r2.raise_for_status()
        r2.encoding = r2.apparent_encoding
        pattern2 = re.compile("<a href='(.*?)'>(.*?)<")  # 正则表达式提取目标字段
        result2 = list(set(re.findall(pattern2, r2.text)))
        # print(result2)
        result2a = []
        for i2a in result2:  # 爬取的城市信息和城市代码混在一起，需要将代码清除
            if '0' in i2a[1]:
                n += 1
            else:
                result2a.append(i2a)
        # print('result2a')
        # print(result2a)
    except:
        print('错误')
        with open(save_route, 'a', encoding='utf-8')as f:
            f.write('一级错误 一级错误 一级错误 一级错误')
            f.write('\n')
            f.close()
        time.sleep(10)
        continue
    i3 = 0
    for i3 in range(len(result2a)):
        try:
            url3a = result2a[i3][0]
            address2 = result2a[i3][1]  # 二级地址
            i3 += 1
            url3 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/' + url3a
            # http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/34/3401.html
            r3 = requests.get(url3, headers=kv)
            r3.raise_for_status()
            r3.encoding = r3.apparent_encoding
            pattern3 = re.compile("<a href='(.*?)'>(.*?)<")
            result3 = list(set(re.findall(pattern3, r3.text)))
            # print(result3)
            result3a = []
            for i3a in result3:
                if '0' in i3a[1]:
                    n += 1
                else:
                    result3a.append(i3a)
            # print('result3a')
        except:
            # print('错误')
            with open(save_route, 'a', encoding='utf-8')as f:
                f.write('二级错误 二级错误 二级错误 二级错误')
                f.write('\n')
                f.close()
            time.sleep(10)
            continue
        # print(result3a)
        i4 = 0
        for i4 in range(len(result3a)):
            try:
                url4a = result3a[i4][0]
                address3 = result3a[i4][1]  # 二级地址
                i4 += 1
                url4 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/' + url4a[3:5] + '/' + url4a
                # print(url4)
                # http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/41/04/410481.html
                r4 = requests.get(url4, headers=kv)
                r4.raise_for_status()
                r4.encoding = r4.apparent_encoding
                pattern4 = re.compile("<a href='(.*?)'>(.*?)<")
                result4 = list(set(re.findall(pattern3, r4.text)))
                # print(result4)
                result4a = []
                for i4a in result4:
                    if '0' in i4a[1]:
                        n += 1
                    else:
                        result4a.append(i4a)
                # print('result4a')
            except:
                # print('错误')
                with open(save_route, 'a', encoding='utf-8')as f:
                    f.write('三级错误 三级错误 三级错误 三级错误')
                    f.write('\n')
                    f.close()
                time.sleep(10)
                continue
            # print(result4a)
            results5 = []
            i5 = 0
            for i5 in range(len(result4a)):
                try:
                    address4 = result4a[i5][1]
                    i5 += 1
                    address = str(address1) + ' ' + str(address2) + ' ' + str(address3) + ' ' + str(address4)
                    print(address)
                    with open(save_route, 'a', encoding='utf-8')as f:
                        f.write(address)
                        f.write('\n')
                        f.close()
                except:
                    # print('错误')
                    with open(save_route, 'a', encoding='utf-8')as f:
                        f.write('四级错误 四级错误 四级错误 四级错误')
                        f.write('\n')
                        f.close()
                    time.sleep(10)
                    continue
print('well_done')
