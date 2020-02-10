import pickle
library_database = {1:['Genre', 'Title',  'Developer', 'Publisher', 'System', 'Rating' , 'release date', 'single/multi?', 'price', 'completion status', 'purchase date', 'notes'], 2:['1','2','3','4', '5', '6', '7' ,'8', '9', '10', '11', '12']}
datafile = open("game_lib.pickle", "wb")
pickle.dump(library_database, datafile)
datafile.close()