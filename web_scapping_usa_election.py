import pandas
wiki = pandas.read_html('https://en.wikipedia.org/wiki/2020_United_States_presidential_election')
election = wiki[3]
print(election)
candidate_1 = election[1]
candidate_1_name = candidate_1[1]
candidate_1_party = candidate_1[2]
candidate_1_votes = candidate_1[5]

candidate_2 = election[2]
candidate_2_name = candidate_2[1]
candidate_2_party = candidate_2[2]
candidate_2_votes = candidate_2[5]

if candidate_1_votes > candidate_2_votes:
    print(candidate_1_name, 'of', candidate_1_party, 'party is the winner')
else:
    print(candidate_2_name, 'of', candidate_2_party, ' is the winner')