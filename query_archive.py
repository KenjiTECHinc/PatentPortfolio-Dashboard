pieChartQuery = """
SELECT "Holder", COUNT("Holder ID") AS "Patents"                       
FROM '1- Patents'                                                                                                   
NATURAL JOIN '2- Holders'                                                                                           
GROUP BY "Holder ID"                                                                                                
ORDER BY COUNT("Holder ID");
"""

pieChartQuery2 = """
SELECT 
    h."Holder ID",
    h."Holder",
    SUM(CASE WHEN p."Legal Status" = 'Valid' THEN 1 ELSE 0 END) AS Valid,
    SUM(CASE WHEN p."Legal Status" = 'Overdue' THEN 1 ELSE 0 END) AS Overdue,
    SUM(CASE WHEN p."Legal Status" = 'Pub.' THEN 1 ELSE 0 END) AS Published
FROM 
    "1- Patents" p
JOIN 
    "2- Holders" h
ON 
    p."Holder ID" = h."Holder ID"
GROUP BY 
    h."Holder ID", h."Holder"
ORDER BY 
    h."Holder";
"""

### Line Chart Queries ###

lineChartQuery = """SELECT strftime('%Y', DATE(REPLACE("Publication Date", '/', '-'))) AS Year,                                                                                                    
SUM(CASE WHEN "Holder ID" = 'H002' THEN 1 ELSE 0 END) AS "Intel Corporation",                    
SUM(CASE WHEN "Holder ID" = 'H003' THEN 1 ELSE 0 END) AS "Samsung Electronics",                     
SUM(CASE WHEN "Holder ID" = 'H001' THEN 1 ELSE 0 END) AS "Taiwan Semiconductor Manufacturing Company"                        
FROM '1- Patents'                                                                                                   
NATURAL JOIN '2- Holders'                                                                                           
GROUP BY Year                                                                                                
ORDER BY Year;"""

lineIntelQuery = """SELECT strftime('%Y', DATE(REPLACE("Publication Date", '/', '-'))) AS Year, CASE 
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1' 
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3' 
        ELSE 'Q4'                                                                                                     
    END AS Quarter,                                                                                                   
SUM(CASE WHEN "Citation Type" = 'Domestic' AND "Holder" = "Intel Corporation" THEN "Citation Count" ELSE 0 END) AS Domestic,                         
SUM(CASE WHEN "Citation Type" = 'Foreign' AND "Holder" = "Intel Corporation" THEN "Citation Count" ELSE 0 END) AS "Foreign"                        
FROM '1- Patents'
NATURAL JOIN '2- Holders'                                                                                                   
NATURAL JOIN '4- Citations'                                                                                           
GROUP BY Year, Quarter                                                                                                
ORDER BY Year, Quarter;"""

lineSamsungQuery = """SELECT strftime('%Y', DATE(REPLACE("Publication Date", '/', '-'))) AS Year, CASE 
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1' 
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3' 
        ELSE 'Q4'                                                                                                     
    END AS Quarter,                                                                                                   
SUM(CASE WHEN "Citation Type" = 'Domestic' AND "Holder" = "Samsung Electronics" THEN "Citation Count" ELSE 0 END) AS Domestic,                         
SUM(CASE WHEN "Citation Type" = 'Foreign' AND "Holder" = "Samsung Electronics" THEN "Citation Count" ELSE 0 END) AS "Foreign"                        
FROM '1- Patents'
NATURAL JOIN '2- Holders'                                                                                                   
NATURAL JOIN '4- Citations'                                                                                           
GROUP BY Year, Quarter                                                                                                
ORDER BY Year, Quarter;"""

lineTSMCQuery = """SELECT strftime('%Y', DATE(REPLACE("Publication Date", '/', '-'))) AS Year, CASE 
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 1 AND 3 THEN 'Q1' 
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 4 AND 6 THEN 'Q2'
        WHEN CAST(strftime('%m', DATE(REPLACE("Publication Date", '/', '-'))) AS INTEGER) BETWEEN 7 AND 9 THEN 'Q3' 
        ELSE 'Q4'                                                                                                     
    END AS Quarter,                                                                                                   
SUM(CASE WHEN "Citation Type" = 'Domestic' AND "Holder" = "Taiwan Semiconductor Manufacturing Company" THEN "Citation Count" ELSE 0 END) AS Domestic,                         
SUM(CASE WHEN "Citation Type" = 'Foreign' AND "Holder" = "Taiwan Semiconductor Manufacturing Company" THEN "Citation Count" ELSE 0 END) AS "Foreign"                        
FROM '1- Patents'
NATURAL JOIN '2- Holders'                                                                                                   
NATURAL JOIN '4- Citations'                                                                                           
GROUP BY Year, Quarter                                                                                                
ORDER BY Year, Quarter;"""

lineChartQuery3 = """WITH TopMIPC3 AS (
    SELECT MIPC3
    FROM '1- Patents'
    WHERE "Publication Year" >= strftime('%Y', 'now', '-7 years')
    GROUP BY MIPC3
    ORDER BY COUNT(*) DESC
    LIMIT 5
)
SELECT "Publication Year", MIPC3, COUNT(*) as Patent_Count
FROM '1- Patents'
WHERE MIPC3 IN (SELECT MIPC3 FROM TopMIPC3)
  AND "Publication Year" >= strftime('%Y', 'now', '-7 years')
GROUP BY "Publication Year", MIPC3
ORDER BY "Publication Year", MIPC3;
"""



# """WITH TopMIPC3 AS (
#     SELECT MIPC3
#     FROM '1- Patents'
#     WHERE "Publication Year" >= strftime('%Y', 'now', '-5 years')
#     GROUP BY MIPC3
#     ORDER BY COUNT(*) DESC
#     LIMIT 5
# )
# SELECT "Publication Year", MIPC3, COUNT(*) as Patent_Count
# FROM '1- Patents'
# WHERE MIPC3 IN (SELECT MIPC3 FROM TopMIPC3)
#   AND "Publication Year" >= strftime('%Y', 'now', '-5 years')
# GROUP BY "Publication Year", MIPC3
# ORDER BY "Publication Year", MIPC3;
# """