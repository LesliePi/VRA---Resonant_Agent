import numpy as np

def resonance_score(input_v, target_v):
delta_phi = target_v["phase"] - input_v["phase"]
delta_freq = abs(target_v["frequency"] - input_v["frequency"])
delta_amp = abs(target_v["amplitude"] - input_v["amplitude"])
score = np.cos(delta_phi) * np.exp(-delta_freq) * (1 - delta_amp)
return score

def find_most_resonant(input_vector, dataset):
best = None
best_score = -np.inf
for item in dataset:
score = resonance_score(input_vector, item)
if score > best_score:
best = item
best_score = score
return { "match": best, "resonance_score": best_score }

