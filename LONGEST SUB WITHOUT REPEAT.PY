def length_of_longest_substring(s):
    seen = {}
    l = max_len = 0
    for r in range(len(s)):
        if s[r] in seen and seen[s[r]] >= l:
            l = seen[s[r]] + 1
        seen[s[r]] = r
        max_len = max(max_len, r - l + 1)
    return max_len

print(length_of_longest_substring("abcabcbb"))  # 3
#Time Complexity: O(n)
