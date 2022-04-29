
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_movies,get_movie,search_movie
from ..models import Reviews
from .forms import ReviewForm

#views
@main.route('/')#route decorator
def index():
    #view root page function. returns movie  page and its data
    
    #get popular movie
    popular_movies=get_movies('popular')
    upcoming_movie=get_movies('upcoming')
    now_showing_movie=get_movies('now_playing')
    print(popular_movies)#pass the result from get_movies() function call to our template

    #dynamically add title to index page
    title='Home - Welcome to the best movie review website online'

    #search section
    search_movie=request.args.get('movie_query')
    #when we submit the form inside our index.html it creates a query with the name of the input movie_query and the value as the input value

    if search_movie:#check if value exists
        return redirect(url_for('.search',movie_name=search_movie))
    else:
        return render_template('index.html',title=title,popular=popular_movies, upcoming=upcoming_movie,now_showing=now_showing_movie)

    

@main.route('/movie/<int:index>')
def movie(index):
    #view movie page that returns movie details page and its data
    movie=get_movie(index)
    title=f'{movie.title}'
    reviews=Reviews.get_reviews(movie.index)

    return render_template('movie.html',title=title,movie=movie,reviews=reviews)

@main.route('/search/<movie_name>')#passes in a dynamic variable
def search(movie_name):
    #view function to display search results
    movie_name_list=movie_name.split(' ')
    movie_name_format='+'.join(movie_name_list)
    #format the movie_name to add + sign between the multiple words
    searched_movies=search_movie(movie_name_format)
    # call the search_movie() and pass in the formated movie name then pass the searched_movies list
    title=f'search results for {movie_name} '

    return render_template('search.html',movies=searched_movies)
#dynamic route <>
@main.route('/movie/review/new/<int:index>',methods=['GET','POST'] ) #methods argument on our decorator tells flask to register the view function as a handler for both GET and POST requests. 
def new_review(index):
    form=ReviewForm()#instance of the ReviewForm class
    movie=get_movie(index)#get movie object using id

    if form.validate_on_submit():
        #method returns True when form is submitted and all data is validated
        title=form.title.data
        review=form.review.data
        new_review=Reviews(movie.index,title,movie.poster,review)
        #create new review object and save it
        new_review.save_review()
        #redirect response to movie view function and pass in the dynamic movie id
        return redirect(url_for('.movie',index=movie.index))

    #if method returns false we render new_review.html template file & pass in title,form object,movie object
    title=f'{movie.title} review '
    return render_template('new_review.html',title=title,review_form=form,movie=movie)