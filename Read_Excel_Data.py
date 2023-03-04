import xlrd
import pandas as pd # import xlrd(to read excel file) otherwise gives error

df = pd.read_excel('Axes_Points.xlsx')
print("Reading Data of axes from excel:")
print(df)
print("Printing average of all axes:")
print('X axis avg:',df["x"].mean())
print('Y axis avg:',df["y"].mean())
print('Z axis avg:',df["z"].mean())
