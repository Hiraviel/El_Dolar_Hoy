# importing libraries
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime

fecha = datetime.now().strftime('%d/%m/%Y')
hora = datetime.now().strftime('%H:%M:%S')

url = "https://www.eldolar.info/es-MX/mexico/dia/hoy"

page = urllib.request.urlopen(url)  # conntect to website

try:
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')
    # print(soup)

    tr_elements = soup.find_all('table')[0].find_all('tr')
    # print(tr_elements)

    content = []

    for tr in tr_elements:
        content.append(tr.getText(separator="-").split('\n')[0])

    # print(content[7].split("-"))
    dolar_oficial = (content[7].split("-"))
    #print("Institución: " + dolar_oficial[0] + "\n" + "Dolar: " + dolar_oficial[1] + "\n" + "Fecha: " + fecha + "\n" + "\n        Powered by Python")

    # with open('content.txt', 'w') as f:
    #    for i in content:
    #        f.write(i + "\n")

    DOF_Historico = open('DOF_Historico.txt', 'a')
    DOF_Historico.write('\n' + dolar_oficial[1] + "         " + fecha + "   " + "   " + hora + "        " + dolar_oficial[0])
    DOF_Historico.close()

    DOF_Hoy = open('DOF_Hoy.txt', 'w')
    DOF_Hoy.write("Costo del Dolar hoy " + fecha + " [" + hora + "]: " + dolar_oficial[1])
    DOF_Hoy.close()

except:
    print("An error occured.")
