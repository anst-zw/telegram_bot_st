def sample_reply(input_text):

    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Hey! How is it going?"
    
    return "I don't know what you are talking about!"