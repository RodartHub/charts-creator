import utils
import read_csv as read
import charts

def create_bar_charts(data):

    data = read.read_csv(data)

    country = input('Type Country -> ')

    result = utils.population_by_country(data, country)

    if len(result)>0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

def create_pie_charts(data, continent):
    
    data = read.read_csv(data)
    data = list(filter(lambda item: item['Continent']== continent, data))

    countries = list(map(lambda x: x['Country/Territory'],data))
    percentages = list(map(lambda x: x['World Population Percentage'],data))
    charts.generate_pie_chart(countries, percentages)

def run():

    # create_bar_charts('main/app/data.csv')
    continent = input('Give me the continent -> ')
    create_pie_charts('main/app/data.csv', continent)

if __name__ == '__main__':
    run()
    