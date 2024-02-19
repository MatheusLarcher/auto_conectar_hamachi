from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Inicializa o driver do Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abre a URL desejada
driver.get("https://app.powerbi.com/groups/me/list?experience=power-bi")


time.sleep(6)
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("seuemail@exemplo.com")
try:
    # Espera até que o elemento seja encontrado ou até 10 segundos
    search_box = WebDriverWait(driver, 100000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tri-search-box"]'))
    )
    search_box.send_keys('texto para pesquisa')
finally:
   # driver.quit()  # Ou manter a sessão aberta conforme necessário
   print('ok')