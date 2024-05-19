import pandas as p 
from sklearn.impute import SimpleImputer

#loading the data set
df = p.read_csv("country_vaccination_stats.csv")

#Imputing the missing values using median 
imputer = SimpleImputer(strategy = 'median')
df['daily_vaccinations'] = imputer.fit_transform(df[['daily_vaccinations']])

#calculate median daily vaccinations for each country 
median_vaccinations = df.groupby('country')['daily_vaccinations'].median().reset_index()

#sorting the countries by median daily vaccinations and getting top 3 
top_3_countries = median_vaccinations.sort_values(by='daily_vaccinations', ascending=False).head(3)

#printing results
print(top_3_countries)
