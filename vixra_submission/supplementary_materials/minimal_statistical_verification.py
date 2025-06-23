#!/usr/bin/env python3
"""
MINIMAL STATISTICAL VERIFICATION
Verifies key statistical claims from the ai.viXra.org paper

Requirements: pip install pandas scipy
"""

import pandas as pd
from scipy import stats

def verify_key_statistics():
    """Verify the main statistical claims from the paper"""
    
    # Load data
    data = pd.read_csv('raw_results_dataset.csv')
    print(f"Dataset loaded: {len(data)} evaluations")
    
    # Prepare score matrix
    score_matrix = data.pivot(index='test_id', columns='technique', values='final_score')
    print(f"Score matrix: {score_matrix.shape[0]} tests × {score_matrix.shape[1]} techniques")
    
    # Remove any rows with missing values
    score_matrix_clean = score_matrix.dropna()
    print(f"Clean matrix: {score_matrix_clean.shape[0]} complete tests")
    
    # Friedman test
    statistic, p_value = stats.friedmanchisquare(*score_matrix_clean.values.T)
    kendall_w = statistic / (score_matrix.shape[0] * (score_matrix.shape[1] - 1))
    
    print(f"\n=== KEY STATISTICAL RESULTS ===")
    print(f"Friedman Chi-square: {statistic:.1f}")
    print(f"P-value: {p_value:.2e}")
    print(f"Kendall's W: {kendall_w:.3f}")
    
    # Win rate verification
    win_counts = data[data['is_winner']]['technique'].value_counts()
    print(f"\n=== WIN RATE VERIFICATION ===")
    print(f"TRIZ Innovation: {win_counts.get('TRIZ Innovation', 0)} wins")
    print(f"Biomimicry: {win_counts.get('Biomimicry', 0)} wins")
    print(f"Total tests: {len(score_matrix)}")
    
    # Verify paper claims
    expected_triz_wins = 30
    expected_bio_wins = 13
    actual_triz_wins = win_counts.get('TRIZ Innovation', 0)
    actual_bio_wins = win_counts.get('Biomimicry', 0)
    
    print(f"\n=== CLAIM VERIFICATION ===")
    print(f"TRIZ wins: Expected {expected_triz_wins}, Actual {actual_triz_wins} ✓" if actual_triz_wins == expected_triz_wins else "✗")
    print(f"Biomimicry wins: Expected {expected_bio_wins}, Actual {actual_bio_wins} ✓" if actual_bio_wins == expected_bio_wins else "✗")
    print(f"Friedman p < 0.001: {'✓' if p_value < 0.001 else '✗'}")
    effect_size = "large" if kendall_w > 0.3 else "medium" if kendall_w > 0.1 else "small"
    print(f"Effect size: {effect_size} (W = {kendall_w:.3f})")
    
    # Calculate Cohen's d values
    import numpy as np
    def cohen_d(group1, group2):
        n1, n2 = len(group1), len(group2)
        pooled_std = np.sqrt(((n1 - 1) * group1.var() + (n2 - 1) * group2.var()) / (n1 + n2 - 2))
        return (group1.mean() - group2.mean()) / pooled_std

    triz_scores = data[data['technique'] == 'TRIZ Innovation']['final_score']
    other_scores = data[data['technique'] != 'TRIZ Innovation']['final_score']
    bio_scores = data[data['technique'] == 'Biomimicry']['final_score']
    top2_techniques = ['TRIZ Innovation', 'Biomimicry']
    top2_scores = data[data['technique'].isin(top2_techniques)]['final_score']
    bottom17_scores = data[~data['technique'].isin(top2_techniques)]['final_score']

    print(f"\n=== EFFECT SIZES (COHEN'S D) ===")
    print(f"TRIZ vs Others: {cohen_d(triz_scores, other_scores):.2f}")
    print(f"Biomimicry vs Others: {cohen_d(bio_scores, other_scores):.2f}")
    print(f"Top 2 vs Bottom 17: {cohen_d(top2_scores, bottom17_scores):.2f}")

if __name__ == "__main__":
    verify_key_statistics() 