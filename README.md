# **<u>Vaciar tickets proservice</u>**
## Crawler que borra tickets de [soporteproservice.nexe.com](https://soporteproservice.nexe.com) para no tener que hacerlo tu.

### Dependencias necesárias:
* [Python 3](https://www.python.org/downloads/)
* [Selenium]()
* [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
* Terminal/Powershell en tu sistema

### Instalación
Se necesita:
 * [Python 3](https://www.python.org/downloads/) o una version mayor en el equipo. 
 * Tener el driver Geckodriver en el PATH del sistema ([por ejemplo](https://stackoverflow.com/questions/42524114/how-to-install-geckodriver-on-a-windows-system)).
 * Tener los permisos para poder ejecutar el programa desde una terminal.

 Para poder usar Selenium hay que ejecutar el siguiente comando en la terminal para descargarlo para Python:

    python -m pip install selenium

### Uso
Hay que rellenar el archivo credenciales.py con las credenciales del usuario de [https://soporteproservice.nexe.com/login](https://soporteproservice.nexe.com/login) para que pueda acceder a la página. Sin espacios y entre las comillas.

Para ejecutar el programa solamente hay que ejecutar el archivo de Python:

    python.exe .\vaciar_tickets_proservice.py

Copyright (C) 2022 Robert Nieto Molina