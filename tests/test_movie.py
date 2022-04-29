import unittest
from app.models import Movie #import Movie class


class MovieTest(unittest.TestCase):
    #test case to test behaiour of movie class
    def setUp(self):
        #setup method to run before every test
        self.new_movie=Movie(1234,'python must be crazy','a thrilling new python series','khsjha27hbs',8.5,129993)
        print('setup')

    def tearDown(self):
        print('teardown')

    def test_init(self):
        #check instanciation of object
        self.assertEqual(self.new_movie.index,1234)
        self.assertEqual(self.new_movie.title,'python must be crazy' )
        self.assertEqual(self.new_movie.overview,'a thrilling new python series')
        self.assertEqual(self.new_movie.poster,'khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average,8.5)
        self.assertEqual(self.new_movie.vote_count,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

