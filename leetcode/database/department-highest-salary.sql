SELECT Department.Name as Department , Employee.Name as Employee ,
 hs.Salary 
 FROM (SELECT DepartmentId, MAX(Salary) as Salary FROM Employee Group by DepartmentId) hs
INNER JOIN Employee on Employee.Salary = hs.Salary and Employee.DepartmentId = hs.DepartmentId
INNER JOIN Department on Department.Id = hs.DepartmentId
