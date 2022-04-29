class Movie:
    #class to define movie objects
    def __init__(self,index,title,overview,poster,vote_average,vote_count):
        self.index=index
        self.title=title
        self.overview=overview
        self.poster='https://image.tmdb.org/t/p/w500/'+poster
        self.vote_average=vote_average
        self.vote_count=vote_count


class Reviews:
    all_reviews=[]

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id=movie_id
        self.title=title
        self.imageurl=imageurl
        self.review=review

    def save_review(self):
        Reviews.all_reviews.append(self)

    @classmethod
    def get_reviews(cls,index):
        response=[]

        for review in cls.all_reviews:
            if review.movie_id==index:
                response.append(review)

        return response
         

    @classmethod
    def clear_reviews(cls):
        Reviews.all_reviews.clear()
    
