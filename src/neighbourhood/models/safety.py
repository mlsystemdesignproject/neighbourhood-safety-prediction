""" safety levels function """

# need pandas data frames:
#
# - predictions [crimes + boroughs] -> together
# - all months for last year [crimes + boroughs + city] -> together
# - population last year (and now if possible) -> population_area.csv


# Как лучше как класс оформить? или просто как функцию,
# нормально, что тип DataFrame - переменная?
# или пути и имена файлов???


# safety_lavels - должны пользоваться в streamlit
# в streamlit -> своя загрузка файлов!!!
# Значит safety_lavels будет получать уже pandas дата фреймы

__all__ = [
    "safety_levels_for_one_crime_vs_city",
    "safety_levels_for_one_crime_vs_last_year",
]


def safety_levels_for_one_crime_vs_city(
    crimes=None, population=None, data_hist=None, data_pred=None
):
    # надо посмотреть как у романа чтение данных
    # predictions, last_year
    # надо прочитать и что-то сделать
    print("Here")

    # where from Roma read data?


def safety_levels_for_one_crime_vs_last_year(
    crimes=None, population=None, data_hist=None, data_pred=None
):
    print("Here2")
