# find elements need to add in page object class ,( email, pwd and login)
# capture locators
from selenium.webdriver.common.by import By


class Login:
# identify all locators  of login page
#   textbox_username_id="Email"           #  locators
    textbox_username_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    button_login_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="Logout"
# implemenet action method for every locator
# so initialize driver
    def __init__(self,driver):# python constructor to initialize constructor, driver will come from actual test case
        self.driver=driver # intiate local driver, class variable, use self.driver to write all action methods on this elements

    def setUserName(self,username):       # parameter to pass from actual testcase,
#        self.driver.find_element_by_id(self.textbox_username_id).clear()
         self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
         self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):  # parameter to pass from actual testcase,
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()