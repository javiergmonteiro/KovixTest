def format_string(string, repeat):
    try:
        formatted_string = string[0]
    except IndexError:
        return ""
    count = 1
    for char in string:
        if char == formatted_string[-1]:
            if count < repeat:
                formatted_string += char
                count += 1
        else:
            formatted_string += char
            count = 1
    return formatted_string
