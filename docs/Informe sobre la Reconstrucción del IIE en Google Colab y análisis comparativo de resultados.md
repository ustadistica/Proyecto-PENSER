# Informe sobre la Reconstrucción del Índice de Impacto de Egresados (IIE) implementado en Google Colab y su respectivo análisis comparativo de resultados

## Introducción
Este informe presenta la reconstrucción del Índice de Impacto de Egresados (IIE) implementado en Google Colab a partir de la encuesta aplicada a graduados. El objetivo es medir, con una sola cifra y con cuatro subíndices, qué tanto impacto han tenido los estudios universitarios en diferentes aspectos de la vida del egresado: formación disciplinar (FD), desarrollo de competencias interpersonales (DCI), movilidad social (MS) y percepción de la calidad de vida (PMCV).

Para lograrlo, partimos del archivo en Excel con las respuestas de la encuesta y transformamos cada respuesta en puntos usando los pesos definidos por los autores del artículo (metodología A). Con esos puntajes construimos los cuatro componentes y, luego, el índice general por persona.El cuestionario original tiene 143 preguntas. El estudio base eligió 29 de ellas para construir el IIE y definió los pesos por respuesta. En nuestra implementación utilizamos 26 de esas 29. Las 3 restantes no se incluyeron porque, aunque el artículo sí especifica los pesos, no indica con claridad qué preguntas exactas del cuestionario deben combinarse para cumplir las condiciones de esas variables, y las dejamos explícitamente para revisión. Al final del informe señalamos algunas diferencias que aparecen al comparar nuestros resultados con los de la publicación.

## Método
El IIE se construye con cuatro componentes:
- **Formación disciplinar (FD)** y **Desarrollo de competencias interpersonales (DCI):** miden el aporte de la Universidad a la formación integral del egresado, tanto en conocimientos profesionales como en habilidades clave (comunicación, trabajo con otros, toma de decisiones, etc.).
- **Movilidad social (MS):** observa señales de progreso del egresado asociadas a su formación (p. ej., rol económico en el hogar, cambios en ingresos, y comparación de su escolaridad con la de sus padres).
- **Percepción del mejoramiento de la calidad de vida (PMCV):** recoge cómo la persona percibe que la formación influyó en su bienestar (ingresos, vivienda, acceso a oportunidades y servicios, etc.).

Para cada pregunta, el artículo define un peso por respuesta *(por ejemplo, “Sí” = 0,03)*. Sumamos esos valores por persona dentro de cada componente para obtener los subíndices FD, DCI, MS y PMCV. El índice global se calcula como combinación ponderada, manteniendo la ponderación del estudio:

<p align="center">IIE = 0,30·FD + 0,30·DCI + 0,20·MS + 0,20·PMCV</p>

Con este procedimiento replicamos la metodología original y dejamos anotadas las tres preguntas sin peso claro. Más adelante, el informe muestra y comenta las inconsistencias detectadas al contrastar nuestros resultados con los del artículo.

## Resultados del IIE 
Durante el proceso de verificación, cuyo objetivo fue reconstruir el IIE, aplicando la metodología A y los pesos del Cuadro 1 del artículo Enfoque Metodológico para la Evaluación de Impacto de los y las Egresadas en el Entorno, comparamos nuestros cálculos con los reportados por el estudio. Aunque seguimos la misma lógica de cálculo, encontramos algunas diferencias en los resultados promedio de cada componente y en él % alcanzado respecto al valor esperado que serán especificadas más adelante. A continuación, se presentan nuestros resultados y, componente por componente, se señalan las principales diferencias identificadas.

<div align="center">

### Cuadro 1 – Resultados del índice de impacto de los y las egresadas

| Componente                              | Resultado | Máximo teórico | % alcanzado |
|-----------------------------------------|-----------|----------------|-------------|
| Formación disciplinar                   | 0.143     | 0.33           | 43.255      |
| Desarrollo de competencias interpersonales | 0.231  | 0.30           | 76.856      |
| Movilidad social                        | 0.078     | 0.09           | 86.722      |
| Percepción de la calidad de vida        | 0.151     | 0.20           | 75.394      |
| **Resultado**                           | **0.602** | **0.92**       | **65.451**  |
<br>
<sub><i>Creado por el Grupo PENSER de Consultoría e Investigación de la Universidad Santo Tomás</i></sub>

</div>

<div align="center">
  
### Cuadro 2 presentado en el artículo – Resultados del índice de impacto de los y las egresadas

![Imagen de WhatsApp 2025-09-29 a las 14 23 43_1a610962](https://github.com/user-attachments/assets/69800b16-3279-4f74-a749-a6ba49bd94dc)

</div>

Al reconstruir el índice con la metodología y ponderaciones del artículo, nuestro IIE global fue 0,602, equivalente a 65% del valor esperado; el estudio reporta 0,717 y 72%. En Desarrollo de competencias interpersonales (DCI) obtuvimos 0,231 con un 77% de logro, muy cerca del 76% del artículo. En Percepción del mejoramiento de la calidad de vida (PMCV) el resultado fue 0,151 y 75%, prácticamente igual al 75% publicado. Las diferencias aparecen sobre todo en Formación disciplinar (FD), donde logramos 0,143 y 43% frente a 0,218 y 73% del estudio; una explicación probable es que tratamos “No aplica” como cero en lugar de excluirlo del cálculo. En Movilidad social (MS) ocurrió lo contrario: alcanzamos 0,078 y 87%, mientras el artículo presenta 0,122 y 61%; aquí influyó que solo incorporamos parte de las variables de ese componente.

### Formación disciplinar (FD)

<div align="center">

### Cuadro 2 – Resultados del componente de formación disciplinar del IIE

| Variable                                             | Resultado | % alcanzado |
|---------------------------------------------------- -|-----------|-------------|
| Vinculación laboral                                  | 0.024     | 78.565      |
| Tipo de cargo                                        | 0.018     | 60.903      |
| Premios y reconocimientos                            | 0.006     | 18.512      |
| Vinculación a gremio, red y/o asociación científica  | 0.002     | 5.043       |
| Desarrollo de proyectos comunitarios                 | 0.004     | 11.692      |
| Desarrollo de proyectos de investigación             | 0.003     | 9.655       |
| Desarrollo de competencias cognitivas disciplinares  | 0.024     | 79.469      |
| Desarrollo de competencias digitales                 | 0.017     | 74.695      |
| Desarrollo de competencia en lengua extranjera inglés| 0.019     | 62.167      |
| Desarrollo de competencias investigativas            | 0.022     | 74.508      |

<br>
<sub><i>Creado por el Grupo: PENSER de Consultoría e Investigación – Universidad Santo Tomás</i></sub>

</div

<div align="center">
  
### Cuadro 3 presentado en el artículo – Resultados del componente de formación disciplinar del IIE

<img width="614" height="370" alt="image" src="https://github.com/user-attachments/assets/54ef96eb-f03b-4e7b-a56d-3fff530d06c5" />

</div>

Observamos similitudes en varias variables, pero también diferencias puntuales. Un caso es “Tipo de cargo”: en la base hay categorías (“Directivo”, “Profesional”, “Técnico”, “Operativo”, “Asistencial”), mientras que en el artículo el peso mostrado parece corresponder a opciones Sí/No, lo que deja dudas sobre cómo ponderaron exactamente esa variable.
Para premios y reconocimientos, vinculación a gremios/redes, proyectos comunitarios, proyectos de investigación y pertinencia del programa, nuestros resultados difieren en algunos decimales (p. ej., en “premios” ellos reportan 0,016 y nosotros 0,006). Para validar, contamos respuestas “Sí/No” directamente en el Excel, multiplicamos por el peso y dividimos por el total de encuestados; el cálculo respalda nuestro valor.
En las variables de logro (p. ej., Desarrollo de competencias cognitivas, digitales, inglés e investigativas), el artículo usa la escala Muy insuficiente → Muy suficiente, pero en la base aparece Muy alto → Muy bajo + No aplica, entonces lo que nuestro equipo hizo fue asociar las opciones de respuesta a las que ellos les dieron los pesos por ejemplo Muy alto lo relacionamos con Muy suficiente y asi fue como asignamos los pesos a las opciones de respuesta correspondientes a las preguntas del componente de Formación Disciplinar.

### Desarrollo de competencias interpersonales

<div align="center">

### Cuadro 3 – Resultados del componente “desarrollo de competencias interpersonales”

| Variable                            | Resultado | % alcanzado |
|-------------------------------------|-----------|-------------|
| Comunicación efectiva               | 0.024     | 79.203      |
| Relaciones interpersonales          | 0.024     | 78.512      |
| Toma de decisiones                  | 0.024     | 79.114      |
| Solución de problemas y conflictos  | 0.024     | 78.565      |
| Pensamiento creativo                | 0.023     | 77.644      |
| Pensamiento crítico                 | 0.024     | 79.008      |
| Manejo de emociones y sentimientos  | 0.021     | 73.357      |
| Manejo de tensiones y estrés        | 0.021     | 71.461      |
| Multiculturales                     | 0.023     | 75.235      |
| Interculturalidad                   | 0.023     | 76.457      |

<br>
<sub><i>Creado por el Grupo: PENSER de Consultoría e Investigación – Universidad Santo Tomás</i></sub>

</div>

<div align="center">
  
### Cuadro 4 presentado en el artículo – Resultados del componente “desarrollo de competencias interpersonales”

<img width="616" height="346" alt="image" src="https://github.com/user-attachments/assets/6d9261a3-7732-4690-92d8-6c7ba9034c2d" />

</div>

Los resultados son muy cercanos. Por ejemplo, en Comunicación efectiva obtuvimos 0,024 (79%) frente a 0,023 (76,7%) del artículo y así con las demás respuestas son similares los resultados. Como en FD, la pequeña diferencia tal vez sea porque al momento de asignar los pesos a las respuestas nuestro equipo encontró que las opciones de respuestas a estas preguntas eran Muy alto, Alto, Medio, Bajo, Muy bajo, No aplica y las opciones de respuesta a las que ellos les asignaban peso en el articulo eran Muy insuficiente, Insuficiente, Ni suficiente, ni insuficiente, Suficiente y Muy suficiente, entonces lo que nuestro equipo hizo fue asociar las opciones de respuesta a las que ellos les dieron los pesos por ejemplo Muy alto lo relacionamos con Muy suficiente y asi fue como asignamos los pesos a las opciones de respuesta correspondintes a las preguntas de Desarrollo de competencias interpersonales

### Componente de Movilidad Social

<div align="center">

### Cuadro 4 – Resultados del componente “movilidad social”

| Variable                                        | Resultado | % alcanzado |
|-------------------------------------------------|-----------|-------------|
| Responsabilidad económica en el hogar           | 0.026     | 86.182      |
| Nivel de escolaridad alcanzado por la madre     | 0.026     | 86.076      |
| Nivel de escolaridad alcanzado por el padre     | 0.026     | 87.907      |

<br>
<sub><i>Creado por el Grupo: PENSER de Consultoría e Investigación – Universidad Santo Tomás</i></sub>

</div>

<div align="center">
  
### Cuadro 5 presentado en el artículo – Resultados del componente “movilidad social”

<img width="613" height="268" alt="image" src="https://github.com/user-attachments/assets/b1545f6f-96a7-470d-982d-38ab8f0ca4bd" />

</div>

