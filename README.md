# MetagenomicsPipeline
Pipeline utilizada para analizar y visualizar la metataxonomía de muestras ambientales con Qiime2.
Procesamiento de Secuencias
1. Análisis_Calidad: Importar los datos de secuenciación con el formato “Casava 1.8 demultiplexed fastq”; Paired-End. 
2. Eliminacion_primers: Eliminar los primers de las secuencias para evitar malas identificaciones con el programa DADA2 dentro de la interfaz de Qiime2 con la función Cutadapt.

