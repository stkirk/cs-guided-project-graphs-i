# in a city of n people:
# one of the n people might be a spy
# By definition the spy:
    # does not trust anyone else (trusts themselves)
    # IS trusted by EVERYONE else (so everyone trusts them including themselves)
    # works alone, only can be ONE spy
# given trust, a list of pairs
    # Each trust[i] = [a, b] --> person a trusts person b
# return the identity of the spy
# if no spy can be found (maybe if there is 2 spies???) return -1

# represent people by their index in trust list
import enum


def spy_finder(n, trust):
    # build out a dictionary with the person's index as a key, and a list of people they trust as value
    trusts = {i: [] for i in range(1, n + 1)}
    # create trusted_by dict
    # init trusted_by dict
    trusted_by = {i: [] for i in range(1, n + 1)}
    # loop through trust
    for trusted in trust:
        # trusted is a list [a, b] --> person a trusts person b
        # append trusted[1] to trusts[trusted[0]] list
        trusts[trusted[0]].append(trusted[1])
        # trusted is a list [a, b] --> person a trusts person b
        # append trusted[0] to trusted_by[trusted[1]]
        trusted_by[trusted[1]].append(trusted[0])

    # We know in trusts if a person (key/n index) has an empty trust list, they could be the spy
    potenital_spy = []
    # loop through trusts
    for person, trust_list in trusts.items():
        # if n is an empty list
        if len(trust_list) == 0:
            # append n to potential_spy list
            potenital_spy.append(person)


    # Need to cross-reference potential_spy in trusted_by dict to see if everyone else (n-1 people) trusts them
    # possible edge case: len(potential_spy) > 1 ?????
    # if trusted_by[potential_spy[0]] length == n - 1
    if len(potenital_spy) == 1 and len(trusted_by[potenital_spy[0]]) == n - 1:
        # return potential_spy[0] 
        return potenital_spy[0]


    # The spy cannot be found, return -1
    return -1


print(spy_finder(2, [[1, 2]])) # 2
print(spy_finder(3, [[1, 3], [2, 3]])) # 3
print(spy_finder(3, [[1, 3], [2, 3], [3, 1]])) # -1
print(spy_finder(3, [[1, 2], [2, 3]])) # -1
print(spy_finder(4, [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]])) # 3
