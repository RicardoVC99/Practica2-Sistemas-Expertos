import os
import msvcrt
import random

os.system('mode con: cols=150 lines=40')

#Bienvenida y reglas
print("Bienvenido a Clue")
print(" ")
print("El juego consiste en encontrar al culpable de un crimen que ha acontecido en el campus de una universidad CETI, para ello contarás con 5 pistas que te ayudarán a resolver el misterio.")
print("Para ganar el juego debes de acertar quien fue el culpable, la escena del crimen y el arma con que se realizó el crimen, si fallas en encontrar al culpable, el lugar o el arma perderás el juego. Es decir, necesitas encontrar los 3 para poder ganar, con que falles en uno pierdes.")
print("")
print("Cuando aparezca el mensaje al final de la pantalla 'Presiona ENTER o barra espaciadora' para avanzar, hazlo. Si presionas cualquier otra tecla puede que ocurra un error y se termine la ejecución del juego.")
print("")
print("El juego se juega unicamente con los numeros del 1 al 5, la barra espaciadora y el ENTER.")
print("")
print("Para ingresar los números al juego, solo tienes que presionar la tecla del número en tu teclado y presionar ENTER para introducirlo.")
print("")
print("ES RECOMENDABLE JUGAR EN PANTALLA COMPLETA PARA UNA MEJOR VISUALIZACIÓN")
print("")
print("Buena suerte.")
print("")

print("Presione la barra espaciadora o ENTER para comenzar... ")
msvcrt.getch()
os.system("cls")

#Juego en bucle
###############################################################################################################################################

ciclo = 1
while ciclo == 1:

    i=0
    SUS_R = 0         #sospechoso
    weap_R = 0        #arma
    place_R = 0       #Lugar

    os.system("cls")

    #Generación del sospechoso, arma y lugar
    sospechoso = ["Gortari", "Coloso", "Bob patiño", "el Negro", "el Blanco"]
    SUS_R = random.randrange(0,5)

    armas = ["Cuchillo", "Libro", "Cuerda", "Veneno", "Palanca"]

    Lugar = ["Jardín", "Biblioteca", "Oficina de la directora", "Teatro", "Baño"]

    #Acomodo random para lugares y armas diferentes en cada historia
    arma_sample = random.sample(armas, len(armas))
    Lugar_sample = random.sample(Lugar, len(Lugar))

    if SUS_R==0:
        weap_R = arma_sample[2]
        place_R=Lugar_sample[3]
    elif SUS_R==1:
        weap_R = arma_sample[0]
        place_R=Lugar_sample[0]
    elif SUS_R==2:
        weap_R = arma_sample[4]
        place_R=Lugar_sample[2]
    elif SUS_R==3:
        weap_R = arma_sample[3]
        place_R=Lugar_sample[4]
    else:
        weap_R = arma_sample[1]
        place_R=Lugar_sample[1]

    #Historia
    print("Has sido invitado al campus del CETI,en Guadalajara , donde se lleva a cabo una conferencia con 5 de las personas más reconocidas del mundo de lo \noculto y lo paranormal. Entre esas personas se encuentran:\n-> Gortari, un investigador y explorador sobre la consiencia humana, los mundos ocultos, los dioses primigenios y el conocimiento ignoto.\n-> Coloso, un árabe que muchos tildan de loco por asegurar que uno de los dioses primigenios le dio el conocimiento neceasrio para escribir ""El Necronomicón"".\n-> Bob Patiño, un reconocido brujo dentro de la comunidad de lo oculto por sus e                                            xtraños rituales para contactar seres de otra dimensión.\n > El Negro, un famoso quiromántico debido a sus acertadas predicciones en las personas, además de ser  un buen hipnotizador.\n-> El Blanco, un señor de entrada edad quien en sus días dio clases sobre teología en la universidad y que ahora está metido en lo oculto.")

    print("")

    print("Durante de la reunión después de la conferencia alguien grita horrorizado por alguna razón, al parecer han encontrado muerto a Kathya, la organizadora \nde la conferencia.")
    print("")
    print("Kathya era una persona muy reconocida no solo dentro de la comunidad, sino también en la universidad ya que acababa de asumir el puesto de directora hace 3 meses.\nAl parecer, ella era muy amiga de cada uno de los invitados que estuvieron en la conferencia de hoy, ya que se le vio conviviendo de agradable manera con todos ellos. \nSin embargo, ninguno de ellos fue visto durante la hora a la que encontraron a Kathya, sino que aparecieron 1 hora después cuando se declaró cerrada la universidad por \nla policía, convirtiéndolos en los principales sospechosos del asesinato.")

    print("")

    print("Tú, quien antes trabajó como investigador privado, convences a la policía para ayudar a resolver el misterio ya que hay testigos asegurando que te vieron en todo momento,\npor lo que estás descartado como sospechoso.")

    #Bucle de las 5 pistas
    for i in range(5):

        print("")
        pista = int(input("¿Qué vas a investigar?\n 1)Sospechoso\n 2)Arma\n 3)Lugar\n"))
        print("")

        #Investigación de sospechoso (ORIGINAL)
        ##########################################################################################################################################################################################
        if pista==1:
            SUS_P = int(input(" 1)Gortari\n  2)Coloso\n 3)Bob patiño\n 4)el Negro\n 5)el Blanco\n"))
            if SUS_P==1:
                if SUS_R==0:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                elif SUS_R==1:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                elif SUS_R==2:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                elif SUS_R==3:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==4:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

            elif SUS_P==2:
                if SUS_R==0:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==1:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                elif SUS_R==2:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                elif SUS_R==3:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                elif SUS_R==4:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

            elif SUS_P==3:
                if SUS_R==0:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                elif SUS_R==1:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==2:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                elif SUS_R==3:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                elif SUS_R==4:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

            elif SUS_P==4:
                if SUS_R==0:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                elif SUS_R==1:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==2:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                elif SUS_R==3:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                elif SUS_R==4:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

            elif SUS_P==5:
                if SUS_R==0:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==1:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                elif SUS_R==2:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                elif SUS_R==3:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==4:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[4] + " en el lugar, tampoco vieron " + arma_sample[4])

            else:
                print("Entrada erronea, vuelva a intentar...")
                while SUS_P!=(1 or 2 or 3 or 4 or 5):
                    SUS_P = int(input(" 1)Gortari\n  2)Coloso\n 3)Bob patiño\n 4)el Negro\n 5)el Blanco\n"))
                    if SUS_P==1:
                        if SUS_R==0:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                        elif SUS_R==1:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                        elif SUS_R==2:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==3:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==4:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

                    elif SUS_P==2:
                        if SUS_R==0:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==1:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                        elif SUS_R==2:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                        elif SUS_R==3:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                        elif SUS_R==4:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                    elif SUS_P==3:
                        if SUS_R==0:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                        elif SUS_R==1:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==2:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                        elif SUS_R==3:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                        elif SUS_R==4:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                    elif SUS_P==4:
                        if SUS_R==0:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==1:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==2:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                        elif SUS_R==3:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                        elif SUS_R==4:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                    elif SUS_P==5:
                        if SUS_R==0:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==1:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                        elif SUS_R==2:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                        elif SUS_R==3:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==4:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[4] + " en el lugar, tampoco vieron " + arma_sample[4])

        #Investigación de arma (ORIGINAL)
        ###############################################################################################################################################################################################
        elif pista == 2:
            print(" 1) " + arma_sample[0] + "\n 2) " + arma_sample[1] + "\n 3) " + arma_sample[2] + "\n 4) " + arma_sample[3] + "\n 5) " + arma_sample[4])
            weap_P = int(input())
            if weap_P == 1:
                if SUS_R==0:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                elif SUS_R==1:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                elif SUS_R==2:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                elif SUS_R==3:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                elif SUS_R==4:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

            elif weap_P == 2:
                if SUS_R==0:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==1:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==2:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                elif SUS_R==3:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==4:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

            elif weap_P == 3:
                if SUS_R==0:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                elif SUS_R==1:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                elif SUS_R==2:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                elif SUS_R==3:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                elif SUS_R==4:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

            elif weap_P == 4:
                if SUS_R==0:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                elif SUS_R==1:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                elif SUS_R==2:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                elif SUS_R==3:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                elif SUS_R==4:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

            elif weap_P == 5:
                if SUS_R==0:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==1:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==2:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                elif SUS_R==3:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==4:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

            else:
                print("Entrada erronea, vuelva a intentar...")
                while weap_P!=(1 or 2 or 3 or 4 or 5):
                    print(" 1) " + arma_sample[0] + "\n 2) " + arma_sample[1] + "\n 3) " + arma_sample[2] + "\n 4) " + arma_sample[3] + "\n 5) " + arma_sample[4])
                    weap_P = int(input())
                    if weap_P == 1:
                        if SUS_R==0:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                        elif SUS_R==1:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                        elif SUS_R==2:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                        elif SUS_R==3:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                        elif SUS_R==4:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                    elif weap_P == 2:
                        if SUS_R==0:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==1:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==2:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                        elif SUS_R==3:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==4:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                    elif weap_P == 3:
                        if SUS_R==0:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                        elif SUS_R==1:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                        elif SUS_R==2:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                        elif SUS_R==3:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                        elif SUS_R==4:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

                    elif weap_P == 4:
                        if SUS_R==0:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==1:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                        elif SUS_R==2:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==3:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                        elif SUS_R==4:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                    elif weap_P == 5:
                        if SUS_R==0:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==1:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==2:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                        elif SUS_R==3:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==4:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

        #Investigación de lugar (ORIGINAL)
        #######################################################################################################################################################################################################
        elif pista == 3:
            print(" 1) " + Lugar_sample[0] + "\n 2) " + Lugar_sample[1] + "\n 3) " + Lugar_sample[2] + "\n 4) " + Lugar_sample[3] + "\n 5) " + Lugar_sample[4])
            place_P = int(input())
            if place_P == 1:
                if  SUS_R==0:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                elif SUS_R==1:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                elif SUS_R==2:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                elif SUS_R==3:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                elif SUS_R==4:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

            elif place_P == 2:
                if  SUS_R==0:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==1:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                elif SUS_R==2:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                elif SUS_R==3:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                elif SUS_R==4:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

            elif place_P == 3:
                if  SUS_R==0:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                elif SUS_R==1:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                elif SUS_R==2:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                elif SUS_R==3:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==4:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

            elif place_P == 4:
                if  SUS_R==0:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                elif SUS_R==1:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==2:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                elif SUS_R==3:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                elif SUS_R==4:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

            elif place_P == 5:
                if  SUS_R==0:
                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==1:
                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                elif SUS_R==2:
                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                elif SUS_R==3:
                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                    print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                elif SUS_R==4:
                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])
            else:
                print("Entrada erronea, vuelva a intentar")
                while place_P!=(1 or 2 or 3 or 4 or 5):
                    print(" 1) " + Lugar_sample[0] + "\n 2) " + Lugar_sample[1] + "\n 3) " + Lugar_sample[2] + "\n 4) " + Lugar_sample[3] + "\n 5) " + Lugar_sample[4])
                    place_P = int(input())
                    if place_P == 1:
                        if  SUS_R==0:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                        elif SUS_R==1:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                        elif SUS_R==2:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                        elif SUS_R==3:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                        elif SUS_R==4:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                    elif place_P == 2:
                        if  SUS_R==0:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==1:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                        elif SUS_R==2:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                        elif SUS_R==3:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                        elif SUS_R==4:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                    elif place_P == 3:
                        if  SUS_R==0:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                        elif SUS_R==1:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                        elif SUS_R==2:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==3:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==4:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                    elif place_P == 4:
                        if  SUS_R==0:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==1:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==2:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                        elif SUS_R==3:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==4:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

                    elif place_P == 5:
                        if  SUS_R==0:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==1:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==2:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                        elif SUS_R==3:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                        elif SUS_R==4:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

        else:
            print("Entrada erronea, vuelva a intentar...")
            while pista!=(1 or 2 or 3):
                print("")
                pista = int(input("¿Qué vas a investigar?\n 1)Sospechoso\n 2)Arma\n 3)Lugar\n"))
                print("")

                #Investigación de sospechoso (EN CASO DE ERROR)
                ##########################################################################################################################################################################################
                if pista==1:
                    SUS_P = int(input(" 1)Gortari\n  2)Coloso\n 3)Bob patiño\n 4)el Negro\n 5)el Blanco\n"))
                    if SUS_P==1:
                        if SUS_R==0:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                        elif SUS_R==1:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                        elif SUS_R==2:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==3:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==4:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

                    elif SUS_P==2:
                        if SUS_R==0:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==1:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                        elif SUS_R==2:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                        elif SUS_R==3:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                        elif SUS_R==4:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                    elif SUS_P==3:
                        if SUS_R==0:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                        elif SUS_R==1:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==2:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                        elif SUS_R==3:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                        elif SUS_R==4:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                    elif SUS_P==4:
                        if SUS_R==0:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==1:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==2:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                        elif SUS_R==3:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                        elif SUS_R==4:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                    elif SUS_P==5:
                        if SUS_R==0:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==1:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                        elif SUS_R==2:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                        elif SUS_R==3:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==4:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[4] + " en el lugar, tampoco vieron " + arma_sample[4])

                    else:
                        print("Entrada erronea, vuelva a intentar...")
                        while SUS_P!=(1 or 2 or 3 or 4 or 5):
                            SUS_P = int(input(" 1)Gortari\n  2)Coloso\n 3)Bob patiño\n 4)el Negro\n 5)el Blanco\n"))
                            if SUS_P==1:
                                if SUS_R==0:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                                elif SUS_R==1:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                                elif SUS_R==2:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                                elif SUS_R==3:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==4:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

                            elif SUS_P==2:
                                if SUS_R==0:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==1:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                                elif SUS_R==2:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                                elif SUS_R==3:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                                elif SUS_R==4:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                            elif SUS_P==3:
                                if SUS_R==0:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                                elif SUS_R==1:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==2:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                                elif SUS_R==3:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                                elif SUS_R==4:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                            elif SUS_P==4:
                                if SUS_R==0:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                                elif SUS_R==1:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==2:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                                elif SUS_R==3:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                                elif SUS_R==4:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                            elif SUS_P==5:
                                if SUS_R==0:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==1:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                                elif SUS_R==2:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                                elif SUS_R==3:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==4:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[4] + " en el lugar, tampoco vieron " + arma_sample[4])

                #Investigación de arma (EN CASO DE ERROR)
                ###############################################################################################################################################################################################
                elif pista == 2:
                    print(" 1) " + arma_sample[0] + "\n 2) " + arma_sample[1] + "\n 3) " + arma_sample[2] + "\n 4) " + arma_sample[3] + "\n 5) " + arma_sample[4])
                    weap_P = int(input())
                    if weap_P == 1:
                        if SUS_R==0:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                        elif SUS_R==1:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                        elif SUS_R==2:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                        elif SUS_R==3:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                        elif SUS_R==4:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                    elif weap_P == 2:
                        if SUS_R==0:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==1:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==2:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                        elif SUS_R==3:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==4:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                    elif weap_P == 3:
                        if SUS_R==0:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                        elif SUS_R==1:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                        elif SUS_R==2:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                        elif SUS_R==3:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                        elif SUS_R==4:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

                    elif weap_P == 4:
                        if SUS_R==0:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==1:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                        elif SUS_R==2:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==3:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                        elif SUS_R==4:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                    elif weap_P == 5:
                        if SUS_R==0:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==1:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==2:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                        elif SUS_R==3:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==4:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

                    else:
                        print("Entrada erronea, vuelva a intentar...")
                        while weap_P!=(1 or 2 or 3 or 4 or 5):
                            print(" 1) " + arma_sample[0] + "\n 2) " + arma_sample[1] + "\n 3) " + arma_sample[2] + "\n 4) " + arma_sample[3] + "\n 5) " + arma_sample[4])
                            weap_P = int(input())
                            if weap_P == 1:
                                if SUS_R==0:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                                elif SUS_R==1:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                                elif SUS_R==2:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                                elif SUS_R==3:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                                elif SUS_R==4:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                            elif weap_P == 2:
                                if SUS_R==0:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==1:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==2:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                                elif SUS_R==3:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==4:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                            elif weap_P == 3:
                                if SUS_R==0:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                                elif SUS_R==1:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                                elif SUS_R==2:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                                elif SUS_R==3:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                                elif SUS_R==4:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])

                            elif weap_P == 4:
                                if SUS_R==0:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                                elif SUS_R==1:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                                elif SUS_R==2:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                                elif SUS_R==3:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                                elif SUS_R==4:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                            elif weap_P == 5:
                                if SUS_R==0:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==1:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==2:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                                elif SUS_R==3:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==4:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

                #Investigación de lugar (EN CASO DE ERROR)
                ##############################################################################################################################################################################################
                elif pista == 3:
                    print(" 1) " + Lugar_sample[0] + "\n 2) " + Lugar_sample[1] + "\n 3) " + Lugar_sample[2] + "\n 4) " + Lugar_sample[3] + "\n 5) " + Lugar_sample[4])
                    place_P = int(input())
                    if place_P == 1:
                        if  SUS_R==0:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                        elif SUS_R==1:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                        elif SUS_R==2:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                        elif SUS_R==3:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                        elif SUS_R==4:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                    elif place_P == 2:
                        if  SUS_R==0:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==1:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                        elif SUS_R==2:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                        elif SUS_R==3:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                        elif SUS_R==4:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                    elif place_P == 3:
                        if  SUS_R==0:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                        elif SUS_R==1:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                        elif SUS_R==2:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==3:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==4:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                    elif place_P == 4:
                        if  SUS_R==0:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                        elif SUS_R==1:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==2:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                        elif SUS_R==3:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                        elif SUS_R==4:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

                    elif place_P == 5:
                        if  SUS_R==0:
                            print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==1:
                            print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                        elif SUS_R==2:
                            print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                        elif SUS_R==3:
                            print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                            print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                        elif SUS_R==4:
                            print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                            print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])
                    else:
                        print("Entrada erronea, vuelva a intentar")
                        while place_P!=(1 or 2 or 3 or 4 or 5):
                            print(" 1) " + Lugar_sample[0] + "\n 2) " + Lugar_sample[1] + "\n 3) " + Lugar_sample[2] + "\n 4) " + Lugar_sample[3] + "\n 5) " + Lugar_sample[4])
                            place_P = int(input())
                            if place_P == 1:
                                if  SUS_R==0:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[0])
                                elif SUS_R==1:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[0] + ", pero vieron a " + sospechoso[4] + " cerca del lugar, no vieron " + arma_sample[2])
                                elif SUS_R==2:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[0] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[0])
                                elif SUS_R==3:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[3])
                                elif SUS_R==4:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[0] + " y que vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[0] + " y que vieron a " + sospechoso[1] + " en el lugar, vieron " + arma_sample[1])

                            elif place_P == 2:
                                if  SUS_R==0:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==1:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[0] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[0] + " en el lugar, vieron " + arma_sample[0])
                                elif SUS_R==2:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[1] + " y que vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que vieron a " + sospechoso[4] + " en el lugar, vieron " + arma_sample[4])
                                elif SUS_R==3:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[1] + " y que no vieron a " + sospechoso[3] + " en el lugar, tampoco vieron " + arma_sample[2])
                                elif SUS_R==4:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[1] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[1] + ", pero vieron a " + sospechoso[2] + " cerca del lugar, no vieron " + arma_sample[0])

                            elif place_P == 3:
                                if  SUS_R==0:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[2] + " y que vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[2] + " en el lugar, vieron " + arma_sample[2])
                                elif SUS_R==1:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que no vieron a " + sospechoso[1] + " en el lugar, tampoco vieron " + arma_sample[3])
                                elif SUS_R==2:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[2] + ", pero vieron a " + sospechoso[0] + " cerca del lugar, no vieron " + arma_sample[3])
                                elif SUS_R==3:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==4:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[2] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[2] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[3])

                            elif place_P == 4:
                                if  SUS_R==0:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[3] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[3] + ", pero vieron a " + sospechoso[3] + " cerca del lugar, no vieron " + arma_sample[3])
                                elif SUS_R==1:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[2] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==2:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[1] + " en el lugar, no vieron " + arma_sample[2])
                                elif SUS_R==3:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[1])
                                elif SUS_R==4:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[3] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[3] + " y que no vieron a " + sospechoso[0] + " en el lugar, tampoco vieron " + arma_sample[4])

                            elif place_P == 5:
                                if  SUS_R==0:
                                    print(sospechoso[4] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[4] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==1:
                                    print(sospechoso[3] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[4] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[3] + " en el lugar, no vieron " + arma_sample[4])
                                elif SUS_R==2:
                                    print(sospechoso[2] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[1] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que no vieron a " + sospechoso[2] + " en el lugar, tampoco vieron " + arma_sample[1])
                                elif SUS_R==3:
                                    print(sospechoso[1] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[0] + " cerca de él.")
                                    print("No hay testigos asegurando haber estado en " + Lugar_sample[4] + ", pero vieron a " + sospechoso[1] + " cerca del lugar, no vieron " + arma_sample[0])
                                elif SUS_R==4:
                                    print(sospechoso[0] + " dice que estuvo en " + Lugar_sample[4] + " y que no vio " + arma_sample[2] + " cerca de él.")
                                    print("Algunos testigos aseguran haber estado en " + Lugar_sample[4] + " y que vieron a " + sospechoso[0] + " en el lugar, no vieron " + arma_sample[2])


        print("")
        print("Presione la barra espaciadora o ENTER para investigar la siguiente pista")
        msvcrt.getch()
        os.system("cls")

#Inferencia del jugador
#############################################################################################################
    print("")
    print("Haz reunido suficientes pistas para resolver el crimen, presiona una tecla para avanzar a la recta final...")
    msvcrt.getch()
    os.system("cls")

    print("Haz reunido suficientes pistas para resolver el crimen, ¿Cuál será tu conclusión?")

#Escogiendo al Culpable
#####################################################################################################
    SUS_F=int(input("El asesino fue...\n 1)Gortari\n  2)Coloso\n 3)Bob patiño\n 4)el Negro\n 5)el Blanco\n"))

    if SUS_F == 1:
        print("Haz elegido como culpable a: " + sospechoso[0])
    elif SUS_F == 2:
        print("Haz elegido como culpable a: " + sospechoso[1])
    elif SUS_F == 3:
        print("Haz elegido como culpable a: " + sospechoso[2])
    elif SUS_F == 4:
        print("Haz elegido como culpable a: " + sospechoso[3])
    elif SUS_F == 5:
        print("Haz elegido como culpable a: " + sospechoso[4])
    else:
        print("Esa es una respuesta inválida, vuelva a elegir")
        while SUS_F!=(1 or 2 or 3 or 4 or 5):
            SUS_F=int(input("El asesino fue...\n  1)Gortari\n  2)Coloso\n 3)Bob patiño\n 4)el Negro\n 5)el Blanco\n"))

            if SUS_F == 1:
                print("Haz elegido como culpable a: " + sospechoso[0])
            elif SUS_F == 2:
                print("Haz elegido como culpable a: " + sospechoso[1])
            elif SUS_F == 3:
                print("Haz elegido como culpable a: " + sospechoso[2])
            elif SUS_F == 4:
                print("Haz elegido como culpable a: " + sospechoso[3])
            elif SUS_F == 5:
                print("Haz elegido como culpable a: " + sospechoso[4])

    print("")

#Escogiendo el Arma
##########################################################################################################
    print("El arma del homicidio fue...")
    print(" 1) " + arma_sample[0] + "\n 2) " + arma_sample[1] + "\n 3) " + arma_sample[2] + "\n 4) " + arma_sample[3] + "\n 5) " + arma_sample[4])
    weap_F = int(input())

    if weap_F==1:
        print("Haz elegido como arma a: " + arma_sample[0])
    elif weap_F == 2:
        print("Haz elegido como arma a: " + arma_sample[1])
    elif weap_F==3:
        print("Haz elegido como arma a: " + arma_sample[2])
    elif weap_F==4:
        print("Haz elegido como arma a: " + arma_sample[3])
    elif weap_F == 5:
        print("Haz elegido como arma a: " + arma_sample[4])
    else:
        print("Esa es una respuesta inválida, vuelva a elegir")
        while weap_F!=(1 or 2 or 3 or 4 or 5):
            print("El arma del homicidio fue...")
            print(" 1) " + arma_sample[0] + "\n 2) " + arma_sample[1] + "\n 3) " + arma_sample[2] + "\n 4) " + arma_sample[3] + "\n 5) " + arma_sample[4])
            weap_F = int(input())

            if weap_F==1:
                print("Haz elegido como arma a: " + arma_sample[0])
            elif weap_F == 2:
                print("Haz elegido como arma a: " + arma_sample[1])
            elif weap_F==3:
                print("Haz elegido como arma a: " + arma_sample[2])
            elif weap_F==4:
                print("Haz elegido como arma a: " + arma_sample[3])
            elif weap_F == 5:
                print("Haz elegido como arma a: " + arma_sample[4])

    print("")

#Escogiendo el Lugar
##################################################################################################
    print("El lugar donde se cometió el asesinato fue...")
    print(" 1) " + Lugar_sample[0] + "\n 2) " + Lugar_sample[1] + "\n 3) " + Lugar_sample[2] + "\n 4) " + Lugar_sample[3] + "\n 5) " + Lugar_sample[4])
    place_F = int(input())

    if place_F==1:
        print("Haz elegido como lugar a: " + Lugar_sample[0])
    elif place_F==2:
        print("Haz elegido como lugar a: " + Lugar_sample[1])
    elif place_F==3:
        print("Haz elegido como lugar a: " + Lugar_sample[2])
    elif place_F==4:
        print("Haz elegido como lugar a: " + Lugar_sample[3])
    elif place_F==5:
        print("Haz elegido como lugar a: " + Lugar_sample[4])
    else:
        print("Esa es una r espuesta inválida, vuelva a elegir")
        while place_F!=(1 or 2 or 3 or 4 or 5):
            print("El lugar donde se cometió el asesinato fue...")
            print(" 1) " + Lugar_sample[0] + "\n 2) " + Lugar_sample[1] + "\n 3) " + Lugar_sample[2] + "\n 4) " + Lugar_sample[3] + "\n 5) " + Lugar_sample[4])
            place_F = int(input())

            if place_F==1:
                print("Haz elegido como lugar a: " + Lugar_sample[0])
            elif place_F==2:
                print("Haz elegido como lugar a: " + Lugar_sample[1])
            elif place_F==3:
                print("Haz elegido como lugar a: " + Lugar_sample[2])
            elif place_F==4:
                print("Haz elegido como lugar a: " + Lugar_sample[3])
            elif place_F==5:
                print("Haz elegido como lugar a: " + Lugar_sample[4])

    print("")
    print("Presione la barra espaciadora o ENTER para revelar al culpable")
    msvcrt.getch()
    os.system("cls")
#Final
###############################################################################################
    if SUS_F==1:
        sosp=0
    elif SUS_F==2:
        sosp=1
    elif SUS_F==3:
        sosp=2
    elif SUS_F==4:
        sosp=3
    else:
        sosp=4

    if weap_F==1:
        instru=0
    elif weap_F==2:
        instru=1
    elif weap_F==3:
        instru=2
    elif weap_F==4:
        instru=3
    else:
        instru=4

    if place_F==1:
        espacio=0
    elif place_F==2:
        espacio=1
    elif place_F==3:
        espacio=2
    elif place_F==4:
        espacio=3
    else:
        espacio=4

    culpable_final=sospechoso[sosp]
    arma_fianl=arma_sample[instru]
    lugar_final=Lugar_sample[espacio]

    #Mensajes personalizados
    ############################################################################################################
    if SUS_R==0:
        if place_R=="Jardín":
            mensaje_l="el jardín, ya que ambos disfrutaban estar al aire fresco de la noche."
        elif place_R=="Biblioteca":
            mensaje_l="la biblioteca, ya que ambos amaban estar rodeados de libro.s"
        elif place_R=="Oficina de la directora":
            mensaje_l="la oficina del decano, ya que " + sospechoso[SUS_R] + " insistió en conocer la nueva oficina de su amigo."
        elif place_R=="Teatro":
            mensaje_l=" el teatro, ya que los dos gustaban de ir a esos lugares."
        elif place_R=="Baño":
            mensaje_l="el baño, ya que dijo que se sentía muy mal."

        if weap_R=="Cuchillo":
            mesaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leído en un libro de había una forma de obtener un poder que va más allá de la comprensión humana, pero para ello era necesario la sangre un gran amigo. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Libro":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leido el Necronomicón, dijo que unos seres se han estado comunicando con él diciendole que le pueden dar un gran conocimiento y poder si liberase a éstas criaturas utilizando el libro y un alma de un ser querido. Una vez obtenida el alma, podría invocar a este mundo a estas criaturas y desatar el caos. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Cuerda":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que muy en el fondo de su ser, sentía envidia de todo lo que había logrado hasta entonces y que la única manera de sentirse mejor sería acabando con la existencia de éste. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Veneno":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que el conocimiento que había alcanzado era muy peligroso como para ponerlo en práctica. Al parecer, Kathya había accedido al conocimiento de los Dioses Primigeneos, lo cual si pusiese en práctica terminaría acabando con la existencia humana si así lo quisiese. " + sospechoso[SUS_R] + " le reveló a Kathya que le había puesto un tipo de veneno en su copa de vino, y que no faltaba mucho para que hiciese efecto. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Palanca":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo que había estado estudiando una misteriosa Palanca que había encontrado en uno de sus viajes a los lugares más ocultos de México. Le dijo que dicha Palanca era la llave para comunicarse con la diencion del inframundo Kathya quedó anonadada ante tal afirmación, momentos después " + sospechoso[SUS_R] + " procedió a golpearla con la palanca, para asi recojer un sacrifiicio de sangre. Al parecer la Palanca necesitaba de un sacrificio para funcionar, cosa que no le contó " + sospechoso[SUS_R] + " a Kathya. Momentos después, Kathya yacía en el suelo sin vida."

        print("Al parecer " + sospechoso[SUS_R] + " engañó a Kathya para que lo siguiera a " + mensaje_l + " " + mensaje_a)

    elif SUS_R==1:
        if place_R=="Jardín":
            mensaje_l="el jardín, ya que ambos disfrutaban estar al aire fresco de la noche."
        elif place_R=="Biblioteca":
            mensaje_l="la biblioteca, ya que ambos amaban estar rodeados de libro.s"
        elif place_R=="Oficina de la directora":
            mensaje_l="la oficina del decano, ya que " + sospechoso[SUS_R] + " insistió en conocer la nueva oficina de su amigo."
        elif place_R=="Teatro":
            mensaje_l=" el teatro, ya que los dos gustaban de ir a esos lugares."
        elif place_R=="Baño":
            mensaje_l="el baño, ya que dijo que se sentía muy mal."

        if weap_R=="Cuchillo":
            mesaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leído en un libro de había una forma de obtener un poder que va más allá de la comprensión humana, pero para ello era necesario la sangre un gran amigo. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Libro":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leido el Necronomicón, dijo que unos seres se han estado comunicando con él diciendole que le pueden dar un gran conocimiento y poder si liberase a éstas criaturas utilizando el libro y un alma de un ser querido. Una vez obtenida el alma, podría invocar a este mundo a estas criaturas y desatar el caos. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Cuerda":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que muy en el fondo de su ser, sentía envidia de todo lo que había logrado hasta entonces y que la única manera de sentirse mejor sería acabando con la existencia de éste. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Veneno":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que el conocimiento que había alcanzado era muy peligroso como para ponerlo en práctica. Al parecer, Kathya había accedido al conocimiento de los Dioses Primigeneos, lo cual si pusiese en práctica terminaría acabando con la existencia humana si así lo quisiese. " + sospechoso[SUS_R] + " le reveló a Kathya que le había puesto un tipo de veneno en su copa de vino, y que no faltaba mucho para que hiciese efecto. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Palanca":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo que había estado estudiando una misteriosa Palanca que había encontrado en uno de sus viajes a los lugares más ocultos de México. Le dijo que dicha Palanca era la llave para comunicarse con la diencion del inframundo Kathya quedó anonadada ante tal afirmación, momentos después " + sospechoso[SUS_R] + " procedió a golpearla con la palanca, para asi recojer un sacrifiicio de sangre. Al parecer la Palanca necesitaba de un sacrificio para funcionar, cosa que no le contó " + sospechoso[SUS_R] + " a Kathya. Momentos después, Kathya yacía en el suelo sin vida."

        print("Al parecer " + sospechoso[SUS_R] + " engañó a Kathya para que lo siguiera a " + mensaje_l + " " + mensaje_a)
    elif SUS_R==2:
        if place_R=="Jardín":
            mensaje_l="el jardín, ya que ambos disfrutaban estar al aire fresco de la noche."
        elif place_R=="Biblioteca":
            mensaje_l="la biblioteca, ya que ambos amaban estar rodeados de libro.s"
        elif place_R=="Oficina de la directora":
            mensaje_l="la oficina del decano, ya que " + sospechoso[SUS_R] + " insistió en conocer la nueva oficina de su amigo."
        elif place_R=="Teatro":
            mensaje_l=" el teatro, ya que los dos gustaban de ir a esos lugares."
        elif place_R=="Baño":
            mensaje_l="el baño, ya que dijo que se sentía muy mal."

        if weap_R=="Cuchillo":
            mesaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leído en un libro de había una forma de obtener un poder que va más allá de la comprensión humana, pero para ello era necesario la sangre un gran amigo. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Libro":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leido el Necronomicón, dijo que unos seres se han estado comunicando con él diciendole que le pueden dar un gran conocimiento y poder si liberase a éstas criaturas utilizando el libro y un alma de un ser querido. Una vez obtenida el alma, podría invocar a este mundo a estas criaturas y desatar el caos. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Cuerda":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que muy en el fondo de su ser, sentía envidia de todo lo que había logrado hasta entonces y que la única manera de sentirse mejor sería acabando con la existencia de éste. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Veneno":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que el conocimiento que había alcanzado era muy peligroso como para ponerlo en práctica. Al parecer, Kathya había accedido al conocimiento de los Dioses Primigeneos, lo cual si pusiese en práctica terminaría acabando con la existencia humana si así lo quisiese. " + sospechoso[SUS_R] + " le reveló a Kathya que le había puesto un tipo de veneno en su copa de vino, y que no faltaba mucho para que hiciese efecto. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Palanca":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo que había estado estudiando una misteriosa Palanca que había encontrado en uno de sus viajes a los lugares más ocultos de México. Le dijo que dicha Palanca era la llave para comunicarse con la diencion del inframundo Kathya quedó anonadada ante tal afirmación, momentos después " + sospechoso[SUS_R] + " procedió a golpearla con la palanca, para asi recojer un sacrifiicio de sangre. Al parecer la Palanca necesitaba de un sacrificio para funcionar, cosa que no le contó " + sospechoso[SUS_R] + " a Kathya. Momentos después, Kathya yacía en el suelo sin vida."

        print("Al parecer " + sospechoso[SUS_R] + " engañó a Kathya para que lo siguiera a " + mensaje_l + " " + mensaje_a)
    elif SUS_R==3:
        if place_R=="Jardín":
            mensaje_l="el jardín, ya que ambos disfrutaban estar al aire fresco de la noche."
        elif place_R=="Biblioteca":
            mensaje_l="la biblioteca, ya que ambos amaban estar rodeados de libro.s"
        elif place_R=="Oficina de la directora":
            mensaje_l="la oficina del decano, ya que " + sospechoso[SUS_R] + " insistió en conocer la nueva oficina de su amigo."
        elif place_R=="Teatro":
            mensaje_l=" el teatro, ya que los dos gustaban de ir a esos lugares."
        elif place_R=="Baño":
            mensaje_l="el baño, ya que dijo que se sentía muy mal."

        if weap_R=="Cuchillo":
            mesaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leído en un libro de había una forma de obtener un poder que va más allá de la comprensión humana, pero para ello era necesario la sangre un gran amigo. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Libro":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leido el Necronomicón, dijo que unos seres se han estado comunicando con él diciendole que le pueden dar un gran conocimiento y poder si liberase a éstas criaturas utilizando el libro y un alma de un ser querido. Una vez obtenida el alma, podría invocar a este mundo a estas criaturas y desatar el caos. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Cuerda":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que muy en el fondo de su ser, sentía envidia de todo lo que había logrado hasta entonces y que la única manera de sentirse mejor sería acabando con la existencia de éste. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Veneno":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que el conocimiento que había alcanzado era muy peligroso como para ponerlo en práctica. Al parecer, Kathya había accedido al conocimiento de los Dioses Primigeneos, lo cual si pusiese en práctica terminaría acabando con la existencia humana si así lo quisiese. " + sospechoso[SUS_R] + " le reveló a Kathya que le había puesto un tipo de veneno en su copa de vino, y que no faltaba mucho para que hiciese efecto. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Palanca":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo que había estado estudiando una misteriosa Palanca que había encontrado en uno de sus viajes a los lugares más ocultos de México. Le dijo que dicha Palanca era la llave para comunicarse con la diencion del inframundo Kathya quedó anonadada ante tal afirmación, momentos después " + sospechoso[SUS_R] + " procedió a golpearla con la palanca, para asi recojer un sacrifiicio de sangre. Al parecer la Palanca necesitaba de un sacrificio para funcionar, cosa que no le contó " + sospechoso[SUS_R] + " a Kathya. Momentos después, Kathya yacía en el suelo sin vida."

        print("Al parecer " + sospechoso[SUS_R] + " engañó a Kathya para que lo siguiera a " + mensaje_l + " " + mensaje_a)
    else:
        if place_R=="Jardín":
            mensaje_l="el jardín, ya que ambos disfrutaban estar al aire fresco de la noche."
        elif place_R=="Biblioteca":
            mensaje_l="la biblioteca, ya que ambos amaban estar rodeados de libro.s"
        elif place_R=="Oficina de la directora":
            mensaje_l="la oficina del decano, ya que " + sospechoso[SUS_R] + " insistió en conocer la nueva oficina de su amigo."
        elif place_R=="Teatro":
            mensaje_l=" el teatro, ya que los dos gustaban de ir a esos lugares."
        elif place_R=="Baño":
            mensaje_l="el baño, ya que dijo que se sentía muy mal."

        if weap_R=="Cuchillo":
            mesaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leído en un libro de había una forma de obtener un poder que va más allá de la comprensión humana, pero para ello era necesario la sangre un gran amigo. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Libro":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que había leido el Necronomicón, dijo que unos seres se han estado comunicando con él diciendole que le pueden dar un gran conocimiento y poder si liberase a éstas criaturas utilizando el libro y un alma de un ser querido. Una vez obtenida el alma, podría invocar a este mundo a estas criaturas y desatar el caos. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Cuerda":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que muy en el fondo de su ser, sentía envidia de todo lo que había logrado hasta entonces y que la única manera de sentirse mejor sería acabando con la existencia de éste. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Veneno":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo a Kathya que el conocimiento que había alcanzado era muy peligroso como para ponerlo en práctica. Al parecer, Kathya había accedido al conocimiento de los Dioses Primigeneos, lo cual si pusiese en práctica terminaría acabando con la existencia humana si así lo quisiese. " + sospechoso[SUS_R] + " le reveló a Kathya que le había puesto un tipo de veneno en su copa de vino, y que no faltaba mucho para que hiciese efecto. Momentos después, Kathya yacía en el suelo sin vida."
        elif weap_R=="Palanca":
            mensaje_a="Una vez en el lugar, " + sospechoso[SUS_R] + " le dijo que había estado estudiando una misteriosa Palanca que había encontrado en uno de sus viajes a los lugares más ocultos de México. Le dijo que dicha Palanca era la llave para comunicarse con la diencion del inframundo Kathya quedó anonadada ante tal afirmación, momentos después " + sospechoso[SUS_R] + " procedió a golpearla con la palanca, para asi recojer un sacrifiicio de sangre. Al parecer la Palanca necesitaba de un sacrificio para funcionar, cosa que no le contó " + sospechoso[SUS_R] + " a Kathya. Momentos después, Kathya yacía en el suelo sin vida."

        print("Al parecer " + sospechoso[SUS_R] + " engañó a Kathya para que lo siguiera a " + mensaje_l + " " + mensaje_a)

    #Mensaje de victoria o derrota
    #############################################################################################################################################
    print("")
    if (culpable_final==sospechoso[SUS_R]) and (arma_fianl==weap_R) and (lugar_final==place_R):
        print("Felicidades, has encontrado al culpable y los policías lo han detenido antes de que escapase")
    else:
        print("No todas tus pistas han sido correctas, por lo que el culpable se ha ido del lugar")
#Bucle
##############################################################################################
    print("")
    ciclo = int(input("Presione 1 y después ENTER para volver a jugar\nPresoine cualquier otro numero y después ENTER para salir. "))