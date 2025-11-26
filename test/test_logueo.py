from utils.funciones import get_csv
from page.logueo_pagina import Login
import pytest

@pytest.mark.parametrize("username, password, bool", get_csv())
def test_login(driver_conf, username, password, bool ):
    loginPage = Login(driver_conf)
    loginPage.open()
    loginPage.user(username, password)

    if bool: 
        assert "inventory.html" in driver_conf.current_url
    else:
        assert "inventory.html" not in driver_conf.current_url


