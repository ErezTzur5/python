list_of_tuples = [
    ("Erez", [100, 90, 100]),
    ("Elik", [95, 95, 100]),
    ("Tal", [90, 85, 50])
]


def calculate_average_scores(list_of_tuples:list):
    """
    This function takes a list of tuples and takes applies the name as key in new dictionary and the value as sum of the scores in the list.
    this function returns a dict.
    """
    result = {}
    for name, scores in list_of_tuples:
        average_score = sum(scores) / len(scores)
        result[name] = average_score
    return result

average_scores = calculate_average_scores(list_of_tuples)
print(average_scores)