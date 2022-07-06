import re
import long_response as long


class Interpreter:
    def __init__(self, arr):
        self.inputs = arr

    def message_probability(self, recongnised_words, single_response=False, required_words=[]):
        message_certainty = 0
        has_required_words = True
        for word in self.inputs:
            if word in recongnised_words:
                message_certainty += 1
        percentage = float(message_certainty) / float(len(recongnised_words))
        for word in required_words:
            if word not in self.inputs:
                has_required_words = False
                break
        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_messages(self, message):
        highest_prob_list = {}

        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = self.message_probability(list_of_words, single_response,
                                                                       required_words)

        response("Hello!", ["hello", "hi", "sup", "hey"], single_response=True)
        for index, key in enumerate(long.responses):
            response(key, long.responses[key])

        best_match = max(highest_prob_list, key=highest_prob_list.get)
        # print(highest_prob_list)
        return long.unknown() if highest_prob_list[best_match] < 1 else best_match

    def get_response(self, user_input):
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        responses = self.check_all_messages(split_message)
        return responses

    def run(self):
        while True:
            print(f"Bot: {self.get_response(input('You: '))}")
