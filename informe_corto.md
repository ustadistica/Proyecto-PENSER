#  Un Proyecto del Consultorio de Estadística y Ciencia de Datos  
## **Del Índice a los Arquetipos**

> *Un nuevo modelo metodológico que pasa de un índice unidimensional a una visión más amplia y humana sobre el impacto de los egresados de la Universidad Santo Tomás.*

---

##  Introducción

Este informe cuenta el proceso que seguimos para revisar y mejorar el **Índice de Impacto de Egresados (IIE)**, una herramienta del proyecto **PENSER** que busca entender cómo los estudios en la **Universidad Santo Tomás (USTA)** han influido en la vida de sus graduados.

El trabajo se desarrolló en el **Consultorio de Estadística y Ciencia de Datos**, con la idea de verificar si el índice original representaba bien la realidad y si podía replicarse con nuevos datos.  
A partir de ese análisis, construimos una versión más clara, comprensible y cercana, que muestra el impacto de la formación universitaria desde diferentes perspectivas.

El proyecto tuvo tres etapas:

1. **Reconstrucción del índice:** se intentó reproducir el cálculo original del IIE para revisar su claridad y consistencia.  
2. **Nuevo enfoque metodológico:** al encontrar dificultades, se aplicó un método más moderno que permitió descubrir qué aspectos realmente explican el impacto de los egresados.  
3. **Identificación de arquetipos:** con la información obtenida, se crearon cinco tipos o perfiles de egresados, que muestran distintas maneras de vivir el impacto de la formación universitaria.

Este recorrido —desde el índice hasta los arquetipos— ofrece una mirada más completa y humana sobre los egresados, y deja las bases para fortalecer las futuras evaluaciones institucionales.

---

##  **1. Reconstrucción del Índice de Impacto de Egresados (IIE)**

La primera etapa consistió en volver a calcular el **Índice de Impacto de Egresados** exactamente como se había hecho originalmente, para comprobar si se obtenían los mismos resultados.  
Este ejercicio es importante porque permite saber si el modelo es **claro, consistente y reproducible**.

### Cómo se hizo

Usamos la base de datos **“Data Depurada Santo Tomás – Estudio PENSER (mayo 2025)”**, donde están las respuestas de cientos de egresados sobre su formación, su trabajo y su vida después del grado.

El índice se calculaba combinando cuatro aspectos:

<p align="center">
  <b>IIE = (0.30×FD) + (0.30×DCI) + (0.20×MS) + (0.20×PMCV)</b>
</p>

Donde:  
- **FD** significa *Formación Disciplinar* (lo que se aprende en la carrera).  
- **DCI** es *Desarrollo de Competencias Interpersonales* (habilidades blandas, comunicación, liderazgo).  
- **MS** es *Movilidad Social* (mejoras en ingresos o vivienda).  
- **PMCV** es *Percepción de Mejoramiento de la Calidad de Vida*.

Cada parte del índice refleja un tipo de impacto que la universidad podría tener en la vida de los graduados.

### Qué encontramos

- En dos de los cuatro componentes (**DCI** y **PMCV**) los resultados fueron muy parecidos al estudio original.  
- En los otros dos (**FD** y **MS**) hubo dificultades, porque la descripción original no explicaba con claridad cómo se combinaban las variables ni qué hacer con respuestas ambiguas como “No aplica”.

Como resultado, el nuevo cálculo arrojó un **IIE global de 67.5%**, mientras que el estudio original reportaba **72%**.  
Esta diferencia mostró que **el modelo inicial no era completamente claro ni replicable**.

### Qué aprendimos

Al intentar reproducir el índice original, vimos que hacía falta una estructura más sólida y transparente.  
Por eso, el equipo decidió cambiar de enfoque y aplicar una técnica que dejara hablar a los datos por sí mismos, sin imponer fórmulas previas.  
Así nació la segunda etapa: el **análisis factorial exploratorio**.

---

##  **2. Un nuevo enfoque metodológico**

### ¿Por qué cambiar el método?

El índice original trataba de resumir toda la información en una sola cifra.  
Sin embargo, descubrimos que el impacto de la universidad no puede representarse de manera tan simple.  
Por eso, decidimos usar una técnica más flexible, que permitiera ver cómo las respuestas de los egresados se agrupan de forma natural.  
Esa técnica se llama **Análisis Factorial Exploratorio (AFE)**.

### Explicado en palabras sencillas

El **AFE** es una herramienta que sirve para **descubrir patrones dentro de muchos datos**.  
En lugar de mirar cada pregunta por separado, agrupa las que están relacionadas y muestra los grandes temas que hay detrás de ellas.  
Así se pueden identificar las ideas principales, como “habilidades”, “formación”, “calidad de vida”, etc.

### Pasos del proceso

1. **Preparar los datos:**  
   Se transformaron las respuestas escritas (por ejemplo, “Muy alto”, “De acuerdo”) en números del 1 al 5, para poder analizarlas.  
   También se limpiaron errores y se completaron datos faltantes.

2. **Comprobar la calidad:**  
   Antes de hacer el análisis, se aplicaron pruebas estadísticas para asegurarse de que los datos servían.  
   En palabras simples, estas pruebas nos dijeron que las respuestas estaban relacionadas y eran adecuadas para el estudio.

3. **Descubrir los factores:**  
   El análisis mostró que las preguntas no estaban aisladas, sino que se organizaban naturalmente en **grandes grupos o factores**.

### Principales hallazgos

| Tema analizado | Qué se descubrió | Qué significa |
|----------------|------------------|----------------|
| **Competencias transversales** | Todas las habilidades blandas (trabajo en equipo, comunicación, resolución de problemas) se mueven juntas, como un solo gran grupo. | Los egresados perciben estas competencias como una sola capacidad general. |
| **Formación disciplinar** | Las preguntas sobre lo aprendido se agrupan en tres dimensiones: lo que se aprende, cómo se valora y cómo se aplica. | La formación profesional tiene varias capas, no es un bloque único. |
| **Movilidad social** | Hay una relación clara entre mejorar los ingresos y mejorar la vivienda. | Cuando a una persona le va mejor económicamente, suele mejorar también su calidad de vida. |
| **Calidad de vida** | Todos los aspectos de la vida (salud, empleo, ingresos, bienestar) están conectados. | La formación universitaria influye en la vida de los egresados de manera integral. |

### Conclusión de la etapa

Con este análisis, pasamos de tener muchos datos dispersos a un modelo organizado y entendible.  
Identificamos cinco grandes dimensiones que resumen el impacto de los graduados.  
Esta nueva base permitió avanzar hacia una tercera etapa: **descubrir los diferentes tipos de egresados**.

---

##  **3. Identificación de Arquetipos de Egresados**

### 3.1 ¿Qué son los arquetipos?

Un **arquetipo** es una forma de representar a un grupo de personas que comparten características parecidas.  
En este caso, los arquetipos permiten ver los distintos tipos de experiencias de los egresados: cómo viven su éxito, qué valoran de la universidad y cómo ha cambiado su vida.

### 3.2 Cómo se identificaron los arquetipos

1. **Elegimos siete variables** que representaban lo más importante del análisis anterior:  
   competencias, valoración del programa, logros, calidad de vida, ingresos y vivienda.  

2. **Agrupamos a los egresados** según sus similitudes, sin imponer categorías previas.  
   El análisis mostró que existían **cinco grupos naturales** dentro de la población.  

3. **Validamos los resultados**, comprobando que los grupos estuvieran bien separados y que cada uno tuviera sentido desde lo social y lo humano.

El resultado fueron **cinco arquetipos de egresados**, cada uno con su historia, fortalezas y retos.

---

### 3.3 Los Cinco Arquetipos de Egresados

| Arquetipo | % de egresados | Cómo son |
|------------|----------------|-----------|
| **1. Profesional Exitoso y Crítico** | 39 % | Personas con gran éxito profesional y económico, pero exigentes con la universidad. |
| **2. Graduado Agradecido** | 13 % | Aprecian profundamente la formación recibida, aunque sus logros materiales sean modestos. |
| **3. Profesional en Transición** | 17 % | Están creciendo laboralmente; van mejorando, pero aún no alcanzan estabilidad total. |
| **4. Líder de Alto Desempeño** | 12 % | Son referentes en su campo, con logros sobresalientes, aunque suelen ser muy autoexigentes. |
| **5. Subjetivamente Satisfecho** | 19 % | No destacan en logros materiales, pero viven felices y equilibrados. |

---

### 3.4 Descripción de los arquetipos

####  1. El Profesional Exitoso y Crítico
Es el grupo más numeroso.  
Han mejorado sus ingresos y condiciones de vida, y ocupan puestos de responsabilidad.  
Aunque reconocen el valor de su formación, también son exigentes y piensan que la universidad podría adaptarse más a las demandas actuales.  
**Ven su éxito como fruto tanto de la formación como del esfuerzo personal.**

####  2. El Graduado Agradecido
Valoran profundamente lo que aprendieron.  
No todos tienen grandes logros económicos, pero sienten que su paso por la universidad transformó su vida y la de su familia.  
Expresan gratitud, compromiso y sentido de pertenencia institucional.

####  3. El Profesional en Transición
Representa a quienes están en proceso de crecimiento.  
Han mejorado sus ingresos, pero aún no logran estabilidad.  
Ven la formación universitaria como una base importante y mantienen un deseo constante de aprender y avanzar.

####  4. El Líder de Alto Desempeño
Son los egresados más destacados: ocupan posiciones de liderazgo, han recibido reconocimientos y son referentes en su entorno.  
Aun así, suelen ser muy exigentes consigo mismos y no siempre sienten equilibrio entre el éxito profesional y el bienestar personal.

####  5. El Subjetivamente Satisfecho
Son personas que se sienten felices y realizadas, aunque sus ingresos o logros no sean los más altos.  
Para ellos, el éxito se mide más por el bienestar emocional, la estabilidad familiar y las relaciones sociales.

---

### 3.5 Qué nos dicen estos arquetipos

Los cinco arquetipos muestran que **el impacto de la universidad no es uno solo, sino muchos**.  
Algunas personas miden el éxito por los logros materiales; otras, por su bienestar o su crecimiento personal.

- Los arquetipos **1 y 4** representan el éxito profesional y económico.  
- Los **2 y 5** representan la satisfacción emocional y el sentido de pertenencia.  
- El **3** está en medio: es el proceso de crecimiento que viven muchos egresados jóvenes.

En resumen:
- El éxito material no siempre trae felicidad.  
- La gratitud no depende del dinero.  
- Cada historia de impacto es diferente y valiosa.

---

### 3.6 Conclusiones finales

1. El análisis de arquetipos cambió la forma de entender el impacto de los egresados:  
   ya no se trata solo de una cifra, sino de historias, experiencias y trayectorias.  
2. Cada arquetipo representa una manera legítima de éxito e impacto.  
3. Este modelo ayudará a la universidad a **crear estrategias diferenciadas**, como:  
   - Fortalecer la relación con los egresados exitosos y críticos.  
   - Apoyar a los que están en transición profesional.  
   - Reconocer el valor emocional de los agradecidos y satisfechos.  
4. Finalmente, este trabajo deja las bases para un **seguimiento continuo y humano** del egresado, donde los datos sirven para comprender, no solo para medir.

---

 **Fin del Informe – “Del Índice a los Arquetipos”**  
_Consultorio de Estadística y Ciencia de Datos – Universidad Santo Tomás_
