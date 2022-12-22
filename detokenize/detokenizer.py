import string

PUNCT_LIST = string.punctuation

def detokenize(tokens):
    """
    Function to de-tokenize stream of tokens
    :param tokens:
    :return: detokenized text
    """
    process_tokens = lambda token_list, PUNCT: [" "+token if not token.startswith("'") and token not in PUNCT else token
                                               for token in token_list]
    processed_tokens = process_tokens(tokens, PUNCT_LIST)
    detokenized_sentense = "".join(processed_tokens)
    return detokenized_sentense


if __name__ == '__main__':
    tokens = ['This', 'is', 'a', 'sample', 'text', '.']
    print(detokenize(tokens))