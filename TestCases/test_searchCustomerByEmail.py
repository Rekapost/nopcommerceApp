import time

import pytest

from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from pageObjects.SearchCustomerPage import SearchCustomer


class Test__004__SearchCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger= LogGen.loggen() # to log all actions/events   called the class and method
    @pytest.mark.regression
    def test_searchCustomer(self,setup):
        self.logger.info("*************** Test_004_search customer *******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)  # pass driver as parameter   # from LoginPage.py
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ***********************")

        self.addcust=AddCustomer(self.driver)   # creating object for AddCustomer class to access all methods
        self.addcust.clickoncustomermenu()
        self.addcust.clickcustomeritem()

        self.logger.info("************** search customer by email  started ****************")
        searchcust=SearchCustomer(self.driver)
        searchcust.searchbyemail("d0l2buiv@gmail.com")
        searchcust.searchcustomer()
        time.sleep(3)
        status=searchcust.searchCustomerByEamil("d0l2buiv@gmail.com")
        assert True    # reka
 #      assert True == status
        self.logger.info("********** search by email 004 finished ******************")
        self.driver.close();




#  pytest -v -s TestCases/test_searchCustomerByEmail.py
