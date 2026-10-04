
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_count = {}

        for num in nums:
            freq_count[num] = freq_count.get(num, 0)+1

        heap = []

        for num, count in freq_count.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        answer = []

        for count, num in heap:
            answer.append(num)

        return answer