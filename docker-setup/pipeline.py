import pandas as pd
import sys

print(sys.argv)

day = sys.argv[1]
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

print(df)
print(f"Day: {day}")
print("Pipeline executed successfully")
print(sys.argv[0])
