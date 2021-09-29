from datetime import datetime

def sample_reply(input_text):

    user_message = str(input_text).lower()

    if user_message in ("hello", "hello!", "hi", "hi!", "hey", "hey!"):
        return "Hey! How is it going?"
    
    if user_message in (
        "time",
        "time?",
        "date",
        "date?",
        "what time is it",
        "what time is it?"
        ):
        now = datetime.now()
        now_formatted = now.strftime("%d/%m/%Y, %H:%M:%S")
        return now_formatted

    return "I don't know what you are talking about! Sorry, try again"