def remove_nth_char(s, n):
    if (n < 0 or n >= len(s)):
        return "Error: Index out of range."
    return s[:n] + s[n+1:]


input_str = "sanket"
index_to_remove = 2
result = remove_nth_char(input_str, index_to_remove)
print("Original String:", input_str)
print("Modified String:", result)