import pandas as pd

data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

print(df.loc[0])

df = pd.read_csv(r"C:\Users\Lasaki Binta O\Documents\SCHOOL\CEN434\cenclasswork.csv")
print(df)

a = df.to_numpy()
reshaped_a = a.reshape(3, 5)  # Reshape and assign it to a new variable
#if you reshape it into (2,5) you'll get an erro saying:ValueError: cannot reshape array of size 15 into shape (2,5) becauseoccurs because the total number of elements in your array, which is 15, doesn't match the number of elements needed for a shape of (2, 5), which requires 10 elements.so you either change the number if element in array or change the reshape size to accomodat 15 elements i.e(3,5)
print(reshaped_a)