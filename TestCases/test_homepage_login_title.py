import pytest

from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
# access all action methods in pageObjects  in our test case
class Test_OO1_Login:  # provide testcase unique id
#   baseURL="https://admin-demo.nopcommerce.com/"
#   username="admin@yourstore.com"
#   password="admin"
# AS per config.ini and readProperties
# for three variables we have to create method
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger= LogGen.loggen() # to log all actions/events   called the class and method
# creating two test methods
#1.Match homepage title test
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login *********************")
        self.logger.info("************** verify homepage title *********************")
        self.driver=setup  ## driver returned through setup will be saved here
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True   # pass my test method
            self.logger.info("************** Homepage title test passed *********************")
            self.driver.close()

        else:                   ## to capture screen shot if test fails
            self.driver.save_screenshot(".//ScreenShots//"+"test_homePageTitle.png")
            self.logger.error("************** Homepage title test failed *********************")
            self.driver.close()
            assert False   # fail my test method


# 2. login page title test
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************** verify Login test *********************")
        self.driver=setup
        self.driver.get(self.baseURL)
# access all action methods in pageObjects  in our test case, we need to create object for pageObject class
# through that object we can access the action methods
        # to access methods in pageObjects class we have to create object for class Login
        # creating object for Login
        self.lp=Login(self.driver)  # pass driver as parameter
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # validation point
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login test passed *********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//ScreenShots//"+"test_login.png")  # name of test method
            self.logger.error("************** Login test failed*********************")
            self.driver.close()
            assert False



#pytest -s -v -m "sanity" --html=./Reports/report.html TestCases/ --browser chrome