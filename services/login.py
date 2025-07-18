from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
import os



def loginExecute(driver):
    
    # Carrega as variáveis do arquivo .env
    load_dotenv()

    # Acessa as variáveis usando os.getenv()
    senha = os.getenv("senhaPadrao")
    senhaNova = os.getenv("senhaNova")
    email = os.getenv("email")
    
    try:
        time.sleep(2)
        # Campo Senha
        passwordInput = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        passwordInput.send_keys(senha)

        # Botão de login
        loginButton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]'))
        )
        loginButton.click()

        try:
            # Checkbox de política de privacidade
            policyCheckbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="isAgreePolicy"]'))
            )
            policyCheckbox.click()

            # Botão de continuar
            continueButton = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
            )
            continueButton.click()

        except:
            print("Checkbox de política de privacidade não encontrado, continuando...")

        # Input senha antiga
        oldPasswordInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="userOldPwd"]'))
        )
        oldPasswordInput.send_keys(senha)

        # Input nova senha
        newPasswordInput = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="userPwd"]'))
        )
        newPasswordInput.send_keys(senhaNova)

        # Input confirmação de senha
        confirmPasswordInput = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="userConfirmPwd"]'))
        )
        confirmPasswordInput.send_keys(senhaNova)

        # Input email
        emailInput = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="emailNumberCfg"]'))
        )
        emailInput.send_keys(email)

        # Botão de continuar
        continueButton2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
        )
        continueButton2.click()

        # Botão de finalizar
        finishButton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
        )
        finishButton.click()

    except Exception as e:
        print(f"Erro ao executar o login: {e}. Tentando novamente com senha padrão...")
        time.sleep(2)
        
        try:
            # Limpa o campo de senha e insere a senha padrão
            passwordInput = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
            )
            passwordInput.clear()
            passwordInput.send_keys(senhaNova)

            # Clica no botão de login novamente
            loginButton = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]'))
            )
            loginButton.click()

        except Exception as e:
            print(f"Falha crítica ao tentar login com senha padrão: {e}")
            raise  # Opcional: encerra o script ou tenta outra ação