# analyze_inventory.py
import csv
import statistics
import matplotlib.pyplot as plt

# Data
quarters = ["Q1", "Q2", "Q3", "Q4"]
turnovers = [4.31, 4.19, 7.53, 9.57]

# Compute average (verify)
avg = statistics.mean(turnovers)  # should be 6.4
industry_target = 8.0

# Save CSV
with open("inventory_2024.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["quarter", "turnover"])
    for q, t in zip(quarters, turnovers):
        writer.writerow([q, t])

# Plot
plt.figure(figsize=(8,5))
plt.plot(quarters, turnovers, marker='o', linewidth=2)
plt.title("Inventory Turnover Ratio — 2024 Quarterly")
plt.xlabel("Quarter")
plt.ylabel("Inventory Turnover Ratio")
plt.ylim(0, max(turnovers)+2)

# Average line
plt.axhline(avg, linestyle='--', linewidth=1.2)
plt.text(3.95, avg+0.1, f"Average = {avg:.1f}", va='center', ha='right')

# Industry target line
plt.axhline(industry_target, linestyle=':', linewidth=1.2)
plt.text(3.95, industry_target+0.1, f"Industry Target = {industry_target}", va='center', ha='right')

# Annotate points
for i, (q, t) in enumerate(zip(quarters, turnovers)):
    plt.scatter([q], [t])
    plt.text(i, t+0.15, f"{t:.2f}", ha='center', va='bottom')

# Extra annotation for Q3 and Q4
plt.annotate("Q3 recovery", xy=(2, turnovers[2]), xytext=(2, turnovers[2]+1.0),
             arrowprops=dict(arrowstyle="->"))
plt.annotate("Q4 above target", xy=(3, turnovers[3]), xytext=(3, turnovers[3]+1.0),
             arrowprops=dict(arrowstyle="->"))

plt.tight_layout()
plt.savefig("inventory_turnover_2024.png", dpi=300)
print(f"Average turnover: {avg:.2f}")
print("Saved: inventory_2024.png and inventory_2024.csv")
