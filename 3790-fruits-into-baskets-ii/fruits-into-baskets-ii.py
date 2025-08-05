class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if(fruits[i]<=baskets[j]):
                    fruits[i] = 0
                    baskets[j] = 0
                    break

        counter = 0 
        for i in range(len(fruits)):
            if(fruits[i] != 0):
                counter +=1
        return(counter)

        