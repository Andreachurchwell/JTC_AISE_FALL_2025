# def lengthOfLastWord(s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # we will need a list to hold substrings
#         # we will need to split at white space and find the len of the last string
#         result = []
#         for item in s.split():
#             result.append(item)
#         return len(item)
        
# print(lengthOfLastWord('Hi my name is andrea'))

class Solution:
    def longestCommonPrefix(self, strs):
        # Step 1: handle edge cases
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        # Step 2: start with the first word as a baseline
        first_word = strs[0]
        prefix = ""

        # Step 3: loop through each character position in the first word
        for i in range(len(first_word)):
            current_char = first_word[i]  # letter at position i

            # Step 4: compare this letter with the same position in all other words
            for word in strs[1:]:
                # if we reach the end of a word OR letters don't match, stop
                if i >= len(word) or word[i] != current_char:
                    return prefix  # everything before this point was common

            # Step 5: if we made it through the loop, add this character to prefix
            prefix += current_char

        # Step 6: return the final prefix after all checks
        return prefix