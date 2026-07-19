SELECT * FROM movies where industry = "Bollywood";
SELECT distinct industry from movies;
SELECT * FROM movies;
SELECT * FROM movies WHERE title LIKE "%thor%";
SELECT * FROM movies WHERE title LIKE "%avenger%";
SELECT * FROM movies WHERE title LIKE "%america%";
SELECT * FROM movies WHERE studio = "";
SELECT * FROM movies WHERE imdb_rating >= 9;
SELECT * FROM movies WHERE imdb_rating BETWEEN 6 AND 10;

SELECT * FROM movies WHERE release_year IN (2022, 2019, 2018);

SELECT * FROM movies WHERE studio IN ('Marvel Studios', 'Zee Studios');

SELECT * FROM movies WHERE imdb_rating IS NULL;

SELECT * FROM movies WHERE imdb_rating IS NOT NULL;
SELECT title, imdb_rating, industry FROM movies WHERE industry = 'bollywood';


SELECT * FROM movies WHERE industry = 'bollywood' ORDER BY imdb_rating;

SELECT * FROM movies WHERE industry = 'bollywood' ORDER BY imdb_rating DESC;

SELECT * FROM movies WHERE industry = 'bollywood' ORDER BY imdb_rating DESC LIMIT 5;
SELECT * FROM movies WHERE industry = 'hollywood' ORDER BY imdb_rating DESC LIMIT 5 OFFSET 1;

SELECT MIN(imdb_rating) AS min_rating, 
	ROUND(AVG(imdb_rating), 2) AS avg_rating, 
	MAX(imdb_rating) AS max_rating 
FROM movies WHERE studio = 'Marvel Studios';


SELECT industry, COUNT(industry) AS count FROM movies
GROUP BY industry
ORDER BY count DESC;

SELECT industry, COUNT(industry) AS count,
ROUND(AVG(imdb_rating), 2) AS avg_rating
FROM movies
GROUP BY industry
ORDER BY count DESC;

SELECT studio, COUNT(studio) AS count,
ROUND(AVG(imdb_rating), 1) AS avg_rating
FROM movies
GROUP BY studio
ORDER BY avg_rating DESC;

SELECT studio, COUNT(studio) AS count,
ROUND(AVG(imdb_rating), 1) AS avg_rating
FROM movies WHERE studio != ''
GROUP BY studio
ORDER BY avg_rating DESC;

SELECT release_year, COUNT(*) as movies_cnt
FROM movies 
GROUP BY release_year
ORDER BY movies_cnt DESC;


SELECT release_year, COUNT(*) as movies_cnt
FROM movies 
GROUP BY release_year
HAVING movies_cnt > 2 
ORDER BY movies_cnt DESC;













