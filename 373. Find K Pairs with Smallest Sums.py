from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int) :
        
        m=len(nums1)
        n=len(nums2)



        res =[]
        visited = set()

        minheap = [(nums1[0]+nums2[0],(0,0))]
        visited.add((0,0))

        while k > 0 and minheap:
            val,(i,j) = heappop(minheap)
            res.append([i,j])
            
            if i+1 < m and (i+1,j) not in visited:
                heappush(minheap,(nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j))
            if j+1 < n and (i,j+1) not in visited:
                heappush(minheap,(nums1[i]+nums2[j+1],(i,j+1)))
                visited.add((i,j+1))
            k-=1
        return res





obj = Solution()
#print(obj.kSmallestPairs([1,2,3],[4,5,6],2))
print(obj.kSmallestPairs([1,7,11],[2,4,6],3))
print(obj.kSmallestPairs([1,1,2],[1,2,3],2))
print(obj.kSmallestPairs([1,2],[3],3))
print(obj.kSmallestPairs([1,2,4,5,6],[3,5,7,9],3)) #[[1,3],[2,3],[1,5]]

    
    