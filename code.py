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

#304. Range Sum Query 2D - Immutable
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.newMatrix = []
        for i in range(len(matrix)):
            newLinearArray = [0] * len(matrix[i])
            self.newMatrix.append(newLinearArray)
        self.newMatrix[0][0] = matrix[0][0]
        for r in range(1,len(self.newMatrix)):
            self.newMatrix[r][0] = self.newMatrix[r-1][0] + matrix[r][0]
        for c in range(1,len(self.newMatrix[0])):
            self.newMatrix[0][c] = matrix[0][c] + self.newMatrix[0][c-1]
        for row in range(1,len(self.newMatrix)):
            for col in range(1,len(self.newMatrix[0])):
                self.newMatrix[row][col] = matrix[row][col] + self.newMatrix[row-1][col] + self.newMatrix[row][col-1] - self.newMatrix[row-1][col-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = 0
        upperValue = 0
        leftValue = 0
        addAgain = 0
        totalSum = self.newMatrix[row2][col2] 
        if row1-1 >= 0:
            upperValue = self.newMatrix[row1-1][col2] 
        else:
            upperValue = 0
        if col1-1 >= 0:
            leftValue = self.newMatrix[row2][col1-1]
        else:
            leftValue = 0
        if row1-1 >= 0 and col1-1 >= 0:
            addAgain = self.newMatrix[row1-1][col1-1]
        else:
            addAgain = 0
        return totalSum - (upperValue + leftValue) + addAgain


#128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxLength = 0
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1
        for key,val in hashMap.items():
            currVal = key
            if currVal - 1 not in hashMap:
                nextVal = currVal + 1
                currLength = 1
                while nextVal in hashMap:
                    nextVal += 1
                    currLength += 1
                maxLength = max(maxLength, currLength)
        return maxLength
        
       

        
        
