## ChatIA-Panda
# 💻 Prueba tecnica Python

  Esta fue una prueba tecnica en PYTHON para la empresa **[ANONIMA](https://ww.h.com.ar/)**
  
## 📋 Consigna
1)Crea una API de chatbot simple que pueda:
- Manejar mensajes de saludo de los usuarios (por ejemplo, 'hola', 'hola')
- Proporcionar una respuesta genérica para mensajes no reconocidos (por ejemplo,
'Lo siento, no entendí eso')
Requisitos:
- Utiliza lenguaje de programación Python.
- La API debería poder manejar múltiples solicitudes simultáneas
- Incluir algunas pruebas unitarias básicas para probar el saludo y las respuestas
predeterminadas.


2) Tienes la siguiente hoja de cálculo llamada “Employee Data 2.xlsx” y necesitas
extraer cierta información sobre la nómina de empleados de esta empresa: Nombre
Completo, Puesto, Salario, País.

**Resueltos:** 
- [1 API CHATBOT CON IA](https://github.com/lnxxxxxxxx/ChatIA-Panda/tree/main/PTPY)
- [2 SCRIPT PYTHON CON PANDAS EXCEL](https://github.com/lnxxxxxxxx/ChatIA-Panda/tree/main/PTPY2Excel)

## 📋 Tecnologias
- Environment 
  - [Python3.1.2](https://www.python.org/downloads/)
  - [Visual Studio](https://code.visualstudio.com/download)
  - [Postman](https://www.postman.com/product/rest-client/)
 
## 🔧 Instalación y uso
  Si deseas correr la API en un entorno local debes tener en cuenta lo siguiente: 
  1. Clona el repositorio utilizando GIT o descargando el archivo ZIP:

      `git clone https://github.com/lnxxxxxxxx/ChatIA-Panda.git`
     - Instala **flask** `pip install flask`
     - Instala **tensorflow** `pip install tensorflow`
     - Instala **pandas** `pip install pandas`
     - Instala **nltk** `pip install nltk`


      
  2. Abrelo en VS, corre python:
     -  app.py. Se abrira en el puerto 500 de localhost por default [localhost:500](http://localhost:5000/)
     -  extract.py. Se extraera los datos del excel y devolvera los primeros 5 en una tabla por print.   
     -  test.py. Hara un testing del chatbot con 2 entradas, hola y cualquier otro string para recibir las respuestas correctas.
  
  3. Abre Postman, utiliza el endpoint con el metodo POST.
   - Endpoint:
     - Enviar mensaje: *POST* /chat
       
       - ``{
         "message" : "hola"
          }`` 
          *Recibiras de respuesta un Hola*
       - ``{
             "message" : "cualquier cosa escribe aqui"
            }``
          *Recibiras de respuesta Lo siento, no entiendo el mensaje.*
        
     






