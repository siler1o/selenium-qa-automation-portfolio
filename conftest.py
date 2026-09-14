import os

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()

    if os.getenv("CI"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)

    # Prevent third-party ads from interrupting practice-site tests
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd(
        "Network.setBlockedURLs",
        {
            "urls": [
                "*://*.googlesyndication.com/*",
                "*://*.doubleclick.net/*",
                "*://*.googleadservices.com/*",
            ]
        },
    )

    yield driver
    driver.quit()
