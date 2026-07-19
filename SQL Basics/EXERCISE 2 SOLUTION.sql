SELECT  title, group_concat(name) AS actors
FROM movies
JOIN movie_actor ma USING(movie_id)
JOIN actors a USING(actor_id)
GROUP BY movie_id
;

SELECT  a.name, group_concat(m.title SEPARATOR  '|') AS movie,
COUNT(m.title) AS No_Of_Movie
FROM actors a
JOIN movie_actor ma USING(actor_id)
JOIN movies m USING(movie_id)
GROUP BY a.actor_id
ORDER BY No_Of_Movie DESC;
;

#1) Generate a report of all Hindi movies sorted by their revenue amount in millions. Print movie name, revenue, currency, and unit


SELECT title, revenue, currency, unit,
CASE
	WHEN unit = 'Thousands' THEN ROUND((revenue)/1000, 2)
	WHEN unit = 'Billions' THEN ROUND((revenue)*1000, 2)
    ELSE (revenue) 
END AS revenue_in_mln
FROM movies m
JOIN financials f USING(movie_id)
JOIN languages l USING(language_id)
WHERE l.name = 'Hindi'
ORDER BY revenue_in_mln DESC;

    


