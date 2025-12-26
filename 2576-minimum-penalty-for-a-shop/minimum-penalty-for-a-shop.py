class Solution:
    def bestClosingTime(self, customers: str) -> int:
        counter = defaultdict(int)
        counter_2 = defaultdict(int)
        counter[len(customers)] = 0
        suffex_counter = 0
        for i in range(len(customers)-1  , -1 , -1):
            if(customers[i] == 'Y'):
                suffex_counter +=1
            counter[i] = suffex_counter

        prefix_counter = 0
        counter_2[0] = 0
        for i in range(0 , len(customers)):
            counter_2[i] = prefix_counter
            if(customers[i] == 'N'):
                prefix_counter +=1
        counter_2[len(customers)] = prefix_counter

        # print(counter , counter_2)
        result = float('inf')
        ans_hour  = 0
        for i in range(0 ,len(customers)):
            if((counter_2[i] + counter[i]) < result):
                result = (counter_2[i] + counter[i])
                ans_hour = i

        if(counter[len(customers)] + counter_2[len(customers)] < result):
            ans_hour = len(customers)


        return (ans_hour)