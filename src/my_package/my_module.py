def reverse(message: str) -> str:
    message_length = len(message)
    my_new_string = "-"* message_length + message[::-1] + "-"* message_length
    return my_new_string