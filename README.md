# Proyecto-PENSER📊📝- Reconstrucción del Índice de Impacto de Egresados (IIE)

Proyecto del curso Consultoría e Investigación – Facultad de Estadística
Equipo: [Yeimy Alarcón], [Karen Suarez], [Josue Pedraza], [Maria José Galindo], [Paula Guevara], [Kevin Baracaldo] · [Universidad Santo Tomás] · [Octavo Semestre/2025-2]

> **Estado:** En progreso · **Repositorio:** _[Link Repositorio](https://github.com/ustadistica/Proyecto-PENSER.git)_ · **Última actualización:** 2025-09-16

Este repositorio está dedicado a la reconstrucción del Índice de Impacto de Egresados (IIE) del proyecto PENSER. Nuestro objetivo, como equipo, es evaluar el impacto de la educación superior en el desempeño profesional de los egresados de la Universidad Santo Tomás, usando la información de la encuesta suministrada por los autores del estudio y siguiendo una metodología clara, reproducible y transparente.

El IIE es un indicador sintético que resume, en un solo valor, varios aspectos relevantes de la trayectoria de los egresados. En particular, integra cuatro componentes que reflejan dimensiones clave del perfil y la inserción laboral:

- Formación Disciplinar (FD): conocimientos y habilidades técnicas propias de la carrera y su pertinencia en el empleo.
- Desarrollo de Competencias Interpersonales (DCI): habilidades “blandas” como comunicación, trabajo en equipo, liderazgo, toma de decisiones y manejo de emociones.
- Movilidad Social (MS): cambios en la posición social y económica (aporte al hogar, suficiencia de ingresos, movilidad educativa frente a los padres).
- Percepción de Mejoramiento de la Calidad de Vida (PMCV): evaluación del egresado sobre cómo su formación universitaria ha mejorado su bienestar y oportunidades.

La metodología original presentada por los autores construye el IIE a partir de estos cuatro componentes y los combina mediante suma ponderada. Para iniciar el trabajo, recibimos de los autores:
- Artículos donde presentan sus resultados y explican el proceso seguido para construir el índice (metodología, ponderaciones y lecturas).
- Presentaciones (diapositivas) con información del proyecto y resúmenes clave.
- La base de datos depurada y un tablero de Power BI con indicadores.

Durante la revisión preliminar realizamos una Verificación de Consistencia entre Power BI y la Base Depurada y registramos algunas inconsistencias, ese análisis se documenta en el archivo correspondiente dentro del repositorio

---

## 🗂️🧮 Planteamiento metodologías complementarias:

1. *Metodología A (réplica del artículo):* Con esta buscamos replicar el enfoque de los autores. El artículo ya trae, para cada pregunta y cada opción de respuesta, un valor numérico (los “puntajes” por opción) que aparecen en el Cuadro 1 del documento “Enfoque Metodológico para la evaluación de impacto de los y las Egresadas en el Entorno: un Estudio de Caso”, tomando exactamente esos valores, construimos cada componente sumando los valores que correspondan a las respuestas del egresado y luego combinamos los cuatro componentes con los porcentajes de bloque definidos por los autores.
