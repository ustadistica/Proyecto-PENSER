# Informe sobre la Reconstrucción y Proyección del Modelo de Impacto de Egresados 

### \# Introducción

El análisis de los diferentes documentos revisados —presentaciones institucionales, artículos académicos y bases de datos depuradas— permite evidenciar el trabajo desarrollado en torno a la evaluación del impacto de los egresados universitarios. Dichos insumos muestran un proceso sistemático orientado a medir la pertinencia de la formación, su relación con la empleabilidad y la movilidad social, así como los efectos en la calidad de vida de los graduados.

De manera transversal, todos los materiales coinciden en la relevancia del **Índice de Impacto de Egresados (IIE)** como herramienta central para sintetizar y cuantificar los resultados. Este índice articula cuatro dimensiones fundamentales: **Formación Disciplinar (FD)**, **Desarrollo de Competencias Interpersonales (DCI)**, **Movilidad Social (MS)** y **Percepción de Mejora en la Calidad de Vida (PMCV)**. El modelo de impacto propuesto establece que el IIE se obtiene como una combinación lineal de estas dimensiones, ponderadas según su importancia relativa, permitiendo obtener un indicador normalizado y comparable.

La reconstrucción de la experiencia muestra que la aplicación del modelo por parte de **PENSER** y la **Universidad Santo Tomás** permitió identificar fortalezas y retos. Entre los logros más destacados se encuentran los altos niveles de empleabilidad (superiores al 75%), la percepción positiva respecto a las competencias cognitivas disciplinares y la valoración del impacto de la formación en la calidad de vida. Al mismo tiempo, se detectaron debilidades persistentes en bilingüismo, competencias digitales y la necesidad de mayor énfasis en emprendimiento e internacionalización.

Asimismo, la evidencia recopilada señala que el modelo no solo permite evaluar resultados inmediatos, como la tasa de ocupación o el tipo de contrato, sino también impactos más profundos en la trayectoria vital de los egresados, reflejados en el ascenso de estrato socioeconómico, el aumento de ingresos o la superación del nivel educativo de los padres. Estos elementos confirman que la educación universitaria tiene un efecto transformador que trasciende el ámbito académico y se proyecta en la vida social y cultural de los graduados.

## Verificación de consistencia entre Power BI y la base de datos depurada

En el marco del proyecto se llevó a cabo un proceso de verificación de los resultados presentados en el tablero de **Power BI** elaborado por PENSER, en contraste con la información contenida en la base depurada **SANTO TOMÁS_ESTUDIO PENSER_MAYO DE 2025**.

La base corresponde a una encuesta aplicada a **1.129 egresados**, seleccionados mediante **muestreo aleatorio simple** a partir de una población de **52.556 graduados**.

El objetivo de esta verificación fue determinar el nivel de consistencia entre los datos reportados en las visualizaciones y los registros originales, así como identificar posibles sesgos derivados del manejo de porcentajes, valores faltantes y elementos gráficos.

La revisión permitió establecer que los **conteos absolutos** tienden a coincidir entre Power BI y la base en Excel. No obstante, se detectaron inconsistencias recurrentes en el cálculo de porcentajes, la omisión de celdas vacías y algunos errores de presentación.

### Principales hallazgos:

-   Diferencia de un caso en la distribución por sede en Bogotá y DUAD (406 en Power BI vs. 405 en Excel), atribuible a una celda vacía reclasificada.\
-   En el **tipo de vinculación laboral**, los porcentajes en Power BI fueron calculados excluyendo las 242 celdas vacías, lo que sobredimensiona la participación de los contratos indefinidos (41,3% vs. 32,4%).\
-   En el **tipo de cargo**, los conteos coinciden, pero los porcentajes están sobrestimados, reportando el cargo “Profesional” en 71,6% frente al 56,2% real.\
-   En la sección de **movilidad social**, los porcentajes difieren levemente y las respuestas faltantes no se consideraron en las gráficas.\
-   En la pregunta sobre **nivel máximo de estudios alcanzado**, se detectó un error de duplicación de la gráfica en Power BI.\
-   En la valoración de las **condiciones de vivienda**, aunque los conteos coinciden, los porcentajes presentan pequeñas diferencias respecto a los cálculos en Excel y nuevamente no se incluyen los valores faltantes.

**Conclusión de la verificación:**\
Aunque la información base es consistente en términos de conteos absolutos, las visualizaciones en Power BI presentan sesgos debido a errores en los porcentajes, exclusión de valores faltantes y problemas de presentación gráfica. Se recomienda ajustar los cálculos, incorporar categorías explícitas para las respuestas vacías y corregir los errores de duplicación, a fin de garantizar la confiabilidad de los resultados mostrados.

Este ejercicio de verificación constituye un insumo clave dentro de la fase de reconstrucción del proyecto, ya que permite depurar el modelo de análisis y garantizar que el IIE se calcule sobre bases metodológicas sólidas y visualizaciones confiables.

## Fase I. Reconstrucción del modelo de impacto

En esta fase, el equipo asumirá la tarea de sistematizar y narrar de manera integral la experiencia previa. Esto implica:

1.  Documentar el modelo de impacto y el funcionamiento del IIE, explicando con claridad sus dimensiones, variables y fórmula de cálculo.\
2.  Sistematizar los hallazgos obtenidos en las aplicaciones previas, tanto a nivel de resultados cuantitativos (empleabilidad, ingresos, movilidad social) como cualitativos (percepciones de pertinencia y calidad de vida).\
3.  Incorporar la verificación de consistencia, mostrando cómo la revisión de Power BI frente a la base depurada permitió corregir errores y asegurar la calidad metodológica.\
4.  Identificar aprendizajes clave sobre fortalezas y limitaciones del modelo.\
5.  Generar un informe comparativo que muestre cómo los egresados perciben su proceso formativo y cuáles han sido las transformaciones más significativas en sus vidas.

## Fase II. Muestreo y proyección del modelo

La segunda parte del proyecto corresponde a un nuevo ejercicio de muestreo, que busca ampliar y actualizar los hallazgos obtenidos en la reconstrucción. Mientras la fase inicial se centra en recuperar y documentar la experiencia de PENSER, la fase de muestreo permitirá validar el modelo de impacto con información fresca y representativa.

El diseño muestral se plantea como un **muestreo aleatorio simple**, ajustado a la disponibilidad de información actualizada de los egresados en la base institucional.

Este proceso permitirá:\
- Replicar el cálculo del IIE con nuevas cohortes de graduados.\
- Comparar resultados frente a los obtenidos en el estudio de PENSER para identificar cambios en tendencias de empleabilidad, ingresos, movilidad social y calidad de vida.\
- Refinar el modelo de impacto, incorporando ajustes metodológicos como análisis factorial, construcción de perfiles mediante k-medias y exploración de modelos explicativos.\
- Consolidar un sistema de seguimiento continuo, que no dependa de una aplicación aislada, sino que se proyecte como un mecanismo institucional de evaluación del egresado.

## Conclusión

El proyecto se estructura, por tanto, en **dos momentos complementarios**:

-   **Reconstrucción**, que sistematiza y valida la experiencia previa, corrige inconsistencias y documenta la base conceptual y metodológica del modelo de impacto.\
-   **Muestreo**, que extiende y actualiza la aplicación del modelo, consolidando el IIE como una herramienta institucional para evaluar la trayectoria y el aporte de los egresados.

Con esta doble estrategia se asegura no solo la preservación del conocimiento generado, sino también la proyección de un modelo sólido y sostenible que oriente la toma de decisiones estratégicas en torno a la formación universitaria y el impacto real de los graduados en la sociedad.
