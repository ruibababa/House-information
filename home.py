# @Author  : ShiRui

import requests
import time
from bs4 import BeautifulSoup
import warnings
import pandas as pd


class CrawlData:

	def __init__(self):

		self.url = "https://nj.fang.lianjia.com/loupan/"  # 这是地址
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
			'Referer': 'https://nj.fang.lianjia.com/',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate, br'
		}  # 头信息

	def start_procedure(self):

		warnings.filterwarnings('ignore')  # 用beautifulsoup使避免报错
		price = []  # 空列表
		name = []  # 空列表
		place = [] # 空列表
		for i in range(1, 10):

			url = self.url + 'pg' + str(i)  # 构造url
			html = requests.get(url=url, headers=self.headers)  # 请求响应
			data = html.content.decode()  # 获取页面信息
			time.sleep(0.5)
			bf = BeautifulSoup(data)  # 用beautifulsoup来解析
			soup1 = bf.find_all('div', 'resblock-price')  # 定位信息
			soup2 = bf.find_all('a', 'name')  # 定位信息
			soup3 = bf.find_all('div', 'resblock-location')  # 定位信息
			x = len(soup1)
			y = len(soup2)
			z = len(soup3)
			for m in range(x):

				price.append(soup1[m].span.string)  # 把获取的信息加入到空列表中

			for k in range(y):

				name.append(soup2[k].string)  # 把获取的信息加入到空列表中

			for h in range(z):

				place.append(soup3[h].span.string + soup3[h].a.string)  # 把获取的信息加入到空列表中

		return price, name, place  # 返回值

	def analysis_data(self):

		price, name, place = self.start_procedure()  # 接收返回值
		form = pd.DataFrame([name, place, price], index=['小区名', '地段', '价格'], )  # 用pandas处理信息，构造二维的表格
		print(form.T)  # 转置这个二维表格

if __name__ == "__main__":

	cd = CrawlData()  # 实例化对象
	cd.analysis_data()  # 调用函数
