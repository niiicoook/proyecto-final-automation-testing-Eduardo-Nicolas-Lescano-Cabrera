# from utils.manejo_datos import get_csv, get_json
# from utils.simular_datos import get_fake_user
# from page.logueo_pagina import Login
# import pytest

# @pytest.mark.parametrize("username, password, bool", get_fake_user())
# def test_login(driver_conf, username, password, bool ):
#     loginPage = Login(driver_conf)
#     loginPage.open()
#     loginPage.user(username, password)

#     if bool: 
#         assert "inventory.html" in driver_conf.current_url
#     else:
#         assert "inventory.html" not in driver_conf.current_url


