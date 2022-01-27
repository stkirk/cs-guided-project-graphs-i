# Town Judge Problem
"""
In a town, there are `N` people labelled from `1` to `N`.  There is a rumor
that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that
the person labelled a trusts the person labelled `b`.

If the town judge exists and can be identified, return the label of the town
judge.  Otherwise, return `-1`.

Constraints:

- `1 <= N <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `trust[i]` are all different
- `trust[i][0] != trust[i][1]`
- `1 <= trust[i][0], trust[i][1] <= N`
"""
"""
Inputs:
N -> int
trust -> List[List[int]]

Output:
int
"""
# trust is an array of pairs
# `trust[i] = [a, b]` --> a trusts b
# draw nodes for each N (person) and point to the person(or people) they trust(connection adjacency list)
# take the trust input and figure out how to get the neighbors for a particular node
def find_judge(N, trust):
    # first need to find neighbors, transform trust into a dictionary with N's as keys and lists of people they trust as values
    trusts = { i: [] for i in range(1, N + 1)}
    # need second dictionary with N's as keys and list of who they are trusted by as values
    trusted_by = { i: [] for i in range(1, N + 1)}
    # ex. if N == 1, return list with n's they trust [3, 2]
    # loop through trust and fill out dictionaries
    for truster, trustee in trust:
        # keys should already be in there for every N, just need to append to their values
        trusts[truster].append(trustee)
        trusted_by[trustee].append(truster)

    # Find out if only 1 person doesn't trust anyone else, empty trusts list
    potential_judge = []
    for n in trusts:
        if len(trusts[n]) == 0:
            potential_judge.append(n)
    if len(potential_judge) != 1:
        return -1
    # Once we have the one person that doesn't trust anyone, maked sure N-1 people trust them in trusted_by
    if len(trusted_by[potential_judge[0]]) != N -1:
        return -1
    else:
        return potential_judge[0]


print(find_judge(2, [[1,2]])) # 2
print("----------------")
print(find_judge(3, [[1,3],[2,3]])) # 3
print("----------------")
print(find_judge(3, [[1,3],[2,3],[3,1]])) # -1
print("----------------")
print(find_judge(3, [[1,2],[2,3]])) # -1
print("----------------")
print(find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) # 3

'''
Example 1:

```plaintext
Input: N = 2, trust = [[1,2]]
Output: 2
```

Example 2:

```plaintext
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```

Example 3:

```plaintext
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

Example 4:

```plaintext
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```

Example 5:

```plaintext
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```
'''