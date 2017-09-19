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

    import string
    base_string = string.digits + string.ascii_uppercase + string.ascii_lowercase

    base62_encoded_list = l
    base62_encoded_number = ''.join(base62_encoded_list)

    print "base62 encoded value - {}".format(base62_encoded_number)

    # base_string_as_list = list(base_string)

    # import random
    # random.shuffle(base_string_as_list)
