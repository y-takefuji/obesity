import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Filter data for 'LocationAbbr' == 'US'
df = df[df['LocationAbbr'] == 'US']

# Group data by 'Question' and 'YearStart'
grouped = df.groupby(['Question', 'YearStart'])

# Calculate mean 'Data_Value' and sum 'Sample_Size' for each group
df = grouped.agg({'Data_Value':'mean', 'Sample_Size':'sum'}).reset_index()

# Get unique questions
questions = df['Question'].unique()

plt.figure(figsize=(10, 6))

# Plot a line for each unique question
for i, question in enumerate(questions):
    data = df[df['Question'] == question]
    # If the question includes 'obesity', use a thick solid line
    if 'obesity' in question.lower():
        plt.plot(data['YearStart'], data['Data_Value'], color='black', linewidth=3)
    else:
        plt.plot(data['YearStart'], data['Data_Value'], color='black')
    # Add unique number at the end of each line
    plt.text(data['YearStart'].values[-1], data['Data_Value'].values[-1], str(i+1), va='center')
    # Add the number of participants at the start of each line
    plt.text(data['YearStart'].values[0], data['Data_Value'].values[0], str(int(data['Sample_Size'].sum())), va='top')

plt.xlabel('Year')
plt.ylabel('Percent of adults')
plt.title('Percent of adults for each question over years')

# Save the figure
plt.savefig('result.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

# Print unique questions with their numbers
for i, question in enumerate(questions):
    print(f'{i+1}: {question}')

# Print total number of participants
print(f'Total number of participants: {int(df["Sample_Size"].sum())}')

