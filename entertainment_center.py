import media
import fresh_tomatoes

# initialize movie objects: finding_nemo, school_of_rock, hermano
finding_nemo = media.Movie("Finding Nemo",
                           "https://lumiere-a.akamaihd.net/v1/images/"
                           "open-uri20150422-12561-h6g489_491206e7.jpeg",
                           "https://www.youtube.com/watch?v=SPHfeNgogVs")

school_of_rock = media.Movie("School of Rock",
                             "https://upload.wikimedia.org/wikipedia/en/"
                             "1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=yMvpJDbWX_c")

the_greatest_showman = media.Movie("The Greatest Showman",
                                   "https://goo.gl/q26gzZ"
                                   "",
                                   "https://www.youtube.com/"
                                   + "watch?v=jr9QtXwC9vc")

movies = [finding_nemo, school_of_rock, the_greatest_showman]
fresh_tomatoes.open_movies_page(movies)
