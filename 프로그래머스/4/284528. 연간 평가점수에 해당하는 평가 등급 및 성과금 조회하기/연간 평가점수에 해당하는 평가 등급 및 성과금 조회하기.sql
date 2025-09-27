-- 코드를 작성해주세요
SELECT e.EMP_NO, e.EMP_NAME, 
    CASE 
        WHEN g.SCORE>=96 THEN 'S'
        WHEN g.SCORE>=90 THEN 'A'
        WHEN g.SCORE>=80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE
        WHEN g.SCORE>=96 THEN 0.2*e.SAL
        WHEN g.SCORE>=90 THEN 0.15*e.SAL
        WHEN g.SCORE>=80 THEN 0.1*e.SAL
        ELSE 0
    END AS BONUS
    
FROM HR_EMPLOYEES AS e
    JOIN (
        SELECT g2.EMP_NO, g2.YEAR, AVG(g2.SCORE) AS SCORE
        FROM HR_GRADE AS g2
        GROUP BY g2.EMP_NO, g2.YEAR
    ) AS g
    ON e.EMP_NO = g.EMP_NO
ORDER BY e.EMP_NO;