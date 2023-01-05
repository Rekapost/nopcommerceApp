import time
import pytest
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtilityFile
# access all action methods in pageObjects  in our test case
class Test_OO2_DDT_Login:  # provide testcase unique id
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData//logindataExcel.xlsx"
    logger= LogGen.loggen() # to log all actions/events   called the class and method
# 1. login page title test
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("************** verify Test_OO2_DDT_Login test *********************")
        self.logger.info("************** verify Login DDT test *********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.rows=ExcelUtilityFile.getRowCount(self.path,'Sheet1')
        print("no of rows:",self.rows)
        list_status=[]   # empty list variable
        for r in range(2,self.rows+1):
            self.user=ExcelUtilityFile.readData(self.path,'Sheet1',r,1)
            self.password=ExcelUtilityFile.readData(self.path,'Sheet1',r ,2)
            self.exp=ExcelUtilityFile.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='pass':
                    self.logger.info("*** passed *****")
                    self.lp.clickLogout();
                    list_status.append("pass")
                elif self.exp=='fail':
                    self.logger.info("*** failed *****")
                    self.lp.clickLogout();
                    list_status.append("fail")
            elif act_title!=exp_title:
                if self.exp=='pass':
                    self.logger.info("*** failed *****")
                    list_status.append("fail")
                elif self.exp=='fail':
                    self.logger.info("*** passed *****")
                    list_status.append("pass")
        if "fail" not in list_status:
            self.logger.info("**********Login DDT Test Passed ****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***********Login DDT Test Failed **********************")
            self.driver.close()
            assert False
        self.logger.info("***************End of Login DDT Test*********************")
        self.logger.info("************** Completed  TC_LoginDDT_002 ********************************");









