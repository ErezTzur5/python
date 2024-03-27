scores = [
    {"name":"tal" , "score":90},
    {"name":"erez" , "score":80},
    {"name":"elik" , "score":60},
    {"name":"tomer" , "score":70},
    {"name":"yuval" , "score":85},
    {"name":"noa" , "score":79},
    {"name":"raz" , "score":88},
]


def sorting_by_score(data:dict):
    """
    This function sorts all the dictionary by the highest score to lowest.
    """
    return sorted(scores,key=lambda x: x["score"], reverse=True) # need to ask elik how this row works.

        


result = sorting_by_score(scores)
print(result)