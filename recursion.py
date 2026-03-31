def permutations(s, step=0):
    if step == len(s):        # Base case: all positions fixed
        print("".join(s))
        return

    for i in range(step, len(s)):
        s[step], s[i] = s[i], s[step]   # Swap to try element at current position
        permutations(s, step + 1)       # Recursive call for next position
        s[step], s[i] = s[i], s[step]   # Backtrack: undo swap

# Example
string = list("ABC")
permutations(string)