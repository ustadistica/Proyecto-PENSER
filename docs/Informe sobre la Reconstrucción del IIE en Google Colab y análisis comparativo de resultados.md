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
