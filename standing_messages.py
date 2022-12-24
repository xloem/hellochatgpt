import random

def get_stand_up_message():
    """
    Return a random message to encourage the user to stand up.
    """
    messages = [
        "Take a break from sitting and stand up for a moment.",
        "Stretch your arms and legs.",
        "Get some movement in your body.",
        "Take a few steps around the room.",
        "Stand up and take a short walk outside."
    ]
    return random.choice(messages)

def get_exercise_or_progress_message():
    """
    Return a random message to encourage the user to get a little exercise or make progress on their day while standing.
    """
    messages = [
        "Take a few minutes to make a little progress on your day.",
        "Pick one small task and complete it.",
        "Write down one thing you're grateful for.",
        "Do some stretches or light exercises while standing.",
        "Take a short walk around the room."
    ]
    return random.choice(messages)
