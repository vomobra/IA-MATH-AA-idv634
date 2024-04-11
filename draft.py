import random

# Probabilités cumulatives pour chaque seed d'obtenir chaque choix
probabilities = {
    1: [0.140, 0.1342, 0.1275, 0.1197, 0.4786],
    2: [0.140, 0.1342, 0.1275, 0.1197, 0.2784, 0.2002],
    3: [0.140, 0.1342, 0.1275, 0.1197, 0.1484, 0.2600, 0.0702],
    # Complétez avec les probabilités des autres seeds selon le tableau
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