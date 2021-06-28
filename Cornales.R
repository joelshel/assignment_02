library(pcaMethods)
geno_data = read.csv("~/Documents/ASB/assignment_02/Cornales.csv",
                    header=TRUE,
                    row.names=1,
                    sep=" ",
                    na.strings=9)


geno_data = geno_data[rowSums(is.na(geno_data)) != ncol(geno_data)-1,]


View(geno_data)


colors = factor(geno_data$Species)
        
tlep_pca = pca(geno_data[,-c(1)],
               scale="none",
               center=T,
               nPcs=2,
               method="nipals")


print(tlep_pca@R2)

slplot(tlep_pca,
       scol=colors,
       scoresLoadings=c(TRUE,FALSE),
       sl=NULL,  # What does this do?
       spch="x")

legend("topright",
       legend=unique(colors), # sort(unique(geno_data[, "Species"])),
       col=unique(colors),
       pch="x")
