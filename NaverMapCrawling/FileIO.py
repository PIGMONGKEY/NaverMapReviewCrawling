from selenium.webdriver.common.by import By


def open_file(brand_name):
    return open(f"../Reviews/{brand_name}.txt", "w")


def write_file(file, review):
    file.write(review + "\n\n")


def close_file(file):
    file.close()


def review_write(brand_name, driver):
    file = open_file(brand_name)

    for s in driver.find_elements(By.CSS_SELECTOR, "span.zPfVt"):
        if s.text.__len__() >= 5:
            write_file(file, s.text)

    close_file(file)
