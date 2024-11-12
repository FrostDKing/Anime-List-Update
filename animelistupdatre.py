from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

location = r"C:\Users\Tinil\AppData\Local\Google\Chrome\User Data"

options = Options()
options.add_argument(f"user-data-dir={location}")  # Path to the user data directory
options.add_argument("profile-directory=Profile 2")  # Profile name (e.g., "Profile 2")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(r"chromedriver.exe"), options=options)

with open(r"Path", "r") as file:
    all_data = file.readlines()
    driver.get("https://myanimelist.net/")

    for data in all_data:
        data = data.strip()  # Remove any leading or trailing whitespace/newlines

        if data == "### Watching":
            continue
        elif data.startswith("###"):
            print("Next category reached")
            break

        elif data.startswith("#"):
            continue

        elif "https://myanimelist.net/anime/" in data:
            driver.get(data)  # Load the page

            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.ID, "showAddtolistAnime"))
            )

            add_to_list = driver.find_element(By.ID, "showAddtolistAnime")
            add_to_list.click()

            button = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.NAME, "myinfo_submit"))
            )
            button.click()
        
        else:
            continue

# Close the browser if necessary
driver.quit()