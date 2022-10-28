# **<u>Vaciar tickets proservice</u>**
## Crawler que borra tickets de [soporteproservice.nexe.com](https://soporteproservice.nexe.com) para no tener que hacerlo tu.

### Dependencias necesárias:
* [Python 3](https://www.python.org/downloads/)
* [Selenium](https://www.selenium.dev/)
* [GeckoDriver](https://github.com/mozilla/geckodriver/)
* [Terminal del sistema](https://es.wikipedia.org/wiki/Terminal_(inform%C3%A1tica))

### Instalación
Se necesita:
 * [Python 3](https://www.python.org/downloads/) o una version mayor en el equipo. Se puede descargar directamente de su web.
 * [GeckoDriver](https://github.com/mozilla/geckodriver/), se puede descargar desde [su Github](https://github.com/mozilla/geckodriver/releases). Hace falta descargar la versión para el sistema operativo en uso y poner el driver en el PATH del sistema ([por ejemplo](https://stackoverflow.com/questions/42524114/how-to-install-geckodriver-on-a-windows-system)).
 * Selenium, para descargarlo hay que ejecutar el siguiente comando en la terminal:

        python -m pip install selenium
 
 * Tener los permisos para poder ejecutar el programa desde una terminal.

### Uso
Hay que rellenar el archivo credenciales.py con las credenciales del usuario de [https://soporteproservice.nexe.com/login](https://soporteproservice.nexe.com/login) para que pueda acceder a la página.

Para ejecutar el programa hay que ejecutar el archivo de Python:

    python.exe .\vaciar_tickets_proservice.py

Copyright (C) 2022 Robert Nieto Molina