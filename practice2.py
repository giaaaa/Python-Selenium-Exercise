# 1.进入智联招聘官网；
# 2.输入Python；
# 3.选择地区：上海；
# 4.获取第一页的所有信息。

from selenium import webdriver

from xixi.settings import executable_path
# executable_path is the chromedriver's path

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)

driver.get("http://www.51job.com")

input = driver.find_element_by_id('kwdselectid') # 找到输入框
input.click()
input.send_keys('python') # 输入Python
driver.find_element_by_id('work_position_input').click() # 点击地区选择
div = driver.find_element_by_id('work_position_click_multiple') # 找到已选地区列表
spans = div.find_elements_by_css_selector('#work_position_click_multiple_selected > span') # 只有当已选列表里有元素才会有的元素列表

if spans != []:
    for one in spans:# 遍历整个列表
        one.find_element_by_tag_name('em').click()    # 取消已选中的每一个地区
else:
    pass

driver.find_element_by_id('work_position_click_center_right_list_category_000000_020000').click()  # 选择上海
driver.find_element_by_id('work_position_click_bottom_save').click()  # 点击确定
driver.find_element_by_css_selector('div[class="ush top_wrap"] div ~ button').click()   # 点击搜索

jobs = driver.find_elements_by_css_selector('#resultList > div[class="el"]')
for job in jobs:
    spans = job.find_elements_by_tag_name('span')
    data = [one.text for one in spans]
    print(' | '.join(data))


driver.quit()