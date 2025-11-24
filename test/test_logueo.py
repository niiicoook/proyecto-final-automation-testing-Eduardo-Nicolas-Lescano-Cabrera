from page.logueo_pagina import Login

def test_login(driver_conf):
    loginPage = Login(driver_conf)
    loginPage.open()
    loginPage.user()

