import fresh_tomatoes
import media

# createing instances of Movie class and setting values for parameters
toy_story =media.Movie("Toy Story","A story of kid with toys coming alive","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=ZZv1vki4ou4")

padmavati=media.Movie("Padmavati","Historical Indian movie starring Deepika Padukone and Ranveer Singh","https://upload.wikimedia.org/wikipedia/en/4/47/Padmavati_Poster.jpg","https://www.youtube.com/watch?v=X_5_BLt76c0")

bajirao_mastani=media.Movie("Bajirao Mastani","Historical Love story Movie based on Peshve Bajirao by Sanjay leela Bhansali","https://upload.wikimedia.org/wikipedia/en/5/52/Bajirao_Mastani_Poster_2.jpg","https://www.youtube.com/watch?v=eHOc-4D7MjY")

simran=media.Movie("Simran","Story of an Indian immigrant in USA played by National award winner Kangana Ranaut","https://upload.wikimedia.org/wikipedia/en/d/d3/Simran_Poster.jpg","https://www.youtube.com/watch?v=_LUe4r6eeQA")

queen= media.Movie("Queen","Rani, an under-confident Punjabi girl from New Delhi embarks on her honeymoon to Paris and Amsterdam by herself after her fiance calls off their wedding","https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg","https://www.youtube.com/watch?v=KGC6vl3lzf0")

highway=media.Movie("Highway","Its tells the story of a girl (Alia Bhatt) who develops Stockholm syndrome after being kidnapped","https://upload.wikimedia.org/wikipedia/en/c/c5/Highway_OST.jpg","https://www.youtube.com/watch?v=LijcpDrSNVI")

# Listing all the movies together in movies 
movies=[toy_story,padmavati,bajirao_mastani,simran,queen,highway]

# creating webpage with array of 6 movies 
fresh_tomatoes.open_movies_page(movies)