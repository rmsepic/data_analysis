import pandas as pd 

from numbers_parser import Document

doc = Document("jobs.numbers")
sheets = doc.sheets
tables = sheets[0].tables
data = tables[0].rows(values_only=True)
df = pd.DataFrame(data[1:], columns=data[0])

print(df)

#currently_pending_jobs = df['Status'].value_counts()
#print(currently_pending_jobs)

