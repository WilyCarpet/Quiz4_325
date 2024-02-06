def pick_movie(number):
    moives = ['Batman', 'Barbie', 'Jurassic Park', 'Friday the 13th']

    movie_selecter = number % 3
    print('You should watch the movie', moives[movie_selecter])