function nbPremiers(n)
	premiers = []
	if n > 1
		push!(premiers,2)
		for i in range(3,2,div(n+1,2)-1)
			estPremier = true
			for p in premiers
				if i%p == 0
					estPremier = false
					continue
				end
			end
			if estPremier
				push!(premiers,i)
			end
		end
	end
	return premiers
end
