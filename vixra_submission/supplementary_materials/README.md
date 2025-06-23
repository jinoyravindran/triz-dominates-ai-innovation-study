# AI-Powered Innovation Technique Evaluation - Reproducibility Materials

This folder contains all materials needed to verify the statistical claims and reproduce the key findings from our ai.viXra.org paper on AI-powered innovation techniques.

## 📁 Essential Files (5 total)

### 1. **`raw_results_dataset.csv`** - Complete Results Dataset (273KB)
   - All 948 technique evaluations from 50 business idea tests
   - Each row contains scores, rankings, and metadata for one technique application
   - This is the primary data file that powers all statistical analysis

### 2. **`minimal_statistical_verification.py`** - Quick Verification Script (2.3KB)
   - **Most important for reviewers** - verifies key paper claims in 30 seconds
   - Minimal dependencies: `pip install pandas scipy`
   - Confirms: Friedman test results, win rates, effect sizes

### 3. **`business_idea_prompts.txt`** - Test Prompts (3.0KB)
   - All 50 business idea prompts used in the study
   - Shows diversity of tested concepts across industries
   - Enables understanding of what was actually evaluated

### 4. **`scoring_rubric.md`** - Scoring Methodology (6.6KB)
   - Detailed explanation of how each technique was scored
   - Documents the 11 evaluation criteria and weighting
   - Critical for understanding result validity

### 5. **`README.md`** - This File (usage instructions)

## 🚀 Quick Start for Reviewers

### **30-Second Verification** (Recommended)
```bash
# Clone the GitHub repository with all materials
git clone https://github.com/jinoyravindran/triz-dominates-ai-innovation-study.git
cd triz-dominates-ai-innovation-study

# Install minimal dependencies and verify
pip install pandas scipy
python minimal_statistical_verification.py
```

**Expected Output:**
```
=== KEY STATISTICAL RESULTS ===
Friedman Chi-square: 145.5
P-value: 5.65e-22
Kendall's W: 0.162

=== CLAIM VERIFICATION ===
TRIZ wins: Expected 30, Actual 30 ✓
Biomimicry wins: Expected 13, Actual 13 ✓
Friedman p < 0.001: ✓
Effect size: medium (W = 0.162)
```

### **Data Exploration** (Optional)
```bash
# View the dataset structure
head -5 raw_results_dataset.csv

# Check dataset size
wc -l raw_results_dataset.csv  # Should show 949 lines (948 + header)

# View test prompts
head -10 business_idea_prompts.txt
```

## 🎯 What Reviewers Can Verify

### **Statistical Claims:**
- **Friedman Test**: χ² = 145.5, p < 0.001 (highly significant)
- **Effect Size**: Kendall's W = 0.162 (medium effect)
- **Win Rates**: TRIZ 60%, Biomimicry 26%, Others 14%

### **Data Integrity:**
- **Total Evaluations**: 948 complete technique applications
- **Test Coverage**: 50 diverse business concepts
- **Technique Coverage**: 19 different innovation methods
- **Missing Data**: Only 2 incomplete tests (99.8% completion rate)

### **Key Findings:**
- **TRIZ Innovation dominance**: 30/50 wins (60% win rate)
- **Systematic vs Creative**: Top techniques are knowledge-based
- **Statistical Significance**: Results not due to chance (p < 0.001)

## 📊 Dataset Structure

The `raw_results_dataset.csv` contains these key columns:
- **test_id**: Unique identifier for each business idea test
- **technique**: Which innovation technique was applied
- **final_score**: Overall score (0-100) for the enhanced idea
- **is_winner**: Boolean indicating if this was the best technique for this test
- **rank**: Ranking within the test (1 = best, 19 = worst)

## 🔬 Methodology Transparency

- **Scoring**: Multi-criteria evaluation (innovation, feasibility, market potential, etc.)
- **Bias Prevention**: Identical prompts, randomized order, automated scoring
- **Statistical Rigor**: Friedman test for non-parametric ranked data
- **Effect Sizes**: Cohen's d calculations for practical significance

## 📋 File Sizes & Dependencies

| File | Size | Dependencies | Purpose |
|------|------|-------------|---------|
| `raw_results_dataset.csv` | 273KB | None | Primary data |
| `minimal_statistical_verification.py` | 2.3KB | pandas, scipy | Quick verification |
| `business_idea_prompts.txt` | 3.0KB | None | Test inputs |
| `scoring_rubric.md` | 6.6KB | None | Methodology |
| `README.md` | This file | None | Instructions |

## ✅ Streamlined for Reviewers

We've simplified these materials to focus on what reviewers actually need:
- **Quick verification** of statistical claims
- **Understanding** of what was tested and how
- **Access** to complete raw data for deeper analysis
- **No unnecessary** implementation details or data processing scripts

The verification script runs in under 30 seconds and confirms all major paper claims with minimal setup required. 