"""
Contiene la configuracion inicial del logueo 
"""
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)



import pytest
from utils.funciones import configuracion



@pytest.fixture
def driver_conf():
    driver = configuracion()
    yield driver
    driver.quit()
