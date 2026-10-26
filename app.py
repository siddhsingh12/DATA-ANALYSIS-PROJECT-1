#importing necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import tabulate as tab

#printing the IPL dataset in a tabular format
def print_table(title, data):
    print(f"\n{title}")
    print(tab.tabulate(data, headers="keys", tablefmt="grid", showindex=False))

#reading the IPL dataset

df = pd.read_csv("ipl.csv")

#printing the number of rows and columns in the dataset

dataset_size = pd.DataFrame({
    "Metric": ["Number of rows", "Number of columns"],
    "Value": [df.shape[0], df.shape[1]]
})
print_table("Dataset size", dataset_size)

#printing the winner column to see the number of matches won by each team

team_wins = df["winner"].dropna().value_counts()

#printing the number of matches won by each team

team_wins_table = team_wins.rename_axis("Team").reset_index(name="Matches won")
print_table("Matches won by each team", team_wins_table)


#most matches per season

matches_per_season = df["season"].value_counts().sort_index()
matches_per_season_table = matches_per_season.rename_axis("Season").reset_index(name="Matches")
print_table("Matches per season", matches_per_season_table)

#season's with the most matches

most_matches = matches_per_season.max()
most_matches_table = matches_per_season[matches_per_season == most_matches].rename_axis("Season").reset_index(name="Matches")
print_table("Season's with the most matches", most_matches_table)

#season's with the least matches

least_matches = matches_per_season.min()
least_matches_table = matches_per_season[matches_per_season == least_matches].rename_axis("Season").reset_index(name="Matches")
print_table("Season's with the least matches", least_matches_table)

#sorting the dataset by city in descending order
sort_values = df.sort_values(by="city", ascending=False)
print_table("Matches sorted by city", sort_values)

#season matches bar chart
matches_per_season.plot(kind="bar", figsize=(10, 5), title="IPL Matches per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

#team wins bar chart

team_wins.plot(kind="bar", figsize=(10, 5), title="IPL Match Wins by Team")
plt.xlabel("Team")
plt.ylabel("Matches won")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()