"""
2023 Delawer
"""

from selenium.webdriver.common.by import By


URL = "https://testqastudio.me/"

def test_product_view_sku(browser):
    """
    Test case WERT-1
    """
    browser.get(URL)
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()

    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = browser.find_element(By.XPATH, value=x_path_table)
    element.click()

    sku = browser.find_element(By.CLASS_NAME, value="sku")

    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"

    print("ok")