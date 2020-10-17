from urllib.request import urlopen
import ssl

def check_link(url):
  try:
    urlopen(url)
    return True
  except:
    return False