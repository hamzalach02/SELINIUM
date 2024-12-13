from selenium.webdriver.common.by import By

def sql_injection_scanner(driver, url, payloads):
    driver.get(url)
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    for input_field in inputs:
        for payload in payloads:
            input_field.clear()
            input_field.send_keys(payload)
            input_field.submit()
            if "error" in driver.page_source.lower():
                print(f"Potential SQL Injection detected with payload: {payload}")
