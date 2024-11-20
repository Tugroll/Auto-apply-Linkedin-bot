import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class LinkedInBot:
    def __init__(self, email, password, phone):
        self.email = email
        self.password = password
        self.phone = phone
        self.driver = None
        self.action = None

    def initialize_driver(self):
        #Initialize the WebDriver and set Chrome options.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.action = ActionChains(self.driver)

    def login(self):
        #Log in to LinkedIn with the provided credentials.
        self.driver.get("https://www.linkedin.com/")
        time.sleep(2)

        signin_button = self.driver.find_element(By.LINK_TEXT, "Sign in")
        signin_button.click()
        time.sleep(3)

        user_id = self.driver.find_element(By.ID, "username")
        user_id.send_keys(self.email)

        user_password = self.driver.find_element(By.ID, 'password')
        user_password.send_keys(self.password, Keys.ENTER)
        time.sleep(10)

    def navigate_to_jobs(self):
       #Navigate to the Jobs page.
        job_button = self.driver.find_element(By.XPATH, "/html/body/div[6]/header/div/nav/ul/li[3]/a")
        job_button.click()
        time.sleep(5)

        self.driver.maximize_window()
        self.action.scroll_by_amount(0, 400).perform()
        time.sleep(2)

        see_all_button = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[6]/div[3]/div/div[3]/div/div/main/div/div[1]/div[3]/div/div/div/section/div[2]/a')
        see_all_button.click()
        time.sleep(5)

    def apply_to_jobs(self):
        #Apply to jobs using the Easy Apply feature.
        easy_apply_button = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button")
        easy_apply_button.click()
        time.sleep(3)

        all_listings = self.driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
        for listing in all_listings:
            print("Opening Listing")
            listing.click()
            time.sleep(2)

            try:
                # Click Apply Button
                apply_button = self.driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
                apply_button.click()
                time.sleep(5)

                # Insert Phone Number if empty
                phone_input = self.driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
                if not phone_input.get_attribute("value"):
                    phone_input.send_keys(self.phone)

                # Submit application
                submit_button = self.driver.find_element(By.CSS_SELECTOR, "footer button")
                submit_button.click()
                time.sleep(2)

                # Close confirmation modal
                close_button = self.driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)

            except Exception as e:
                print(f"Error applying to job: {e}")
                continue

    def run(self):
        #Run the LinkedIn job application bot
        try:
            self.initialize_driver()
            self.login()
            self.navigate_to_jobs()
            self.apply_to_jobs()
        finally:
            self.cleanup()

    def cleanup(self):
        #Close the WebDriver.
        if self.driver:
            self.driver.quit()