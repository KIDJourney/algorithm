class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        idx = len(coins) - 1
        cnt = 0
        while idx >= 0:
            cv = coins[idx]
            if cv <= amount:
                ccnt = amount // cv
                amount -= ccnt * cv
                cnt += ccnt

                print(cv, amount, ccnt, cnt)

            else:
                idx -= 1

        if amount != 0:
            return -1

        return cnt


s = Solution()
print(s.coinChange([186, 419, 83, 408], 6249))
