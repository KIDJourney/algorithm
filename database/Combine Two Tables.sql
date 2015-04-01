/* 
* @Author: kidjourney
* @Date:   2015-04-01 22:26:17
* @Last Modified by:   kidjourney
* @Last Modified time: 2015-04-01 22:36:47
*/
SELECT P.FirstName , P.LastName , A.City , A.State
FROM Person P 
LEFT JOIN Address A on  P.PersonId = A.PersonId