"""
NBA Team Per-Game Stats (2024–25 Season)

Column key:
- G    = Games played
- MP   = Minutes played (team total per game ≈ 240)
- FG   = Field Goals made
- FGA  = Field Goals attempted
- FG%  = Field Goal percentage
- 3P   = 3-Point Field Goals made
- 3PA  = 3-Point attempts
- 3P%  = 3-Point percentage
- 2P   = 2-Point Field Goals made
- 2PA  = 2-Point attempts
- 2P%  = 2-Point percentage
- FT   = Free Throws made
- FTA  = Free Throw attempts
- FT%  = Free Throw percentage
- ORB  = Offensive Rebounds
- DRB  = Defensive Rebounds
- TRB  = Total Rebounds
- AST  = Assists
- STL  = Steals
- BLK  = Blocks
- TOV  = Turnovers
- PF   = Personal Fouls
- PTS  = Points scored
"""


import pandas as pd

df = pd.read_csv('nba_team_per_game.csv')
print(df.head())
print(df.columns)

df = df.drop(columns=['Rk'])

df = df.rename(columns={
    'Team': 'team',
    'PTS': 'points',
    'AST': 'assists',
    'TRB': 'rebounds',
    'STL': 'steals',
    'BLK': 'blocks'
})
# Dictionary mapping full team names to abbreviations
team_map = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BRK",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS",
}

# normalize team labels before mapping
# removing * and any extra spaces
df['team'] = df['team'].astype(str).str.replace('*', '', regex=False).str.strip()

# check if "League Average" row exists, drop if it does
if df["team"].str.lower().eq("league average").any():
    df = df[df["team"].str.lower() != "league average"]
    print("Dropped 'League Average' row.")
else:
    print("No 'League Average' row found.")

# Apply the mapping
df["team"] = df["team"].replace(team_map)

print(df[["team", "points"]].head())
print(df[['team','points']].head())
print('\nCleaned dataset preview: ')
print(df.head())

# check for missing values
print('\nMissing values per column:')
print(df.isnull().sum())

# summary stats(crazy highs/lows)
print('\nSummary Stats:')
print(df.describe())

import matplotlib.pyplot as plt

plt.boxplot(df['points'])
plt.title('Team Points Per Game 2024-2025')
plt.ylabel('Points')
plt.show()

# The box is the middle 50% of teams (around 111 → 116 pts).
# The line inside is the median (~114 pts).
# The whiskers stretch from the lowest (~105) to highest (~122) scoring teams.
# No dots = no extreme outliers → all teams fall in a reasonable range.

print('\nTop 5 Scoring NBA Teams:')
print(df.sort_values('points', ascending=False)[['team', 'points']].head())
print('\nBottom 5 Scoring NBA Teams:')
print(df.sort_values('points')[['team', 'points']].head())
team_colors = {
    "ATL": "#E03A3E",  # Hawks red
    "BOS": "#007A33",  # Celtics green
    "BRK": "#000000",  # Nets black
    "CHA": "#1D1160",  # Hornets purple
    "CHI": "#CE1141",  # Bulls red
    "CLE": "#860038",  # Cavs wine
    "DAL": "#00538C",  # Mavs blue
    "DEN": "#0E2240",  # Nuggets navy
    "DET": "#C8102E",  # Pistons red
    "GSW": "#1D428A",  # Warriors blue
    "HOU": "#CE1141",  # Rockets red
    "IND": "#002D62",  # Pacers navy
    "LAC": "#C8102E",  # Clippers red
    "LAL": "#552583",  # Lakers purple
    "MEM": "#5D76A9",  # Grizzlies blue
    "MIA": "#98002E",  # Heat red
    "MIL": "#00471B",  # Bucks green
    "MIN": "#0C2340",  # Wolves navy
    "NOP": "#0C2340",  # Pelicans navy
    "NYK": "#006BB6",  # Knicks blue
    "OKC": "#007AC1",  # Thunder blue
    "ORL": "#0077C0",  # Magic blue
    "PHI": "#006BB6",  # Sixers blue
    "PHX": "#1D1160",  # Suns purple
    "POR": "#E03A3E",  # Blazers red
    "SAC": "#5A2D81",  # Kings purple
    "SAS": "#C4CED4",  # Spurs silver
    "TOR": "#CE1141",  # Raptors red
    "UTA": "#002B5C",  # Jazz navy
    "WAS": "#002B5C",  # Wizards navy
}


import matplotlib.pyplot as plt

df_sorted = df.sort_values("points", ascending=False)
colors = [team_colors[t] for t in df_sorted["team"]]
plt.figure(figsize=(12, 6))
bars = plt.bar(df_sorted["team"], df_sorted["points"], color=colors)
plt.title("NBA Team Points Per Game (2024–25)")
plt.xlabel("Team")
plt.ylabel("Points per Game")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Add labels on top of bars
for b in bars:
    h = b.get_height()
    plt.text(b.get_x() + b.get_width()/2, h, f"{h:.1f}", ha="center", va="bottom", fontsize=8)

plt.show()  



conference_map = {
    "ATL": "East", "BOS": "East", "BRK": "East", "CHA": "East", "CHI": "East", 
    "CLE": "East", "DET": "East", "IND": "East", "MIA": "East", "MIL": "East",
    "NYK": "East", "ORL": "East", "PHI": "East", "TOR": "East", "WAS": "East",
    
    "DAL": "West", "DEN": "West", "GSW": "West", "HOU": "West", "LAC": "West",
    "LAL": "West", "MEM": "West", "MIN": "West", "NOP": "West", "OKC": "West",
    "PHX": "West", "POR": "West", "SAC": "West", "SAS": "West", "UTA": "West",
}

df["conference"] = df["team"].map(conference_map)
print(df[["team", "conference", "points"]].head())

# check to see if all 30 teams are there now
print(df["conference"].value_counts())


stats = ['points', 'rebounds', 'assists', 'steals', 'blocks', 'TOV']

# Use the list of column names, not the string 'stats'
conf_summary = df.groupby('conference')[stats].mean().round(1)

print("\nCONFERENCE SUMMARY (averages):")
print(conf_summary)

ax = conf_summary.T.plot(
    kind="bar",
    figsize=(8,5),
    title="East vs West: Per-Game Averages",
    ylabel="Per Game",
    rot=0
)
ax.legend(title="Conference")
plt.tight_layout()
plt.show()


print('\nLeague Average Shot Attemps:')
print(df[['2PA', '3PA']].mean().round(1))

conf_shots = df.groupby('conference')[['2PA','3PA']].mean().round(1)
print("\nConference Average Shot Attempts:")
print(conf_shots)

ax = conf_shots.plot(kind='bar', figsize=(7,5), rot=0)
plt.title("East vs West: Average 2PA vs 3PA")
plt.ylabel("Attempts per Game")
plt.tight_layout()
plt.show()



# --- 3 Point Reliance Analysis ---
# the celtics and golden state live and die by the 3, denver was the lowest out of 30 teams
# Calculate 3-point attempt rate
df["3P_rate"] = df["3PA"] / df["FGA"]

# Sort by 3-point rate
df_sorted_3p = df.sort_values("3P_rate", ascending=False)

print("\nTop 5 Teams by 3-Point Reliance:")
print(df_sorted_3p[["team", "3PA", "FGA", "3P_rate"]].head())

print("\nBottom 5 Teams by 3-Point Reliance:")
print(df_sorted_3p[["team", "3PA", "FGA", "3P_rate"]].tail())

# Plot
colors = [team_colors[t] for t in df_sorted_3p["team"]]
plt.figure(figsize=(12,6))
bars = plt.bar(df_sorted_3p["team"], df_sorted_3p["3P_rate"], color=colors)
plt.title("NBA Team 3-Point Reliance (3PA / FGA)")
plt.ylabel("Share of Shots that are 3s")
plt.xlabel("Team")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Add % labels
for b in bars:
    h = b.get_height()
    plt.text(b.get_x() + b.get_width()/2, h, f"{h:.1%}", ha="center", va="bottom", fontsize=8)

plt.tight_layout()
plt.show()



# League-average 3P rate for context
league_3p_rate = (df["3PA"].sum() / df["FGA"].sum())

# Ranked table with key payoff stats
cols = ["team","points","FGA","3PA","3P%","2P%","FTA","FT%","assists"]
rank_3p = df.assign(three_pt_rate = df["3PA"]/df["FGA"]) \
            .sort_values("three_pt_rate", ascending=False)[cols + ["three_pt_rate"]]

print("\nTop 8 by 3P reliance:")
print(rank_3p.head(8).to_string(index=False))

print("\nBottom 8 by 3P reliance:")
print(rank_3p.tail(8).to_string(index=False))

print(f"\nLeague average 3P rate: {league_3p_rate:.1%}")


# =============================
# EXTRA ANALYSIS (add here)
# =============================

# League average 3P rate
league_3p_rate = df["3PA"].sum() / df["FGA"].sum()

# Ranked table
rank_3p = df.assign(three_pt_rate = df["3PA"]/df["FGA"]) \
            .sort_values("three_pt_rate", ascending=False)

print("\nLeague average 3P rate:", f"{league_3p_rate:.1%}")
print("\nTop 8 by 3P reliance:")
print(rank_3p[["team","points","FGA","3PA","3P%","2P%","FTA","FT%","assists","three_pt_rate"]].head(8))
print("\nBottom 8 by 3P reliance:")
print(rank_3p[["team","points","FGA","3PA","3P%","2P%","FTA","FT%","assists","three_pt_rate"]].tail(8))

# Add dashed league average line to chart
plt.figure(figsize=(12,6))
bars = plt.bar(df_sorted_3p["team"], df_sorted_3p["3P_rate"], color=colors, edgecolor="black")
plt.axhline(league_3p_rate, linestyle="--", color="red", alpha=0.7)
plt.text(-0.5, league_3p_rate+0.005, f"League Avg {league_3p_rate:.1%}", fontsize=9, color="red")

plt.title("NBA Team 3-Point Reliance vs League Average", fontsize=14, fontweight="bold")
plt.ylabel("Share of Shots that are 3s")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()