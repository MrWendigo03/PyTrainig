import re
import long_response


def mes_probability(user_message, recognised_words, single_response=False, required_word=[]):
    mess_certanity = 0
    has_required_word = True

    # Посчитать слова в сообщении
    for word in user_message:
        if word in recognised_words:
            mess_certanity += 1

    # Посчитать проценит узнаваемых слов
    percentage = float(mess_certanity) / float(len(recognised_words))

    for word in recognised_words:
        if word not in user_message:
            has_required_word = False
            break

    if has_required_word or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_message(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_probList
        highest_prob_list[bot_response]= mes_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'greetings', 'Good '], single_response=True)
    response("I'm fine, thank you!", ['how', 'you', 'do', 'are', 'doing'], required_words=['how'])
    response('Thanks!', ['i', 'like', 'code', 'palace'], required_words=['code', 'palace'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long_response.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_responses(user_input):
    split_message = re.split(r'\s+|[],;?!.-]|s*', user_input.lower())
    response = check_message(split_message)
    return response

while True:
    print('Bot: ' + get_responses(input('You:')))
