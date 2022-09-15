import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

def linkedin_sign_in():
    global password_input
    # Clicking the Sign-In button
    driver.find_element(By.CSS_SELECTOR, "nav div .nav__button-secondary").click()
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(2)
    # Entering Email/Username
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(EMAIL)
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(2)
    # Entering Password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(PASSWORD)
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(2)
    # Clicking sign in button
    password_input.send_keys(Keys.ENTER)
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(5.05)


def submit_job_application():
    # Entering the mobile phone number
    phone_num_input = driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text input")
    # Only enter a phone number if the field is empty
    if phone_num_input == "":
        phone_num_input.send_keys("1234567890")
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(1)
    # Clicking the "Next" Button
    driver.find_element(By.CSS_SELECTOR, ".ph5 button").click()
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(3)


    try:
        # Clicking the review button - https://stackoverflow.com/a/58400631
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']").click()
    except NoSuchElementException:
        # Sometimes it will say the next button. So for that this code needs to run
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']").click()
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(3)

    print("Before Try Except")

    # Some applications may have additional questions or extra info is needed. If so, then we just discard that application and move on
    try:
        print("In Try block")
        # Clicking the "Submit Application" Button
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']").click()

    except NoSuchElementException:
        # Click the "x" / dismiss button
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss']")

        # Clicking discard
        driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar .artdeco-button--secondary")
        print("In Except block")


job_application_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

# Setting up selenium
chrome_driver_path = os.environ["CHROME_DRIVER_PATH"]
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))

# Opening URL to job applications
driver.get(job_application_URL)

# Signing into Linkedin #
linkedin_sign_in()

# Applying for a job #
# Get a list of all the jobs available - currently only able to get 7
jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")
# Loop through every job
for job in jobs:
    # Click on the job
    job.click()
    # Sleeping time - to make sure Linkedin doesn't restrict because of bot
    time.sleep(2)

    try:
        # Clicking the "Easy Apply" Button
        driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()
        # Sleeping time - to make sure Linkedin doesn't restrict because of bot
        time.sleep(1.05)

        # Go through the job application
        submit_job_application()
    except NoSuchElementException:
        continue
