#diego canales

import urllib.parse
import requests

principal_api = "https://www.mapquestapi.com/directions/v2/route?"
llave = "0FwXUG6YPUsuBOWN1D7NVvu6vxGvz7Z8"

while True:
    origen = input("ubicacion inicial: ")
    if origen == "salir" or origen == "s":
        break

    destino = input("destino: ")
    if destino == "salir" or destino == "s":
        break

    url = principal_api + urllib.parse.urlencode({"key" :llave, "from" :origen, "to" :destino})
    print("URL: " + (url))

    json_datos = requests.get(url).json()
    json_estatus = json_datos ["info"] ["statuscode"]

    if json_estatus == 0:
        print("API estatus: " + str(json_estatus) + " = llamada a la ruta fue exitosa.\n")
        print("=============================================")
        print("direcciones desde" + (origen) + " a " + (destino))
        print("duracion del viaje:   " + (json_datos["route"]["formattedTime"]))
        print("kilometros:           " + str("{:.2f}".format((json_datos["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_datos["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")