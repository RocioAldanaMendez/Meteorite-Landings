![header](https://capsule-render.vercel.app/api?type=waving&height=300&section=header&text=%20Standard%20and%20Poor's%20500&fontSize=30&&color=15:92a8d1,100:f7cac9&desc=%20%20&fontColor=ff6347&fontAlignY=35)


## INDICE:
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#header">TÍTULO E IMAGEN DE PORTADA</a></li>
    <li><a href="#INDICE">ÍNDICE</a></li>
    <li><a href="#INTRODUCCIÓN">INTRODUCCIÓN</a></li>
    <li><a href="#OBJETIVO">OBJETIVO</a></li>
    <li><a href="#SCOPE-OF-WORK">SCOPE OF WORK</a></li>
    <li><a href="#ESTADO">ESTADO</a></li>
    <li><a href="#EDA-ETL">EDA - ETL</a></li>
    <li><a href="#FastAPI">FastAPI</a></li>
    <li><a href="#MINI-DEMO1">MINI-DEMO1</a></li>
    <li><a href="#MINI-DEMO2">MINI-DEMO2</a></li>
    <li><a href="#ACCESO-AL-PROYECTO">ACCESO AL PROYECTO</a></li>
    <li><a href="#TECNOLOGÍAS">TECNOLOGÍAS UTILIZADAS</a></li>
    <li><a href="#DESARROLLADORES">DESARROLLADORES DEL PROYECTO</a></li>
    <li><a href="#VIDEO">VIDEO</a></li>
  </ol>
</details>

## INTRODUCCIÓN
Este proyecto forma parte de la etapa Labs del curso de Data Science de la Academia Soy Henry.
En esta ocasión brinda fuentes de información asociadas al sector de finanzas. Se propone hacer un analisis minucioso de un índice en particular, el indicador S&P 500. Este índice pondera la capitalización bursátil de las 500 mayores empresas que cotizan en la bolsa de los Estados Unidos. El índice está considerado como el mejor indicador de la renta variable estadounidense y es ampliamente utilizado y referenciado

## OBJETIVO
- Hacer analisis minucioso del indice sp500
- Sacar información y conclusiones de valor para determinar decisiones de inversion
- Identificar Industrias o Sectores con mejor Retorno y contraponerlas con la información que se obtuvo anteriormente
- Identificar días en donde conviene generar inversiones

## SCOPE-OF-WORK
La propuesta de trabajo se llevará a cabo en las siguientes etapas:

1. Adquisición de información de las siguientes fuentes: 
   -  API de yahoo finance
   - Librería: https://pypi.org/project/yfinance/ 
   - Página oficial
   - Lista índice SP500

2. Análisis exploratorio de datos (EDA) Link: (https://github.com/RocioAldanaMendez/FastAPI/blob/main/ETL-EDA/modelo2.ipynb)
3. Análisis Introductorio de la primera fuente de datos
4. Agregar más información de la segunda fuente de datos
5. Union de toda la información
6. Agregar columna de días, cambiar el idioma de los encabezados, convertir fechas en formato date, verificar nulos, outliers
7. Analisis minucioso: análisis univariado, análisis bivariado, verificar el promedio de cierre del indice desde el 2000 a la actualidad, variación de las industrias, variación de las industrias tomando mas valores.
8. Primeras conclusiones
9. Variación de los cierres a lo largo de los años, cálculo de volatilidad, evaluación del retorno total.
10. Segundas conclusiones
11. Cálculo de mejores dias de inversión.
12. Exportación de datos en .parquet, y .csv (siempre es mejor tener un respaldo)
13. Creación de Dashboard para presentar ante un cliente: Link 


![arquitectura](https://github.com/RocioAldanaMendez//Meteorite-Landings/blob/main/assets/Screenshot%202023-02-25%20191257.jpg)

## ESTADO:
<h4 align="center">
:white_check_mark: Proyecto finalizado :white_check_mark:
</h4>

## EDA-ETL
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/>  
Como paso inicial, los datos se cargarán utilizando la biblioteca pandas. En esta instancia, se realizará un análisis exploratorio de los datos y se realizarán las transformaciones necesarias para limpiar los datos. Para ver con más detalle el trabajo realizado con las ETD y ETL puede recurrir a la carpeta que contiene esos dos archivos. A continuación se adjunta una hoja de ruta que establecí para el desarrollo:


## PowerBI
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=40px/>



## MINI-DEMO1:
- `KPI 1`: Consultar película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

                    La consulta debe generarse con el siguiente formato: {year}/{platform}/{duration_type}: 200/netflix/min
                    
- `KPI 2`: Consultar cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

                   Formato: {platform}/{scored}/{year}: netflix/(numeros del 0 al 5)/2000
                    
- `KPI 3`: Consultar cantidad de películas por plataforma con filtro de PLATAFORMA

                    La consulta debe generarse con el siguiente formato: {platform}: netflix
                    
- `KPI 4`: Consultar actor que más se repite según plataforma y año.

                    La consulta debe generarse con el siguiente formato: {platform}/{year}/: netflix/2000
                    
  Donde plataforma puede ser: netflix, hulu, disney, amazon.
  
  Y duration_time puede ser: min o season.
  
Link Proyecto POWER BI: https://mega.nz/file/VZ40zRgQ#2OhQOR6IZmTGIEqyP-rKaz2MTtsqrrwRWYlXDdWmcjk


## ACCESO-AL-PROYECTO
            ## 🛠️ Abre y ejecuta el proyecto
            -  Para correr la api completa es necesario descomprimir el archivo que contiene el modelo, para que la api consuma de ese archivo, y como se subió la carpeta donde se desarrolló la api completa, debe correr.
            -Para visualizar la salida final en los Deploys podes ir al link de punto 7 y 8 del scope of work, o ingresar al alrchivo txt que contiene todos los links.
            
 
## TECNOLOGÍAS
 <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=40px/> 

## DESARROLLADORES

| [<img src="https://avatars.githubusercontent.com/u/83037176?v=4" width=115><br><sub>Rocío Méndez</sub>](https://github.com/RocioAldanaMendez) |
| :---: | 


Gracias por ver este desarrollo, podes seguir los futuros cambios dandole una estrellita en la parte superior derecha del repositorio. Podes Clonarlo, y/o podes hacer un PullRequest ya que todo aporte es bienvenido. 


