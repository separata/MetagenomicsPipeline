#Eliminación de los primers de las secuencias
qiime cutadapt trim-paired \
    --i-demultiplexed-sequences <demux.qza> \
    --p-cores <número> \
    --p-front-f ^<primer forward> \
    --p-front-r ^<primer reverse> \
    --o-trimmed-sequences <trimmed.qza>
#primer forward y primer reverse: 16S, 18S o los primers del gen que se haya secuenciado
qiime demux summarize \
    --i-data <trimmed.qza> \
    --o-visualization <trimmed.qzv>
#Pasar el archivo a visualizador para decidir por dónde cortar

