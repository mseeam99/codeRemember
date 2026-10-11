#14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for w in range(1,len(strs)):
                word = strs[w]
                if i >= len(word) or word[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

#347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        array = []
        for key,val in hashMap.items():
            array.append((val,key))
        heapq.heapify(array)
        array = heapq.nlargest(k,array)
        returnArray = []
        for i in range(k):
            returnArray.append(array[i][1])
        return returnArray 
        '''
        #Bucket Sort
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1        
        array = []
        for i in range(len(nums)+1):
            array.append([])
        for key,val in hashMap.items():
            array[val].append(key)
        answer = []
        count = 0
        for i in range(len(array)-1,-1,-1):
            if len(array[i])!=0:
                for j in range(len(array[i])):
                    if count >= k:
                        break
                    answer.append(array[i][j])
                    count += 1
        return answer











        

        
       

        
        
