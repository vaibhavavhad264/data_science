SELECT movie_id, title, budget, revenue, currency, unit,
CASE
	WHEN unit = 'thousands' THEN round((revenue-budget)/1000, 2)
    WHEN unit = 'billions' THEN round((revenue-budget)*1000, 2)
    ELSE (revenue-budget)
END AS profit_mln
FROM moviesdb.movies m
LEFT JOIN moviesdb.financials f
USING(movie_id)
WHERE industry = 'Bollywood'
ORDER BY profit_mln DESC;