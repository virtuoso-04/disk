import pandas as pd
import matplotlib.pyplot as plt

# Read the log file
data = pd.read_csv("disk_usage.csv")

# Convert "Datetime" column to datetime objects
data['Datetime'] = pd.to_datetime(data['Datetime'])

# Plot disk usage trends
plt.figure(figsize=(10, 6))
plt.plot(data['Datetime'], data['Usage'], label="Disk Usage (%)", color='blue')

# Add titles and labels
plt.title("Disk Usage Trends Over Time")
plt.xlabel("Time")
plt.ylabel("Disk Usage (%)")
plt.axhline(y=80, color='red', linestyle='--', label="Warning Threshold (80%)")
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
