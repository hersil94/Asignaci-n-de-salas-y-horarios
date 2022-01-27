#Distribución de salas, horarios y alumnos

#Este programa crea horarios de clases e inscribe alumnos en ellos a partir
#de tres archivos de texto, "salas.txt", "alumnos.txt" y "areas.txt" cada uno
#cumpliendo con el formato proporcionado en el informe adjunto.


#Los alcances del programa solo cubren un día, dado que no se proporcionó ninguna información
#sobre cuantos días o cuantas horas de cada ramo debería impartirse por sección.
#Si se requiere se puede copiar el horario de ese día en otros días, o bien, pueden
#proporcionarse por separado archivos con información para diferentes días y ejecutar
#el programa varias veces, sin embargo los archivos de salida resultantes de cada ejecución
#DEBEN ser respaldados o cambiar el nombre de estos, de otra forma estos archivos serán reescritos en cada
#ejecución del programa, resultado solo la información requerida para el último día
#otra indicación importante sería que cada ejecución entrega como dato de salida un archivo de alumnos que no
#pudieron inscribir algún ramo con el mismo formato que el archivo de entrada, por lo que la salida de una ejecución(n)
#podría eventualmente considerarse como la entrada de una ejecución(n+1).

#El programa es plenamente funcional en la medida de que los datos proporcionados sean
#consistentes con el formato indicado en el informe adjunto,
#que los alumnos estén intentando tomar ramos que existan dentro del archivo "areas",
#así como también que la escritura de los archivos de entrada sea la especificada en el informe
#adjunto, es decir que cada elemento de los archivos esté separado únicamente por comas (",")

## Autor: GRUPO 3 Laboratorio de fundamentos de programación, sección ????, Usach (Hernán Silva)
## Versión 1.13
## Fecha:19/11/2019


###Importación de funciones###

#No se usa ninguna función importada.
#inicialmente se importó la función mode del módulo statistics, sin embargo durante el desarrollo se
#evidenció que la función mode solo funcionaba para modas únicas, por lo que se terminó creando una 
#función para el cálculo de modas que admitiese mas de una moda



###Importación de constantes###

#No se importó ninguna constante



##### BLOQUE DE FUNCIONES #####


##Función que pide al usuario ingresar el número de alumnos por sala
#este debe ser un número natural, se valida que así sea, si no se ha
#ingresado un número natural, se informa al usuario y se vuelve a solicitar un número
#entrada: numero natural ingresado por el usuario                                                                      #DUDA ACÁAA
#salida: un numero natural ingresado por el usuario que haya sido validado
def ingresarNumero():
    num=input("Ingrese el número de alumnos por sala como número natural: ")
    condicion=num.isdigit() #la condición es que el valor ingresado solo tenga caracteres numéricos
    if condicion==False:
        print("No ha ingresado un número natural")#si la condición no se cumple se avisa al usuario
        num=ingresar() #si la condición no se cumple se vuelve a solicitar un número natural
    
            
    num=int(num) #si el valor solo tiene caracteres numéricos se convierte a int
    if num==0: # si el número es igual a 0 se vuelve a pedir un número natural
        print("El 0 no es un número natural, ingrese un número natural:")
        num=ingresar()
    print("Ha ingresado un número válido.") #si el número pasa todas las condiciones
    #es un número apto para el programa y se le informa al usuario que se ingresó correctamente
    print(" ") #se imprime una línea vacía para diferenciar esta función de los valores imprimidos en la salida del programa
       
    return num

        

##Función para leer el archivo de alumnos y pasarlo a lista
#cada fila del texto es un elemento de la lista
#entrada:ninguna ???                                                                                                    #DUDA ACÁAA
#salida:una lista donde cada elemento es una de las líneas del archivo de texto "alumnos.txt"
def leerAlumnos():
    archivo=open("alumnos.txt","r")
    lista=[]
    for linea in archivo:
        lista.append(linea)
    archivo.close()
    
    
    return lista

##Función para contar la cantidad de alumnos
#cada fila del archivo es un alumno
#entrada=lista de lineas de archivo "alumnos" [fila1,fila2,fila3,...], cada fila es un string
#salida= la cantidad de alumnos como número entero
def contarAlumnos():
    archivo=open("alumnos.txt","r")
    lineas=0
    for linea in archivo:
        lineas=lineas+1
    archivo.close()
    
    return lineas

##Función para leer el archivo de áreas y pasarlo a lista
#cada fila del texto es un elemento de la lista
#entrada:ninguna
#salida:una lista donde cada elemento es una de las líneas del archivo de texto "areas.txt"
def leerAreas():
    archivo=open("areas.txt","r")
    lista=[]
    for linea in archivo:
        lista.append(linea)
    archivo.close()
    return lista

##Función para contar la cantidad de áreas
#cada fila del archivo es una área
#entrada=lista de lineas de archivo "Areas" [fila1,fila2,fila3,...] cada fila es un string
#salida= la cantidad de áreas como número entero
def contarAreas():
    archivo=open("areas.txt","r")
    lineas=0
    for linea in archivo:
        lineas=lineas+1
    archivo.close()
    return lineas    

##Función para leer el archivo de salas y pasarlo a lista
#cada fila del texto es un elemento de la lista
#entrada:ninguna
#salida:una lista donde cada elemento es una de las líneas del archivo de texto "salas.txt"
def leerSalas():
    archivo=open("salas.txt","r")
    lista=[]
    for linea in archivo:
        lista.append(linea)
    archivo.close()
    return lista

#Función para contar la cantidad de salas
#cada fila del archivo es una sala
#entrada=lista de lineas de archivo "salas" [fila1,fila2,fila3,...] cada fila es un string
#salida= la cantidad de salas como número entero
def contarSalas():
    archivo=open("salas.txt","r")
    lineas=0
    for linea in archivo:
        lineas=lineas+1
    archivo.close()
    return lineas

##Función que construye una matriz de alumnos y sus solicitudes
#entrada=lista de lineas de archivo "alumnos" [fila1,fila2,fila3,...]
#salida= una lista de listas [alumno1,ramo1,ramo2],[alumno2,ramo3,ramo4],[alumno3,ramo1,ramo4,ramo5]
def crearMatrizAlumnos(listaAlumnos):
    matriz=[]
    for elemento in listaAlumnos:
        nuevoElemento=elemento.split(",")#se convierte cada fila en lista
        limpios=[] #se crea una lista vacía para poner los valores sin salto de línea
        for ramo in nuevoElemento:
            limpio=ramo.strip(("\n")) #se limpia los elementos de las sublistas para no dejar el salto de línea
            
            limpios.append(limpio) #se agregan los strings limpios a la sublista
        matriz.append(limpios) #se agrega cada sublista limpia a una lista de listas
    
    return matriz


##Función que construye una matriz de areas y sus respectivos ramos
#entrada=lista de lineas de archivo "areas" [fila1,fila2,fila3,...]
#salida= una lista de listas [area1,ramo1,ramo2],[area2,ramo3,ramo4],[area3,ramo1,ramo4,ramo5]
def crearMatrizAreas(listaAreas):
    matriz=[]
    for elemento in listaAreas:
        nuevoElemento=elemento.split(",")#se convierte cada fila en lista
        limpios=[]#se crea una lista vacía para poner los valores sin salto de línea
        for ramo in nuevoElemento:
            limpio=ramo.strip(("\n")) #se limpia los elementos de las sublistas para no dejar el salto de línea
            limpios.append(limpio) #se agregan los strings limpios a la sublista
        matriz.append(limpios) #se agrega cada sublista limpia a una lista de listas
    return matriz

##Función que construye una matriz de salas y sus horarios
#entrada=lista de lineas de archivo "salas" [fila1,fila2,fila3,...]
#salida= una lista de listas [sala1,hora1,hora2],[sala2,hora3,hora4],[sala3,hora5,hora6,hora7]
def crearMatrizSalas(listaSalas):
    matriz=[]
    for elemento in listaSalas:
        nuevoElemento=elemento.split(",")#se convierte cada fila en lista
        limpios=[]#se crea una lista vacía para poner los valores sin salto de línea
        for ramo in nuevoElemento:
            limpio=ramo.strip(("\n")) #se limpia los elementos de las sublistas para no dejar el salto de línea
            limpios.append(limpio) #se agregan los strings limpios a la sublista
        matriz.append(limpios) #se agrega cada sublista limpia a una lista de listas
       
    return matriz


##Funcion que cuenta el total de ramos, haciendo una matriz con la informacion de las áreas
#pero sin contar el primer elemento de cada fila, ya que corresponde al nombre del área y no a una asignatura
#entrada:la matriz de ramos[area1,ramo1,ramo2...][area2,ramo3,ramo4...][area3,ramo5,ramo6,ramo7..]...
#salida: el número de ramos ingresados en el archivo de áreas como número entero
def contarRamos(ramos):
    total=0
    
    for area in ramos:
        for asignatura in area: #se suma la cantidad de elementos de cada area [area1,ramo1,ramo2,ramo3...]
            total=total+1
    for area in ramos:
        total=total-1 #se descuenta una unidad por área, ya que el primer elemento de cada área es el nombre de la misma
    return total

    
        
        
#Función que construye una lista con las solicitudes de los alumnos
#entrada: lista de listas, [[alumno1,ramo1,ramo2,ramo3...],[alumno2,ramo4,ramo5...],[alumno3,ramo6,ramo7,ramo8...]...]
#salida: lista de solicitudes de ramos: [ramo1,ramo2,ramo3,ramo4,ramo5,ramo5,...]
def calcularDemanda(matrizAlumnos):
    demanda=[]

    for alumno in matrizAlumnos: #se recorren los alumnos
        for asignatura in alumno: #se recorren los elementos de un alumno [alumno1,ramo1,ramo2,...]
            if asignatura!=alumno[0]: #si el elemento iterador es diferente al primer elemento de cada alumno(nombre de este)
                demanda.append(asignatura) #se agrega a la  lista de demanda, solo se agregan ramos
    
    return demanda


##Función para calcular moda en listas
#entrada: una lista, en este caso, la lista de demanda [ramo1,ramo2,ramo3,ramo4,ramo5,ramo5,...]
#salida: una lista con el o los elementos que mas se repiten en la lista de entrada
def calcularModa(demanda):
    contadorModal=0 #es la frecuencia del elemento con mas apariciones actualmente
    modas=[]
    
    for ramo in demanda: #para cada ramo
        conteo=demanda.count(ramo) #se cuenta cuantas veces aparece en la lista
        if conteo> contadorModal: #si la frecuencia del elemento actual supera al que hasta ese punto tenía mayor frecuencia
            contadorModal=conteo #contadorModal se sobreescribe con la nueva mayor frecuencia
            
    for ramo in demanda:#se cuentan las apariciones de cada ramo nuevamente
        conteo=demanda.count(ramo)
        if conteo==contadorModal and ramo not in modas: #si durante el conteo algún elemento tiene la misma frecuencia que el contadorModal
            modas.append(ramo) #ese elemento es la moda y se agrega a la lista de modas, es válida para modas únicas y no únicas

    return modas


##Función que ordena en una lista los ramos según su demanda
#entrada: lista 
#salida: lista ordenada donde el primer elemento es el de mayor frecuencia
#y los siguientes los que le siguen en frecuencia hasta llegar al último elemento

def calcularPrioridad(lista):
    largoDemanda=len(lista)#se toma en cuenta el largo de la lista para poner la condición de borde
    lista2=[]
       
    prioridad=[]
    modas=[]
    contadorModal=0
    i=0

        #se duplica la lista de entrada para trabajar con la copia
        #ya que mas adelante se borran elementos de esta
        #esto traía problemas cuando se requería la lista para otras funciones
    for elemento in lista:
        lista2.append(elemento)
       

        #se calcula la moda en bucle, ya que la lista de demanda irá variando
        #la moda es una lista con los elementos que tengan mayor frecuencia
    while i < largoDemanda:
        moda=calcularModa(lista2) 
        

        
        #se agregan los elementos de la lista moda a la lista de prioridad
        for ramo in moda:
            prioridad.append(ramo)

        

        #para cada ramo, si este ya está incluido en la lista de prioridad
        #se elimina de la lista2 (demanda)
        #se repite el proceso con una lista2 cada vez mas pequeña
        #hasta incluir todos los ramos demandados en la prioridad
        #según su moda
        for ramo in moda:
            if ramo in lista2:
                lista2.remove(ramo)

        
        #la función tiene un problema       
        #se elimina solo una frecuencia, hay que hacer un ajuste
        #por ejemplo, para un elemento que se repita 3 veces en la demanda
        #se elimina solo una vez y la siguiente vez ese elemento
        #continúa repitiéndose 2 veces e influye en el cálculo de la moda
    
    
        i=i+1 #se avanza al siguiente valor de la demanda para repetir el proceso las veces que haga falta
   
    return prioridad




##Función para ajustar la prioridad
#elimina los ramos repetidos de la lista de prioridad desde su segunda aparición
#entrada: la lista de prioridad con valores repetidos[ramo1,ramo2,ramo2,ramo2,ramo3,ramo3....]
#salida: una lista de prioridad similar a la de entrada, pero sin valores repetidos [ramo1,ramo2,ramo3,ramo4]

def ajustarPrioridad(prioridad):
    prioridadBien=[]
    #se crea una segunda lista para tomar elementos de la primera
    #sin repetir ninguno
    for ramo in prioridad:
        if ramo not in prioridadBien:
            prioridadBien.append(ramo)
            #solo se agregan los ramos que no se hayan agregado ya
         
    
    return prioridadBien
            
 




##Función que asocia a cada ramo el número de personas que quieren
#inscribir ese ramo en forma de lista
#cada elemento de la lista es de la forma ramo:número de gente que lo solicita
#entrada: la lista de demanda [ramo1,ramo2,ramo3,ramo4,ramo1,ramo3...]
#salida: una lista similar en el mismo orden donde a cada elemento se le agrega ;numero de personas que solicitan ese ramo
#resultando cada elemento un string de la forma ramo;personas que solicitan ese ramo
        
def asociarDemandaRamo(demanda):
    
    frecuencias=[]
    pares=[]
    corregido=[]
    i=0

    #se cuenta cuantas veces se repite cada elemento de la demanda
    #se agregan esos valores a la lista "frecuencias"   
    for ramo in demanda:
        conteo=demanda.count(ramo)
        frecuencias.append(conteo)
    


    
    while i<len(demanda): #se itera desde 0 hasta el largo de la demanda
        contador=frecuencias[i]#el valor de la posición i de la lista de frecuencias
        elementoY=str(contador)#ese mismo valor como string
        par=demanda[i]+";"+elementoY # ramo i+ ";" +la frecuencia del ramo i
        pares.append(par)   #se agrega ese par a una lista de pares
        i=i+1
        

    for par in pares: #se recorre la lista de pares
        if par not in corregido: #se toma una vez cada par, sin repetir ningún valor
            corregido.append(par) #y se agrega a la lista "corregido"

    #para leer estos pares se puede aplicar .split a cada elemento
    #de la lista creada por split lista[0] es el ramo
    #lista[1] es la demanda de ese ramo
    
    return corregido




#Función que calcula el número de salas que se requiere para cada ramo
#entrada:la lista demandaNumeros, donde cada elemento de la lista es un string de la forma:
#ramo;demanda
#salida: una lista donde cada elemento es un string de la forma: ramosalas;numerodesalas
def calcularPorRamo(demandaNumeros):
    matriz=[]
    numeroSalas=[]
    
    for ramo in demandaNumeros: #se recorren los elementos de demandaNumeros
        par=ramo.split(";") #se cortan esos elementos en los ; para convertirlo a lista
        matriz.append(par) #se crea lista de listas de 2 elementos, ramo; demanda
    
    for ramo in matriz:
        
        y=int(ramo[1]) #solicitantes para el ramo x
        valor=y/porSala #se divide los solicitantes por la capacidad de cada sala
        i=0
        while valor>1: #hasta que no se alcance a llenar una sala
            valor=valor-porSala #se resta del total los alumnos de una sala cada vez
            i=i+1
        string=str(i+1) #se pasa a string el número de salas necesarias para el ramo x
        numero=ramo[0]+"salas;"+string # ramoxsalas; número de salas necesarias para x
        numeroSalas.append(numero)   #se agregan a una lista
    
        
        
    return numeroSalas

    
               

#Función para hacer una lista de prioridad con numero de salas requeridas para cada ramo
#con la diferencia de que esta vez se ordenan por orden de prioridad
#entradas: lista de salasPorRamo donde cada elemento es un string de la forma ramox;numero de salas necesarias para x
#lista de prioridadBien, ordenada según moda y sin repetir elementos de la forma [ramo1,ramo2,ramo3]
#salida: una lista ordenada según prioridad donde cada elemento es un string de la forma ramox;salas requeridas para el ramo x
def calcularPrioridadConSala(salasPorRamo,prioridadBien):
    prioridad=[]
    nueva=[]
    for ramo in prioridadBien: #se duplica la lista de ramos prioritarios, por precaución
        prioridad.append(ramo)
    for ramo in salasPorRamo: #se recorren los elementos de salasPorRamo
        par=ramo.split("salas;") #como cada elemento es un string este se corta en una lista
        for prioritario in prioridad: #para cada ramo prioritario
            
            if prioritario==par[0]: # si el algun ramo prioritario es igual a algun ramo de salasPorRamo
                nuevoElemento=par[0]+";"+par[1] #se construye un string sala;ramo con los elementos de salasPorRamo
                nueva.append(nuevoElemento) #ese string se agrega a la lista nueva, donde están los elementos ordenados
                #por prioridad con la forma ramox;sala requeridas
    
                
    return nueva
        

#Función para construir trios prioritarios
#de la forma ramo;area;numero de salas
#estos tríos son elementos de una lista y se ordenan por orden de prioridad
#entradas:lista prioridadSala, con elementos de la forma ramo; salas requeridad para el ramo.
#matriz de ramos [[area1,ramo1,ramo2],[area2,ramo3,ramo4,ramo5],[area3,ramo6,ramo7]]
#lista de prioridadBien [ramo1,ramo2,ramo3,ramo4]
#salida: lista de strings, cada string es de la forma ramo;Area;salas y están ordenados en orden de prioridad

def asociarSalaArea(prioridadSala,ramos,prioridadBien): #lista, matriz y lista
    trios=[]
    trios2=[]
    
    for prioritario in prioridadSala: # cada elemento es un string ramo;número
        par=prioritario.split(";") #se separan en una lista de 2 elementos
        asignatura=par[0] ##ramo  ##, ramo[0] y numero de salas[1]
        numero=par[1] # número de salas para el ramo prioritario actual en la iteración
        
        for area in ramos:#se recorren las areas de la matriz
            if asignatura in area: #se recorren las asignaturas de un área
                
                #se forma un string con elementos de la lista prioridadSala y la matriz ramos
                trio=str(par[0])+";"+ area[0]+";"+str(par[1]) #ramo;area;salas
                
                trios.append(trio) #se agrega cada trio a una lista "trios"
                #un detalle es que las areas van con mayúscula para diferenciarse de los ramos aún mas
                #se desordenaron, ya no están en orden de prioridad


        #se ordenan los elementos otra vez según prioridad
        #mantienen la misma forma de antes
    for prioritario in prioridadBien:#se recorre la lista de prioridad
        for elemento in trios: #y la lista de trios elemento=ramo;area;salas
            trio=elemento.split(";")#se convierte en lista el string elemento de trios
            criterio=trio[0] #el primer valor de la lista trio es el nombre del ramo
            if criterio==prioritario:#si el nombre del ramo de trio  es el mismo que el del prioritario 
                trios2.append(elemento) #se agrega el trio a una lista similar a la primera, pero por orden prioritario
                #este proceso permite comparar cada elemento con el de la lista de prioridad para ordenar
     
      
    return trios2





##Función para poner todos los ramos demandados en una lista, primero los prioritarios
#se repite cada ramo según la cantidad de salas que necesita
#cada elemento de la lista es un string y van ordenados como pares de la forma ramo;area
#entrada: lista salaArea, es una lista de strings donde cada string es un trio de la forma ramo;Area;salas
#salida: una lista de strings, cada string es un par ramo;Area, estos están ordenados según prioridad y se repiten
#dentro de la lista según el número de salas requeridas para el ramo

    
def crearSuperLista(salaArea):
    superLista=[]
    salaArea2=[]
    for prioritario in salaArea: #se duplica para trabajar por la copia, solo por si acaso
        salaArea2.append(prioritario)
        
    for prioritario in salaArea2: #se recorren los elementos de salaArea, cada elemento es un string
        trio=prioritario.split(";") #se divide cada string en una lista de 3 elementos ramo,area,numero de salas
        ramo=trio[0]
        area=trio[1]
        salas=int(trio[2]) #es el numero que indica las salas necesarias para cada ramo
        par=str(ramo)+";"+str(area) #se construye un string ramo;area para cada elemento de salaArea
        while salas>0: #para cada ramo mientras queden salas requeridas
            superLista.append(par) #se agrega el par ramo;area a la superLista
            salas=salas-1 #se le resta una unidad a las salas de ese ramo
                          #cuando lleguen a cero ese ramo está listo y se avanza al siguiente
    
    return superLista

            
##Función que asigna salas y horarios a las diferentes asignaturas en virtud de las salas disponibles
#y de las salas requeridas para cada ramo
#entradas: lista SuperLista, cada elemento de esta lista es un string ramo;Area
#cada elemento se repite por al cantidad de salas necesarias para ese ramo
#la segunda entrada es la matriz de salas[[sala1,hora1,hora2...],[sala2,hora3,hora4...],[sala3,hora5,hora6,hora7...]...]
#salida: una tupla (cuartetos,superLista2)
#cuartetos es la lista de strings sala;hora;ramo;Area
#superLista2 son los ramos que quedan sin asignar, si resulta una lista vacía es porque todos los ramos demandados consiguen sala
def asignarSala(superLista,salas):
    
    superLista2=[]#una lista tipo ramo1;area,ramo2;area,...
    salas2=[] #lista de listas[sala1,hora1,hora2],[sala2,hora1,hora2],[sala3,hora1,hora2,hora3]
    listas=[]
    
    completa=[]
    
    for ramo in superLista:
        superLista2.append(ramo)#copias para no alterar el original
    
    for sala in salas:
        salas2.append(sala)#copia para no alterar el original
   
    
    cuartetos=[]     #sala;hora;ramo;area   

    for sala in salas2:
        i = 0
        j = 1 #parte desde 1 porque con j=0 tomaría el numero de la sala
        aux = 0 #valor actual del indice para listaSala
        listaSala = [sala[0]] # Lista N°sala + areas de los ramos que se le asignan

        # eand i<len(superLista2) es condición para que no se intenten llamar elementos que no existen en superLista2
        while j<len(sala) and i<len(superLista2):
            ramoArea = superLista2[i] #un elemento ramo;area
            
            par = ramoArea.split(";") #se convierte en lista ramo,area
            area = par[1]
            if area != listaSala[aux]:   #listaSala[aux] es el numero de la sala o las áreas de ramos asignados previamente
                #sala[0]=numero de sala; sala[j]=hora  ; ramo;Area
                asignacion = sala[0] +";"+ sala[j] +";"+ ramoArea #sala;hora;ramo;Area
                #Se pasa a la siguiente hora de la sala
                j = j+1
                #Se agrega al cuarteto
                cuartetos.append(asignacion)
                #Se agrega el area a la lista temporal
                listaSala.append(area)
                #Se elimina el ramo de la lista porque se asignó a un horario
                superLista2.pop(i)
                aux = aux+1
                i = 0 #i sigue siendo 0 porque el primer elemento de superLista2 se borró                
            else:
                #Se pasa al siguiente ramoArea
                if(i<len(superLista2)):
                    i = i+1    
    #se define una tupla como salida, porque se necesita los horarios pero también los ramos que no pudieron inscribirse
    return cuartetos,superLista2
                
                
        
        

##Función que asigna un número determinado de estudiantes a cada clase,cada clase esta definida por un string sala;hora;ramo;area
#entradas: -lista de horarios, cada elemento es un string sala;hora;ramo;Area
#-matriz de alumnos: [[alumno1,ramo1,ramo2,...],[alumno2,ramo3,ramo4,ramo5,...],[alumno3,ramo6,ramo7,...]...]
#salidas:-un diccionario {clase1:listaDeAlumnos1,clase2:listaDeAlumnos2,...}
#-lista alumnos2, una matriz de alumnos pendientes por inscribir ramos, cada elemento es una lista de la forma
#[alumno,ramo1,ramo2,ramo2], si esta lista solo tiene un elemento este será el nombre del alumno, lo que quiere decir que no tiene ramos pendientes
#el diccionario y la lista salen como tupla(diccionario,lista)
def llenarSala(horarios,alumnos):
    horarios2=[]
    alumnos2=[]
    diccHoras={} #diccionario donde agregar elementos de llave=numero de sala, valor=hora;ramo;Area
    for hora in horarios: #duplicado por seguridad
        horarios2.append(hora)
    
    for alumno in alumnos: #duplicado de seguridad
        alumnos2.append(alumno)

    for cuarteto in horarios2: #se recorre la lista de horarios. 
        
        llave=cuarteto #sala;hora;ramo;Area
        clase=[] #lista para inscribir alumnos en una clase
        i=0

        while i < porSala: #por sala es el valor ingresado por el usuario, número de alumnos por sala
            cortado=cuarteto.split(";") #sala,hora,ramo,area
            ramo=cortado[2]
            for alumno in alumnos2:
                nombre=alumno[0]#nombre del alumno
                
                if ramo in alumno: # si el alumno actual solicita el ramo actual
                    if len(clase)< porSala: #si la sala aún tiene capacidad
                        clase.append(nombre) #se agrega el alumno a esa clase
                        alumno.remove(ramo) #se elimina la solicitud del alumno, ya que fue inscrito
                        diccHoras[cuarteto]=clase #se actualiza la lista de esa clase como valor del diccionario asociado a la clave=número de sala
                i=i+1 #avanza el contador
               
    return diccHoras, alumnos2


##Función que elimina de la lista de alumnos pendientes a aquellos alumnos
#que no necesitan mas ramos por asignar
#entrada: matriz de alumnos pendientes, cada elemento de la lista es una lista [alumno,ramo1,ramo2,ramo2]
#salida: matriz de alumnos pendientes, similar a la de entrada, con la diferencia que las listas de un solo elemento se eliminan

def limpiarPendientes(alumnosPendientes):
    pendientesOk=[]
    for alumno in alumnosPendientes: #copia de seguridad
        pendientesOk.append(alumno)
    i=0
    while i<len(alumnosPendientes): #se repite el proceso segun el total de alumnos
        for alumno in pendientesOk: #se recorren todos los alumnos
            
            if len(alumno)==1:#si para algun alumno su lista solo tiene un elemento, el nombre
                pendientesOk.remove(alumno) #se quita de la lista de pendientes
        i=i+1 #se incrementa el contador
            
    
    return pendientesOk

                
                
            
        
    
##Función que tiene escribe en un archivo de texto la información sobre los horarios
#entrada: el diccionario de clases donde cada item del diccionario es un string y una lista
# de la forma("sala;hora;ramo;area",[alumno1,alumno2,alumno3,..])
#como salida un archivo de texto de nombre "horarios" donde cada linea tiene la forma
#sala;hora;ramo;area;alumnos=[alumno1,alumno2,alumno3]
#este diccionario son los horarios de clases del establecimiento
#con sus respectivos alumnos por cada sección

def escribirHorarios(clases):
    #se abre un archivo "horarios" en modo escritura, si no existe lo crea
    archivo=open("horarios.txt","w")

    #se define una lista de tuplas donde cada tupla es llave y valor del
    #diccionario de clases
    #cada elemento de la lista es de la forma(sala;hora;ramo;area),(lista de alumnos)
    tuplas=clases.items()

    #se recorren todos los valores de la lista y se define para cada uno
    #la línea que se escribe en el archivo 
    for clase in tuplas:# para cada clase de las tuplas se define un string
        superString=""
        for elemento in clase[1]: # a ese string se van sumando todas las clases(alumnos)
            superString=superString+","+elemento #separando cada alumno por una coma ,
        limpioString=superString.strip(",") #se limpia el string para que no queden comas en los bordes
        linea=clase[0]+";alumnos="+limpioString+"\n" #se define la línea que se escribe en el texto incluyendo salto de línea
        #se escribe la línea en el archivo
        archivo.write(linea)
        
    
    archivo.close() #se cierra el archivo "horarios.txt"
    
    return archivo



##Función que escribe en un archivo de texto los nombres de los alumnos que quedaron con ramos sin inscribir
#así como los respectivos ramos que no pudieron inscribir
#entrada: una matriz de alumnos donde solo están aquellos alumnos que quedaron con ramos sin escribir
#de la forma [[alumno1,ramo1],[alumno2,ramo2,ramo3],[alumno3,ramo4]]
#salida: un archivo de texto donde cada línea es de la forma alumno,ramo x,ramo y...

def escribirPendientes(pendientesLimpio):
    #se abre un archivo "pendientes" en modo escritura, si no existe lo crea
    archivo=open("pendientes.txt","w")  

    for alumno in pendientesLimpio:
        
        superString="" #para cada lista alumno se define un string
        for elemento in alumno: #se recorre cada elemento de esa lista
            superString=superString+","+elemento #dicho elemento se agrega al string, separados por una coma
        limpioString=superString.strip(",") #se limpia el string resultante para que no queden comas en los extremos
        linea=limpioString+"\n" #se define la línea como el string mas un salto de linea
        archivo.write(linea) #se escribe la línea en el archivo
    archivo.close() #se cierra el archivo "pendientes.txt"
    return archivo
                
                
           
                
            


    
            
        
        



#########################################################################
###### BLOQUE PRINCIPAL #####

# ENTRADA
#Número de alumnos por sala
porSala=ingresarNumero() #se solicita al usuario ingresar el número con una función


#los archivos de texto

#alumnos.txt
#areas.txt
#salas.txt

#################################################################################

# PROCESAMIENTO

###Conteo y lectura####
listaAlumnos=leerAlumnos()
cantidadAlumnos = contarAlumnos()

listaAreas=leerAreas()
cantidadAreas=contarAreas()

listaSalas=leerSalas()
cantidadSalas=contarSalas()


#Matrices de datos#
alumnos=crearMatrizAlumnos(listaAlumnos)
ramos=crearMatrizAreas(listaAreas)
salas=crearMatrizSalas(listaSalas)


#Demanda#
demanda=calcularDemanda(alumnos)

#Conteo de ramos#
cantidadRamos=contarRamos(ramos)

#Calcular moda en una lista#
moda=calcularModa(demanda)

#Prioridad según demanda#
prioridad=calcularPrioridad(demanda)
prioridadBien=ajustarPrioridad(prioridad)

#Demanda por ramo#
demandaNumeros=asociarDemandaRamo(demanda)


#Número de salas para cada ramo# 

salasPorRamo=calcularPorRamo(demandaNumeros) #lista de elementos de la forma salax;numero#

#Prioridad con numero de salas requeridas para cada ramo y el área asociada a cada ramo#
prioridadSala=calcularPrioridadConSala(salasPorRamo,prioridadBien)
salaArea=asociarSalaArea(prioridadSala,ramos,prioridadBien)



#SuperLista, lista que representa como strings los ramos con sus respectivas areas, por orden prioritario#
#Cada elemento se repite según el número de salas que requiere ese ramo
superLista=crearSuperLista(salaArea)


#Asignar sala#
#Asignar es una tupla (horario,superLista2) por la salida de la función
asignar=asignarSala(superLista,salas)
horarios=asignar[0] #horarios como diccionario {sala:clase,sala2:clase2} cada clase es hora;ramo;Area
superListaPendiente=asignar[1] #alumnos que no pudieron inscribir asignatura por falta de salas

#Llenar sala, asignar alumnos a cada clase e identificar los alumnos pendientes#
conGente=llenarSala(horarios,alumnos) #devuelve tupla(horarios,alumnosPendientes)

clases=conGente[0] #diccionario, cada clase es sala;hora;ramo;area {clase1:lista1,clase2:lista2}
alumnosPendientes=conGente[1] #matriz [[alumno1,ramo1,ramo2],[alumno2,ramo1,ramo3]]
#si cada sublista solo tiene el nombre de un alumno es porque ese alumno no solicita nada mas

#Limpiar pendientes#
pendientesLimpio=limpiarPendientes(alumnosPendientes) #matriz [[alumno1,ramo1,ramo2],[alumno2,ramo1,ramo3]]
#solo contiene alumnos que no pudieron inscribir alguna asignatura, y cuales fueron estas

###############################################################################################


# SALIDA

#Escribir archivos de texto#
#Salas y horarios: 
salasHorarios=escribirHorarios(clases) #cada fila del archivo es: sala;hora;ramo;Area;alumnos=alumno1,alumno2,alumno3...


#Pendientes:
pendientes=escribirPendientes(pendientesLimpio) #se escribe un archivo con alumnos que no pudieron inscribir asignaturas por falta de salas

print(" ")
print("Se han realizado los procedimientos correspondientes.")
print(" ")
print("Se han escrito 2 archivos de texto:") #se informa de los resultados y donde encontrarlos

print("-->Los horarios con sus respectivas salas y alumnos")
print("""están en el archivo: horarios.txt
 """)
print("-->Los alumnos que no pudieron inscribir alguna asignatura")
print("""están en el archivo: pendientes.txt
""")
print("-Si el archivo pendientes.txt está vacío")
print("""significa que toda la demanda pudo cubrirse
      """)
print("-Los cálculos y asignaciones se han hecho a considerando que cada") #se recalca que los cálculos se hicieron a partir del número otorgado por el usuario
print("sala admite", porSala, "alumnos, número proporcionado por el propio usuario")
print("")
print("-Si se considera que hay demasiados alumnos con ramos pendientes se") #se dan recomendaciones en caso de que el resultado no sea satisfactorio
print("recomienda proporcionar mayor cantidad de salas y horarios o en su")  
print("defecto, aumentar la cantidad de alumnos por sala de ser posible")
print(" ")
print("Si el resultado presenta alguna anomalía,asegúrese de haber") #se indica que si hay algún error o algo no cuadra en los resultados
print("""proporcionado los archivos: "alumnos.txt","salas.txt" y "areas.txt" 
en la forma correcta e intente ejecutar el programa nuevamente,""") #el usuario entregar los datos en la forma que el programa requiere
print("si el problema persiste, póngase en contacto con el equipo de desarrollo.") 
print("")
#se indica al usuario que en caso de que no pueda solucionar el problema se ponga en contacto con el equipo de desarrollo para encontrar
#el motivo por el cual el programa no está funcionando correctamente y solucionarlo


