"""Restaurant rating lister."""


def read_ratings():
    restaurant_dictionary = {}
    rating = open("scores.txt")
    for line in rating:
        line = line.strip()
        line = line.split(":")
        restaurant = line[0]
        scores = line[1]
        restaurant_dictionary[restaurant] = scores
    print (sorted(dict.keys(restaurant_dictionary)))




    # print (new2)

read_ratings()

