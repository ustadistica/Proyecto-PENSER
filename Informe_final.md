<div align="center">

# Un Proyecto del Consultorio de Estadística y Ciencia de Datos 📊📝🏗️ Del Índice a los Arquetipos  

Proyecto del curso <b>Consultoría e Investigación</b> – Facultad de Estadística  
<b>Universidad Santo Tomás</b> · <b>Octavo Semestre (2025-2)</b>
<br/>

<b>Equipo:</b> Yeimy Alarcón · Karen Suarez · Maria José Galindo 

</div>

> **Estado:** En progreso · **Repositorio:** _[Link Repositorio](https://github.com/ustadistica/Proyecto-PENSER.git)_ · **Última actualización:** 2025-11-17

*Un nuevo modelo metodológico que transita desde la reconstrucción de un índice unidimensional hacia un modelo multidimensional que revela los perfiles complejos y diversos de nuestros graduados.*

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

#### Hallazgo 4: Calidad de Vida  

En este bloque analizamos las preguntas relacionadas con la calidad de vida de los egresados, que muestran cómo su formación universitaria ha influido en distintos aspectos personales y laborales. Primero comprobamos que los datos fueran adecuados para el análisis, y los resultados fueron muy buenos obteniendo un KMO = 0.88 y Bartlett significativo.

<p align="center">
  <img width="758" height="459" alt="Figura 8. Gráfico de Sedimentación para Calidad de Vida" src="https://github.com/user-attachments/assets/e1a91004-ba19-4181-a953-1002b5de8444" />
  <br>
  <strong>Figura 8.</strong> Gráfico de Sedimentación para Calidad de Vida
</p>

En el gráfico de sedimentación se observa una caída muy marcada en el primer punto y luego una línea casi plana, lo que muestra que todas las variables se agrupan en un solo factor.

<p align="center">
  <img width="1252" height="454" alt="Figura 9. Tabla de cargas factoriales para Calidad de Vida" src="https://github.com/user-attachments/assets/335e3ce6-ae11-453c-bbdd-a8aed45712f2" />
  <br>
  <strong>Figura 9.</strong> Tabla de cargas factoriales para Calidad de Vida
</p>

La tabla de resultados confirma que todas las preguntas tienen valores altos y muy parecidos (entre -0.70 y -0.79), lo que muestra que todas se mueven en la misma dirección. Cuando un egresado siente que su formación le ayudó a mejorar sus ingresos, casi siempre también nota mejoras en su empleo, vivienda, salud, educación, recreación y bienestar en general.

Estos resultados muestran que los distintos aspectos de la calidad de vida están conectados y forman un solo gran conjunto, al que llamamos **“Percepción general de mejora en la calidad de vida”**. En general, la formación universitaria no solo influye en el trabajo o los ingresos, sino que también tiene un impacto positivo más amplio, que se refleja en varios ámbitos de la vida de los egresados.


### Conclusión de la etapa  

Con este análisis logramos pasar de tener muchos datos sueltos a un modelo claro y organizado. Identificamos cinco grandes factores que resumen todo el impacto de los graduados: **competencias transversales, formación disciplinar, movilidad social, calidad de vida y otros indicadores de apoyo**. Con eso construimos una base final con **959 registros y siete variables clave**, que ahora nos permite analizar y tomar decisiones de una forma mucho más ordenada y precisa.

Con esta última parte empezamos una nueva etapa del proyecto. Ahora que ya tenemos la base de datos limpia y los factores definidos, el siguiente paso es **agrupar a los graduados por perfiles parecidos**. Esto nos va a permitir identificar distintos tipos de graduados según su nivel de impacto y diseñar estrategias más claras para comunicarnos con ellos, hacer seguimiento o crear políticas que respondan mejor a sus realidades.


---

# 3. Identificación de Arquetipos

*(Una comprensión humana y estructurada de los perfiles de nuestros graduados )*

Con la base de datos depurada y las dimensiones estadísticas ya definidas, procedo a la etapa de identificación de arquetipos, cuyo propósito es caracterizar grupos de graduados que comparten patrones similares en sus trayectorias, percepciones y condiciones posteriores a la finalización de sus estudios.

Los arquetipos no son categorías rígidas; más bien representan perfiles derivados directamente del comportamiento de los datos. Permiten organizar la variabilidad observada de manera clara y comprensible.

---

## Objetivo de esta etapa

- Transformar los resultados estadísticos en perfiles interpretables.
- Identificar grupos con características similares.
- Describir cada arquetipo a partir de sus puntuaciones promedio en las dimensiones analizadas.

---

## Resumen del procedimiento (paso a paso)

1. **Preparación de datos**  
   Se seleccionaron las observaciones con información completa en las dimensiones clave. Las variables fueron estandarizadas para garantizar comparabilidad y se utilizaron las puntuaciones factoriales como insumo del agrupamiento, con el fin de trabajar con un conjunto reducido de dimensiones más estables.

2. **Método de agrupamiento**  
   Se evaluaron distintos algoritmos, incluyendo métodos particionales, jerárquicos y modelos de mezcla. La elección final se basó en la claridad interpretativa y en la coherencia interna de los grupos

3. **Selección del número de clusters**  
   Se emplearon criterios como la gráfica del codo y el índice de Silhouette para determinar una solución adecuada. La elección final buscó un equilibrio entre calidad estadística y facilidad de interpretación.

4. **Validación y robustez**  
   Se revisó la estabilidad de la clasificación con múltiples corridas del algoritmo y análisis de sensibilidad. Se prestó atención a los casos ubicados en los límites entre grupos para evitar sobreinterpretaciones..

5. **Interpretación y etiquetado**  
   Los grupos fueron descritos a partir de las medias de cada factor y de variables complementarias que permitieron dar sentido a las diferencias observadas.

---

## Dimensiones utilizadas

El análisis se basó en las puntuaciones factoriales de las siguientes dimensiones:

- **Competencias transversales** (comunicación, trabajo en equipo, pensamiento crítico, etc.)  
- **Formación disciplinar** (y sus 3 subdimensiones operativas)  
- **Movilidad social** (cambios en ingresos, ascensos, estabilidad laboral)  
- **Calidad de vida** (vivienda, salud autopercibida, bienestar)  
- **Indicadores complementarios** (tipo de vínculo laboral, informalidad, responsabilidades familiares)

---

## Resultado: cinco arquetipos (descripción ampliada y acciones sugeridas)

### Arquetipo 1 — *El Profesional Integral y Ascendente*  
Este grupo presenta puntuaciones altas en la mayoría de las dimensiones. Los graduados que lo conforman describen una experiencia formativa positiva, acompañada de resultados favorables tanto en el ámbito laboral como en su calidad de vida. La percepción del impacto académico tiende a ser alta y consistente.

En general, este arquetipo representa trayectorias donde la formación y el desarrollo posterior muestran correspondencia clara.

---

### Arquetipo 2 — *El Técnico Fuerte con Crecimiento Moderado*  
Los integrantes de este grupo destacan principalmente por su sólida formación disciplinar y capacidades técnicas. Las competencias transversales tienen valores intermedios y su trayectoria laboral muestra un crecimiento sostenido pero más gradual.

Su perfil refleja un avance progresivo, donde la base académica técnica constituye el elemento más relevante en su desarrollo.

---

### Arquetipo 3 — *El Persistente con Limitaciones Estructurales*  
Este arquetipo se caracteriza por presentar resultados intermedios en formación y competencias, pero niveles bajos en movilidad social. Las mejoras económicas y laborales son más lentas, influenciadas principalmente por condiciones del entorno.

El grupo refleja trayectorias donde la formación no se traduce inmediatamente en cambios significativos, debido a factores externos o contextuales.

---

### Arquetipo 4 — *El Profesional Valioso con Reconocimiento Bajo*  
Este grupo presenta altas competencias transversales, lo que sugiere habilidades sólidas en ámbitos como comunicación, resolución de problemas y trabajo en equipo. Sin embargo, sus valoraciones sobre la formación disciplinar son más bajas, especialmente en cuanto a su pertinencia para el entorno laboral.

La percepción general es que su desempeño profesional se apoya más en sus capacidades personales que en contenidos estrictamente académicos.

---

### Arquetipo 5 — *El En Riesgo o Desconectado*  
Es el grupo con los puntajes más bajos en prácticamente todas las dimensiones. La percepción del impacto formativo es limitada y predominan condiciones laborales más inestables o informales.

Este arquetipo refleja trayectorias donde la conexión entre la formación y los resultados posteriores es débil o se ve afectada por restricciones externas significativas.

---

## Robustez y límites de la clasificación

El análisis mostró una estructura relativamente estable de cinco grupos, los cuales se mantuvieron consistentes bajo variaciones del método y del conjunto de variables empleadas.Sin embargo, como en todo proceso de agrupamiento, los arquetipos representan tendencias generales y no sustituyen el análisis individual de cada caso. Existen graduados con perfiles intermedios o cambiantes que pueden situarse cerca de los límites entre dos grupos.


---



## Cierre — ¿qué aporta esta etapa?

La identificación de arquetipos permite sintetizar de manera clara la diversidad de trayectorias observadas entre los graduados. Los cinco perfiles obtenidos proporcionan una comprensión más detallada del impacto de la formación y de la multiplicidad de experiencias posteriores, sin reducir la realidad a un único indicador o promedio.

---

# Análisis de Arquetipos de Graduados USTA

En esta etapa del proyecto se desarrolló un análisis integral de los arquetipos de graduados de la Universidad Santo Tomás, con el propósito de comprender los distintos perfiles que surgen a partir del impacto de la formación universitaria en su vida profesional y personal.

Estas visualizaciones facilitaron una lectura más clara del comportamiento de cada grupo, revelando patrones relevantes: la concentración de perfiles exitosos en determinadas carreras, la evolución de los arquetipos en el tiempo, y las diferencias entre bienestar material y satisfacción percibida.

---

## Distribución de arquetipos por seccional

_Esta gráfica permite identificar cómo varía la composición de los cinco arquetipos entre las seccionales de la Universidad Santo Tomás. Analizar estas diferencias ayuda a comprender cómo influyen los contextos regionales en el tipo de profesional que forma cada sede, orientando decisiones académicas y de acompañamiento específicas._

<img width="620" height="352" alt="image" src="https://github.com/user-attachments/assets/44fef2c8-7184-447a-a85c-45b51749f4ca" />

En esta gráfica se observa cómo se distribuyen los diferentes perfiles de graduados en cada seccional de la Universidad Santo Tomás. En todas las sedes predomina el Arquetipo 1 (El Profesional Exitoso y Crítico), lo que muestra una tendencia general hacia graduados con alto desarrollo de competencias y logros materiales, pero con una percepción más analítica y exigente frente al impacto de su formación.

La Sede Principal Bogotá y DUAD presenta la mayor diversidad de perfiles, con una proporción importante del Arquetipo 0 (Subjetivamente Satisfecho) y una participación más visible del Arquetipo 4 (Líder de Alto Desempeño). En cambio, seccionales como Tunja y Villavicencio tienen una composición más concentrada en los arquetipos 1 y 3, reflejando perfiles en consolidación profesional y con percepción positiva, aunque moderada, sobre su calidad de vida.

---

## Tasa de mejora (ingresos y vivienda) por arquetipo

_Esta comparación revela qué tan tangible ha sido el impacto de la formación universitaria en las condiciones de vida de los graduados. Relacionar el tipo de arquetipo con la mejora de ingresos y vivienda permite identificar qué grupos alcanzan mayor movilidad social y cuáles requieren más acompañamiento institucional._

<img width="687" height="361" alt="image" src="https://github.com/user-attachments/assets/3f6abb8f-a051-472a-9637-febd3f410677" />

Esta gráfica compara el porcentaje de graduados que reportaron haber mejorado sus ingresos y su vivienda según el arquetipo al que pertenecen. Se observa que los Profesionales Exitosos y Críticos (Arquetipo 1) y los Profesionales en Transición (Arquetipo 3) son los grupos con mejores resultados económicos: casi todos aumentaron sus ingresos, aunque el Arquetipo 3 no refleja la misma mejora en vivienda.

El Líder de Alto Desempeño (Arquetipo 4) también presenta altos niveles de progreso material, lo que confirma su perfil de éxito y estabilidad. Por otro lado, el Egresado Agradecido (Arquetipo 2) muestra un avance moderado, con una mayoría que mejoró ingresos, pero no tanto su vivienda. Finalmente, el Subjetivamente Satisfecho (Arquetipo 0) es el grupo con menor crecimiento económico, ya que pocos reportan mejoras en estas dimensiones.

---

## Distribución de arquetipos por carrera/programa

_La comparación por carrera permite detectar programas donde predominan ciertos tipos de graduados, lo que ayuda a las facultades a comprender mejor los impactos diferenciados de la formación y a diseñar estrategias de mejora curricular o de acompañamiento profesional específicas._

<img width="708" height="338" alt="image" src="https://github.com/user-attachments/assets/d76992b8-852e-4d13-9743-bfd987c945d3" />

Esta gráfica muestra cómo se distribuyen los distintos perfiles de graduados en las carreras con mayor participación dentro del estudio. En general, el Arquetipo 1 (Profesional Exitoso y Crítico) predomina en casi todos los programas, lo que sugiere que la mayoría de los graduados han alcanzado estabilidad económica y laboral, aunque mantienen una postura exigente frente al impacto de su formación.

Carreras como Administración de Empresas, Contaduría Pública e Ingeniería Civil presentan una fuerte concentración de este perfil, seguido del Arquetipo 3 (Profesional en Transición), que representa a graduados en proceso de consolidar su desarrollo profesional. Por otro lado, programas como Odontología y Tecnología en Laboratorio Dental muestran mayor presencia del Arquetipo 0 (Subjetivamente Satisfecho), reflejando una valoración positiva de su bienestar personal aunque sin grandes mejoras materiales.

---

## Evolución de los arquetipos de graduados entre 2017 y 2024

_Permite ver tendencias en el tiempo: qué perfiles crecen o caen en las cohortes recientes. Esto orienta ajustes curriculares y de acompañamiento según cómo está cambiando la “canasta” de graduados._

<img width="710" height="411" alt="image" src="https://github.com/user-attachments/assets/afccdb13-a4df-40c6-b119-2a13781f14a8" />


Esta gráfica muestra cómo ha cambiado la composición de los diferentes perfiles de graduados a lo largo de los años. Se observa que el Arquetipo 1 (Profesional Exitoso y Crítico) ha mantenido una presencia dominante en casi todas las cohortes, reflejando estabilidad en los perfiles de éxito laboral y económico. Sin embargo, en los años más recientes —especialmente a partir de 2022— aumenta la proporción del Arquetipo 0 (Subjetivamente Satisfecho) y del Arquetipo 3 (Profesional en Transición), lo que indica una tendencia hacia graduados que valoran más su bienestar y se encuentran en procesos de desarrollo profesional.

En contraste, los Arquetipos 2 (Egresado Agradecido) y 4 (Líder de Alto Desempeño) presentan una disminución progresiva, mostrando que cada vez hay menos graduados con perfiles de fuerte gratitud institucional o con logros sobresalientes. En conjunto, la evolución temporal sugiere un cambio generacional: los graduados más recientes tienden a equilibrar la búsqueda de éxito profesional con una mayor satisfacción personal, lo que refleja transformaciones en las expectativas y valores frente al papel de la educación universitaria en su vida.

---
