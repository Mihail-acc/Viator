# Two browsers test for Google and Wikipedia with Waiting functional
import time
from turtle import delay

from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
import HtmlTestRunner

driver = webdriver.Chrome()


class ChromeViator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_TC03(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds

    def test_TC04(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds

    def test_TC05(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds

    def test_TC06(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds

    def test_TC07(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds

    def test_TC08(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds

    def test_TC09(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds

    def test_TC10(self):
        driver = self.driver
        driver.get(
            "https://www.viator.com/tours/Paris/Seine-River-Cruise-Bateaux-Parisiens-Sightseeing-Cruise-with-Dinner-and-Live-Music/d479-5836DINNERCRUISE")
        driver.find_element(By.XPATH, "//button[@id='_evidon-accept-button']").click()
        driver.find_element(By.XPATH, "//span[contains(.,'Check Availability')]").click()
        driver.find_element(By.XPATH, "//div[@class='priceDate__1tt3'][contains(.,'20')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Apply')]").click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "//button[@data-automation='tour-grade-buy-now-button']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[8]").send_keys("Mihail")

        driver.find_element(By.XPATH, "(//input[contains(@data-parsley-pattern,'')])[9]").send_keys("Suruceanu")
        driver.find_element(By.XPATH, "(//select[@data-parsley-required='true'])[1]").send_keys("E")
        driver.execute_script("window.scrollBy(0,1000)", "")
        # Insert CardHolder Name
        driver.find_element(By.XPATH, "//input[@data-parsley-minlength='3']").send_keys("Suruceanu Mihail")
        # Insert Credit Card Number
        # driver.find_element(By.XPATH, "(//input[@id='paymentInfoFullName']").send_keys("56764756475647564")
        # Select ExpiryMonth
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateMonth')]").send_keys("10")
        # Select ExpiryYear
        # driver.find_element(By.XPATH, "//select[contains(@id,'expiryDateYear')]").send_keys("2023")
        # Insert Cvv Code
        # driver.find_element(By.XPATH, "//input[contains(@id,'securityCode')]").send_keys("000")

        # Insert Email address
        # driver.find_element(By.XPATH, "(//input[@type='email']").send_keys("email@gmail.com")
        # Insert Phone number
        driver.find_element(By.XPATH, "(//input[contains(@type,'tel')])[1]").send_keys("677857465")

        # Click Book Now
        # driver.find_element(By.XPATH, "(//button[contains(@id,'bookNow')]").click()

        # Check that payment is not processing
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Secure Checkout')]")))
            not_found = False
        except:
            not_found = True

        assert not_found
        # In this case we'll get AssertionError if element appeared in DOM within 10 seconds


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/suruc/PycharmProjects/test21/Html Reports'))
