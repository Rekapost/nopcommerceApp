from selenium.webdriver.common.by import By

class SearchCustomer:
    txtSearchEmail_xpath="//*[@id='SearchEmail']"
    txtSearchFirstName="//input[@id='SearchFirstName']"
    txtsearchLastName="//input[@id='SearchLastName']"
    btnSearchCustomer="//*[@id='search-customers']"
    tblsearchResults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"



    def __init__(self,driver):
        self.driver=driver
    def searchbyemail(self,email):
        self.driver.find_element(By.XPATH,self.txtSearchEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtSearchEmail_xpath).send_keys(email)
    def searchbyfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.txtSearchFirstName).clear()
        self.driver.find_element(By.XPATH,self.txtSearchFirstName).send_keys(fname)
    def searchbylastname(self,lname):
        self.driver.find_element(By.XPATH,self.txtsearchLastName).clear()
        self.driver.find_element(By.XPATH,self.txtsearchLastName).send_keys(lname)
    def searchcustomer(self):
        self.driver.find_element(By.XPATH,self.btnSearchCustomer).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))
    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))
    def searchCustomerByEamil(self,email):
        flag=False  # initial assign flag=false, once i find  the record ,, i put flag as true
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            # where exactly email is present in result table
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
            return flag

    def searchCustomerByname(self, Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name==Name:
                flag=True
                break
            return flag






