import sys

errorMsg = '<h2 style="color: red;">{message}</h2>'
successMsg = "<h2>{message}</h2>"
paragraph = "<p>{message}</p>"


def get_threshold():
    try:
        threshold = int(sys.argv[2])
    except ValueError:
        print(errorMsg.format(message="Invalid threshold value"))
        return
    except IndexError:
        print(errorMsg.format(message="Please provide threshold value"))
        return
    return threshold


def get_list():
    received_list = (sys.argv[1]).split(",")
    try:
        new_list = [int(item) for item in received_list]
    except ValueError:
        print(errorMsg.format(message="Invalid list value"))
        return
    if len(new_list) == 0:
        print(errorMsg.format(message="Please provide list of numbers"))
        return
    return new_list


def main():
    received_list = get_list()
    threshold = get_threshold()
    print(successMsg.format(message="Received list"))
    print(paragraph.format(message=received_list))
    print(successMsg.format(message="Threshold"))
    print(paragraph.format(message=threshold))
    result_and = received_list[0]
    result_or = received_list[0]
    result_xor = received_list[0]
    for item in received_list:
        result_and = result_and & item
        result_or = result_or | item
        result_xor = result_xor ^ item
    print(successMsg.format(message="Bitwise operations"))
    print(paragraph.format(message=f"AND: {result_and}"))
    print(paragraph.format(message=f"OR: {result_or}"))
    print(paragraph.format(message=f"XOR: {result_xor}"))
    filter_result = [item for item in received_list if item > threshold]
    print(successMsg.format(message="Filtering"))
    print(paragraph.format(message=f"Numbers greater than {threshold}: {filter_result}"))


if __name__ == "__main__":
    main()
