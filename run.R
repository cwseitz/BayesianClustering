source("internal.R")
foldername="230516_Hela_j646_50pm overnight_High_10ms_10000frames_buffer_02"
r = readLines(con=file.path(paste(foldername, "/config.txt", sep="")))
get <- function(type){i = grep(type,r); strsplit(r[i], "=")[[1]][2]}
as.v <- function(ch){as.numeric(strsplit(ch,",")[[1]])}
model=get("model")
{if (model=="Gaussian(prec)"){
  xlim = as.v(get("xlim"))
  ylim = as.v(get("ylim"))
  histbins = as.v(get("histbins"))
  histvalues = as.v(get("histvalues"))
  if (length(grep("pbackground",r))==0 | length(grep("alpha",r))==0){
    useplabel=FALSE; pb=NULL; alpha=NULL
  }
  else {
    useplabel=TRUE; 
    pb=as.numeric(get("pbackground"))
    alpha=as.numeric(get("alpha"))
  }
}
else {stop("Haven't implemented anything else!")}}

o <- order(histbins)
histbins <- histbins[o]
histvalues <- histvalues[o]
f <- approxfun(histbins, histvalues, yleft = histvalues[1], yright = histvalues[length(histvalues)])
cst <- integrate(f, lower = histbins[1], upper = histbins[length(histbins)])$value

psd <- function(sd){
  log(f(sd))-log(cst) 
}
minsd = histbins[1]; maxsd = histbins[length(histbins)]

ld=list.dirs(foldername, recursive=FALSE)
ld=ld[ld!=foldername]

sapply(file.path(ld), function(foldername){



data= read.csv(file.path(paste(foldername, "/data.txt", sep="")))
pts = data[,1:2]; sds = data[,3];
res=Kclust(pts=pts, sds=sds, xlim=xlim, ylim=ylim, psd=psd, minsd=minsd, maxsd=maxsd, useplabel=useplabel, alpha=alpha, pb=pb, score=TRUE, rlabel=TRUE, report=TRUE)
writeRes(res, file.path(paste(foldername, "/r_vs_thresh.txt", sep="")), file.path(paste(foldername, "/labels", sep="")))

})




