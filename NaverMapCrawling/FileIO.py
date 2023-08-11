from selenium.webdriver.common.by import By


def open_file(brand_name):
    return open(f"../Reviews/{brand_name}", "w")


def write_file(file, review):
    file.write(review + "\n\n")


def close_file(file):
    file.close()


def review_write(driver, file):
    for s in driver.find_elements(By.CSS_SELECTOR, "span.zPfVt"):
        if s.text >= 5:
            write_file(file, s.text)
