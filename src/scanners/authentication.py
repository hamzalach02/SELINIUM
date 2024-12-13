def authentication_scanner(driver, login_url, credentials):
    driver.get(login_url)
    for username, password in credentials:
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.submit()
        if "invalid" not in driver.page_source.lower():
            print(f"Weak credentials accepted: {username}:{password}")
