# coding=utf-8
__author__ = 'lshxiao'
import requests, json
from lxml import etree
import re


class wechats():
    def search_subscription(self, key, page=1):
        url = 'http://weixin.sogou.com/weixin?query=%s&_sug_type_=&s_from=input&_sug_=n&type=1&page=%d&ie=utf8' % (key, int(page))
        res = requests.get(url)
        tree = etree.HTML(res.content)
        search_item = tree.xpath('//ul[@class="news-list2"]/li')
        counts = wechats().get_article_count(tree)
        gzh = []
        reg = re.compile(r'\d+')   # 提取数字的正则
        for s in search_item:
            wx_key = s.xpath('@d')[0]
            name_em = s.xpath('descendant::p[@class="tit"]/a/em/text()')
            name_em = name_em[0] if name_em else ''
            name_text = s.xpath('descendant::p[@class="tit"]/a/text()')
            name_text = name_text[0] if name_text else ''
            name = name_em+name_text
            link = s.xpath('descendant::div[@class="img-box"]/a/@href')[0]
            logo = s.xpath('descendant::div[@class="img-box"]/a/img/@src')[0]
            wx_id = s.xpath('descendant::p[@class="info"]/label/text()')[0]
            company = s.xpath('descendant::dl[2]/dd/text()')
            company = company[0].strip() if company else ''
            inner_script = s.xpath('descendant::script[not(@src) and not(@type)]')
            time, post_count, post_total = 0, 0, 0
            for index, t in enumerate(inner_script):
                if 'document.write(timeConvert(' in t.text:
                    time = reg.findall(t.text)[0]
            for c in counts:
                if c == wx_key:
                    post_count = counts[c].split(',')[0]
                    post_total = counts[c].split(',')[1]
            gzh.append({'name': name, 'link': link, 'logo': logo, 'wx_id': wx_id, 'wx_key': wx_key, 'company': company, 'time': time*1000, 'post_count': post_count, 'post_total': post_total})

        # 获取结果总条数
        total = tree.xpath('//div[@class="mun"]/text()')
        total = reg.findall(total[0])[0] if total else ''
        pager = {'total': total, 'page': page, 'per_page': 10}
        return gzh, pager

    # 获取评论数
    def get_article_count(self, s):
        script = s.xpath('//script[not(@src) and not(@type)]')
        script_text = script[-2].text
        url_2 = 'http://weixin.sogou.com' + script_text.split('= "')[1]
        try:
            result = requests.get(url_2)
            rs = json.loads(result.content)
        except:
            rs = {}
        return rs.get('msg', {})

