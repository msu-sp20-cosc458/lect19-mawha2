import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEquals(response, "")
        
    def test_add_command(self):
        response = functions.get_chatbot_response("!! add 10 10")
        self.assertEquals(response, 20)
        
    def test_divide_comand(self):
        response = functions.get_chatbot_response("!! divide 20 5")
        self.assertEquals(response, 4)
    
    def test_hey_command(self):
        response = functions.get_chatbot_response("!! Hey maya")
        self.assertEquals(response, "What's up!")
    
    def test_say_command(self):
        response = functions.get_chatbot_response("!! say word")
        self.assertEquals(response, "word")

if __name__ == '__main__':
    unittest.main()
