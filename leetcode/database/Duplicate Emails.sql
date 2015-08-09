/* 
* @Author: KIDJourney
* @Date:   2015-03-15
* @Last Modified by:   KIDJourney
* @Last Modified time: 2015-03-15
*/
SELECT b.Email FROM Person b
WHERE b.Email NOT IN (SELECT DISTINCT a.Email FROM Person a)