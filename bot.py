import re

import long_response as long


def message_probability(user_message, recongnised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    for word in user_message:
        if word in recongnised_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recongnised_words))
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list: dict = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response("Hello!", ["hello", "hi", "sup", "hey"], single_response=True)

    for _, key in enumerate(long.responses):
        response(key, long.responses[key], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    # split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    strip_message = list()
    strip_message.append(user_input.strip())
    responses = check_all_messages(strip_message)
    # print(strip_message)
    return responses


# def run():
#     while True:
#         print(f"Bot: {get_response(input('You: '))}")
#
#
# if __name__ == '__main__':
#     run()
