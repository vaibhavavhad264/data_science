SELECT * FROM movies;

SELECT movies.movie_id, title, budget, revenue, unit 
FROM movies
JOIN financials
ON movies.movie_id = financials.movie_id;

SELECT m.movie_id, title, budget, revenue, unit 
FROM movies m
JOIN financials f
ON m.movie_id = f.movie_id;

SELECT m.movie_id, title, budget, revenue, unit 
FROM movies m
LEFT JOIN financials f
ON m.movie_id = f.movie_id;

SELECT m.movie_id, title, budget, revenue, unit 
FROM movies m
LEFT JOIN financials f
ON m.movie_id = f.movie_id

UNION

SELECT f.movie_id, title, budget, revenue, unit 
FROM movies m
RIGHT JOIN financials f
ON m.movie_id = f.movie_id;

SELECT m.title, l.name
FROM movies m
LEFT JOIN languages l
ON m.language_id = l.language_id;

SELECT title 
FROM movies m
LEFT JOIN languages l
ON m.language_id = l.language_id
WHERE l.name = 'telugu';  

SELECT l.name, count(m.movie_id) AS no_of_movies 
FROM languages l 
LEFT JOIN movies m
USING(language_id)
GROUP BY language_id
ORDER BY no_of_movies DESC;


SELECT 
            l.name, 
            COUNT(m.movie_id) as no_movies
	FROM languages l
	LEFT JOIN movies m USING (language_id)        
	GROUP BY language_id
	ORDER BY no_movies DESC;





