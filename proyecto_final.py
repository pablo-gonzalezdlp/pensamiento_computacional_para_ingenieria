#Programa Final: Programa diseñado para ayudar a los usuarios a aprender
#conceptos y mejorar sus conocimientos en la materia de Ciencias de la
#Salud con una evaluación inicial y final, al igual que con un
#memorama para hacerlo de manera más dinámica

#Pablo González de la Parra - (A01745096)

#Importando archivo de texto con las preguntas del programa
miArc = open("preguntas_finales.txt", "r", encoding="utf8")

#Definiendo las listas globales
incorrectas = []
incorrectas2 = []

#Función que despliega un mensaje de bienvenida al usuario
def bienvenida():
    print(
    "---------------------------------------------------------------------"\
    "-----------------------------"\
    "-----------------------------------------------------\n"\
    "Bienvenidos, \n"\
    "Este programa está diseñado con el fin de ayudar a las personas a "\
    "aprender distintos temas de una manera efectiva, fácil y dinámica \n"\
    "para no solo poder adquirir y reforzar sus conocimientos pasados, "\
    "sino también para poder presentar y aprobar la prueba PISA y "\
    "representar a México.\nA continuación se mostrarán una serie de 15 "\
    "preguntas de la materia de Ciencias de la Salud, "\
    "tomando como referencia preguntas de evaluaciones pasadas\n"\
    "que nos ayudarán a poder determinar su nivel de aprendizaje, "\
    "al igual que esos temas que se le dificulten.\n"\
    "-----------------------------------------------------------------------"\
    "---------------------------"\
    "-----------------------------------------------------")
    conti = int(input("\nPara continuar presione 1: "))
    
    if conti==1:
        return conti
    
    else:
        print("\nInicia cuando estes listo\n")
        preguntas()

#Función que despliega las 15 preguntas de la evaluación final
def preguntas():
    
    #Llamando a la lista global
    global incorrectas 
    
    c = bienvenida()
    if c == 1:
        
        #Pregunta 1
        print("\nPregunta 1:\n",miArc.readline())      
        print("a) 340 \nb) 200 \nc) 300  \nd) 208 \ne) 206 ")
        
        r1=input("\nIngresa el inciso que consideres correcto: ")
        
        if r1 == "c":
            print("Tu respuesta es correcta")
        
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p1")

            
        #Pregunta 2
        print("\nPregunta 2:\n", miArc.readline())     
        print("a) cien billones \nb) cien millones \nc) "\
              "mil billones \nd) treinta millones \ne) cien trillones ")
        
        r2=input("\nIngresa el inciso que consideres correcto: ")
        
        if r2 == "a":
            print("Tu respuesta es correcta")
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p2")
        
        #Pregunta 3
        print("\nPregunta 3:\n",miArc.readline())
              
        print("a) 208 \nb) 228 \nc) 215 \nd) 230 \ne) 218 ")
        
        r3=input("\nIngresa el inciso que consideres correcto: ")
        
        if r3 == "d":
            print("Tu respuesta es correcta")
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p3")
        
        #Pregunta 4
        print("\nPregunta 4 \n",miArc.readline())
              
        print("a) raquis \nb) estribo \nc) frontal \n"\
                    "d) clavícula \ne) humero ")
        
        r4=input("\nIngresa el inciso que consideres correcto: ")
        
        if r4 == "b":
            print("Tu respuesta es correcta")
 
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p4")
        
        #Pregunta 5
        print("\nPregunta 5 \n",miArc.readline())
              
        print("a) nasal \nb) temporal \nc) tibia \n"\
              "d) falanjes \ne) fémur ")
        
        r5=input("\nIngresa el inciso que consideres correcto: ")
        
        if r5 == "e":
            print("Tu respuesta es correcta")
 
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p5")
        
        #Pregunta 6
        print("\nPregunta 6 \n",miArc.readline())
              
        print("a) huesos \nb) intestino \nc) pancreás \nd) higado \n"\
        "e) sistema nervioso ")
        
        r6=input("\nIngresa el inciso que consideres correcto: ")
        
        if r6 == "c":
            print("Tu respuesta es correcta")
           
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p6")
              
        #Pregunta 7
        print("\nPregunta 7 \n",miArc.readline())
              
        print("a) infección urinaria \nb) diabetes \nc) asma \n"\
              "d) Obesidad \ne) sinusitis ")
        
        r7=input("\nIngresa el inciso que consideres correcto: ")
        
        if r7 == "b":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p7")
        
        #Pregunta 8
        print("\nPregunta 8 \n",miArc.readline())
              
        print("a) membrana celular \nb) citoplasma \n"\
        "c) reticulo endoplásmico \nd) ribosomas \ne) mitocondria ")
        
        r8=input("\nIngresa el inciso que consideres correcto: ")
        
        if r8 == "e":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p8")
        
        #Pregunta 9
        print("\nPregunta 9 \n",miArc.readline())
              
        print("a) hemoglobina \nb) celulas de defensa \n"\
              "c) sodio \nd) potasio \ne) leucocitos ")
        
        r9=input("\nIngresa el inciso que consideres correcto: ")
        
        if r9 == "a":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p9")
        
        #Pregunta 10
        print("\nPregunta 10 \n",miArc.readline())
              
        print("a) hemoglobina \nb) vitaminas \nc) grasas \nd)"\
              "glucosa \ne) proteinas ")
        
        r10=input("\nIngresa el inciso que consideres correcto: ")
        
        if r10 == "d":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p10")
         
        #Pregunta 11
        print("\nPregunta 11 \n",miArc.readline())
              
        print("a) exceso de azucares \nb) falta de fibra y agua \n"\
              "c) falta de fibra y azucar \nd) exceso de fibra \n"\
              "e) exceso de ejercicio ")
        
        r11=input("\nIngresa el inciso que consideres correcto: ")
        
        if r11 == "b":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p11")
         
        #Pregunta 12
        print("\nPregunta 12 \n",miArc.readline())
              
        print("a) traquea \nb) pleura \nc) alveolos \n"\
              "d) bronquios \ne) laringe ")
        
        r12=input("\nIngresa el inciso que consideres correcto: ")
        
        if r12 == "c":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p12")
          
        #Pregunta 13
        print("\nPregunta 13 \n",miArc.readline())
              
        print("a) Cerebro \nb) intestinos \nc) pulmones \n"\
              "d) corazón \ne) piel ")
        
        r13=input("\nIngresa el inciso que consideres correcto: ")
        
        if r13 == "e":
            print("Tu respuesta es correcta")
           
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p13")
         
        #Pregunta 14
        print("\nPregunta 14 \n",miArc.readline())
              
        print("a) una auricula y dos ventriculos \n"\
              "b) dos auriculas y dos ventriculos \n"\
              "c) tres auriculas y un ventriculo \n"\
              "d) un auricula y un ventriculo \n"\
              "e) cuatro auriculas ")
        
        r14=input("\nIngresa el inciso que consideres correcto: ")
        
        if r14 == "b":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p14")
              
        #Pregunta 15
        print("\nPregunta 15 \n",miArc.readline())
              
        print("a) estrogenos \nb) testosterona \n"\
              "c) insulina \nd) hormona tiroidea \ne) somatropina ")
        
        r15=input("\nIngresa el inciso que consideres correcto: ")
              
        if r15 == "d":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas.append("p15")

#Función que despliega el memorama al igual que el promedio
#y calificación del test inicial
def memorama():
    
    #Llamando a la lista global
    global incorrectas 
    tam = len(incorrectas)
    prom = ((15-tam)/15)*10
    
    #Mensaje personalizado de acuerdo a la califiación del usuario
    if tam >= 0:
        print(f"\nTuviste {tam} preguntas incorrectas de 15. "\
              f"Tu promedio es de {round(prom,2)}")
        
        if tam >=7:
            print("No aprobaste el examen inicial, pero no te preocupes. "\
                  "¡Sigue intentándolo!")
        else:
            print("¡Felicidades, aprobaste el exámen!")
            
        #Instrucciones del memorama y parámetros
        print(
            "\n--------------------------------------------------------------"\
            "------------------------------------"\
            "-----------------------------------------------------\n"\
            "¡Muy bien!\n"\
            "Después del examen inicial ahora jugarás un memorama para reforzar "\
            "tus conocimientos e intentar mejorar tu calificación.\n"\
            "Primero escogerás una fila (con una letra) y después una columna "\
            "(con un número). "\
            "Cada cuadro tiene una pregunta escondida.\n"\
            "Elige cualquier cuadrado dentro del memorama y cuando aparezca "\
            "podrás intentar encontrar la respuesta correcta. \nSi la tienes "\
                "bien se eliminará "\
            "el inciso del memorama. Una vez que hayas encontrado todas las "\
            "respuestas correctas, \n"
            "habrás ganado y podrás avanzar a la siguiente parte.\n"\
            "Nota: Las respuestas deben ser ingresadas sin acentos y con minúsculas.\n"\
            "------------------------------------------------------------------"\
            "--------------------------------"\
            "-----------------------------------------------------\n")
        
        #Lista de preguntas
        lista =  [miArc.readline(), miArc.readline(), miArc.readline(), \
                  miArc.readline(), miArc.readline()]
        lista2 = [miArc.readline(), miArc.readline(), miArc.readline(), \
                  miArc.readline(), miArc.readline()]
        lista3 = [miArc.readline(), miArc.readline(), miArc.readline(), \
                  miArc.readline(), miArc.readline()]
        
        #Lista que se muestra al usuario
        list1 = [0,1,2,3,4]
        list2 = [0,1,2,3,4]
        list3 = [0,1,2,3,4]

        #Lista de respuestas del memorama
        anslis  = ["300","bulimia","diabetes","piel","estribo"]
        anslis2 = ["alveolos","auriculas y ventriculos","sistole y diastole","4","boca"]
        anslis3 = ["hemoglobina","2","pancreas","230","mitocondria"]

        #contador
        cont = 15

        while cont >0:
            
            print("     MEMORAMA\n")
            print("A", list1)
            print("B", list2)
            print("C", list3)

            f = (input("\nQue letra de pregunta quieres responder?: "))
            r = int(input("Cual quieres responder?: "))
            
    
            if r <=4 and f.upper()=="A":
                
                print("\n", lista[r])
                
                ans = input("Respuesta: ")
        
                if ans==anslis[r]:
            
                    print("¡Muy bien!\n")
                    list1[r] = '-'
                    cont = cont-1
                else:
                    print("La respuesta es incorrecta. Inténtalo de Nuevo.\n")
                
            if r <=4 and f.upper()=="B":
        
                print("\n", lista2[r])
                
                ans = input("Respuesta: ")
        
                if ans==anslis2[r]:
            
                    print("¡Muy bien!\n")
                    list2[r] = "-"
                    cont = cont-1
            
                else:
                    print("La respuesta es incorrecta. Inténtalo de Nuevo.\n")
            
            if r <=4 and f.upper()=="C":
                
                print("\n", lista3[r])
                
                ans = input("Respuesta: ")
        
                if ans==anslis3[r]:
            
                    print("¡Muy bien!\n")
                    list3[r] = "-"
                    cont = cont-1
            
                else:
                    print("La respuesta es incorrecta. Inténtalo de Nuevo.\n")
        
        
#Función que muestra la última evaluación al igual que las
#preguntas incorrectas del primer test, cantidad de errores, y promedio final               
def evaluacionFinal():
    print("¡Felicidades! Acabaste el memorama. "\
          "Estás listo para terminar tu aprendizaje")
    
    #Llamando a las listas globales
    global incorrectas
    global incorrectas2
    
    #Instrucciones de la evaluación final
    print(
        "\n---------------------------------------------------------------"\
        "-----------------------------------"\
        "-----------------------------------------------------\n"\
        "¡Muy bien!\n"\
        "Ahora que acabaste de estudiar, memorizar y practicar algunos "\
        "temas importantes "\
        "se te realizará una evaluación final\npara comprobar tu aprendizaje "\
            "durante este programa. "\
        "Se te mostrarán las preguntas que tuviste incorrectas en el primer test.\n"\
        "El promedio final se evaluará con las preguntas que tengas bien "\
            "ahorita con las del principio.\n"\
        "Intenta concentrate y dar tu mejor esfuerzo. ¡Mucha suerte!"
        "\n----------------------------------------------------------------"\
        "----------------------------------"\
        "-----------------------------------------------------\n")
    
    preg1=miArc.readline()
    if "p1" in incorrectas:
    #Pregunta 1
        print("Pregunta 1:\n",preg1)      
        print("a) 340 \nb) 200 \nc) 300  \nd) 208 \ne) 206 ")
        
        r1=input("\nIngresa el inciso que consideres correcto: ")
        
        if r1 == "c":
            print("Tu respuesta es correcta")
        
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p1")
   
    preg2=miArc.readline()
    if "p2" in incorrectas:
    #Pregunta 2
        print("\nPregunta 2:\n", preg2)     
        print("a) cien billones \nb) cien millones \nc) mil billones \n"\
              "d) treinta millones \ne) cien trillones ")
        
        r2=input("\nIngresa el inciso que consideres correcto: ")
        
        if r2 == "a":
            print("Tu respuesta es correcta")
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p2")
        
    preg3=miArc.readline()
    if "p3" in incorrectas:
    #Pregunta 3
        print("\nPregunta 3:\n",preg3)
              
        print("a) 208 \nb) 228 \nc) 215 \nd) 230 \ne) 218 ")
        
        r3=input("\nIngresa el inciso que consideres correcto: ")
        
        if r3 == "d":
            print("Tu respuesta es correcta")
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p3")
        
    preg4=miArc.readline()
    if "p4" in incorrectas:
    #Pregunta 4
        print("\nPregunta 4 \n",preg4)
              
        print("a) raquis \nb) estribo \nc) frontal \nd) clavícula \ne) humero ")
        
        r4=input("\nIngresa el inciso que consideres correcto: ")
        
        if r4 == "b":
            print("Tu respuesta es correcta")
 
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p4")
            
    preg5=miArc.readline()
    if "p5" in incorrectas:
    #Pregunta 5
        print("\nPregunta 5 \n",preg5)
              
        print("a) nasal \nb) temporal \nc) tibia \nd) falanjes \ne) fémur ")
        
        r5=input("\nIngresa el inciso que consideres correcto: ")
        
        if r5 == "e":
            print("Tu respuesta es correcta")
 
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p5")
        
    preg6=miArc.readline()
    if "p6" in incorrectas:
    #Pregunta 6
        print("\nPregunta 6 \n",preg6)
              
        print("a) huesos \nb) intestino \nc) pancreás \n"\
              "d) higado \ne) sistema nervioso ")
        
        r6=input("\nIngresa el inciso que consideres correcto: ")
        
        if r6 == "c":
            print("Tu respuesta es correcta")
           
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p6")
              
    preg7=miArc.readline()
    if "p7" in incorrectas:
    #Pregunta 7
        print("\nPregunta 7 \n",preg7)
              
        print("a) infección urinaria \nb) diabetes \nc) asma \n"\
              "d) Obesidad \ne) sinusitis ")
        
        r7=input("\nIngresa el inciso que consideres correcto: ")
        
        if r7 == "b":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p7")
        
    preg8=miArc.readline()
    if "p8" in incorrectas:
    #Pregunta 8
        print("\nPregunta 8 \n",preg8)
              
        print("a) membrana celular \nb) citoplasma \n"\
              "c) reticulo endoplásmico \nd) ribosomas \ne) mitocondria ")
        
        r8=input("\nIngresa el inciso que consideres correcto: ")
        
        if r8 == "e":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p8")
    
    preg9=miArc.readline()
    if "p9" in incorrectas:
    #Pregunta 9
        print("\nPregunta 9 \n",preg9)
              
        print("a) hemoglobina \nb) celulas de defensa \n"\
              "c) sodio \nd) potasio \ne) leucocitos ")
        
        r9=input("\nIngresa el inciso que consideres correcto: ")
        
        if r9 == "a":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p9")
        
    preg10=miArc.readline()
    if "p10" in incorrectas:
    #Pregunta 10
        print("\nPregunta 10 \n",preg10)
              
        print("a) hemoglobina \nb) vitaminas \nc) grasas \n"\
              "d) glucosa \ne) proteinas ")
        
        r10=input("\nIngresa el inciso que consideres correcto: ")
        
        if r10 == "d":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p10")
         
    preg11=miArc.readline()
    if "p11" in incorrectas:
    #Pregunta 11
        print("\nPregunta 11 \n",preg11)
              
        print("a) exceso de azucares \nb) falta de fibra y agua \n"\
              "c) falta de fibra y azucar \nd) exceso de fibra \n"\
              "e) exceso de ejercicio ")
        
        r11=input("\nIngresa el inciso que consideres correcto: ")
        
        if r11 == "b":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p11")
         
    preg12=miArc.readline()
    if "p12" in incorrectas:
    #Pregunta 12
        print("\nPregunta 12 \n",preg12)
              
        print("a) traquea \nb) pleura \nc) alveolos \n"\
              "d) bronquios \ne) laringe ")
        
        r12=input("\nIngresa el inciso que consideres correcto: ")
        
        if r12 == "c":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p12")
        
    preg13=miArc.readline()
    if "p13" in incorrectas:
    #Pregunta 13
        print("\nPregunta 13 \n",preg13)
              
        print("a) Cerebro \nb) intestinos \nc) pulmones \n"\
              "d) corazón \ne) piel ")
            
        r13=input("\nIngresa el inciso que consideres correcto: ")
        
        if r13 == "e":
            print("Tu respuesta es correcta")
           
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p13")
    
    preg14=miArc.readline()
    if "p14" in incorrectas:
    #Pregunta 14
        print("\nPregunta 14 \n",preg14)
              
        print("a) una auricula y dos ventriculos \n"\
              "b) dos auriculas y dos ventriculos \n"\
              "c) tres auriculas y un ventriculo \n"\
              "d) un auricula y un ventriculo \ne) cuatro auriculas ")
        
        r14=input("\nIngresa el inciso que consideres correcto: ")
        
        if r14 == "b":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p14")
    
    preg15=miArc.readline()
    if "p15" in incorrectas:
    #Pregunta 15
        print("\nPregunta 15 \n",preg15)
              
        print("a) estrogenos \nb) testosterona \nc) insulina \n"\
              "d) hormona tiroidea \ne) somatropina ")
        
        r15=input("\nIngresa el inciso que consideres correcto: ")
              
        if r15 == "d":
            print("Tu respuesta es correcta")
            
        else:
            print("Tu respuesta es incorrecta")
            incorrectas2.append("p15")

    
    tam2 = len(incorrectas2)
    
    #Promedio Final de las evaluaciones
    promfin = ((15-tam2)/15)*10

    #Mensaje de felicitaciones
    print("\nFelicidades, has acabado el examen!")
     
    #Mensaje personalizado de acuerdo a la califiación
    #obtenida en la evaluación final
    if promfin <= 6:    
        print(f"\nTuviste todavia {tam2} preguntas incorrectas. "\
              f"Esto te da un promedio de {round(promfin,2)}. "\
              "Te recomendamos mucho intentar repetir el curso "\
              "para sacar una mejor calificación\n")
        
    else:
        print("Estás listo para aprobar ese examen. Muchas felicidades!")
     
    #Mensaje final/despedida
    print(
        "\n------------------------------------------------------------"\
      "--------------------------------------"\
        "-----------------------------------------------------\n"\
        "Bueno,\n"
        "¡Muchas gracias por cursar este programa! Esperemos que los "\
            "haya ayudado a mejorar un poco "\
        "en el área de Ciencias de la Salud.\nDe parte del equipo "\
        "responsable les deseamos "\
        "mucha suerte en cualquier prueba futura sobre estos temas. ¡Saludos!\n"
        "Créditos:\n- Valeria Martinez\n- Maritta Vega\n- Pablo González"
        "\n-------------------------------------------------------------"\
        "-------------------------------------"\
        "-----------------------------------------------------\n")

#Llamando a las funciones correspondientes
preguntas()
memorama()
evaluacionFinal()