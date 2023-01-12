-- Rank band origin 
-- order by nno-unique number of fans

SELECT origin AS origin, SUM(fans) AS nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
