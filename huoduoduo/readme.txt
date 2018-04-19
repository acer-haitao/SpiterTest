selenium
这是一个用于web应用程测试的工具
下载方式
pip install selenium


phantomjs

是一种无界面的浏览器，用于完成网页的渲染，大家可以具体学习，毕竟这个也是门有研究价值的一个技术

下载地址

http://phantomjs.org/download.html

解压就可以用
打卡解压后的文件，找到bin下的phantomjs.exe将这个路径放到PATH路径下

工具准备完成，下面上代码咯

代码实现

from selenium import webdriver
url = "http://www.eshow365.com/zhanhui/html/120062_0.html"
driver = webdriver.PhantomJS(executable_path='E:/phantomjs/bin/phantomjs.exe')//这个路径就是你添加到PATH的路径
driver.get(url)
print (driver.page_source)

运行之后出现如图所示
