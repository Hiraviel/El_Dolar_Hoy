import requests
from bs4 import BeautifulSoup
from datetime import datetime


dia = datetime.now().strftime('%d')
mes = datetime.now().strftime('%m')
year = datetime.now().strftime('%Y')
fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

#r = requests.get('https://www.dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador=158&dfecha=11%2F08%2F2022&hfecha=12%2F08%2F2022#gsc.tab=0', verify=False)

formato_consulta = str('{}%2F{}%2F{}&hfecha={}%2F{}%2F{}#gsc.tab=0'.format(dia, mes, year, dia, mes, year))
dof_url= 'https://www.dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador=158&dfecha={}'.format(formato_consulta)

#print(formato_consulta)
#print('\n')
#print(dof_url)

r = requests.get(dof_url, verify=False, timeout=30)

print(r.status_code)

if r.status_code == 200:
    try:
        soup_data = BeautifulSoup(r.text,  'html.parser')
        valor = soup_data.find('td', attrs={'class':'txt', 'width':'52%'})
        print('***Valores obtenidos del portal del DOF***\n')
        print('El Dolar al {}: '.format(fecha) + valor.text)
        print('***----------***')
    except:
        print('No se encontraron valores, favor de revisar los parametros de "valor"')
else:
    print('La pagina tiene un estatus {}'.format(r.status_code))
