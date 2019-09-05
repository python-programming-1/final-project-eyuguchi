from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

def setup():
    print("setting up...")

  # todo: setup selenium
    driver.get(https://beachreportcard.org/34.54812069884963/-118.39367242299653/8)
    # todo: load the page
    print("setup done")


def waitForBeaches():
  print("waiting for beaches...")
  areBeachesOnPage = False
  while areBeachesOnPage == False:
      print("still haven't found beaches...")
      # todo: figure out if the beaches are on the page... if they are, then do this:
      delay = 3 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
      areBeachesOnPage = True
  print("out of loop... done waiting for beaches")

def getAllBeaches():
  print("getting all beaches...")
  # todo: get all beaches
  name = []
  url = https://beachreportcard.org/34.54812069884963/-118.39367242299653/8
  name = find('div', attrs = {'class':'jss195'})
  name.append(name.text)

  grades = []
  grade = find('div', attrs = {'class': 'jss8'})
  grades.append(name.text)
  
  # todo: remove this example, and 
  return [
    { "name": "Good Beach", "grade": "A+" },
    { "name": "Bad Beach", "grade": "F" }
  ]

def getCleanestBeach(beaches):
  print("getting cleanest beach...")
  # todo: figure out how to get the cleanest beach from an array of all beaches
  return_dic = {'grade': None}
    grades.sort()
  # todo: for now, i will just return the first one
  return return_dic[0]

def main():
  print("running main...")
  setup()
  waitForBeaches()
  beaches = getAllBeaches()
  cleanestBeach = getCleanestBeach(beaches)
  print("the cleanest beach is " + cleanestBeach["name"])
  print("done")

# run the main function
main()