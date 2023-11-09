#Jason Martin, Project 1


import project1_quotes
import random
h = project1_quotes.get_quotes()
# ------------------------------------------------------------
# Movie Quotes Analysis Section
def is_question(user_string):
    return user_string[-1] == "?"

def get_first_quotes(list_of_quotes):
    first_quotes = []
    for i in list_of_quotes:
        first_quotes.append(i[0])
    return(first_quotes)

def get_first_questions(list_of_quotes):
    first_questions = []
    for i in list_of_quotes:
        if is_question(i[0]):
            first_questions.append(i[0])
    return first_questions

def count_question_quotes(list_of_quotes):
    question_counter = 0
    first_questions = get_first_questions(list_of_quotes)
    for i in first_questions:
        question_counter += 1
    return question_counter
#In a comment right below your function, write how many first quotes there are in the real data that are questions.

def get_average_question_length(list_of_quotes):
    avg_length_of_first_question = 0.0
    list_of_quote_lengths = []
    for quote in get_first_questions(list_of_quotes):
        list_of_quote_lengths.append(len(quote))
    for quote_length in list_of_quote_lengths:
        avg_length_of_first_question += quote_length
    avg_length_of_first_question /= len(list_of_quote_lengths)
    return avg_length_of_first_question

# ------------------------------------------------------------
# Chatbot Section
def get_responses(list_of_quotes, input_question):
    corresponding_responses = []
    for quotes in list_of_quotes:
        if is_question(input_question) and input_question == quotes[0]:
            corresponding_responses.append(quotes[1])
    return corresponding_responses

def get_random_from_list(input_list):
    random_element = input_list[random.randrange(len(input_list))]
    return random_element

def respond(list_of_quotes, input_question):
    if is_question(input_question):
        return get_random_from_list(get_responses(list_of_quotes, input_question))

def chatbot(version):
    user_input = ""
    print("Welcome!")
    if version == 0:
        user_input = input("Ask me anything. When you're done, just type \'bye\'\n - ")
        while user_input != "bye":
            if is_question(user_input):
                if user_input in get_first_quotes(project1_quotes.get_quotes()):
                    user_input = input(f"{respond(project1_quotes.get_quotes(), user_input)}\n - ")
                else:
                    user_input = input("I don't know.\n - ")
            else:
                user_input= input("I only respond to questions!\n - ")
chatbot(0)


