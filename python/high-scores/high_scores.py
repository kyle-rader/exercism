def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_scores = sorted(scores)
    sorted_scores.reverse()
    return sorted_scores[0:3]
