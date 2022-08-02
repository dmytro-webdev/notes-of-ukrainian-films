import pandas as pd
import csv


# 1. create csv_file with named columns for the first time
def create_csv():
    with open("film_notes.csv", 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['film_name', 'note', 'rating'])
        writer.writeheader()


def read_notes(filename):
    df = pd.read_csv(filename)
    print(df)


def add_note(filename):
    new_film = input("Add new film: ")
    description = input("Tell some words about this film: ")
    mark = input("What is your rating? ")

    df = pd.read_csv(filename)
    df = df.append({'film_name': new_film, 'note': description, 'rating': mark}, ignore_index=True)
    df.to_csv(filename, index=False)
    print(df)


def remove_note_by_name(name_of_film, name_scv):
    df = pd.read_csv(name_scv)
    df.drop(df[df.film_name == name_of_film].index, inplace=True)
    df.to_csv(name_scv)
    print(df)


def films_highest_rating(filename):
    df = pd.read_csv(filename)
    df_high_rating = df[df['rating'] == df['rating'].max()]
    print(df_high_rating)


def films_lowest_rating(filename):
    df = pd.read_csv(filename)
    df_low_rating = df[df['rating'] == df['rating'].min()]
    print(df_low_rating)


def average_rating(filename):
    df = pd.read_csv(filename)
    df_average_rating = df['rating'].mean()
    print(f"Average rating among all films: {df_average_rating} of 5")

# uncomment to check functionality:

# create_csv()
# add_note('film_notes.csv')
# films_highest_rating("film_notes.csv")
# films_lowest_rating("film_notes.csv")
# remove_note_by_name("avatar", "film_notes.csv")
# average_rating("film_notes.csv")









