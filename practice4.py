# 登录 http://www.51job.com
# 点击高级搜索
# 输入搜索关键词 Python
# 地区选择 上海
# 职能类别 选 计算机软件 -> 高级软件工程师
# 公司性质选 外资 欧美
# 工作年限选1-3年
# 搜索最新发布的职位，抓取页面信息。

from selenium import webdriver

from xixi.settings import executable_path
# executable_path is the chromedriver's path

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)

driver.get("http://www.51job.com")

driver.find_element_by_css_selector('div[class="fltr radius_5"] div > a').click() # 点击高级搜索
driver.find_element_by_id('work_position_click').click()   # 点击地区选择
div = driver.find_element_by_id('work_position_click_multiple') # 找到已选地区列表
spans = div.find_elements_by_css_selector('#work_position_click_multiple_selected > span') # 只有当已选列表里有元素才会有的元素列表

if spans != []:
    for one in spans: # 遍历整个列表
        one.find_element_by_tag_name('em').click()    # 取消已选中的每一个地区
else:
    pass

driver.find_element_by_id('work_position_click_center_right_list_category_000000_020000').click()  # 选择上海
driver.find_element_by_id('work_position_click_bottom_save').click()  # 点击确定

driver.find_element_by_id('funtype_click').click()  # 点击职能选择
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()  # 点击计算机软件
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()  # 点击高级软件工程师
driver.find_element_by_id('funtype_click_bottom_save').click()   # 点击确定

cotType = driver.find_element_by_id('cottype_list')
cotType.click()
cotType.find_element_by_css_selector('div > span:nth-child(2)').click()  # 选择公司性质


workYear = driver.find_element_by_id('workyear_list')
workYear.click()
workYear.find_element_by_css_selector('div > span:nth-child(3)').click()   # 选择工作年限


driver.find_element_by_css_selector('span[class="p_but"]').click()  # 点击搜索

jobs = driver.find_elements_by_css_selector('#resultList > div[class="el"]') # 第一页的列表

for job in jobs:
    spans = job.find_elements_by_tag_name('span')  # 每个工作的职位名、公司名、工作地点、薪资和发布时间
    data = [one.text for one in spans]
    print(' | '.join(data))




driver.quit()