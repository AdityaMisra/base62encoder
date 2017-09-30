import string
base_string = string.digits + string.ascii_uppercase + string.ascii_lowercase


def customized_encoder(real_number, base=None):
    partial_decoded_number = []
    number = real_number

    # by default base62 will be used
    if not base:
        base = 62

    while number >= base:
        temp_number = number/base
        temp_remainder = number%base
        number = temp_number
        partial_decoded_number.insert(0, temp_remainder)

    partial_decoded_number.insert(0, number)

    print "Original Number - {}".format(real_number)
    print partial_decoded_number

    base62_encoded_list = map(lambda each_decoded_number: base_string[each_decoded_number], partial_decoded_number)
    base62_encoded_number = ''.join(base62_encoded_list)

    print "base62 encoded value - {}".format(base62_encoded_number)

    # base_string_as_list = list(base_string)

    # import random
    # random.shuffle(base_string_as_list)

def customized_decoder(encoded_string, base=62):
    original_number = 0
    index_list = []
    for i in encoded_string:
        index_list.append(base_string.index(i))

    index_list.reverse()
    for idx, each_index_value in enumerate(index_list):
        original_number += each_index_value * pow(base, idx)

    print "Encoded String-{}\nOriginal Number-{}".format(encoded_string, original_number)
