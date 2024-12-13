from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_browser():
   
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    
    service = Service("C:/Users/lachh/Projects/selinium/chromedriver.exe")  

    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        
        driver.get("https://www.google.com")
        
       
        print("Page title is:", driver.title)
    finally:
       
        driver.quit()

if __name__ == "__main__":
    test_browser()
