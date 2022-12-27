import string

PUNCTUATION_LIST = string.punctuation


def detokenize(tokens):
    """
    Function to de-tokenize stream of tokens
    :param tokens:
    :return: detokenized text
    """
    process_tokens = lambda token_list, puncts: [" "+token if
                                                 not token.startswith("'") and token not in
                                                 puncts else token for token in token_list]
    processed_tokens = process_tokens(tokens, PUNCTUATION_LIST)
    detokenized_sentence = "".join(processed_tokens).strip()
    return detokenized_sentence


if __name__ == '__main__':
    tokens_list = ['This', 'is', 'a', 'sample', 'text', '.']
    print(detokenize(tokens_list))
