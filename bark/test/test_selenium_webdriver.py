import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
###Using webdriver manager###
#Chrome
from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Chrome(ChromeDriverManager().install())
#Firefox
from webdriver_manager.firefox import GeckoDriverManager
# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
 
@pytest.fixture(params=["chrome"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        web_driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()
 
@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_open_url(self):
            self.driver.get("https://www.lambdatest.com/")
            print(self.driver.title)
 
            sleep(5)