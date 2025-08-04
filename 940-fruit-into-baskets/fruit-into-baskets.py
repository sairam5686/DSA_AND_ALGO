class Solution(object):
    def totalFruit(self, fruits):
        counter = defaultdict(int)
        left , right  = 0 ,0
        max_len = 0
        while(right<len(fruits)):
            counter[fruits[right]] +=1
            while(len(counter)>2):
                counter[fruits[left]] -=1
                if(counter[fruits[left]] == 0):
                    counter.pop(fruits[left])
                left +=1
            if(len(counter)<=2):
                max_len = max(max_len , (right - left + 1))
            right +=1

        return(max_len)
                        
                        