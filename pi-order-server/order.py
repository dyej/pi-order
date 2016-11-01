from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Order:

	def __init__(self, username, password, url):
		self.username = username
		self.password = password
		self.url = url
		self.display = Display(visible=0, size=(1920, 1080))
		self.display.start()
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(15)


	def goToPage(self):
		self.browser.get(self.url)
		print(self.browser.title)
	
	def login(self):
		loginButton = self.browser.find_element_by_css_selector("a#nav-link-yourAccount span.nav-line-1")
		print(loginButton.text)
		if loginButton.text == "Hello. Sign in":
			loginButton.click()
			email = self.browser.find_element_by_id("ap_email")
			pw = self.browser.find_element_by_id("ap_password")
			email.clear()
			pw.clear()
			email.send_keys(self.username)
			pw.send_keys(self.password)
			submit = self.browser.find_element_by_id("signInSubmit")
			submit.click()
		else:
			print("Already logged in.")

		loginButton = self.browser.find_element_by_css_selector("a#nav-link-yourAccount span.nav-line-1")		
		print(loginButton.text)
			
	def placeOrder(self):
		print(self.browser.title)
		print("Placing order.")
		wait = WebDriverWait(self.browser, 10)
		addToCart = self.browser.find_element_by_css_selector("input#add-to-cart-button")
		addToCart.click()
		time.sleep(10)
		print(self.browser.title)
		wait.until(EC.title_contains('Amazon.com Shopping Cart'))
		checkout = self.browser.find_element_by_css_selector("a#hlb-ptc-btn-native")
		checkout.click()
		time.sleep(10)
		print(self.browser.title)
		wait.until(EC.title_contains('Amazon.com Checkout'))
		placeOrder = self.browser.find_element_by_name("placeYourOrder1")
		placeOrder.click()
		time.sleep(20)
		print(self.browser.title)
		wait.until(EC.title_contains('Amazon.com Thanks You'))
				
	def kill(self):
		self.browser.close()
		self.display.stop()

	def start(self):
		try:
                	self.goToPage()
                	self.login()
                	self.placeOrder()
		except Exception:
			print("Exception Raised")
			raise
		finally:
			self.kill()
