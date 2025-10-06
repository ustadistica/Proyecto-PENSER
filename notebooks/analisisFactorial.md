Se cargó la hoja DATA VALIDA.La inspección inicial muestra que la base tiene 1129 observaciones y 143 columnas. 
Se identificaron columnas administrativas e identificadores a excluir, variables demográficas a estandarizar y un conjunto de ítems ordinales (Likert) que requieren mapeo numérico; una vez realizada la limpieza se procedió con la evaluación de adecuación (KMO y Bartlett) y extracción factorial.

Se aplicó un proceso de normalización de nombres de columnas: todos los encabezados fueron convertidos a minúsculas, sin tildes ni caracteres especiales, reemplazando espacios por guiones bajos. Esto garantiza nombres consistentes y compatibles con los análisis estadísticos posteriores.

Se estandarizaron los encabezados a formato snake_case: sin tildes ni caracteres especiales y acortados a 40 caracteres para garantizar unicidad; el mapeo se exportó a diccionario_columnas_IIE.xlsx para preservar trazabilidad.

Se ejecutó una detección automática de ítems tipo Likert: 91 de 143 columnas fueron identificadas como escalas ordinales (familias: agreement, impact, intensity, etc.) y codificadas a valores enteros 1..K respetando el orden teórico de cada familia. Se generó un likert_map con la familia detectada, la cobertura de coincidencia y los niveles encontrados, y se guardó un diccionario de mapeo por ítem. 
Algunas columnas fueron reconocidas correctamente como Likert, pero presentan una o más respuestas que no encajan exactamente con la escala esperada (Columnas con cobertura parcial: ej. 0.833).
