import media
import fresh_tomatoes

#initialize movie objects: finding_nemo, school_of_rock, hermano
finding_nemo = media.Movie("Finding Nemo",
                        "https://lumiere-a.akamaihd.net/v1/images/"
                        "open-uri20150422-12561-h6g489_491206e7.jpeg",
                        "https://www.youtube.com/watch?v=SPHfeNgogVs")

school_of_rock = media.Movie("School of Rock",
                        "https://upload.wikimedia.org/wikipedia/en/"
                        "1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=yMvpJDbWX_c")

hermano = media.Movie("Hermano",
                    "https://upload.wikimedia.org/"
                    "wikipedia/en/4/4e/Hermano.jpg",
                    "https://www.youtube.com/watch?v=5vrrRJDN64U")

movies = [finding_nemo, school_of_rock, hermano]
fresh_tomatoes.open_movies_page(movies)
