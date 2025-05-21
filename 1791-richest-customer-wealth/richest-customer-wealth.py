class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(0,len(accounts)):
            dummy =sum(accounts[i])
            result = max(result , dummy)
        return(result)
