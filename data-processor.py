import pandas as pd 

df = pd.read_csv(r'job-hunt.csv')

currently_pending_jobs = df['Status'].value_counts()
print(currently_pending_jobs)

