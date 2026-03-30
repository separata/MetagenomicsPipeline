#Visualización de la taxonomía en barplot
qiime taxa barplot \
    --i-table <table.qza> \
    --i-taxonomy <taxonomy.qza> \
    --m-metadata-file <metadata.tsv> \
    --o-visualization <barplot.qzv>