from app import app
import unittest

class AppTestCase(unittest.TestCase):

	#Ensure that flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/index', content_type='html/text')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()