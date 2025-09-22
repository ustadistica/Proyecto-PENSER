---
title: "Metodologías para reconstruir el Índice de Impacto de Egresados (IIE)"
author: "Grupo - Penser"
date: "`r Sys.Date()`"
output: html_document
---

# Metodologías para reconstruir el Índice de Impacto de Egresados (IIE)

El **Índice de Impacto de Egresados (IIE)** resume cuatro componentes los cuales son:  
- **Formación Disciplinar (FD)**  
- **Desarrollo de Competencias Interpersonales (DCI)**  
- **Movilidad Social (MS)**  
- **Percepción de Mejoramiento de la Calidad de Vida (PMCV)**  

La idea central es obtener, para cada persona, un puntaje por cada componente y luego un índice final que combine los cuatro mediante **suma ponderada**, lo que significa que cada componente se multiplica por un porcentaje (su peso) y después se suman los cuatro resultados.  

La fórmula general es:  

$$
IIE = w_{FD} \cdot FD + w_{DCI} \cdot DCI + w_{MS} \cdot MS + w_{PMCV} \cdot PMCV
$$

donde $FD$, $DCI$, $MS$, $PMCV$ son los puntajes por componente de cada persona y  
$w_{FD}$, $w_{DCI}$, $w_{MS}$, $w_{PMCV}$ son los porcentajes asignados a cada componente.  

Para asegurar comparabilidad con el estudio, se mantendrán los mismos porcentajes en ambas metodologías. Lo que cambia entre la **Metodología A** y la **Metodología B** es cómo se construye el puntaje interno de cada componente.

---

## 1. Metodología A: Cálculo con los pesos del artículo

Con esta metodología se busca replicar el enfoque del artículo. Este ya trae, para cada pregunta y opción de respuesta, un valor numérico (puntajes) como se observa en el *Cuadro 1 del artículo “Enfoque Metodológico para la evaluación de impacto de los y las Egresadas en el Entorno: un Estudio de Caso”*.  

Los porcentajes aplicados fueron:  
- **Formación Disciplinar (FD):** 30%  
- **Desarrollo de Competencias Interpersonales (DCI):** 30%  
- **Movilidad Social (MS):** 20%  
- **Percepción del Mejoramiento de la Calidad de Vida (PMCV):** 20%  

Esto garantiza que los resultados sean comparables con los reportados por los autores.

### Pasos

1. Definir qué preguntas pertenecen a cada componente (FD, DCI, MS y PMCV).  
2. Usar los valores por opción tal como aparecen en el Cuadro 1.  
   - Ejemplo: en FD, la pregunta *Vinculación laboral* se codifica: **Sí = 0.03**; **No = 0.00**.  
3. Para cada persona, se suma el valor de sus respuestas dentro del componente → puntaje del bloque.  
4. Se obtiene el índice individual aplicando la fórmula:  

   $$
   IIE_{persona} = 0.30 \cdot FD_{persona} + 0.30 \cdot DCI_{persona} + 0.20 \cdot MS_{persona} + 0.20 \cdot PMCV_{persona}
   $$

5. Promediar los 1129 casos para obtener el **IIE general**.  
6. El resultado queda en escala **0–1** (puede transformarse en porcentaje multiplicando por 100).  

---

## 2. Metodología B: Cálculo con pesos ajustados de las respuestas

En esta metodología se mantiene la misma estructura del índice con los mismos pesos globales (30%, 30%, 20%, 20%), pero se introducen dos cambios:  

1. Los pesos asignados a las opciones de respuesta se ajustan bajo un esquema más equitativo.  
2. Se propone un diseño muestral diferente: **muestreo estratificado proporcional** en lugar de muestreo aleatorio simple.  

### Nuevos pesos

- **Preguntas dicotómicas (Sí/No):** Sí = 1.00; No = 0.00  
- **Escalas ordinales (muy insuficiente → muy suficiente):**  
  - Muy insuficiente = 0.10  
  - Insuficiente = 0.25  
  - Neutral = 0.50  
  - Suficiente = 0.75  
  - Muy suficiente = 1.00  
- **PMCV (percepción de calidad de vida):**  
  - Totalmente en desacuerdo = 0.10  
  - En desacuerdo = 0.25  
  - Neutral = 0.50  
  - De acuerdo = 0.75  
  - Totalmente de acuerdo = 1.00  
- **Movilidad social (educación, estrato, ingresos):**  
  - Ascenso = 1.00  
  - Igual = 0.50  
  - Descenso = 0.10  

### Pasos

1. Definir preguntas por componente (FD, DCI, MS, PMCV).  
2. Aplicar los nuevos pesos a cada respuesta.  
3. Calcular el puntaje de cada bloque (FD, DCI, MS, PMCV) en escala 0–1.  
4. Calcular el índice individual:  

   $$
   IIE_{persona} = 0.30 \cdot FD_{persona} + 0.30 \cdot DCI_{persona} + 0.20 \cdot MS_{persona} + 0.20 \cdot PMCV_{persona}
   $$

5. Promediar los índices individuales para obtener el **IIE general**.  
6. Aplicar el **muestreo estratificado proporcional**: dividir la población de egresados en estratos según sede/seccional y programa académico, y seleccionar proporcionalmente.  
7. El índice final se interpreta igual que en la Metodología A (escala 0–1 o porcentaje).  

---

## Conclusiones

- La **Metodología A** asegura comparabilidad con el estudio original.  
- La **Metodología B** introduce ponderaciones más balanceadas y un diseño muestral más robusto.  
- En ambos casos, el índice final se expresa en una escala de **0 a 1** (o en porcentaje).  
