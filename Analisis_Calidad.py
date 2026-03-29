#Extraer e importar data
unzip -q <.zip>
qiime tools import \
    --type 'SampleData[PairedEndSequencesWithQuality]' \
    --input-path <nombre carpeta> \
    --input-format CasavaOneEightSingleLanePerSampleDirFmt \
    --output-path <demux.qza>

#Pasar el demux.qza a visualizador
qiime demux summarize \
    --i-data <demux.qza> \
    --o-visualization <demux.qzv>
#Este archivo se puede visualizar en Qiime2. Calidad de las seceuncias. Mínimo debemos coger 400-500 pares de bases.

