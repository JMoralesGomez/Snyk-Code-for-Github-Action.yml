# NetScanner.py
# * Descripción: Utilidad de red escrita en Python para escanear y detectar dispositivos en un segmento de red indicado con nmap, 
# * obtener su dirección ip, dirección mac y sus puertos abiertos
# * Author: ClarkCodes

# Imports
import nmap

# Predefined
separator = "********************************************"

# Functions
def printFoundHosts( allHostsList : list[str] ):
    if len( allHostsList ) > 0:
        print( "\n*--- Dispositivos encontrados:\n" )

        for i, host in enumerate( allHostsList ):
            print( separator )
            print( f"*** Dispositivo #{ i + 1 } ***" )
            print( f"Nombre:        { devScanner[host].hostname() }" )
            print( f"Dirección Ip:  { host }" )

            if 'mac' in devScanner[host]['addresses']:
                print( f"Dirección MAC: { devScanner[host]['addresses']['mac'] }" )

            print( f"Estado:        { devScanner[host].state() }" )
            
            protocolsList = devScanner[host].all_protocols()

            if len( protocolsList ) > 0:
                print( "\n* Protocolos *" )

                for proto in devScanner[host].all_protocols():
                    print( f"\tProtocolo: { proto }" )
                    lport = devScanner[host][proto].keys()
                    #lport.sort()
                    for port in lport:
                        print ( f"\t\tPuerto: { port }\tEstado: { devScanner[host][proto][port]['state'] }" )

        print( separator )
    else:
        print( "\nNo se encontraron dispositivos en el segmento de red indicado." )


### Script Body Code
print( "\n*** Clark's Network Devices Scanner ***\n" )

devScanner = nmap.PortScanner()

ip = input( "Ingrese el Rango Ip: " )

print( "\nBuscando dispositivos presentes en la red del rango Ip indicado: ", ip )
print( "Un momento por favor, en breve se mostrará el resultado.\nDetectando..." )

devScanner.scan( ip )

printFoundHosts( devScanner.all_hosts() )

# Fin del Script - Mensaje de Despedida
print( "\nGracias por usar este Script, es todo por ahora, hasta pronto, bye. :)" )
print( "Script escrito por @ClarkCodes(en todas las redes sociales).\n\n" )
