from crypt import methods
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_movies,get_movie,search_movie
from ..models import Review,User
from .forms import ReviewForm,UpdateProfile
from .. import db,photos
from flask_login import login_required,current_user
import markdown2

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
    reviews=Review.get_reviews(movie.index)

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

    return render_template('search.html',movies=searched_movies,title=title)
#dynamic route <>
@main.route('/movie/review/new/<int:index>',methods=['GET','POST'] ) #methods argument on our decorator tells flask to register the view function as a handler for both GET and POST requests.

#@login_required will intercept a request and check if user is authenticated. if not they are redirected to login page
@login_required
def new_review(index):
    form=ReviewForm()#instance of the ReviewForm class
    movie=get_movie(index)#get movie object using id

    if form.validate_on_submit():
        #method returns True when form is submitted and all data is validated
        title=form.title.data
        review=form.review.data

        new_review=Review(movie_id=movie.index,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)
        #create new review object and save it
        new_review.save_review()
        #redirect response to movie view function and pass in the dynamic movie id
        return redirect(url_for('.movie',index=movie.index))

    #if method returns false we render new_review.html template file & pass in title,form object,movie object
    title=f'{movie.title} review '
    return render_template('new_review.html',title=title,review_form=form,movie=movie)


@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form=UpdateProfile()
    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.file['photo'])
        path=f'photos/{filename} '
        user.profile_pic_path=path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/review/<int:index>')
def single_review(index):
    #for handling requests for a single review
    review=Review.query.get(index)
    if review is None:
        abort(404)
    format_review=markdown2.markdown(review.movie_review,extras=["code-friendly","fenced-code-bocks"])
    return render_template('review.html',review=review,format_review=format_review)