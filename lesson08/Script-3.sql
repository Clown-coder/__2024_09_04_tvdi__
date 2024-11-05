--選擇站點名稱
SELECT DISTINCT sitename FROM record


SELECT * FROM record 
WHERE sitename='富貴角'
ORDER BY date ASC;

/*ASC 由小到大  DESC 由大到小*/



SELECT date,county,AQI,PM25,status,lat,lon
FROM record 
WHERE sitename='富貴角'
ORDER  BY date ASC





SELECT DISTINCT county
FROM record 



SELECT DISTINCT sitename 
FROM record 
WHERE county ='新北市'









