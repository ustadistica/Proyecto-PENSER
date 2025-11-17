<div align="center">

# Un Proyecto del Consultorio de Estadística y Ciencia de Datos: Del Índice a los Arquetipos  

Proyecto del curso <b>Consultoría e Investigación</b> – Facultad de Estadística  
<b>Universidad Santo Tomás</b> · <b>Octavo Semestre (2025-2)</b>

<br/>

<b>Equipo:</b> Yeimy Alarcón · Karen Suarez · Maria José Galindo 

> **Estado:** En progreso · **Repositorio:** _[Link Repositorio](https://github.com/ustadistica/Proyecto-PENSER.git)_ · **Última actualización:** 2025-11-17

</div>

> *Un nuevo modelo metodológico que transita desde la reconstrucción de un índice unidimensional hacia un modelo multidimensional que revela los perfiles complejos y diversos de nuestros graduados.*

---

## Introducción  

Este informe presenta el trabajo realizado para revisar y mejorar el Índice de Impacto de Egresados (IIE), una herramienta creada por el Proyecto PENSER que busca entender cómo los estudios en la Universidad Santo Tomás han influido en la vida personal y profesional de sus graduados.

El proyecto se llevó a cabo dentro del Consultorio de Estadística y Ciencia de Datos, con el objetivo de evaluar si el modelo original del índice era claro, confiable y representaba bien la realidad. A partir de ese análisis, se propuso una versión más completa y fácil de interpretar, que permitiera ver el impacto de los graduados desde diferentes perspectivas.

Para lograrlo, el estudio se desarrolló en tres etapas:

1. **Reconstrucción del índice:** se replicó la metodología original del IIE para evaluar su consistencia y determinar qué tan reproducibles eran los resultados publicados.  
2. **Análisis factorial exploratorio:** al identificar inconsistencias en la fase inicial, se adoptó un nuevo enfoque estadístico para descubrir las dimensiones latentes que realmente definen el impacto de los graduados.
3. **Identificación de arquetipos:** finalmente, se agruparon los graduados según sus características y resultados, dando origen a cinco perfiles de impacto con historias únicas.

En conjunto, este proceso, que va desde la revisión del índice hasta la creación de los arquetipos, ofrece una mirada más completa y real sobre el impacto de la universidad en sus graduados, y deja las bases para seguir fortaleciendo futuras evaluaciones institucionales.

---

## 1. Reconstrucción del Índice de Impacto de Egresados (IIE)

El objetivo central de esta primera etapa fue **reconstruir y verificar el IIE**, aplicando rigurosamente la metodología original con el fin de validar los resultados, identificar posibles inconsistencias y documentar las diferencias encontradas.

Se trabajó con la base de datos **“Data Depurada Santo Tomás – Estudio PENSER (mayo 2025)”**, transformando las respuestas de los egresados en puntajes numéricos y calculando los subíndices según la fórmula original:

<p align="center">
  <b>IIE = (0.30×FD) + (0.30×DCI) + (0.20×MS) + (0.20×PMCV)</b>
</p>

donde cada componente representa un aspecto del impacto:

- **FD:** Formación Disciplinar  
- **DCI:** Desarrollo de Competencias Interpersonales  
- **MS:** Movilidad Social  
- **PMCV:** Percepción de Mejoramiento de la Calidad de Vida  

---

### Resultados de la reconstrucción

Durante el proceso se compararon los resultados obtenidos con los valores reportados en el estudio metodológico original.

<p align="center">
  <img width="530" height="97" alt="Figura 1. Análisis IIE Global" src="https://github.com/user-attachments/assets/133e146b-ea5e-4d43-8b59-bb62079808ef" />
  <br>
  <strong>Figura 1.</strong> Análisis IIE Global
</p>

Al realizar la reconstrucción encontramos que dos de los cuatro componentes, **Desarrollo de Competencias Interpersonales (DCI)** y **Percepción de Mejoramiento de la Calidad de Vida (PMCV)**, mostraron una excelente consistencia.  En estos casos, la descripción metodológica fue lo suficientemente clara como para replicar los cálculos y obtener resultados prácticamente iguales a los del estudio original.

Sin embargo, los otros dos componentes: **Formación Disciplinar (FD)** y **Movilidad Social (MS)** presentaron dificultades importantes. En la documentación original no se explicaba con detalle cómo se asignaban los pesos a ciertas respuestas, ni se especificaba con claridad qué variables del cuestionario debían combinarse. Además, algunas preguntas incluían opciones como *“No aplica”* y no existía una guía sobre cómo tratarlas.

Como resultado, no fue posible reproducir con precisión el índice completo. Al aplicar la metodología tal como estaba descrita, el nuevo cálculo arrojó un **IIE global del 67.5%**, mientras que el estudio original reportaba un **72%**. Esta diferencia significativa evidenció que el modelo inicial no contaba con la solidez suficiente para garantizar su replicabilidad.

---

### Conclusión de la etapa

Al intentar reconstruir el índice, se evidenció que el modelo original no podía repetirse con los mismos resultados. Esto mostró que la forma en que estaba planteado no era del todo clara ni precisa. Por esa razón, el equipo decidió **cambiar de enfoque** y buscar una alternativa más confiable que permitiera entender mejor qué explica realmente el impacto de los egresados.  
De esta manera surgió la idea de aplicar un nuevo método, **el análisis factorial exploratorio**, que permitió descubrir los aspectos que más influyen en el impacto de los graduados y avanzar hacia una visión más completa y representativa de su realidad.

---

## 2. Un nuevo enfoque metodológico

En esta segunda parte del proyecto fue necesario cambiar la forma de trabajo, porque el modelo original del índice no funcionaba bien con los datos disponibles.  
Por eso, decidimos usar un método más flexible llamado **Análisis Factorial Exploratorio (AFE)**, que nos permitió descubrir cómo se relacionaban realmente las respuestas de los egresados. En lugar de aplicar una fórmula fija, dejamos que **los propios datos "hablaran"** y mostraran su estructura, ayudándonos a entender qué aspectos explican mejor el impacto de la formación universitaria.

Para entender mejor este método, el análisis factorial es una herramienta que sirve para resumir mucha información y encontrar los temas que se repiten dentro de un conjunto amplio de preguntas. En vez de mirar cada pregunta por separado, este método agrupa aquellas que tienen significados o patrones similares, lo que ayuda a identificar las ideas principales que están detrás de las respuestas, como las competencias, la experiencia profesional o la calidad de vida. Elegimos este método porque nos permite construir una visión más clara, sencilla y realista de lo que piensan los graduados.

### Metodología

El siguiente diagrama muestra las etapas seguidas para aplicar el análisis factorial exploratorio:

<p align="center">
  <img width="301" height="642" alt="Figura 2. Diagrama explicativo metodología" src="https://github.com/user-attachments/assets/d6be1853-26fd-42e9-8c08-ad38275375fd" />
  <br>
  <strong>Figura 2.</strong> Diagrama explicativo metodología
</p>

Primero limpiamos y transformamos los datos para que pudieran analizarse correctamente.
Convertimos las respuestas escritas en texto, como “Muy alto”, “De acuerdo” o “Sí”, en números del 1 al 5, donde 5 representa un nivel alto y 1 un nivel bajo.
También corregimos errores de escritura, espacios vacíos y respuestas duplicadas para dejar una base coherente.

Luego aplicamos dos pruebas estadísticas para verificar si los datos eran adecuados para este tipo de análisis:
- **Prueba de Bartlett**: verifica si las preguntas están relacionadas entre sí. El resultado fue menor a 0.001, lo que indica que sí lo estaban.
- **KMO (Kaiser-Meyer-Olkin)**:mide qué tan bien se pueden agrupar las preguntas en factores.  En nuestro caso, los valores fueron altos (0.93, 0.86 y 0.88), lo que muestra que los datos eran de buena calidad.

Con esos resultados identificamos y nombramos los factores que surgieron, y calculamos los puntajes de cada uno promediando las respuestas que pertenecían al mismo grupo. Con esa información construimos la base de datos final usada para el análisis y las conclusiones.

### Resultados Segunda Etapa  

#### Hallazgo 1: Competencias transversales  

En este bloque analizamos las competencias transversales, que son las **habilidades blandas** que ayudan a las personas a relacionarse y actuar en distintos entornos, como comunicarse bien, resolver problemas o manejar el estrés. Primero comprobamos que los datos eran adecuados para este análisis, y los resultados mostraron muy buena calidad se obtuve un KMO = 0.93 y Bartlett significativo.

<p align="center">
  <img width="665" height="433" alt="Figura 3. Gráfico de Sedimentación para Competencias Transversales" src="https://github.com/user-attachments/assets/a56e4978-0cba-42bd-9d22-bc002af93891" />
  <br>
  <strong>Figura 3.</strong> Gráfico de Sedimentación para Competencias Transversales
</p>

Luego observamos el gráfico de sedimentación, donde se ve una caída fuerte en el primer punto y luego la línea casi plana. Eso indica que todas las competencias se agrupan en un solo gran conjunto, por eso decidimos conservar un solo factor. 

La tabla de cargas factoriales muestra cuánto aporta cada competencia a ese factor común.
<p align="center">
  <img width="1046" height="526" alt="Figura 4. Tabla de cargas factoriales para Competencias Transversales" src="https://github.com/user-attachments/assets/9501d2fb-d78c-4e57-8634-295365f81d37" />
  <br>
  <strong>Figura 4.</strong> Tabla de cargas factoriales para Competencias Transversales
</p>

Los valores van de 0 a 1, y mientras más alto, más peso tiene dentro del grupo. En este caso, todas las competencias tienen valores muy altos (entre 0.80 y 0.89), lo que significa que se mueven juntas y miden prácticamente la misma habilidad general. 

Con estos resultados podemos decir que los graduados perciben estas habilidades como una sola capacidad general. Por eso lo llamamos **Factor General de Competencias Transversales**. Esto nos indica que cuando una persona fortalece una de estas habilidades, normalmente también mejora las demás, ya que todas están conectadas y forman un mismo conjunto

---

#### Hallazgo 2: Formación disciplinar  

En este bloque se analizaron las competencias relacionadas con la formación profesional, que son las habilidades académicas y técnicas que los egresados desarrollaron durante su paso por la universidad. Primero comprobamos que los datos fueran adecuados para el análisis, y los resultados fueron positivos obteniendo un KMO = 0.86 y Bartlett significativo. 

<p align="center">
  <img width="754" height="462" alt="Figura 5. Gráfico de Sedimentación para Formación Disciplinar" src="https://github.com/user-attachments/assets/9b3011c5-574c-4ca8-93a5-c32121c07492" />
  <br>
  <strong>Figura 5.</strong> Gráfico de Sedimentación para Formación Disciplinar
</p>

En el gráfico de sedimentación se observa una caída fuerte al inicio y un cambio de pendiente en el tercer punto, lo que muestra que conviene conservar tres factores. Esto quiere decir que las once preguntas sobre formación disciplinar no son once temas separados, sino tres grandes grupos de competencias.

La tabla de resultados muestra cómo se agrupan esas preguntas y cuánto aporta cada una a su respectivo factor.
<p align="center">
  <img width="920" height="508" alt="Figura 6. Tabla de cargas factoriales para Formación Disciplinar" src="https://github.com/user-attachments/assets/9c8f3979-d2dc-451d-881b-c438e11242df" />
  <br>
  <strong>Figura 6.</strong> Tabla de cargas factoriales para Formación Disciplinar
</p>

En la tabla, los valores sombreados en color amarillo indican las variables que tienen la mayor relación con cada grupo, o sea, las que más peso tienen dentro de cada factor. En el primer factor, marcado en amarillo, se concentran las **competencias académicas**, como las cognitivas, digitales, de inglés, de investigación y de gestión comunitaria. Este grupo refleja lo que se aprende directamente en el programa.

El segundo factor reúne la **percepción de los egresados sobre la calidad del programa**, especialmente qué tan pertinente y suficiente sienten la formación recibida. Por último, el tercer factor agrupa los **logros y la proyección profesional**, como haber liderado proyectos, recibir premios o pertenecer a un gremio.

Podemos decir que la formación disciplinar se organiza en tres dimensiones principales: lo que se aprende, cómo se valora y cómo se aplica después de graduarse. Esta forma de agrupar la información permite entender mejor la formación profesional y resumirla en tres indicadores simples, en lugar de once variables separadas.

---

#### Hallazgo 3: Movilidad Social  

Esta tabla permite ver la relación entre dos aspectos importantes de la calidad de vida los cuales son: si los egresados hoy ganan más dinero que cuando estudiaban y si su vivienda ha mejorado.

<p align="center">
  <img width="1255" height="173" alt="Figura 7. Tabla de contingencia para Movilidad Social" src="https://github.com/user-attachments/assets/60f0bd86-98e1-4a2d-8351-2666e1e3a0fb" />
  <br>
  <strong>Figura 7.</strong> Tabla de contingencia para Movilidad Social
</p>

Lo primero que se nota es que la mayoría de las personas respondió “sí” en ambas con un total de 550 casos, lo que muestra que quienes mejoran sus ingresos también suelen tener una mejor vivienda. El segundo grupo más grande con 265 personas dijo que sí aumentó sus ingresos, pero todavía no ve una mejora en su vivienda, lo que podría significar que el cambio económico aún no se refleja por completo en sus condiciones habitacionales.

Por otro lado, 218 personas respondieron “no” en ambos casos, lo que indica que no han tenido mejoras ni en ingresos ni en vivienda, y 93 personas dijeron que su vivienda mejoró, aunque sus ingresos no aumentaron, algo menos común en los resultados.

La prueba estadística de Chi-Cuadrado confirmó que el resultado fue significativo, lo que muestra que sí existe una conexión real entre tener mayores ingresos y mejorar la vivienda. Cuando la situación económica de los egresados mejora, también tienden a mejorar sus condiciones de vida, especialmente en el lugar donde viven.

---

#### Hallazgo 4: Calidad de Vida  

<p align="center">
  <img width="601" height="365" alt="Figura 8. Gráfico de Sedimentación para Calidad de Vida" src="https://github.com/user-attachments/assets/ab0e8b1c-8e98-4e88-9dc8-cc4af67d17c2" />
  <br>
  <strong>Figura 8.</strong> Gráfico de Sedimentación para Calidad de Vida
</p>


<img width="407" height="149" alt="Figura 9. Tabla de cargas factoriales para Calidad de Vida" src="https://github.com/user-attachments/assets/d7723dd1-d8f7-4de6-a7cc-92e6094de7bc" />


Este análisis muestra cómo la formación universitaria ha influido en distintos aspectos personales y laborales.  
Todas las preguntas se agrupan en un solo factor, lo que significa que cuando mejora un aspecto (por ejemplo, los ingresos), tienden a mejorar también otros (empleo, salud, recreación, bienestar general).

A este conjunto lo llamamos **“Percepción general de mejora en la calidad de vida”**.

---

### Conclusión de la etapa  

Con este análisis logramos pasar de muchos datos dispersos a un modelo claro y organizado.  
Identificamos cinco grandes factores que resumen todo el impacto de los graduados: **competencias transversales, formación disciplinar, movilidad social, calidad de vida y otros indicadores de apoyo.**

Con esa información, construimos una base con **959 registros y siete variables clave**, que ahora nos permite analizar y comprender mejor los diferentes perfiles de impacto.

El siguiente paso consistió en **agrupar a los egresados por similitudes**, para identificar diferentes tipos o **arquetipos** según su nivel de impacto.  
Esto permitió pasar del análisis numérico a una visión más humana y narrativa.

---

(👉 Aquí seguiría la sección **3. Identificación de Arquetipos**, con sus propias figuras y descripciones detalladas de cada perfil).

