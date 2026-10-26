# IPL Data Analysis

A small Python project that explores IPL match data from `ipl.csv`. The script prints summary tables in the terminal and displays charts for matches per season and match wins by team.

## Project files

- `app.py` — loads the CSV, calculates summaries, prints tables, and displays charts.
- `ipl.csv` — match-level IPL data used by the analysis.

## Requirements

- Python 3
- pandas
- matplotlib
- tabulate

Install the required packages with:

```powershell
python -m pip install pandas matplotlib tabulate
```

## Run the analysis

Open a terminal in the project folder and run:

```powershell
python app.py
```

Keep `ipl.csv` in the same folder as `app.py`. The script prints the dataset dimensions, wins by team, matches per season, seasons with the most and fewest matches, and matches sorted by city. It then opens two charts. Close each chart window to continue or finish the program.

## Dataset columns

The CSV contains one row per match and the following columns:

| Column | Description |
| --- | --- |
| `id` | Match identifier |
| `season` | IPL season/year |
| `city` | Match city |
| `date` | Match date |
| `team1`, `team2` | Teams playing the match |
| `toss_winner` | Team that won the toss |
| `toss_decision` | Toss winner's decision |
| `result` | Match result type |
| `dl_applied` | Whether the Duckworth–Lewis method was applied |
| `winner` | Match-winning team |
| `win_by_runs`, `win_by_wickets` | Victory margin |
| `player_of_match` | Player of the match |
| `venue` | Match venue |
| `umpire1`, `umpire2`, `umpire3` | Match umpires; some values may be blank |

The code excludes missing values when counting team wins. The dataset may contain blanks in other fields as well.
