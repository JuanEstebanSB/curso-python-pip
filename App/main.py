import utils
import read_csv
import Charts
import pandas as pd

def run():
    '''
    
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentaje = list(map(lambda x: x['World Population Percentage'], data))
    '''
    
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa']
    
    countries = df['Country/Territory'].values
    percentaje = df['World Population Percentage'].values
    Charts.generate_pie(countries, percentaje)
    
    data = read_csv.read_csv('data.csv')
    country = input('Type Country => ')
    print(country)
    
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        Charts.generate_pie(labels, values)


if __name__ == '__main__':
    run()

