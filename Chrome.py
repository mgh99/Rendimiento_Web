from selenium import webdriver
import time

URL = "https://www.bodasorganizadas.es"

# Iniciamos el navegador con Selenium
driver = webdriver.Chrome()

# Medimos el tiempo de carga completo de la página
start = time.perf_counter()
driver.get(URL)
end = time.perf_counter()

# Calculamos el tiempo que ha tardado en cargar la página
elapsed_time = end - start

# Mostramos el tiempo en pantalla
print("Elapsed time: {:.2f} seconds".format(elapsed_time))

# Cerramos el navegador
driver.quit()
