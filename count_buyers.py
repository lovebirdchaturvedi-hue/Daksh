import pandas as pd

buyers = pd.read_excel(r"C:\Users\DELL\Downloads\Daksh\REAL BUYERS 2026.xlsx")
print(f"Restored Buyers Count: {len(buyers)}")

exporters = pd.read_excel(r"C:\Users\DELL\Downloads\Daksh\Exporters 2026.xlsx")
print(f"Restored Exporters Count: {len(exporters)}")
