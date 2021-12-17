"""
Grading: 9/10 
Missing a figure in section 6
"""


import pandas as pd
import matplotlib.pyplot as plt

# 1 - Importing datasets as DataFrames
review_raw = pd.read_csv('googleplaystore_user_reviews.csv')
apps_raw = pd.read_csv('googleplaystore.csv')

# 2 - Deleteing any reviews without sentiments or translated reviews
reviews = review_raw.dropna(subset=['Translated_Review', 'Sentiment'])

# 3 - Removing Invalid Ratings
apps = apps_raw[apps_raw['Rating'] <= 5]

# 4 - Android Version Pie Chart 
# First we ge the necessary value counts
ver_counts = apps['Android Ver'].value_counts()

# next, we group those with < 5% into an 'Others' category
clean_ver_counts = ver_counts[:7].copy()
others_value = ver_counts[7:].sum()
others_series = pd.Series([others_value], index=['Others'])
clean_ver_counts = clean_ver_counts.append(others_series)

# plot the Andriod Versions pie chart
clean_ver_counts.plot.pie()

# 5- App Category Pie Chart
# First we get the necessary value counts
cat_counts = apps['Category'].value_counts()

# next, we group those with < 3% into an 'Others' category
clean_cat_counts = cat_counts[:13].copy()
others2_value = cat_counts[13:].sum()
others2_series = pd.Series([others2_value], index=['Others'])
clean_cat_counts = clean_cat_counts.append(others2_series)

# plot the App Category pie chart
clean_cat_counts.plot.pie()

# 6 - Rating and Reviews Histograms
# select a subset of data
hist_data = apps[['Rating', 'Reviews']]

#make sure we have the correct data tpes, in this case we need to change reviews to an integer
hist_data['Reviews'] = hist_data['Reviews'].astype(int)

# plot the histograms
hist_data.hist(bins=20)

# 7 - Sentiments histogram
# we get the necessary value counts and the plot them
reviews['Sentiment'].value_counts().plot.bar()

# 8 - Merging the data frames
# we merge on the left to make sure to keep the same number of unique apps
merged_df = pd.merge(apps, reviews, on='App', how='left')

# 9 - Paid Games DataFrames
# we sort by rating and then by reviews making sure that it is descending
paid_apps = merged_df[merged_df['Type'] != 'Free'].sort_values(['Rating', 'Reviews'], ascending=(False,False))


