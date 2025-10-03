from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from dotenv import load_dotenv
import os


def horarioConfig(driver):

    # Carrega as variáveis do arquivo .env
    load_dotenv()

    # Acessa as variáveis usando os.getenv()
    ntp = "10.10.0.35"
    try:

        # Horario
        timeButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Com_timeCfgLink"]'))
        )
        timeButton.click()

        # NTP input
        ntpInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="NTPIPAddr"]'))
        )

        ntpInput.click()
        ntpInput.send_keys(Keys.CONTROL + "a")  # Seleciona todo o texto
        ntpInput.send_keys(Keys.DELETE)  # Apaga o texto selecionado
        ntpInput.send_keys(ntp)

        # Save Button
        saveButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="configContainer"]/div/span/input')
            )
        )
        saveButton.click()

    except Exception as e:
        print(f"Erro ao configurar Horário: {e}")


def OSDconfig(driver, camName):

    try:

        # Botão da Lista chamado OSD
        OSDButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Com_osdLink"]'))
        )
        OSDButton.click()

        time.sleep(1)

        # Área de texto para nome da câmera
        text2checkBox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="InfoEnable1"]'))
        )
        # Verifica se o checkbox NÃO está selecionado antes de clicar
        if not text2checkBox.is_selected():
            text2checkBox.click()

        text2Button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="infoTR1"]/td[3]'))
        )
        text2Button.click()

        textInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Value1"]'))
        )
        textInput.click()
        textInput.send_keys(Keys.CONTROL + "a")  # Seleciona todo o texto
        textInput.send_keys(Keys.DELETE)  # Apaga o texto selecionado
        textInput.send_keys(camName)

        # Área de texto X & Y
        xInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="InfoLeft1"]'))
        )
        xInput.click()
        xInput.send_keys(Keys.CONTROL + "a")  # Seleciona todo o texto
        xInput.send_keys(Keys.DELETE)  # Apaga o texto selecionado
        xInput.send_keys("2")

        yInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="InfoTop1"]'))
        )
        yInput.click()
        yInput.send_keys(Keys.CONTROL + "a")  # Seleciona todo o
        yInput.send_keys(Keys.DELETE)  # Apaga o texto selecionado
        yInput.send_keys("95")

    except Exception as e:
        raise (f"Erro ao configurar OSD: {e}")


def audioVideoConfig(driver):

    try:
        # Botão de configuração de áudio e vídeo
        audioVideoButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menuContent"]/div[7]/a'))
        )
        audioVideoButton.click()

        time.sleep(1)

        # Configuração resolução 1
        selectResolution1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="MainStreamPictureSize"]')
            )
        )
        dropdown = Select(selectResolution1)
        dropdown.select_by_visible_text("1280×720(720P)")

        # Configuração resolução 2
        selectResolution2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="AuxStreamPictureSize"]')
            )
        )
        dropdown2 = Select(selectResolution2)
        dropdown2.select_by_visible_text("1280×720(720P)")

        # Botão de salvar
        saveButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="configContainer"]/span/input')
            )
        )
        saveButton.click()

    except Exception as e:
        raise (f"Erro ao configurar Áudio e Vídeo: {e}")


def redeConfig(driver, ipNovo, mascara, gateway):

    try:
        # Botão de configuração de rede
        redeButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menuContent"]/div[4]/a'))
        )
        redeButton.click()

        time.sleep(1)

        # Tipo de IP
        selectBoxIP = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="IPGetType"]'))
        )
        dropdownIP = Select(selectBoxIP)
        dropdownIP.select_by_visible_text("IP Estático")

        # IP
        ipInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="IpAddress"]'))
        )
        ipInput.click()
        ipInput.send_keys(Keys.CONTROL + "a")  # Seleciona todo o
        ipInput.send_keys(Keys.DELETE)  # Apaga o texto selecionado
        ipInput.send_keys(ipNovo)

        # Máscara de sub-rede
        mascaraInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="IpNetmask"]'))
        )
        mascaraInput.click()
        mascaraInput.send_keys(Keys.CONTROL + "a")  # Seleciona todo o
        mascaraInput.send_keys(Keys.DELETE)  # Apaga o texto selecionado
        mascaraInput.send_keys(mascara)

        # Gateway
        gatewayInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="IpGateway"]'))
        )
        gatewayInput.click()
        gatewayInput.send_keys(Keys.CONTROL + "a")  # Seleciona todo o
        gatewayInput.send_keys(Keys.DELETE)  # Apaga o texto selecionado
        gatewayInput.send_keys(gateway)

        # Botão de salvar
        saveButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="frmSetup"]/span/input'))
        )
        saveButton.click()

        # Esperar e aceitar a alert box (clicar em OK)
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()  # Clica no botão OK
            print("Alert box 'OK' clicado com sucesso!")
        except:
            print("Nenhuma alert box encontrada ou erro ao clicar em OK.")

        time.sleep(5)
    except Exception as e:
        raise (f"Erro ao configurar Rede: {e}")
