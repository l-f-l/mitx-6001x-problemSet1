s = "abcbcd"
longestAlphabeticalSubstring = s[0]
longestAlphabeticalSubstringCheck = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        longestAlphabeticalSubstringCheck += s[i]
    else:
        if len(longestAlphabeticalSubstringCheck) > len(longestAlphabeticalSubstring):
            longestAlphabeticalSubstring = longestAlphabeticalSubstringCheck
        longestAlphabeticalSubstringCheck = ""

if len(longestAlphabeticalSubstringCheck) > len(longestAlphabeticalSubstring):
    longestAlphabeticalSubstring = longestAlphabeticalSubstringCheck

print("Longest substring in alphabetical order is: " + str(longestAlphabeticalSubstring))