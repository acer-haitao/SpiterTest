# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 9:58
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : hddjs.py
# @Software: PyCharm
import json
import re
import sys

import requests

reload(sys)
sys.setdefaultencoding('utf8')
# urls ='https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":1,"maxTime":1521527233776}&&callback=jsonp_1521527268124_06608889123755557&wfr_public={"referService":"h5-shop"}'

urls = [
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":1,"maxTime":1521529718004}&&callback=jsonp_1521529741928_6854484881330787&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":2,"maxTime":1521529718004}&&callback=jsonp_1521529751670_5832557342369098&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":3,"maxTime":1521529718004}&&callback=jsonp_1521529763062_06346274727606949&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":4,"maxTime":1521529718004}&&callback=jsonp_1521529766758_6295723382208891&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":5,"maxTime":1521529718004}&&callback=jsonp_1521529771054_9261887049185157&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":6,"maxTime":1521529718004}&&callback=jsonp_1521529774538_599321625025759&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":7,"maxTime":1521529718004}&&callback=jsonp_1521529779608_6577915763977724&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":8,"maxTime":1521529718004}&&callback=jsonp_1521529783502_13465981420119888&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":9,"maxTime":1521529718004}&&callback=jsonp_1521529789030_04509012456530159&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":10,"maxTime":1521529718004}&&callback=jsonp_1521529792118_8145228653993342&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":11,"maxTime":1521529718004}&&callback=jsonp_1521529796954_14992032214391238&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":12,"maxTime":1521529718004}&&callback=jsonp_1521529801812_3460541129471394&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":13,"maxTime":1521529718004}&&callback=jsonp_1521529854850_2596760435457496&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":14,"maxTime":1521529718004}&&callback=jsonp_1521529857732_5810086438221344&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":15,"maxTime":1521529718004}&&callback=jsonp_1521529860316_8470432745552494&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":16,"maxTime":1521529718004}&&callback=jsonp_1521529862848_01768099588278904&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":17,"maxTime":1521529718004}&&callback=jsonp_1521529868314_15943708128321743&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":18,"maxTime":1521529718004}&&callback=jsonp_1521529870582_9610320156597821&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":19,"maxTime":1521529718004}&&callback=jsonp_1521529873174_735511035228499&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":20,"maxTime":1521529718004}&&callback=jsonp_1521529875900_4471160665230617&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":21,"maxTime":1521529718004}&&callback=jsonp_1521529878322_9620673785246928&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":22,"maxTime":1521529718004}&&callback=jsonp_1521529881528_868049659394435&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":23,"maxTime":1521529718004}&&callback=jsonp_1521529884112_644561454781893&wfr_public={"referService":"h5-shop"}',
    'https://gwh5.api.weidian.com/wd/shop/decorate/getShopItems?param={"shopId":"845925946","showType":1,"sort":1,"pageSize":20,"pageNum":24,"maxTime":1521529718004}&&callback=jsonp_1521529886542_2367895313765641&wfr_public={"referService":"h5-shop"}',
]

headers = {
    'Accept': '* / *',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Cookie': 'vc_fpcookie=30c0ea6a-8350-1896-0dd2-55c9cd9bb771; _pk_id.1.9a21=af3f165533295d37.1499053652.1.1499053652.1499053652.; __spider__visitorid=af3f165533295d37; visitor_id=0b3779b0-d0a5-443d-94a1-6da2e8022795; is_follow_mp=1; WD_seller=845925946; vc_token_id=KDH5-16241163674-6b248ba9-9d55-0eeb-bd7a-5e4afcf59b70-afdc; __spider__sessionid=3d828b7953fcb95c',
    'Host': 'gwh5.api.weidian.com',
    'Referer': 'https://weidian.com/index.html?userid=845925946',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
i = 0


def get_json():
    global i
    for url in urls:
        data = requests.get(url, headers=headers)
        data.encoding = 'utf-8'
        result = re.findall(r'\((.*?)\);', data.text)[0]
        value = json.loads(result)
        # print(value)
        list = value.get('result').get('items')
        for data in list:
            img = data['img']  # 图片地址
            h5url = data['h5url']  # 跳转链接
            itemComment = data['itemComment']  #
            itemName = data['itemName']
            price = data['price']  # 价格
            sold = data['sold']
            i = i + 1
            print("{},{},{}".format(i, h5url, itemName))


if __name__ == '__main__':
    get_json()
