/* 
* @Author: kidjourney
* @Date:   2015-04-01 23:07:59
* @Last Modified by:   kidjourney
* @Last Modified time: 2015-04-01 23:17:59
*/
DELETE P1 FROM Person P1 , Person P2
WHERE P1.Email = P2.Email And P1.Id > P2.Id