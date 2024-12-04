import utils
import read_csv
import Charts

def run():
    data = read_csv.read_csv('data.csv')
    
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentaje = list(map(lambda x: x['World Population Percentage'], data))
    Charts.generate_pie(countries, percentaje)

    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        Charts.generate_pie(labels, values)


if __name__ == '__main__':
    run()

