import github_utils
import stackoverflow_utils
import hn_utils

def calculate_score(github_id=None, stackoverflow_id=None, hn_id=None):

    if github_id:
        contributions = github_utils.get_public_contributions(github_id)
    else:
        contributions = 0
    if stackoverflow_id:
        reputation = stackoverflow_utils.get_reputation(stackoverflow_id)
    else:
        reputation = 0
    if hn_id:
        karma = hn_utils.get_karma(hn_id)
    else:
        hn_id = 0

    contributions = len(str(contributions))*int(str(contributions)[0])
    reputation = len(str(reputation))*int(str(reputation)[0])
    karma = len(str(karma))*int(str(karma)[0])

    score = contributions*2 + reputation*2 + karma*2
    return score

print calculate_score('theycallmeswift', "385913", 'swift')
