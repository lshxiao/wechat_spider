
# 一、使用方法
```python
# 1、安装
pip install wechat_spider

# 2、引用
from wechat_spider import *
wx = wechats()

# 3、调用
wechat_infos, pager = wx.search_subscription(keywords, p)

```
# 二、返回参数说明
> wechat_infos
```python
name: 公众号名称, 
link: 公众号详情页链接, 
logo: 公众号logo, 
wx_id: 微信ID, 
wx_key: 公众号key, 获取评论数时会用到, 
company: 认证公司, 没有时返回空, 
time: 最近发文时间/毫秒, 
post_count: 月发文数, 
post_total: 总发文数
```
> pager
```python
total: 总条数(当总页数大于10页时,搜狗就没办法再翻页了,用的时候要注意),
page: 当前页,
per_page: 10, 固定值

```

pypi下载地址: https://pypi.python.org/pypi/wechatSpider

> 如果使用过程有问题, 请联系我
> author: lshxiao
> wechat: mianhuabingbei
> blog: http://web.pxuexiao.com