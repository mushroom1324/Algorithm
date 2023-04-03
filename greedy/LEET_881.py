class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            weight = 0
            cnt = 0
            while cnt < 2 and j >= i and weight + people[j] <= limit:
                weight += people[j]
                cnt += 1
                j -= 1
            if i > j:
                ans += 1
                break
            while cnt < 2 and i <= j and weight + people[i] <= limit:
                weight += people[i]
                cnt += 1
                i += 1
            ans += 1
        return ans