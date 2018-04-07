
import pandas as pd
df = pd.read_csv('iris_test.csv', header=0)
print(df.head(5))

print(df.tail(5))

df.align=['1','3','5','7']
print(len(df))


pd.options.display.float_format = '{:,.3f}'.format # Limit output to 3 decimal places.
print(df.describe())

print(df['setosa'])
print(df.setosa)

print(df.setosa<4)
print(df[df.setosa<4])

print('qwer')
print(df.pop('setosa'))
