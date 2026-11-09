"""
RECORD CHECK  -  my version
===========================

Name  :Ntihemuka Migambi Darren
Lane  :  AI 
Date  :28/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

df = pd.read_csv(
    "C:/Users/PC/OneDrive/Python MDX/Week 06 - Pandas/LAB/my_files.csv")

df['percent'] = (df['value'] / df['limit']) * 100
df['status'] = df['percent'].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK")
df.add(df[['percent', 'status']])
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.
df.groupby("status")
print(df[df['status'] != "OK"])
print(df['status'].value_counts())
df.to_csv("to_files.csv")
