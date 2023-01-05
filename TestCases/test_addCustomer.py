# pytest format is , test case name should start with test (test_addCustomer.py)
import string
import random
import time
import pytest
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from selenium.webdriver.common.by import By

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger= LogGen.loggen() # to log all actions/events   called the class and method
    @pytest.mark.sanity
    def test_addCustomer(self,setup):  # from conftest.py u will get browser setup
        self.logger.info("*************** Test_003_AddCustomer *******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Login(self.driver)  # pass driver as parameter   # from LoginPage.py
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ***********************")

        self.logger.info("*************** Starting Add Customer Test *************")
        # using AddCustomer class  from page object
        self.addcust=AddCustomer(self.driver)   # creating object for AddCustomer class to access all methods
        self.addcust.clickoncustomermenu()
        self.addcust.clickcustomeritem()
        self.addcust.clickaddnew()

        self.logger.info("************** Provinding customer info ***************************")
        self.email=random_generator()+"@gmail.com"   # Randomly generating unique email id for each customer
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setGender("Female")
        self.addcust.setfirstname("Reka")
        self.addcust.setlastname("NV")
        self.addcust.setdateofbirth("08/15/1983")

    #   self.addcust.setcompanyname("compNV")
    #   self.addcust.setcustomerroles("Guests")

        self.addcust.setmanagerofvendor("Vendor 2")
        self.addcust.admincontent("This is for testing practice...")
        time.sleep(5)
        self.addcust.clickonsave()
        self.logger.info("*********** saving customer info **************************")
        self.logger.info("************** add customer validation started ************************")
        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        # body means , it will capture everything  displayed on the page in the form of text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True   # make test case pass
            self.logger.info("************* ADD customer test passed **************************")
        else:
            self.driver.save_screenshot((".//ScreenShots//"+"test_addCustomer_scr.png"))
            assert True == False

        self.driver.close()
        self.logger.info("************  Ending Adding customer  test page x**********************")

# own user defined function to generate  and return some random unique email id
def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))    # it just give 8 chars string



# run =              pytest -v -s TestCases/test_addCustomer.py

#pytest -s -v --html=Reports\report.html TestCases/test_addCustomer.py --browser chrome
