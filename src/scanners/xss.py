def xss_scanner(driver, url, payloads):
    driver.get(url)
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    for input_field in inputs:
        for payload in payloads:
            input_field.clear()
            input_field.send_keys(payload)
            input_field.submit()
            if payload in driver.page_source:
                print(f"XSS vulnerability found with payload: {payload}")
