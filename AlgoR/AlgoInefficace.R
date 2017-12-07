nbPremiers <- function(n){
	allCombinaisons <- c();
	premiers <- c();
	for (i in 2:n) {
		for (j in 2:n) {
			if (i*j<=n) {
				allCombinaisons <- c(allCombinaisons,i*j);
			}
		}
	}
	for (k in 2:n) {
		if(! k %in% allCombinaisons) {
			premiers <- c(premiers,k);
		}
	}
	return(premiers);
}

