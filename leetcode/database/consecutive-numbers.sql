SELECT DISTINCT  A.Num 
FROM Logs A , Logs B , Logs C
WHERE A.Id = B.Id - 1 and A.Id = C.Id-2
AND A.Num = B.Num and A.Num = C.Num