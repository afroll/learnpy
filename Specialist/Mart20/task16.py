class Film:
    title = ''
    author = ''
    year = 0
    actors = []
    rating = 0
    duration = 0
    is18 = False
    localisation = None

f1 = Film()
f1.title = 'LOTR'
f1.duration = 240

f2 = Film()
f2.title = 'HP'
f2.duration = 150

#print(f1)

films = [f1, f2]

for film in films:
    print('Title:', film.title, ', Dur:', film.duration)

