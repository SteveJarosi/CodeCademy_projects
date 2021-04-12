#import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
print(ad_clicks.groupby('utm_source').user_id.count().reset_index())
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()
clicks_pivot['percent_clicked']=clicks_pivot.apply(lambda row: row[True]*100/(row[True]+row[False]), axis=1)
#clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)
xp_g = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(xp_g)
a_b = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(a_b)
a_b_pivot = a_b.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()
print(a_b_pivot)
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
#print(a_clicks)
a_clicks_by_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
a_clicks_by_day['percent']=a_clicks_by_day.apply(lambda row: row['user_id']*100/a_clicks_by_day['user_id'].sum(), axis=1)
print('A:', a_clicks_by_day)
b_clicks_by_day = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks_by_day['percent']=b_clicks_by_day.apply(lambda row: row['user_id']*100/b_clicks_by_day['user_id'].sum(), axis=1)
print('B:', b_clicks_by_day)
