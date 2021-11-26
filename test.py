from selenium import webdriver
from time import sleep
broexe='E:\Pycharm\PyCharm Community Edition 2021.1.1\jbr\Projects\edge驱动器\msedgedriver.exe'
bro=webdriver.Edge(executable_path=broexe)
url='http://zhjwxk.cic.tsinghua.edu.cn/xklogin.do'
bro.get(url)
interface=bro.window_handles
if(input('输入回车以继续')):  #这里要输入账号密码等，进入后切换到一级课开课信息中；过程中无需关闭窗口
    print('进入课程页面!')
    print('')
sleep(1)
handles=bro.window_handles
for handle in handles:
    if handle!=interface:
        courses_face=handle
bro.switch_to.window(courses_face) 
for _ in range(1,273):
    try:
        with open('THU_Courses.txt','a+',encoding='utf-8') as fp:
            for i in range(2,22):
                course_name=bro.find_element_by_xpath('//*[@id="table_sy"]/table/tbody/tr[{}]/td[4]/a/span'.format(i)).text
                teacher_name=bro.find_element_by_xpath('//*[@id="table_sy"]/table/tbody/tr[{}]/td[6]/div/a/span'.format(i)).text
                fp.write(course_name+'  '+teacher_name+'\n')
    except:
        print('第{}页保存失败！'.format(_))
    else:
        print('第{}页保存成功！'.format(_))
    next_page=bro.find_element_by_xpath('//*[@id="nextpage"]')
    next_page.click()
    sleep(1.5)