#Jason Martin, ICS 31, Project 1, 11/12/23

from project1_quotes import *
from random import *
# ------------------------------------------------------------
# Movie Quotes Analysis Section
def is_question(user_string): #Checks if the user's string ends in a question mark
    return user_string[-1] == "?"
'''
Checks if the user's string ends in a question mark
Args:
user_string: (string) input from the user

Returns: 
returns boolean
returns boolean True if the string ends in a question mark and False if it doesn't end in a question mark
'''

def get_first_quotes(list_of_quotes):
    first_quotes = []
    for i in list_of_quotes:
        first_quotes.append(i[0])
    return(first_quotes)
'''
Sequences through a list of tuples that each contain a pair of quotes and makes a list of only the first quotes in each pair
Args:
list_of_quotes: (list) a list of tuples each containing a pair of strings. the list is derived from project1_quotes.py

Returns: 
returns list
returns list of strings, the first quotes from the list of tuples
'''

def get_first_questions(list_of_quotes):
    first_questions = []
    for i in list_of_quotes:
        if is_question(i[0]):
            first_questions.append(i[0])
    return first_questions
'''
Sequences through a list of tuples that each contain a pair of quotes and makes a list of only the first quotes that end in a question mark in each pair
Args:
list_of_quotes: (list) a list of tuples each containing a pair of strings. the list is derived from project1_quotes.py

Returns: 
returns list
returns list of strings, the first quotes that end in question marks from the list of tuples
'''

def count_question_quotes(list_of_quotes):
    question_counter = 0
    first_questions = get_first_questions(list_of_quotes)
    for i in first_questions:
        question_counter += 1
    return question_counter
#71117 questions
'''
Sequences through a list of tuples that each contain a pair of quotes and returns a counter of the amount of questions that appear among the first quotes in the quote pairs
Args:
list_of_quotes: (list) a list of tuples each containing a pair of strings. the list is derived from project1_quotes.py

Returns: 
returns int
returns an int that increments each time the first quote in each pair of quotes ends in a question mark
'''

def get_average_question_length(list_of_quotes):
    avg_length_of_first_question = 0.0
    list_of_quote_lengths = []
    for quote in get_first_questions(list_of_quotes):
        list_of_quote_lengths.append(len(quote))
    for quote_length in list_of_quote_lengths:
        avg_length_of_first_question += quote_length
    avg_length_of_first_question /= len(list_of_quote_lengths)
    return avg_length_of_first_question
'''
Sequences through a list of tuples that each contain a pair of quotes and finds the average length of the first quotes in each pair of quotes that ends in a question mark
Args:
list_of_quotes: (list) a list of tuples each containing a pair of strings. the list is derived from project1_quotes.py

Returns: 
returns float
returns a float that is the average length of all the first quotes that end in question marks
'''



# ------------------------------------------------------------
# Chatbot Section
def get_responses(list_of_quotes, input_question):
    corresponding_responses = []
    for quotes in list_of_quotes:
        if is_question(input_question) and input_question == quotes[0]:
            corresponding_responses.append(quotes[1])
    return corresponding_responses
'''
Retrieves the responese or responeses, the second quote in each pair of quotes, that correspond to an inputted question
Args:
list_of_quotes: (list) a list of tuples each containing a pair of strings. the list is derived from project1_quotes.py
input_question: (string) input from the user

Returns: 
returns list
returns list of strings, the second quotes from the list of tuples that correspond to the inputted question
'''

def get_random_from_list(input_list):
    random_element = input_list[randrange(len(input_list))]
    return random_element
'''
Generates and returns a random response from an curated list
Args:
input_list: (list) a list of strings curated to be only responses to an inputted question

Returns: 
returns string
returns a string from a list of curated and inputted strings that is supposed to be a response to some inputted question
'''

def respond(list_of_quotes, input_question):
    list_of_responses = get_responses(list_of_quotes, input_question)
    if list_of_responses == []:
        return("I don't know.")
    else:
        random = get_random_from_list(list_of_responses)
        return(random)
'''
Returns a response, either a single, random, response to an inputted question, or returns the string "I don't know."
Args:
list_of_quotes: (list) a list of tuples each containing a pair of strings. the list is derived from project1_quotes.py
input_question: (string) input from the user

Returns: 
returns list or string
returns the list of responeses, the second quotes from the list of tuples that correspond to the inputted question, if they exist. If not, returns the string "I don't know."
'''

def chatbot(version):
    user_input = ""
    print("Welcome!")
    user_input = input("Ask me anything. When you're done, just type \'bye\'\n - ").lower()
    if version == 0:
        while user_input != "bye":
            if is_question(user_input):
                if user_input in get_first_quotes(get_quotes()):
                    user_input = input(f"{respond(get_quotes(), user_input)}\n - ").lower()
                else:
                    user_input = input("I don't know.\n - ").lower()
            else:
                user_input= input("I only respond to questions!\n - ").lower()
    if version == 1:
        THRESH = 0.6
        close_enough = False
        while user_input != "bye":
            if is_question(user_input):
                if user_input in get_first_quotes(get_quotes()):
                    user_input = input(f"{respond(get_quotes(), user_input)}\n - ").lower()
                else:
                    input_minus_question_mark = user_input[0:(len(user_input)-1)]
                    user_input_words = set(input_minus_question_mark.split())
                    for question in get_first_questions(get_quotes()):
                        close_enough = False
                        question_minus_question_mark = question[0:(len(user_input)-1)]
                        question_words = set(question_minus_question_mark.split())
                        similarity = len(user_input_words.intersection(question_words))
                        if len(question_words) >= len(user_input_words):
                            difference = similarity / len(question_words)
                        else:
                            difference = similarity / len(user_input_words)
                        if difference >= THRESH:
                            user_input = input(f"{respond(get_quotes(), question)}\n - ").lower()
                            close_enough = True
                            break
                        else:
                            continue
                    if close_enough == False:
                        user_input = input("I don't know.\n - ").lower()
            else:
                user_input= input("I only respond to questions!\n - ").lower()
    if version == 2:
        THRESH = 0.5
        close_enough = False
        list_of_differences = []
        list_of_hits = []
        highest_difference = 0
        index_of_highest_difference = 0
        final_question = ""
        while user_input != "bye":
            if is_question(user_input):
                if user_input in get_first_quotes(get_quotes()):
                    user_input = input(f"{respond(get_quotes(), user_input)}\n - ").lower()
                else:
                    input_minus_question_mark = user_input[0:(len(user_input)-1)]
                    user_input_words = set(input_minus_question_mark.split())
                    for question in get_first_questions(get_quotes()):
                        close_enough = False
                        question_minus_question_mark = question[0:(len(user_input)-1)]
                        question_words = set(question_minus_question_mark.split())
                        similarity = len(user_input_words.intersection(question_words))
                        difference = similarity / len(question_words)
                        list_of_differences.append(difference)
                        list_of_hits.append(question)
                        for index, differences in enumerate(list_of_differences):
                            if differences > highest_difference:
                                highest_difference = differences
                                index_of_highest_difference = index
                                final_question = list_of_differences[index_of_highest_difference]
                        if highest_difference >= THRESH:
                            user_input = input(f"{respond(get_quotes(), final_question)}\n - ").lower()
                            close_enough = True
                            break
                        else:
                            continue
                    if close_enough == False:
                        user_input = input("I don't know.\n - ").lower()
            else:
                user_input= input("I only respond to questions!\n - ").lower()
'''
Takes in input and displays output, text on the screen. Our main chatbot function. It accepts questions and outputs a random movie quotes corresponding to the question. This bot has failsafes
if the input is not a question or if it has no corresponding quote in response to the question. Version 0, 1, and 2 become increasingly more lenient in question wording
Args:
version: (int) either 0, 1, or 2, to determine which version of the chatbot is being used

Returns:
nothing. prints out prompts and quotes in response to user input
'''

if __name__ == '__main__':
    chatbot(0)


