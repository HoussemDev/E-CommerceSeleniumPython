import pytest
from selenium import webdriver

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getAppURL()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):

        self.logger.info("**************Test_001_Login**********")
        self.logger.info("**************Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("screenShots/" + "test_homePageTitle2.png")
            self.driver.save_screenshot("test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(self.useremail)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("screenShots/" + "test_login.png")
            self.driver.close()
            assert False
