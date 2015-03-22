/* 
* @Author: KIDJourney
* @Date:   2015-03-15
* @Last Modified by:   KIDJourney
* @Last Modified time: 2015-03-15
*/
SELECT E1.Name
FROM Employee as E1 , Employee as E2
where E1.ManagerId = E2.Id and E1.Salary > E2.Salary