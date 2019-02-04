import media
import fresh_tomatoes

kushi = media.Movie(
    "Kushi",
    2001,
    "https://bit.ly/2DSUQBG",
    "https://www.youtube.com/watch?v=jF8q_Vlz714")
robo = media.Movie(
    "Robo",
    2010,
    "https://bit.ly/2E5Oobs",
    "https://www.youtube.com/watch?v=QDKY8CRe1-0")
kaththi = media.Movie(
    "Kaththi",
    2014,
    "https://bit.ly/2RqASly",
    "https://www.youtube.com/watch?v=bMf0IyzyKt4")
vivegam = media.Movie(
    "vivegam",
    2016,
    "https://bit.ly/2TqOCh5",
    "https://www.youtube.com/watch?v=2FhI6gzT_m8")
indra = media.Movie(
    "Indra",
    2002,
    "https://bit.ly/2zzoc57",
    "https://www.youtube.com/watch?v=BcJ7k31Lldw")
dhruva = media.Movie(
    "Dhruva",
    2016,
    "https://bit.ly/2AA7dzf",
    "https://www.youtube.com/watch?v=r_yVN37aCYI")
business_man = media.Movie(
    "Business Man",
    2012,
    "https://bit.ly/2rce8tV",
    "https://www.youtube.com/watch?v=bQ1wYnRJ69o")
janatha_garage= media.Movie(
    "Janatha Garage",
    2016,
    "https://bit.ly/2DRYmvY",
    "https://www.youtube.com/watch?v=7O4Hm070Bc8")
#business_man.show_trailer()
# assign individual movies to movies array
movies = [kushi,robo,kaththi,vivegam,
    indra,dhruva,business_man,janatha_garage]

# call movie trailer page method and pass movies array and sorting option
fresh_tomatoes.open_movies_page(movies,"cron")
