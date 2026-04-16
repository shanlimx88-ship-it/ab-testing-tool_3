cat > README.md << 'EOF'
# Skill 3.3: Heterogeneous Treatment Effect Analysis

## Overview
Analyze whether treatment effects vary across different user segments. Identify which groups benefit most and which may be negatively impacted.

## Features
- **Segment Effect Calculation**: Compute lift, p-value, and 95% CI for each segment
- **Forest Plot**: Visualize treatment effects across segments with confidence intervals
- **High-Effect Segments**: Identify groups with significant positive lift
- **Negative Effect Alert**: Flag segments with negative lift for monitoring
- **Heatmap**: Matrix visualization of effects across segments
- **Summary Dashboard**: Combined view of all key insights
- **HTML Report**: Self-contained report with all charts and tables

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate sample data
python run_analysis.py --generate-sample

# Run analysis
python run_analysis.py
