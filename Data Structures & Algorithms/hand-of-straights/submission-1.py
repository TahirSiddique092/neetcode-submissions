class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize) != 0:
            return False

        noOfGroups = int(len(hand)/groupSize)
        hashmap = defaultdict(int)

        for each in hand:
            hashmap[each] = hashmap[each] + 1

        hand = list(set(hand))
        heapq.heapify(hand)

        for _ in range(noOfGroups):
            curr = hand[0]
            for _ in range(groupSize):
                if hashmap[curr] == 0:
                    return False
                hashmap[curr] -= 1
                if not hashmap[curr]:
                    heapq.heappop(hand)
                curr += 1
        return True

        