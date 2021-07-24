# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# not my solution

digits = '23'


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    numl = {'0': " ", '1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    # needs to be empty string in order to append to it
    existing = [''] if digits else []

    for digit in digits:
        # create a new list of combinations so that existing combinations
        # aren't overwritten (key to making this algorithm work)
        new = []

        # append the current letter to every existing combination for every
        # different letter in the current digit's value pair
        for letter in numl[digit]:
            for comb in existing:
                new.append(comb + letter)

        # reassign the existing combination list to the newly created
        # combinations, which are now all possible combinations of the
        # letters from the digits at this point
        existing = new
    return existing


print(letterCombinations(digits))
