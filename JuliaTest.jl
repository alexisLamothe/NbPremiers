include("AlgoJulia/AlgoPremiersLoop.jl")

println(nbPremiers(200))

function getTimeExecution(f,n)
	t = time()
	f(n)
	println(time()-t)
end

getTimeExecution(nbPremiers,50)
getTimeExecution(nbPremiers,500)
getTimeExecution(nbPremiers,5000)
getTimeExecution(nbPremiers,50000)
# getTimeExecution(nbPremiers,500000)
