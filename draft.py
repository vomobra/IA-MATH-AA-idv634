import random

# Probabilités cumulatives pour chaque seed d'obtenir chaque choix
probabilities = {
    1: [0.140, 0.1342, 0.1275, 0.1197, 0.4786],
    2: [0.140, 0.1342, 0.1275, 0.1197, 0.2784, 0.2002],
    3: [0.140, 0.1342, 0.1275, 0.1197, 0.1484, 0.2600, 0.0702],
    4: [0.125, 0.1223, 0.1189, 0.1146, 0.0724, 0.2574, 0.1674, 0.0219],
    5: [0.105, 0.1054, 0.1056, 0.1053, 0.0222, 0.1961, 0.2674, 0.0868, 0.0062],
    6: [0.090, 0.0920, 0.0941, 0.0962, 0.0000, 0.0862, 0.2977, 0.2055, 0.0368, 0.0015],
    7: [0.075, 0.0780, 0.0814, 0.0852, 0.0000, 0.0000, 0.1972, 0.3411, 0.1288, 0.0130, 0.0003],
    8: [0.060, 0.0634, 0.0674, 0.0722, 0.0000, 0.0000, 0.0000, 0.3447, 0.3210, 0.0675, 0.0038, 0.0001],
    9: [0.045, 0.0483, 0.0523, 0.0571, 0.0000, 0.0000, 0.0000, 0.0000, 0.5072, 0.2590, 0.0301, 0.0009, 0.0001],
    10: [0.030, 0.0327, 0.0360, 0.0401, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.6590, 0.1899, 0.0120, 0.0002, 0.0001],
    11: [0.020, 0.0220, 0.0245, 0.0276, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.7759, 0.1260, 0.0040, 0.0001],
    12: [0.015, 0.0166, 0.0186, 0.0210, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.8610, 0.0670, 0.0007],
    13: [0.010, 0.0111, 0.0125, 0.0143, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.9288, 0.0234],
    14: [0.005, 0.0056, 0.0063, 0.0072, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.9759],
}

teams = [
    "Detroit Pistons",
    "Washington Wizards",
    "San Antonio Spurs",
    "Charlotte Hornets",
    "Portland Trail Blazers",
    "Memphis Grizzlies",
    "Toronto Raptors",
    "Brooklyn Nets",
    "Utah Jazz",
    "Houston Rockets",
    "Atlanta Hawks",
    "Chicago Bulls",
    "Golden State Warriors",
    "Los Angeles Lakers",
]

def simulate_lottery(probabilities, teams):
    draft_order = []
    available_teams = teams.copy()
    
    for pick in range(1, 5):  # Pour les 4 premiers choix
        cumulative_probs = []
        for seed, probs in probabilities.items():
            if len(probs) >= pick:
                cumulative_probs.append((seed, sum(probs[:pick])))
            else:
                cumulative_probs.append((seed, 0))
                
        # Tri par probabilité décroissante, puis par seed en cas d'égalité
        cumulative_probs.sort(key=lambda x: (-x[1], x[0]))
        
        # Sélection aléatoire basée sur les probabilités cumulatives
        total_prob = sum(prob for _, prob in cumulative_probs)
        random_prob = random.uniform(0, total_prob)
        cumulative_sum = 0
        for seed, prob in cumulative_probs:
            cumulative_sum += prob
            if random_prob <= cumulative_sum:
                draft_order.append(available_teams[seed-1])
                available_teams.pop(seed-1)
                break
                
    # Ajouter les équipes restantes basées sur leur seed original
    draft_order.extend(available_teams)
    
    return draft_order

# Simuler la loterie
draft_order = simulate_lottery(probabilities, teams)

# Afficher l'ordre de draft
for i, team in enumerate(draft_order, start=1):
    print(f"{i}. {team}")
