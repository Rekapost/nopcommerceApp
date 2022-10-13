# create locators for all elements
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    lnkcustomers_main_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkcustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnaddnew_customer_xpath="//a[normalize-space()='Add new']"
    txtcustomer_email_xpath="//input[@id='Email']"
    txtcustomer_password_xpath="//input[@id='Password']"
    txtcustomer_firstname_xpath="//input[@id='FirstName']"
    txtcustomer_lastname_xpath="//input[@id='LastName']"
    rdmalecustomer_gender_xpath="//input[@id='Gender_Male']"
    rdfemalecustomer_gender_xpath="//input[@id='Gender_Female']"
    txtcustomer_dateofbirth_xpath="//input[@id='DateOfBirth']"
    txtcustomer_companyname="//input[@id='Company']"
    btncustomer_taxexmpt_xpath="//input[@id='IsTaxExempt']"
    btncustomer_newsletter_xpath="//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover']//input[@role='listbox']"

   # txtcustomer_role_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    txtcustomer_role_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemcustroleradmin_xpath="//span[normalize-space()='Administrators']"
    lstitemcustroleguest_xpath="//span[normalize-space()='Guests']"
    lstitemcustroleregi_xpath="//span[normalize-space()='Registered']"
    lstitemcustrolevend_xpath="//span[normalize-space()='Vendors']"

    drpcustomer_managerofvendor_xpath="//select[@id='VendorId']"
    btncustomer_active_xpath="//input[@id='Active']"
    txtcustomer_admincontent_xpath="//textarea[@id='AdminComment']"
    btncustomer_save_xpath="//button[@name='save']"

# create one constructor, this constructor will get the driver from actual testcase
# to intiatte local driver self.driver=driver
    def __init__(self,driver):
        self.driver=driver
# for every element write action method
    def clickoncustomermenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_main_xpath).click()
    def clickcustomeritem(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_menuitem_xpath).click()
    def clickaddnew(self):
        self.driver.find_element(By.XPATH,self.btnaddnew_customer_xpath).click()
    def setemail(self,email):   # we will get email from actual test case
        self.driver.find_element(By.XPATH,self.txtcustomer_email_xpath).send_keys(email)
    def setpassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txtcustomer_password_xpath).send_keys(pwd)
    def setfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.txtcustomer_firstname_xpath).send_keys(fname)
    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.txtcustomer_lastname_xpath).send_keys(lname)
    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rdmalecustomer_gender_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.rdfemalecustomer_gender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rdmalecustomer_gender_xpath).click()
    def setdateofbirth(self,dob):
        self.driver.find_element(By.XPATH,self.txtcustomer_dateofbirth_xpath).send_keys(dob)
    def setcompanyname(self,cmpname):
        self.driver.find_element(By.XPATH,self.txtcustomer_companyname).send_keys(cmpname)
 #  def taxexmpt(self):
 #      self.driver.find_element(By.XPATH,self.btncustomer_taxexmpt_xpath).click()
 #  def newsletter(self):
 #      self.driver.find_element(By.XPATH,self.btncustomer_newsletter_xpath).click()
    def setcustomerroles(self,role):
        self.driver.find_element(By.XPATH,self.setcustomerroles).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemcustroleregi_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemcustroleradmin_xpath)
        elif role=='Guests':  # here user can be registered user (has account) or guest(no account), only one
            time.sleep(3)  # already registered will be there , if selecting guest ,
            # u have to remove registered by clicking again on registered
            self.driver.find_element(By.XPATH,self.lstitemcustroleregi_xpath).click()
            # then click guests and guests will be saved i the variable listitem
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemcustroleguest_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemcustroleregi_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemcustrolevend_xpath)
        else:   # if nothing is selected , by default guests is selected
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemcustroleguest_xpath)
        time.sleep(3)
        # select one of the item from textbox
        # self.listitem.click() is not working so execute script method
        self.driver.execute_script("arguments[0].click();",self.listitem) # 2 argumenets java script
    def setmanagerofvendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpcustomer_managerofvendor_xpath))
        drp.select_by_visible_text(value)
    def admincontent(self,content):
        self.driver.find_element(By.XPATH,self.txtcustomer_admincontent_xpath).send_keys(content)
    def clickonsave(self):
        self.driver.find_element(By.XPATH,self.btncustomer_save_xpath).click()
