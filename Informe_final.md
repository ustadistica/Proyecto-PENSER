<div align="center">

# Un Proyecto del Consultorio de Estadística y Ciencia de Datos
## Del Índice a los Arquetipos  

Proyecto del curso <b>Consultoría e Investigación</b> – Facultad de Estadística  
<b>Universidad Santo Tomás</b> · <b>Octavo Semestre (2025-2)</b>

<br/>

<b>Equipo:</b> Yeimy Alarcón · Karen Suarez · Maria José Galindo 

</div>

> **Estado:** En progreso · **Repositorio:** _[Link Repositorio](https://github.com/ustadistica/Proyecto-PENSER.git)_ · **Última actualización:** 2025-11-17

**Un nuevo modelo metodológico que transita desde la reconstrucción de un índice unidimensional hacia un modelo multidimensional que revela los perfiles complejos y diversos de nuestros graduados.**

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

$$
\textbf{IIE = (0.30 \times FD) + (0.30 \times DCI) + (0.20 \times MS) + (0.20 \times PMCV)}
$$

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
Por eso, decidimos usar un método más flexible llamado **Análisis Factorial Exploratorio (AFE)**, que nos permitió descubrir cómo se relacionaban realmente las respuestas de los egresados.

En lugar de aplicar una fórmula fija, dejamos que **los propios datos "hablaran"** y mostraran su estructura, ayudándonos a entender qué aspectos explican mejor el impacto de la formación universitaria.

(En palabras simples, este método sirve para encontrar patrones escondidos dentro de muchas preguntas. En lugar de ver cada respuesta por separado, agrupa las que significan cosas parecidas y nos muestra las ideas principales que comparten).

---

### Metodología

El siguiente diagrama muestra las etapas seguidas para aplicar el análisis factorial exploratorio:


<p align="center">
  <img width="192" height="410" alt="Figura 2. Diagrama explicativo metodología" src="https://github.com/user-attachments/assets/28b4f844-5b1a-4b73-8063-415cca8f8f40" />
  <br>
  <strong>Figura 2.</strong> Diagrama explicativo metodología
</p>



Primero limpiamos y transformamos los datos para que pudieran analizarse correctamente.  
Convertimos las respuestas escritas en texto como “Muy alto”, “De acuerdo” o “Sí” en números del 1 al 5 (donde 5 es nivel alto y 1 es nivel bajo).  
También corregimos errores de escritura, espacios vacíos y respuestas duplicadas para dejar una base coherente.

Luego aplicamos dos pruebas estadísticas que nos indicaron si los datos servían para este tipo de análisis:

- **Prueba de Bartlett:** verifica si las preguntas están relacionadas entre sí (resultado: significativo, p < 0.001).  
- **KMO (Kaiser-Meyer-Olkin):** mide la calidad de los datos (resultados: 0.93, 0.86 y 0.88, lo cual es excelente).  

Con estos resultados confirmamos que los datos eran confiables y se podía continuar con el análisis.

---

### Resultados de la Segunda Etapa  

#### Hallazgo 1: Competencias transversales  


<p align="center">
  <img width="722" height="442" alt="Figura 3. Gráfico de Sedimentación para Competencias Transversales" src="https://github.com/user-attachments/assets/f1caee16-782b-477d-a575-a77b4f4adb5a" />
  <br>
  <strong>Figura 3.</strong> Gráfico de Sedimentación para Competencias Transversales
</p>


Estas competencias son las **habilidades blandas** que ayudan a las personas a relacionarse y actuar en diferentes entornos (comunicación, resolución de problemas, manejo del estrés).  
El gráfico de sedimentación mostró que todas las competencias se agrupan en un solo gran conjunto, lo que significa que miden una misma capacidad general.  


<p align="center">
  <img width="367" height="187" alt="Figura 4. Tabla de cargas factoriales para Competencias Transversales" src="https://github.com/user-attachments/assets/f9e8e5e3-3404-4bea-a147-6bfa8ddd33f8" />
  <br>
  <strong>Figura 4.</strong> Tabla de cargas factoriales para Competencias Transversales
</p>



(Todas las variables tienen valores altos entre 0.80 y 0.89, lo cual indica una fuerte relación entre ellas).  
Por eso lo llamamos **“Factor General de Competencias Transversales”**: cuando alguien mejora una de estas habilidades, usualmente mejora las demás también.

---

#### Hallazgo 2: Formación disciplinar  

<p align="center">
  <img width="601" height="365" alt="Figura 5. Gráfico de Sedimentación para Formación Disciplinar" src="https://github.com/user-attachments/assets/6c02fb2c-690f-4ede-9f8e-11307c0af649" />
  <br>
  <strong>Figura 5.</strong> Gráfico de Sedimentación para Formación Disciplinar
</p>



Estas competencias reflejan lo que los egresados aprendieron en su carrera: conocimientos técnicos, académicos y prácticos.  
El análisis mostró tres grandes grupos de competencias en lugar de once variables separadas.


<p align="center">
  <img width="373" height="206" alt="Figura 6. Tabla de cargas factoriales para Formación Disciplinar" src="https://github.com/user-attachments/assets/dded9331-3ebc-4f62-b7e3-3c9ea82ee249" />
  <br>
  <strong>Figura 6.</strong> Tabla de cargas factoriales para Formación Disciplinar
</p>



Los tres grupos son:

1. **Competencias académicas:** cognitivas, digitales, inglés, investigación, gestión comunitaria.  
2. **Percepción de calidad:** qué tan pertinente y suficiente sienten la formación recibida.  
3. **Logros profesionales:** liderazgo, premios, pertenencia a gremios.  

En resumen: la formación disciplinar se organiza en tres dimensiones principales: **lo que se aprende, cómo se valora y cómo se aplica después de graduarse.**

---

#### Hallazgo 3: Movilidad Social  


<p align="center">
  <img width="479" height="66" alt="Figura 7. Tabla de contingencia para Movilidad Social" src="https://github.com/user-attachments/assets/adec8dce-723f-4abe-b362-96a18542b167" />
  <br>
  <strong>Figura 7.</strong> Tabla de contingencia para Movilidad Social
</p>


Aquí analizamos si los egresados **ganan más dinero** que cuando estudiaban y si **su vivienda ha mejorado**.  
La mayoría respondió “sí” en ambos casos (550 personas), lo que muestra una relación clara entre mejores ingresos y mejor vivienda.  
La prueba de **Chi-Cuadrado** confirmó que esta relación es estadísticamente significativa.

(En términos sencillos, cuando mejora la situación económica, también mejora la calidad de vida).

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

