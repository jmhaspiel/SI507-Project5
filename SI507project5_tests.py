import unittest
from SI507project5_code import *


class TestTumlbr(unittest.TestCase):

    def setUp(self):
    	self.tumblr_test = get_data_from_api(tumblr_url,"Tumblr",tumblr_params)
    	self.photofile = open("tumblr_answers.csv")
    	self.answerfile = open("tumblr_answers.csv")


# Card Tests
    def test_tumblr(self):
        self.assertTrue(type(self.tumblr_test) == dict)

    def test_tumblr_keys(self):
        self.assertTrue(len(self.tumblr_test['response']['posts']) == 20)

    def test_csv_files(self):
        self.assertTrue(self.photofile.read())
        self.assertTrue(self.answerfile.read())

    def test_posts(self):
        self.assertEqual(type(self.tumblr_test['response']['posts'][0]), dict)

    def test_result_note_type(self):
        self.assertEqual(type(self.tumblr_test['response']['posts'][0]['note_count']), int)    	

    def tearDown(self):
    	self.photofile.close()
    	self.answerfile.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
