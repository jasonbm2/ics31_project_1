#Jason Martin, Project 1


from project1_quotes import *
from random import *
h = get_quotes()
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
#71117 questions

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
    random_element = input_list[randrange(len(input_list))]
    return random_element

def respond(list_of_quotes, input_question):
    if is_question(input_question):
        return get_random_from_list(get_responses(list_of_quotes, input_question))

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
        THRESH = 0.25
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

if __name__ == '__main__':
    chatbot(1)


