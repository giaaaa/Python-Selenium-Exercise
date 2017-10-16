# 百度新歌榜
# 找出前50首歌里，排名上升的歌名和对应的歌手名


from selenium import webdriver

from xixi.settings import executable_path
# executable_path is the chromedriver's path

from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)

driver.get("http://music.baidu.com/top/new")

lilist = driver.find_elements_by_css_selector('#songListWrapper ul li')


for one in lilist:
    try:
        up = one.find_element_by_css_selector('i[class="up"]') # 排名上升的
        span = one.find_element_by_class_name('song-title ')
        song_title = span.find_element_by_tag_name('a').text # 获取歌名
        span = one.find_element_by_class_name('author_list')
        author_list = span.find_element_by_tag_name('a').text # 获取歌手名
        print(song_title,author_list)
    except NoSuchElementException:
        pass



driver.quit()


