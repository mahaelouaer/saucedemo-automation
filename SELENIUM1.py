from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Naviguer vers SauceDemo
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # 2. Connexion avec utilisateur invalide
    username_field.send_keys("invalid_user")
    password_field.send_keys("invalid_password")
    login_button.click()
    time.sleep(1)

    # 3. Vérifier message d'erreur utilisateur invalide
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message.text == (
        "Epic sadface: Username and password do not match any user in this service"
    )
    print("✅ Utilisateur invalide : message d'erreur correct")

    # 8. Vérifier le bouton de fermeture d'erreur
    close_button = driver.find_element(By.CLASS_NAME, "error-button")
    close_button.click()
    time.sleep(1)

    assert len(driver.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")) == 0
    print("✅ Bouton de fermeture d'erreur fonctionne")

    # 4. Connexion sans nom d'utilisateur
    driver.refresh()
    time.sleep(1)

    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    password_field.send_keys("secret_sauce")
    login_button.click()
    time.sleep(1)

    # 5. Vérifier message d'erreur nom d'utilisateur requis
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message.text == "Epic sadface: Username is required"
    print("✅ Nom d'utilisateur manquant : message correct")

    # 6. Connexion sans mot de passe
    driver.refresh()
    time.sleep(1)

    username_field = driver.find_element(By.ID, "user-name")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    login_button.click()
    time.sleep(1)

    # 7. Vérifier message d'erreur mot de passe requis
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message.text == "Epic sadface: Password is required"
    print("✅ Mot de passe manquant : message correct")

finally:
    driver.quit()
