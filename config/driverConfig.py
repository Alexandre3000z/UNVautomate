import os
import sys
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tkinter.messagebox as messagebox


def resource_path(relative_path):
    """Obtém o caminho absoluto para recursos, funciona para dev e para PyInstaller"""
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def get_webdriver():
    """Configuração robusta do WebDriver para funcionar no EXE"""
    try:
        # Configurações do Chrome
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        
        

        # Caminho para o chromedriver
        if getattr(sys, "frozen", False):
            # Modo EXE - usa o chromedriver incluído
            chromedriver_path = resource_path("chromedriver.exe")
        else:
            # Modo desenvolvimento - usa o chromedriver local
            chromedriver_path = "chromedriver.exe"

        # Configura o serviço
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    except Exception as e:
        error_msg = f"Não foi possível iniciar o navegador:\n{str(e)}"
        if "This version of ChromeDriver only supports Chrome version" in str(e):
            error_msg += "\n\nPor favor, atualize seu Google Chrome"
        messagebox.showerror("Erro no Navegador", error_msg)
        return None
