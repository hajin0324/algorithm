SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS D 
JOIN SKILLCODES S 
ON (D.SKILL_CODE & S.CODE) > 0 AND S.CATEGORY = 'Front End'
ORDER BY ID;