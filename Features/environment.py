from selenium.webdriver import Chrome


def before_all(context):
    path = "C:\\Users\\Viral Parmar\\AppData\\Local\\Programs\\Python\\Python38-32\\chromedriver_win32\\chromedriver.exe"
    context.driver = Chrome()

def after_all(context):
    context.driver.close()