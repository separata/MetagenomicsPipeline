#Taxonomía
qiime feature-classifier classify-sklearn \
    --i-classifier <classifier.qza> \
    --i-reads <repseqs.qza> \
    --o-classification <taxonomy.qza>

#Visualización
qiime metadata tabulate \
    --m-input-file <taxonomy.qza> \
    --o-visualization <taxonomy.qzv>
#Se obtiene familia, género, especie, etc. de los ASVs encontrados