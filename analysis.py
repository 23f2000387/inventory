# analysis.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Quarterly inventory turnover ratio for 2024
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "InventoryTurnover": [4.31, 4.19, 7.53, 9.57]
}
df = pd.DataFrame(data)

# Stats
df['QuarterNum'] = np.arange(1, len(df) + 1)
average = df["InventoryTurnover"].mean()  # will be 6.4
industry_target = 8.0

# Print basic summary
print("Quarterly Inventory Turnover (2024):")
print(df[['Quarter', 'InventoryTurnover']].to_string(index=False))
print(f"\nCalculated average inventory turnover: {average:.1f}")
print(f"Industry target: {industry_target:.1f}")

# Plot: trend + industry target + average
plt.figure(figsize=(8,5))
plt.plot(df['QuarterNum'], df['InventoryTurnover'], marker='o', linewidth=2)
plt.xticks(df['QuarterNum'], df['Quarter'])
plt.axhline(industry_target, linestyle='--', linewidth=1.25, label=f'Industry Target = {industry_target:.1f}')
plt.axhline(average, linestyle=':', linewidth=1.25, label=f'Average = {average:.1f}')
plt.title('Inventory Turnover Ratio — 2024 Quarterly Trend')
plt.ylabel('Inventory Turnover Ratio')
plt.ylim(0, max(df['InventoryTurnover'].max(), industry_target) + 2)
for i, v in enumerate(df['InventoryTurnover']):
    plt.text(df['QuarterNum'][i], v + 0.2, f"{v:.2f}", ha='center')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Save figure
plt.savefig('inventory_turnover_2024_trend.png', dpi=300)
print("\nPlot saved to: inventory_turnover_2024_trend.png")
