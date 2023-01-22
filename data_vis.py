import os

from simpleimage import SimpleImage

VISUALIZATION_WIDTH = 1920
VISUALIZATION_HEIGHT = 1080

MIN_LONGITUDE = -180
MAX_LONGITUDE = 180
MIN_LATITUDE = -90
MAX_LATITUDE = 90

def plot_countries(visualization,filename):
    with open(filename) as file:
        next(file)

        for line in file:
            line = line.strip()
            parts = line.split(",")
            latitude, longitude = float(parts[1]), float(parts[2])
            plot_one_city(visualization, latitude, longitude)



def get_contries():
    pass

"""
    countries = get_contries()

    for country in countries:
        country_filename = "worldcities.csv"
        plot_countries(visualization, country_filename)"""


def main():
    visualization = SimpleImage.blank(VISUALIZATION_WIDTH, VISUALIZATION_HEIGHT)
    filename = "cities.csv"
    plot_countries(visualization, filename)

    visualization.show()

def plot_one_city(visualization, latitude, longitude):

    x = longitude_to_x(longitude)
    y = latitude_to_y (latitude)

    if 0 < x <visualization.width and 0 <y <visualization.height :
        plot_pixel(visualization, x , y)

def plot_pixel(visualization, x , y):
    pixel = visualization.get_pixel(x,y)
    pixel.red = 0
    pixel.green = 0

def longitude_to_x(longitude):

    return VISUALIZATION_WIDTH * (longitude - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)

def latitude_to_y (latitude):

    return VISUALIZATION_HEIGHT * (1.0 - (latitude - MIN_LATITUDE) / (MAX_LATITUDE - MIN_LATITUDE))



if __name__ == '__main__':
    main()