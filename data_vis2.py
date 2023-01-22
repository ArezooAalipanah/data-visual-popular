import csv
import os

from simpleimage import SimpleImage

VISUALIZATION_WIDTH = 1920
VISUALIZATION_HEIGHT = 1080

MIN_LONGITUDE = -180
MAX_LONGITUDE = 180
MIN_LATITUDE = -90
MAX_LATITUDE = 90
" the main difference between data_vis and data_vis 2 is the usage of csv library."
def main():
    visualization = SimpleImage.blank(VISUALIZATION_WIDTH, VISUALIZATION_HEIGHT)
    with open("cities.csv") as file:
        reader = csv.DictReader(file)
        for line in reader:
            lat = float(line["lat"])
            lon = float(line["lng"])
            plot_one_city(visualization, lat, lon)

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