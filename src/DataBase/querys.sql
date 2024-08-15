use StreamETL_DB;

# 1. Number of movies and series (separate) per platform
SELECT count(*) AS amount,platform, category
FROM streaming
WHERE platform = "netflix"
GROUP BY category;

# 2. Maximum duration according to type of film (film/series), by platform and by year
SELECT title,platform, release_year, duration, type_duration
FROM streaming 
WHERE platform = "hulu" and release_year= 2018 and type_duration="min"
ORDER BY duration DESC
LIMIT 1;

 # 3. Actor with the most repetitions according to platform and year
SELECT count(*) AS amount, c.cast, s.platform, s.release_year
FROM actors c
INNER JOIN streaming s ON (c.idStream=s.idStream)
WHERE s.platform="netflix" and s.release_year=2018 and c.cast != "sin dato"
GROUP BY c.cast
ORDER BY 1 DESC
LIMIT 1;

#4. Number of times a genre and platform are repeated most frequently
SELECT s.platform,count(s.platform) AS amount 
FROM gender g 
join streaming s ON (s.idStream = g.idStream)
WHERE g.genre ='Comedy'
GROUP BY by s.platform ORDER BY by amount DESC 
LIMIT 1;


    
