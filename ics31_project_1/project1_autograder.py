from project1 import *
from random import *

"""
ICS31 
Project #1
Autograder
"""

THRESH = 0.6
seed(8)

"""
############################################################
                    HELPER FUNCTIONS
############################################################
"""


def test_is_question():
    assert is_question("do you want some pie?") == True
    assert is_question("of, course!") == False

def test_get_first_quotes():
    simple_quotes = get_practice_quotes()
    assert get_first_quotes(simple_quotes) == ['quote1', 'first', 'first they said this', 'what?', 'what?']
    movie_quotes = get_quotes()
    movie_quotes = movie_quotes[0:5]
    result = get_first_quotes(movie_quotes)
    assert result == ["they do to!", 'she okay?', "wow", 'no', 'i\'m kidding.  you know how sometimes you just become this "persona"?  and you don\'t know how to quit?']

def test_get_first_questions():
    simple_quotes = get_practice_quotes()
    assert get_first_questions(simple_quotes) == ['what?', 'what?']
    movie_quotes = get_quotes()
    movie_quotes = movie_quotes[0:5]
    result = get_first_questions(movie_quotes)
    assert result == ['she okay?', 'i\'m kidding.  you know how sometimes you just become this "persona"?  and you don\'t know how to quit?']

def test_count_question_quotes():
    simple_quotes = get_practice_quotes()
    # Expected count: 2
    assert count_question_quotes(simple_quotes) == 2
    movie_quotes = get_quotes()
    movie_quotes = movie_quotes[0:5]
    result = get_first_questions(movie_quotes)
    assert count_question_quotes(movie_quotes) == 2

def test_get_average_question_length():
    simple_quotes = get_practice_quotes()
    # Expected average length: 5.0
    # print("length: ",get_average_question_length(simple_quotes) )
    assert get_average_question_length(simple_quotes) == 5.0
    movie_quotes = get_quotes()
    movie_quotes = movie_quotes[0:5]
    avg = get_average_question_length(movie_quotes)
    assert avg == 55.0

def test_get_responses():
    simple_quotes = get_practice_quotes()
    responses = get_responses(simple_quotes, "what?") 
    assert responses == ["that's what", "now you've it!"]

def test_get_random_from_list():
    assert get_random_from_list([1, 2, 3, 4, 5]) in [1, 2, 3, 4, 5]

def test_respond():
    simple_quotes = get_practice_quotes()
    assert respond(simple_quotes, "what?") in ["that's what", "now you've it!"]
    assert respond(simple_quotes, "what is your name?") == "I don't know."
    assert respond(simple_quotes, "banana") == "I don't know."

def test_chatbot(version):
    print("Testing Chatbot Version", version)
    chatbot(version)



def main():
    test_is_question()
    print("Passed test_is_question")
    test_get_first_quotes()
    print("Passed test_get_first_quotes")
    test_get_first_questions()
    print("Passed test_get_first_questions")
    test_count_question_quotes()
    print("Passed test_count_question_quotes")
    test_get_average_question_length()
    print("Passed test_get_average_question_length")
    test_get_responses()
    print("Passed test_get_responses")
    test_get_random_from_list()
    print("Passed test_get_random_from_list")
    test_respond()
    print("Passed test_respond")    
    test_chatbot(2)
    # test_chatbot(1)
    # test_chatbot(2)

if __name__ == "__main__":
    main()
