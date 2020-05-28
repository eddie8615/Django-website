from selenium import webdriver

browser = webdriver.Chrome('/Users/USER/Desktop/chromedriver')
browser.get('http://localhost:8000')

assert 'Title' in browser.title