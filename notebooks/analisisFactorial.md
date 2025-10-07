# Análisis Factorial Exploratorio (AFE) — Proyecto PENSER

## Contexto General

En el marco del proyecto **PENSER**, cuyo propósito es **evaluar el impacto de la formación universitaria en el desempeño profesional de los egresados**, se desarrolló un **Análisis Factorial Exploratorio (AFE)** como herramienta estadística para reconstruir el **Índice de Impacto de Egresados (IIE)**.

El objetivo principal fue **pasar de un modelo teórico de ponderaciones fijas** (definido en cuatro componentes:  
- Formación Disciplinar (FD),  
- Desarrollo de Competencias Interpersonales (DCI),  
- Movilidad Social (MS), y  
- Percepción de Mejoramiento de la Calidad de Vida (PMCV)),  

a una **estructura empírica** basada en las **relaciones reales entre las respuestas** de los egresados.

Esta aproximación factorial permite **validar empíricamente la coherencia de los ítems del cuestionario** respecto a los componentes teóricos del IIE, y además **obtener puntajes factoriales objetivos** que reflejan el comportamiento estadístico de los datos.

---

## Preparación de los Datos

- **Fuente de datos:** hoja `DATA_VALIDA` con **1129 observaciones** y **143 columnas**.  
Se excluyeron columnas administrativas e identificadores, y se estandarizaron las variables. Se identificó un conjunto de ítems tipo Likert(ordinales), que fueron mapeados a valores numéricos según sus escalas.

### Limpieza y estandarización

- Los nombres de columnas fueron normalizados a formato `snake_case`, sin tildes ni caracteres especiales.  
- Se creó un diccionario de mapeo (`diccionario_columnas_IIE.xlsx`) para garantizar trazabilidad y unicidad de nombres.  
- Se detectaron automáticamente 91 variables tipo Likert (familias: *agreement, impact, intensity*, etc.) codificadas como valores enteros `1..K` respetando el orden teórico y se generó un archivo de trazabilidad de mapeo (`likert_map.xlsx`) con la familia detectada, niveles encontrados y cobertura de coincidencia. Algunas columnas mostraron **cobertura parcial** (ej. 0.833), indicando respuestas atípicas o fuera de escala esperada.

---

## Evaluación de Adecuación para el AFE

Antes del análisis factorial se verificó la idoneidad de los datos mediante las pruebas de **KMO** y **Bartlett**.

### Medida de Adecuación Muestral (KMO)

- **KMO global = 0.791** → *Adecuación buena*.  
  Esto indica que las variables comparten suficiente varianza común para justificar un análisis factorial.  
  En términos prácticos, los ítems presentan señales compartidas que sugieren la existencia de **dimensiones latentes** (formación, competencias, movilidad, calidad de vida, etc.).

- **KMO por variable:** Se identificaron ítems con valores bajos (p. ej., relacionados con nivel máximo de escolaridad:). Estas variables fueron depuradas al no compartir varianza común suficiente con el resto.

### Test de Esfericidad de Bartlett

- **χ² ≫ 0**, **p ≈ 0** → La matriz de correlaciones no es identidad.  
  Existen correlaciones significativas entre ítems, confirmando que hay información común que justifica el AFE.

En conclusión los datos presentan una estructura correlacional adecuada para extraer factores latentes.

---

## Extracción y Rotación Factorial

- Se retuvieron **60 variables (KMO ≥ 0.50)** de las 91 iniciales.  
- El Scree Plot y el análisis de autovalores mostraron:
  - Un **factor dominante** (autovalor ≈ 10.5; 17.5% de varianza explicada).
  - Un codo entre 4 y 6 factores.
  - La regla de Kaiser (>1) sugería ~15 factores.
     
    Por parsimonia se decidió **explorar soluciones de 4 a 6 factores**.

![Scree Plot](https://github.com/user-attachments/assets/270f87ed-1bcc-46f1-85b7-f4d137492321)


## Resultados del AFE

Se generó una matriz de cargas factoriales con rotación Varimax para una solución de 4 factores sobre las 60 variables retenidas.

Observaciones clave:
- Varias variables (especialmente las asociadas a escolaridad) presentaron cargas cercanas a cero, sin contribuir a la estructura factorial. Esto sugiere la necesidad de depurar los ítems y revisar la consistencia de las dimensiones del IIE.

Se ejecutaron AFE con rotación Varimax para 4, 5 y 6 factores, cuyos resultados fueron exportados a `AFE_comparacion.xlsx`. En la selección final del IIE se conservarán ítems con cargas altas y estables (|carga| ≥ 0.40), descartando ítems con carga máxima < 0.30 o cargas cruzadas elevadas.

---

## Ajuste Confirmatorio

Se ajustó un modelo confirmatorio de 4 factores (Formación, Competencias, Movilidad, Calidad de Vida) mediante `semopy`.

### Índices de ajuste global

| Índice | Valor | Interpretación |
|--------|--------|----------------|
| **CFI** | 0.933 | Ajuste bueno |
| **TLI** | 0.923 | Ajuste aceptable |
| **RMSEA** | 0.078 | Dentro del rango razonable |
| **GFI** | ≈0.924 | Ajuste global adecuado |

- La matriz de covarianza muestral no era definida positiva, por lo que se aplicaron correcciones numéricas.  
- Se observaron cargas mayores a 1 y factores con pocos indicadores (por ejemplo, *Calidad de Vida* con solo 2 ítems). Se requiere depuración, eliminando ítems redundantes o de baja carga antes de validar la estructura final del Índice de Impacto de Egresados (IIE).

## Conclusiones 
El AFE permitió identificar la estructura empírica del cuestionario de egresados. Los resultados confirman la existencia de correlaciones significativas y una estructura factorial interpretable, aunque aún requiere ajustes.  



