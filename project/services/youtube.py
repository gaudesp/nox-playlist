from urllib.parse import urlparse, parse_qs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_video(link):
  url_data = urlparse(link)
  query = parse_qs(url_data.query)

  if ".com" in link:
    video = query["v"][0]
  else:
    video = link.rsplit('/', 1)[-1]
  return video

def get_title(link):
  option = webdriver.ChromeOptions()
  option.add_argument("--incognito")
  option.add_argument("--no-sandbox")
  option.add_argument("--headless")
  browser = webdriver.Chrome(executable_path='/Users/gaudesp/Documents/site/python/playlist/env/chromedriver', chrome_options=option)
  browser.get(link)
  wait = WebDriverWait(browser, 10)

  title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
  browser.close()
  browser.quit()
  return title