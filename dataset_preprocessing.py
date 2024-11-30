import pandas as pd
url = "https://gitlab.com/harsha.rathi/informationvisualizationdataset/-/raw/main/olympics.csv"
# Read the CSV file directly from the URL
df = pd.read_csv(url)
# Display the first few rows
columns_to_fill = ['height', 'weight']
# Fill NA values with the mean of each specified column
df[columns_to_fill] = df[columns_to_fill].fillna(df[columns_to_fill].mean())
data = df
# Filter out only rows with medals
data_with_medals = data[data['medal'].notna()]
# Group by country (NOC) and count medals
top_countries = (data_with_medals.groupby('noc')
                 .size()
                 .reset_index(name='MedalCount')
                 .sort_values(by='MedalCount', ascending=False)
                 .head(15))
# Filter the dataset to include only the top 15 countries
top15_data = data[data['noc'].isin(top_countries['noc'])]
# Group by country (NOC) and count medals
top_sports = (top15_data.groupby('sport')
                 .size()
                 .reset_index(name='ParticipantCount')
                 .sort_values(by='ParticipantCount', ascending=False)
                 .head(25))
# Filter the dataset to include only the top 15 countries
top15_data = top15_data[top15_data['sport'].isin(top_sports['sport'])]
# Save the filtered dataset to a CSV file
top15_data.to_csv("top15_countries_sport.csv", index=False)