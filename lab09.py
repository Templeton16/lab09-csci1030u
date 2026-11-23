# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   I need to find two numbers that add to target.
    #   For [3, 2, 4] and target 6, 2 needs 4, which appears later.
    #   I will keep track of numbers seen so far and their positions.
    seen = {}

    for i in range(len(nums)):
        other = target - nums[i]
        if other in seen:
            return [seen[other], i]
        seen[nums[i]] = i

    return [-1, -1]


def max_profit(prices):
    # Outline:
    #   Buy before selling, so I track the lowest price seen.
    #   At each later price, compare the possible profit with my best profit.
    #   [7, 1, 5, 3, 6, 4] gives 5 by buying at 1 and selling at 6.
    if not prices:
        return 0

    lowest = prices[0]
    best = 0

    for price in prices:
        if price < lowest:
            lowest = price
        elif price - lowest > best:
            best = price - lowest

    return best


def max_subarray(nums):
    # Outline:
    #   I keep the sum of the current block and the largest sum found.
    #   If the current block becomes negative, I start again at the next number.
    #   For [-2, 1, -3], 1 is the largest subarray.
    current = nums[0]
    largest = nums[0]

    for value in nums[1:]:
        current = current + value
        if value > current:
            current = value
        if current > largest:
            largest = current

    return largest


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   Opening brackets go onto a stack.
    #   A closing bracket must match the most recent opening bracket.
    #   At the end, the stack should be empty.
    matching = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in matching:
            if len(stack) == 0 or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return not stack


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
