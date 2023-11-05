import pandas as pd

df = pd.read_csv('q1text.csv')

df = df.sort_values(['Rating', 'Duration'], ascending=[False, True])

df = df.head(100)

print("The Top 100 Sorted Movies are: ")
for index, row in df.iterrows():
    print(row['Title'])

print("Filter Options:")
print("1. Duration")
print("2. Imdb Rating")
print("3. Year of Release")
print("4. Genre")

choice = float(input("Enter the choice: "))
if choice < 4:
    min, max = input("Enter the range:\n").split()
elif choice == 4:
    gen = input("Enter the genre:\n")
else:
    print("Invalid choice")
    exit()

dataFrame = pd.read_csv('q1text.csv')

if choice == 1:
    dataFrame['Duration'] = dataFrame['Duration'].str.split().str[0].astype(float)
    dataFrame = dataFrame[(dataFrame['Duration'] >= float(min)) & (dataFrame['Duration'] <= float(max))]
    for index, row in dataFrame.iterrows():
        print(row['Title'])
elif choice == 2:
    dataFrame = dataFrame[(dataFrame['Rating'] >= float(min)) & (dataFrame['Rating'] <= float(max))]
    print("Movies with Rating between", min, "and", max)
    for index, row in dataFrame.iterrows():
        print(row['Title'])
elif choice == 3:
    dataFrame = dataFrame[(dataFrame['Year'] >= float(min)) & (dataFrame['Year'] <= float(max))]
    print("Movies with Release Year between", min, "and", max)
    for index, row in dataFrame.iterrows():
        print(row['Title'])
elif choice == 4:
    dataFrame = dataFrame[dataFrame['Genre'].str.contains(gen)]
    print("Movies with Genre", gen)
    for index, row in dataFrame.iterrows():
        print(row['Title'])
else:
    print("Invalid choice")
