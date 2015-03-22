SELECT A.Name FROM Customers A 
WHERE A.Id NOT IN (SELECT B.CustomerId FROM Orders B)