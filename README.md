# MetagenomicsPipeline
Pipeline utilizada para analizar y visualizar la metataxonomía de muestras ambientales con **Qiime2**.
Procesamiento de Secuencias
## 1. Análisis_Calidad
Importar los datos de secuenciación con el formato *Casava 1.8 demultiplexed fastq, Paired-End*.
## 2. Eliminacion_primers
Eliminar los primers de las secuencias para evitar malas identificaciones con el programa DADA2 dentro de la interfaz de Qiime2 con la función Cutadapt.
## 3. Secuencias_representativas
Obtención de secuencias representativas (repseqs), tabla y estadísticas (stasts) con DADA2. Cortar (trunc) las secuencias. 
- STATS: tabla con número de ASV totales, porcentaje de ASV filtrados, número de quimeras, etc.
- TABLE: nº de ASVs en cada muestra que se puede filtrar con el parámetro que queramos, las frecuencias de cada ASV y en cuántas muestras se encuentran.
- REPSEQS: ASVs encontrados en las muestras, su longitud media y su desviación típica. BLASTN para ver a qué organismos corresponden.
## 4. Clasificador
Crear y entrenar un clasificador de taxonomía a partir de una biblioteca de secuencias de referencia. En este caso, *SILVA 16S/18S rRNA full-length sequences*.
## 5. Taxonomia
Obtención de la taxonomía de las muestras.
## 6. Barplot
Obtención de un barplot de la taxonomía que se puede visualizar en Qiime2.
