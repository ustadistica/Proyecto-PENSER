# Verificación de Consistencia entre Power BI y Base de Datos Depurada

Dentro del proyecto “Construcción de Referentes Metodológicos para la Evaluación de Impacto del Perfil de Egreso en Programas de América Latina”, se llevó a cabo una verificación de los resultados presentados en el Power BI elaborado por PENSER con respecto a la información contenida en la base depurada SANTO TOMÁS_ESTUDIO PENSER_MAYO DE 2025.  

La base de datos corresponde a una encuesta aplicada a 1.129 egresados de la Universidad Santo Tomás, seleccionados mediante un muestreo aleatorio simple a partir de una población de 52.556 graduados. El propósito de esta revisión fue identificar posibles inconsistencias entre los resultados publicados en el tablero de visualización y los datos originales en Excel.  

La encuesta estuvo estructurada en cuatro secciones que agrupaban las preguntas por áreas temáticas:  

I. Desarrollo de Competencias Disciplinares  
II. Desarrollo de Competencias Transversales  
III. Movilidad Social  
IV. Calidad de Vida  

Durante el proceso de verificación, cuyo propósito fue contrastar los datos presentados en el Power BI con los registros originales de la base depurada en Excel, se evidenció que, si bien los conteos absolutos tienden a coincidir, existen inconsistencias en el cálculo de porcentajes, en la omisión de celdas vacías y en algunos aspectos de presentación gráfica. En particular, se observaron algunas inconsistencias como:  

### Distribución por Sede o Seccional

En el Power BI se reporta que 406 egresados pertenecen a la sede Principal Bogotá y DUAD. No obstante, en la base de Excel aparecen únicamente 405 registros válidos, encontrándose una celda vacía en el campo Sede o Seccional y este egresado pertenecía al programa académico correspondiente a Contaduría Pública. Es probable que este caso haya sido clasificado como sede Principal Bogotá y DUAD en Power BI, ya que en la pregunta de Ciudad en la cual cursó sus estudios el egresado indicó Bogotá.  

---

## Sección de DESARROLLO DE COMPETENCIAS DISCIPLINARES

Se encontraron algunas inconsistencias en las siguientes preguntas:  

### Tipo de Vinculación

Se observó que las cantidades de respuestas coinciden entre el Excel y el Power BI; sin embargo, los porcentajes presentados en la visualización no fueron calculados de manera correcta. Adicionalmente, las celdas vacías registradas en la base no se mencionan ni se contabilizan en el tablero. A continuación, se presenta una tabla comparativa en la que se observan los valores reportados en Power BI frente a los obtenidos en el Excel depurado.  

| Tipo de Vinculación | Cantidad Power BI | % Power BI | Cantidad Excel | % Calculado |
|----------------------|------------------|------------|----------------|-------------|
| Contrato laboral a término indefinido | 366 | 41.3% | 366 | 32.41% |
| Contrato laboral prestación de servicios | 233 | 26.3% | 233 | 20.63% |
| Contrato laboral a término fijo | 212 | 23.9% | 212 | 18.77% |
| Propietario de la empresa | 76 | 8.57% | 76 | 6.73% |
| Celdas vacías |   |   | 242 | 21.43% |

---

### Tipo de Cargo

De manera similar que la pregunta anterior las cantidades absolutas entre Excel y Power BI son correctas, pero nuevamente los porcentajes difieren de los valores reales. Se repite también la parte de las celdas vacías registradas en la base no se mencionan ni se contabilizan en el tablero, lo cual genera un sesgo en la presentación de los resultados. La siguiente tabla muestra la comparación de los resultados entre el Power BI y los datos del Excel.  

| Tipo de Cargo | Cantidad Power BI | % Power BI | Cantidad Excel | % Calculado |
|---------------|------------------|------------|----------------|-------------|
| Profesional | 635 | 71.59% | 635 | 56.24% |
| Directivo | 127 | 14.32% | 127 | 11.24% |
| Operativo | 50 | 5.54% | 50 | 4.42% |
| Técnico | 44 | 4.96% | 44 | 3.89% |
| Asistencial | 31 | 3.49% | 31 | 2.75% |
| Celdas vacías |   |   | 242 | 21.43% |

---

## Sección III. MOVILIDAD SOCIAL

Se encontraron algunas inconsistencias en las siguientes preguntas:  

### III.12. Nivel de responsabilidad económica en el hogar

Se encontró que los conteos absolutos entre Excel y Power BI coinciden, pero los porcentajes difieren ligeramente, además de que las celdas vacías no fueron consideradas en la visualización. A continuación, se presenta una tabla comparativa en la que se observan los valores reportados en Power BI frente a los obtenidos en el Excel depurado.  

| Nivel de Responsabilidad | Cantidad Power BI | % Power BI | Cantidad Excel | % Calculado |
|--------------------------|------------------|------------|----------------|-------------|
| Co-proveedor económico | 560 | 49.73% | 560 | 49.60% |
| Proveedor económico | 413 | 36.68% | 413 | 36.58% |
| Dependiente económico | 153 | 13.59% | 153 | 13.55% |
| Celdas vacías |   |   | 3 | 0.26% |

**NOTA:** En el caso de la Pregunta III.13. Máximo nivel de estudios alcanzado se detectó que la gráfica correspondiente aparece duplicada en el tablero, lo cual constituye un error de presentación que podría inducir a confusión en la interpretación de los resultados.  

---

### III.19.1 Condiciones de la vivienda

¿Considera que las condiciones de su vivienda (infraestructura, ubicación, servicios básicos, entre otros) han mejorado desde que obtuvo su título universitario?  

Las cantidades de respuestas coinciden entre el Power BI y la base de datos; no obstante, los porcentajes reportados en Power BI presentan diferencias leves respecto a los cálculos basados en la base depurada. Como en los casos anteriores, las celdas vacías no fueron incluidas en la visualización.  

| Nivel de logro | Cantidad Power BI | % Power BI | Cantidad Excel | % Calculado |
|----------------|------------------|------------|----------------|-------------|
| Sí | 640 | 56.84% | 640 | 56.68% |
| No | 483 | 42.9% | 483 | 42.78% |
| Totalmente de acuerdo | 2 | 0.18% | 2 | 0.17% |
| De acuerdo | 1 | 0.09% | 1 | 0.08% |
| Celdas vacías |   |   | 3 | 0.26% |

---

## Conclusiones

La revisión realizada permitió identificar diversas inconsistencias entre los resultados reportados en Power BI y los datos de la base depurada, principalmente relacionadas con errores en el cálculo de porcentajes, la presencia de celdas vacías y algunos problemas de presentación como la duplicación de gráficas.  

Cabe resaltar que las preguntas no mencionadas en este informe coinciden plenamente tanto en la cantidad de datos como en los porcentajes, por lo que pueden considerarse consistentes.  

Se recomienda que las visualizaciones en Power BI sean revisadas y ajustadas tomando como referencia la base depurada, que se incorporen categorías explícitas para los valores faltantes y que se corrijan los errores de presentación, a fin de garantizar la confiabilidad y precisión de los resultados mostrados.  

---

# Metodologías para reconstruir el Índice de Impacto de Egresados (IIE)

El Índice de Impacto de Egresados (IIE) resume cuatro componentes los cuales son:  
- Formación Disciplinar (FD)  
- Desarrollo de Competencias Interpersonales (DCI)  
- Movilidad Social (MS)  
- Percepción de Mejoramiento de la Calidad de Vida (PMCV)  

La idea central es obtener, para cada persona, un puntaje por cada componente y luego un índice final que combine los cuatro mediante suma ponderada, lo que significa que cada componente se multiplica por un porcentaje (su peso) y después se suman los cuatro resultados.  

La fórmula general es:  

$$
IIE = w_{FD} \cdot FD + w_{DCI} \cdot DCI + w_{MS} \cdot MS + w_{PMCV} \cdot PMCV
$$

donde $FD$, $DCI$, $MS$, $PMCV$ son los puntajes por componente de cada persona y $w_{FD}$, $w_{DCI}$, $w_{MS}$, $w_{PMCV}$ son los porcentajes asignados a cada componente. Para asegurar comparabilidad con el estudio, se mantienen los mismos porcentajes en ambas metodologías.  

---

## Metodología A: Cálculo con los pesos del artículo

Con esta metodología A buscamos replicar el enfoque del artículo. Este ya trae, para cada pregunta y para cada opción de respuesta, un valor numérico por decir ya trae los puntajes para cada opción de respuesta a la encuesta como se puede observar en el Cuadro 1 del artículo *“Enfoque Metodológico para la evaluación de impacto de los y las Egresadas en el Entorno: un Estudio de Caso”*.

![alt text](<cuadro 1.png>)
![alt text](<cuadro 1.1.png>)

Los porcentajes por componente fueron:  
- Formación Disciplinar: 30%  
- Desarrollo de Competencias Interpersonales: 30%  
- Movilidad Social: 20%  
- Percepción del Mejoramiento de la Calidad de Vida: 20%  

Al usar esta metodología nos garantiza que nuestros resultados sigan la misma lógica que usaron los autores y sean directamente comparables con los que ellos reportan.  

### Cómo se aplica, paso a paso

1. Definimos qué preguntas pertenecen a cada componente (FD, DCI, MS, PMCV).  
2. Construcción de los componentes: se usan los valores por opción del Cuadro 1.  
   - Ejemplo: en FD, la pregunta *Vinculación laboral*: Sí = 0.03, No = 0.00.  
3. Para cada persona se lee su respuesta y se suma el valor correspondiente dentro del componente.  
4. Al tener los cuatro componentes calculados (FD, DCI, MS, PMCV), se obtiene el IIE multiplicando cada componente por su porcentaje y sumando:  

   $$
   IIE_{persona} = 0.30 \cdot FD_{persona} + 0.30 \cdot DCI_{persona} + 0.20 \cdot MS_{persona} + 0.20 \cdot PMCV_{persona}
   $$

5. Luego de tener el índice individual por persona (1129 encuestados), se promedia para obtener el IIE general.  
6. El resultado queda en la escala 0–1 (o en porcentaje multiplicando por 100).  

---

## Metodología B: Cálculo con pesos ajustados de las respuestas

En esta metodología B mantenemos la misma estructura del IIE, con los mismos porcentajes globales de ponderación (30%, 30%, 20%, 20%), pero con dos diferencias:  

1. Los pesos asignados a las opciones de respuesta se ajustan bajo un esquema más equitativo.  
2. Se propone un diseño muestral diferente: muestreo estratificado proporcional.  

### Cómo se aplica, paso a paso

- **Definición de preguntas por componente:** igual que en la metodología A.  
- **Asignación de nuevos pesos a las respuestas:**  
  - Preguntas dicotómicas (Sí/No): Sí = 1.00; No = 0.00.  
  - Escalas ordinales: Muy insuficiente = 0.10; Insuficiente = 0.25; Neutral = 0.50; Suficiente = 0.75; Muy suficiente = 1.00.  
  - PMCV: Totalmente en desacuerdo = 0.10; En desacuerdo = 0.25; Neutral = 0.50; De acuerdo = 0.75; Totalmente de acuerdo = 1.00.  
  - Movilidad social: Ascenso = 1.00; Igual = 0.50; Descenso = 0.10.  
- **Construcción de los componentes:** se leen las respuestas y se calcula el puntaje de cada bloque (FD, DCI, MS, PMCV) en escala 0–1.  
- **Cálculo del IIE individual:**  

  $$
  IIE_{persona} = 0.30 \cdot FD_{persona} + 0.30 \cdot DCI_{persona} + 0.20 \cdot MS_{persona} + 0.20 \cdot PMCV_{persona}
  $$

- **Cálculo del IIE general:** se promedia sobre los 1129 egresados.  
- **Cambio en el diseño muestral:** muestreo estratificado proporcional según sede/seccional y programa académico, seleccionando un número proporcional al tamaño de cada estrato.  
- **Interpretación:** el índice se expresa en escala 0–1 o como porcentaje.  

La ventaja de esta metodología es doble: introduce una ponderación más balanceada en las respuestas y, al mismo tiempo, mejora la representatividad de la muestra.  
