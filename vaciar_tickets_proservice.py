"""
Copyright (C) 2022 Robert Nieto Molina

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from credenciales import usuario
from credenciales import password

class web_bot():
    def __init__(self):  # función de inicialización del bot
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://soporteproservice.nexe.com/login")
        
    def login(self): # loguea en la web de ticketing de soporte proservice
        input_usuario = self.driver.find_element(By.NAME, "usuario")
        input_password = self.driver.find_element(By.NAME, "password")
        input_usuario.send_keys(usuario)
        input_password.send_keys(password)
        self.driver.find_element(By.NAME, "Enviar").click()
        
    def visualizar_lista(self): # le da a la opción de ver 100 tickets a la misma vez, de todos los usuarios y de menor a mayor ticket
        usuarios = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/table/thead/tr[2]/th[5]/select")
        select = Select(usuarios)
        select.select_by_visible_text("")
        
        numero_elements = self.driver.find_element(By.NAME, "tabletickets_length")
        select = Select(numero_elements)
        select.select_by_visible_text("100")
        
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/table/thead/tr[1]/th[1]").click()
        
    def borra(self): # en el ticket rellena los campos de la forma necesaria para cerrar el ticket
        self.driver.find_element(By.ID, "botonactualizarticekt").click() # "ticekt" el typo es de Jero
        
        campo_horas = self.driver.find_element(By.ID, "ticketminhores")
        campo_horas.send_keys("0")
        campo_titol = self.driver.find_element(By.ID, "subtitolticket")
        campo_titol.send_keys("0")
        
        campo_estado = self.driver.find_element(By.ID, "estadosactualizar")
        select = Select(campo_estado)
        select.select_by_visible_text("Tancat")
        
        campo_actuacio = self.driver.find_element(By.ID, "ticketactuacio" )
        select = Select(campo_actuacio)
        select.select_by_visible_text("Tancar")
        
        try:
            campo_asignado = self.driver.find_element(By.ID, "ticketassignado")
            select = Select(campo_asignado)
            select.select_by_visible_text(usuario)
            
        except Exception:
            print("El ticket ya estaba resuelto por " + usuario + ".")
        
        self.driver.find_element(By.NAME, "Guardar").click()
        
    def borra_100(self): # borra los 99 tickets de menor valor numérico de la lista excepto el primero que no se puede eliminar nunca
        original_window = self.driver.current_window_handle
        for n in range (2,100):
            id_ticket = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/table/tbody/tr["+ str(n) +"]/td[1]/a")
            url = id_ticket.get_attribute("href")
            self.driver.switch_to.new_window('tab')
            self.driver.get(url)
            self.borra()
            self.driver.close()
            self.driver.switch_to.window(original_window)
        
bot = web_bot()
bot.login()
bot.visualizar_lista()
#bot.borra()
bot.borra_100()