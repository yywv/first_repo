import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Mantamonis_bacterial_contamination_analysis.xlsx")
#print(df.info)

columns_ls = df.columns.tolist()
#print(columns_ls)

filtered_df = df[['contig ID', 'Seq Coverage']]
filtered_df = filtered_df.sort_values(by='Seq Coverage', ascending=False)
#print(filtered_df)

#filtered_df.to_excel('filtered_mantamonis.xlsx', index=False)

print(df['Preliminary Verdict:'])

#categories = df['Preliminary Verdict:'].unique()
counts = df['Preliminary Verdict:'].value_counts()
counts.plot(kind='bar')
plt.xlabel('Verdict')
plt.ylabel('Count')
plt.title('Preliminary Verdict')

plt.savefig('preliminary_classification.png')
plt.show()
