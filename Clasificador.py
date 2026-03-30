#Obtener las secuencias de referencia a partir de SILVA. Los primers se determinarán según los organismos estudiados
qiime feature-classifier extract-reads \
    --i-sequences <silva-seqs.qza> \
    --p-f-primer <GTGCCAGCMGCCGCGGTAA> \ #Primer F 16SrRNA
    --p-r-primer <GGACTACHVGGGTWTCTAAT> \ #Primer R 16SrRNA
    --p-min-length <número> \ 
    --p-max-length <número> \
    --p-n-jobs <número> \ #número de cores del ordenador usados en el análisis
    --o-reads <refseqs.qza>

#Entrenar el clasificador con la taxonomía  SILVA y las secuencias de referencia del paso anterior. Método Naive-Bayes
qiime feature-classifier fit-classifier-naive-bayes \
    --i-reference-reads <refseqs.qza> \
    --i-reference-taxonomy <silva-taxonomy.qza> \
    --o-classifier <classifier.qza>