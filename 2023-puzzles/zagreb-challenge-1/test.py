from time import time
import matplotlib.pyplot as plt
import random


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if 0 not in nums:
        return 0

    m = max(nums) 
    n = m * (m + 1) / 2 - sum(nums)  
    
    return n if n else m+1


if __name__ == "__main__":
    total = []
    lens = []
    for _ in range(10000):
        sequence = [a for a in range(random.randint(1, 10000))]
        del sequence[random.randint(0, len(sequence)-1)]
        start = time()
        missingNumber(sequence)
        total.append(time() - start)
        lens.append(len(sequence))

    plt.plot(lens, total, 'r+',)
    plt.xlabel('Sequence Length')
    plt.ylabel('Duration')
    plt.savefig('./fig.pdf')

