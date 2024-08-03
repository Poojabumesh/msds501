
def reverse_string(s):
    """
    Reverses the input list of characters in place.
    
    :param s: List[str] - A list of characters to be reversed.
    :return: None - This function modifies the list in place and does not return anything.
    
    Example:
    >>> s = ['h', 'e', 'l', 'l', 'o']
    >>> reverseString(s)
    >>> print(s)
    ['o', 'l', 'l', 'e', 'h']
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def find_max_average(nums, k):
    """
    Finds the maximum average value of a contiguous subarray of length k.

    This function takes an integer array `nums` and an integer `k`, and finds a 
    contiguous subarray of length `k` that has the maximum average value. It 
    returns this maximum average value as a float.

    :param nums: List[int] - The input list of integers.
    :param k: int - The length of the contiguous subarray.
    :return: float - The maximum average value of a contiguous subarray of length `k`.

    Example:
    >>> find_max_average([1, 12, -5, -6, 50, 3], 4)
    12.75

    The contiguous subarray with the maximum average is [12, -5, -6, 50] 
    and the average value is (12 + -5 + -6 + 50) / 4 = 51 / 4 = 12.75.
    """
    max_sum = sum(nums[:k])
    current_sum = max_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum / k


def find_numbers(nums):
    """
    Given an integer array nums, find all the unique numbers x in nums that satisfy
    the following: x + 1 is not in nums, and x - 1 is not in nums.

    :param nums: List[int] - The input list of integers.
    :return: List[int] - A list of integers
    Example:
    >>> find_numbers([1, 2, 3, 6, 7, 8, 10])
    [10]
    
    In this example, the numbers 1, 2, 3, 6, 7, and 8 are adjacent to other numbers, 
    so only 10 is returned in the result.
    """
    num_set = set(nums)
    unique_numbers = []

    for num in nums:
        if (num + 1 not in num_set) and (num - 1 not in num_set):
            unique_numbers.append(num)
    
    return unique_numbers


def contains_duplicate(nums):
    """
    Given an integer array nums, return True if any value appears at least twice in the array, 
    and return False if every element is distinct.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    bool: True if any integer appears at least twice, False if all integers are unique.

    Example:
    >>> contains_duplicate([1, 2, 3, 1])
    True
    >>> contains_duplicate([1, 2, 3, 4])
    False
    >>> contains_duplicate([])
    False
    """
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False


def find_winners_and_losers(matches):
    """
    Given an integer array matches where matches[i] = [winneri, loseri] indicates
    that the player winneri defeated player loseri in a match, return a list answer
    of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

    Both lists in the answer should be sorted in increasing order.

    Parameters:
    matches (List[List[int]]): A list of matches where each match is represented
                               as a list of two integers [winner, loser].

    Returns:
    List[List[int]]: A list containing two lists:
                     - The first list contains all players who have not lost any matches.
                     - The second list contains all players who have lost exactly one match.
                     Both lists are sorted in increasing order.

    Example:
    >>> matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4]]
    >>> find_winners_and_losers(matches)
    [1, 2, 10], [4, 5, 7, 8, 9]
    """
    from collections import defaultdict

    loss_count = defaultdict(int)
    winners = set()

    for winner, loser in matches:
        winners.add(winner)
        loss_count[loser] += 1

    no_losses = [player for player in winners if loss_count[player] == 0]
    one_loss = [player for player, count in loss_count.items() if count == 1]

    return [sorted(no_losses), sorted(one_loss)]
