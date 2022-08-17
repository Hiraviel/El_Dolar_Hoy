import requests
import json

url_dof = "https://sidofqa.segob.gob.mx/dof/sidof/indicadores/"

'''
https://sidofqa.segob.gob.mx/datos_abiertos

Pagina de consulta donde se estipula la forma de los requests para varios tipos de datos del DOF
'''

consulta = requests.get(url_dof, verify=False)
consulta_json = consulta.json()
identificador = consulta_json['ListaIndicadores'][0]['codIndicador']
tipoIndicador = consulta_json['ListaIndicadores'][0]['codTipoIndicador']
fecha = consulta_json['ListaIndicadores'][0]['fecha']
valor = consulta_json['ListaIndicadores'][0]['valor']

print(str(identificador) + "\n" + str(tipoIndicador) + "\n" + str(fecha) + "\n" + str(valor))