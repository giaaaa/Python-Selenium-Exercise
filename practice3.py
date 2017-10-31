# 1.打开12306网站 https://kyfw.12306.cn/otn/leftTicket/init ；
# 2.出发城市 填写"南京南"；
# 3.到达城市 填写"杭州东"；
# 4.发车时间 选6:00--12:00;
# 5.发车日期选当前时间的下一天，也就是日期标签栏的第二个标签；
# 6.需要查找的是所有 二等座还有票的车次，打印出所有这些有票的车次的信息。

from selenium import webdriver

from selenium.webdriver.common.keys import Keys  # 引入keys包

from selenium.webdriver.support.ui import Select

from xixi.settings import executable_path
# executable_path is the chromedriver's path

from time import sleep

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)

driver.get("https://kyfw.12306.cn/otn/leftTicket/init")

fromStat = driver.find_element_by_id('fromStationText')
fromStat.click()   # 点击出发地输入框
fromStat.send_keys('njn')  # 输入南京南的首拼
fromStat.send_keys(Keys.ENTER)  # 按下回车键

toStat = driver.find_element_by_id('toStationText')
toStat.click()
toStat.send_keys('hzd')
toStat.send_keys(Keys.ENTER)

driver.find_element_by_id('query_ticket').click()  # 点击查询
sleep(2)

# 方法一：
# select = driver.find_element_by_id('cc_start_time')
# select.click()  # 点击选择发车时间
# select.find_element_by_css_selector('option[value="06001200"]').click() # 选择6:00-12:00

# 方法二：
select = Select(driver.find_element_by_id('cc_start_time'))
select.select_by_visible_text('06:00--12:00')   # 根据可见的内容选择

driver.find_element_by_css_selector('#date_range > ul > li:nth-child(2)').click()   # 选择当前时间的下一天


xpath = driver.find_elements_by_xpath('//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a')  # 只有有票的元素有class属性，从有票的元素的父元素找到车次信息

for one in xpath:
    print(one.text)




driver.quit()