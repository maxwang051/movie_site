import media                # import necessary modules
import fresh_tomatoes

# create three instances of Movie
django = media.Movie("Django Unchained",
    "A man looks for his wife",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcSnm2FczCxSnt69XUZqqI5-sfy66SvjiV0du9mfUKRRCGqVAurt",
    "https://www.youtube.com/watch?v=eUdM9vrCbow")

interstellar = media.Movie("Interstellar",
    "A man saves the world",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

kingsman = media.Movie("Kingsman: The Secret Service",
    "A boy searches for purpose in his life",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcTn2E6bqcLehK92h215qFnUpCYFqt02Iuwg-N4gVBmixzAXvGfZ",
    "https://www.youtube.com/watch?v=kl8F-8tR8to")

# compose Movie instances into a list and pass it as an argument
# to be displayed by open_movies_page
movies = [django, interstellar, kingsman]
fresh_tomatoes.open_movies_page(movies)
