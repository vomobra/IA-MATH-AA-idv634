# Données d'entrée
east_teams = [
    {"name": "Boston Celtics", "WL": "49-14", "W/L%": 0.778},
    {"name": "Milwaukee Bucks", "WL": "42-23", "W/L%": 0.646},
    {"name": "Cleveland Cavaliers", "WL": "41-23", "W/L%": 0.641},
    {"name": "New York Knicks", "WL": "37-27", "W/L%": 0.578},
    {"name": "Orlando Magic", "WL": "37-28", "W/L%": 0.569},
    {"name": "Philadelphia 76ers", "WL": "36-28", "W/L%": 0.563},
    {"name": "Indiana Pacers", "WL": "36-29", "W/L%": 0.554},
    {"name": "Miami Heat", "WL": "35-29", "W/L%": 0.547},
    {"name": "Chicago Bulls", "WL": "31-33", "W/L%": 0.484},
    {"name": "Atlanta Hawks", "WL": "29-35", "W/L%": 0.453},
    {"name": "Brooklyn Nets", "WL": "26-39", "W/L%": 0.4},
    {"name": "Toronto Raptors", "WL": "23-41", "W/L%": 0.359},
    {"name": "Charlotte Hornets", "WL": "16-48", "W/L%": 0.25},
    {"name": "Washington Wizards", "WL": "11-53", "W/L%": 0.172},
    {"name": "Detroit Pistons", "WL": "10-53", "W/L%": 0.159}
]

west_teams = [
    {"name": "Oklahoma City Thunder", "WL": "45-19", "W/L%": 0.703},
    {"name": "Denver Nuggets", "WL": "44-20", "W/L%": 0.688},
    {"name": "Minnesota Timberwolves", "WL": "44-21", "W/L%": 0.677},
    {"name": "Los Angeles Clippers", "WL": "41-22", "W/L%": 0.651},
    {"name": "New Orleans Pelicans", "WL": "39-25", "W/L%": 0.609},
    {"name": "Phoenix Suns", "WL": "37-27", "W/L%": 0.578},
    {"name": "Sacramento Kings", "WL": "36-27", "W/L%": 0.571},
    {"name": "Dallas Mavericks", "WL": "36-28", "W/L%": 0.563},
    {"name": "Los Angeles Lakers", "WL": "36-30", "W/L%": 0.545},
    {"name": "Golden State Warriors", "WL": "33-30", "W/L%": 0.524},
    {"name": "Houston Rockets", "WL": "29-35", "W/L%": 0.453},
    {"name": "Utah Jazz", "WL": "28-36", "W/L%": 0.438},
    {"name": "Memphis Grizzlies", "WL": "22-43", "W/L%": 0.338},
    {"name": "Portland Trail Blazers", "WL": "18-45", "W/L%": 0.286},
    {"name": "San Antonio Spurs", "WL": "14-50", "W/L%": 0.219}
]

import math

for conference, teams in [("Est", east_teams), ("Ouest", west_teams)]:
    for team in teams:
        w, l = [int(x) for x in team["WL"].split("-")]
        team["Victoires Actuelles"] = w
        team["Matchs Restants"] = 82 - (w + l)
        team["Victoires Estimées"] = round(team["Matchs Restants"] * team["W/L%"])
        team["Victoires Prévues"] = team["Victoires Actuelles"] + team["Victoires Estimées"]
        team["W/L% Prévu"] = team["Victoires Prévues"] / 82
        team["Conférence"] = conference

all_teams = east_teams + west_teams
all_teams.sort(key=lambda x: x["Victoires Prévues"], reverse=True)

tableau1 = [team for team in all_teams if team["Conférence"] == "Est"]
tableau2 = [team for team in all_teams if team["Conférence"] == "Ouest"]
tableau3 = all_teams

for table, title in [(tableau1, "Conférence Est"), (tableau2, "Conférence Ouest"), (tableau3, "Toutes les équipes")]:
    print(f"--- {title} ---")
    for team in table:
        print(f"{team['name']}, Victoires Actuelles: {team['Victoires Actuelles']}, Matchs Restants: {team['Matchs Restants']}, Victoires Estimées: {team['Victoires Estimées']}, Victoires Prévues: {team['Victoires Prévues']}, W/L% Prévu: {team['W/L% Prévu']:.3f}, Position Prévue: {table.index(team) + 1}")
    print()