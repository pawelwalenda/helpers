import pandas as pd

df = pd .read_json("file.json")

df.to_excel('file.xlsx', index=False)
