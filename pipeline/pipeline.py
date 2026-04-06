import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python pipeline.py <day>")
    sys.exit(1)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

output_file = f"output_day_{day}.parquet"
df.to_parquet(output_file)
print(f"Saved to {output_file}")
