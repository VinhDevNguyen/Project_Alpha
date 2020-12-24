import pandas as pd 




# def evaluate_accuracy_at_4(submission,ground_truth):
#     '''checks if the true city is within the four recommended cities'''
#     data_to_eval = submission.join(ground_truth,on='utrip_id')
#     hits = data_to_eval.apply(
#         lambda row: row['city_id'] in (row[['city_id_1', 'city_id_2', 'city_id_3', 'city_id_4']].values),
#             axis = 1)
#     return hits.mean()