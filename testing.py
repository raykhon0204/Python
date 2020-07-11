import unittest
from name_function import get_name
from city_function import city_country
from survey import AnonymousSurvey

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):                
        formatted_name = get_name('wolfgang', 'mozart', 'amadeus')        
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
    
    def test_city_country(self):
        fullCity_name = city_country('Paris', 'France')
        self.assertEqual(fullCity_name, 'Paris, France')

    def test_store_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)
    
    def test_store_3response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Uzbek', 'Tajik']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)        
unittest.main()