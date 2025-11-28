from page.añadir_carrito import Carrito
from page.logueo_pagina import Login
import time

def test_añadirCarrito(driver_conf):
    login = Login(driver_conf)
    carrito = Carrito(driver_conf)

    login.open()
    login.user("standard_user", "secret_sauce")
    time.sleep(5)
    carrito.is_page()

    carrito.logout()
    time.sleep(4)
    assert "https://www.saucedemo.com/" in driver_conf.current_url
