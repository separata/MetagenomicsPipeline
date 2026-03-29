#Truncar secuencias paired-end
qiime dada2 denoise-paired \
    --i-demultiplexed-seqs <demux.qza> \
    --p-trunc-len-f <número> \
    --p-trunc-len-r <número> \
    --p-n-threads 0 \
    --o-representative-sequences <repseqs.qza> \
    --o-table <table.qza> \
    --o-denoising-stats <stats.qza>
#f:forward; r:reverse; trunc:cortar extremo 3'; trim: cortar 5'

#Obtener las visualizaciones de los qza obtenidos
qiime metadata tabulate \
    --m-input-file <stats.qza> \
    --o-visualization <.qzv>
qiime feature-table summarize \
    --i-table <table.qza> \
    --m-sample-metadata-file <.tsv> \
    --o-visualization <.qzv> \
qiime feature-table tabulate-seqs \
    --i-data <repseqs.qza> \
    --o-visualization <.qzv>