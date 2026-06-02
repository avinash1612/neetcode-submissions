class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_tracking_hash = {}
        return_array = []
        max = 0
        array_cnt = []
        for each_element in nums:
            if(each_element not in count_tracking_hash.keys()):
                count_tracking_hash[each_element] =1
            else:
                count_tracking_hash[each_element] +=1
            if(count_tracking_hash[each_element]>max):
                max = count_tracking_hash[each_element]
        for each_key, each_value in count_tracking_hash.items():
            array_cnt.append([each_value,each_key])
        array_cnt.sort()
        #print(array_cnt)
        res = 0
        while(res < k):
            return_array.append(array_cnt.pop()[1])
            res +=1

        return(return_array)
        
        