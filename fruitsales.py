import pandas as pd
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                           index=['2017 Sales', '2018 Sales'])
df = pd.DataFrame(fruit_sales)
df.to_csv('fruit.csv')