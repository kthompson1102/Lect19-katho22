import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEqual(response, "")
        
    def test_add_command(self):
        response = functions.get_chatbot_response('!! add 2 + 5')
        self.assertEqual(response, 7)
    def test_divive_command(self):
        response = functions.get_chatbot_response('!! divide 12 / 3')
        self.assertEqual(response, 4)
    def test_say_command(self):
        response = functions.get_chatbot_response('!! say I can\'t wait for summer')
        self.assertEqual(response, 'I can\'t wait for summer')
    def test_hey_command(self):
        response = functions.get_chatbot_response('!! Hey Chatbot!')
        self.assertEqual(response, 'What\'s up!')
    def test_wrong_command(self):
        response = functions.get_chatbot_response('!! goodbye chatbot!')
        self.assertEqual(response, 'Oops! I didn\'t recognize your command :(')



if __name__ == '__main__':
    unittest.main()
