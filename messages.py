import random

def get_inhale_message():
    """
    Return a random message to display while the user is inhaling.
    """
    messages = [
        "Take a deep breath in...",
        "Breathe in peace and calm...",
        "Inhale positivity and strength...",
        "Fill your lungs with oxygen and vitality...",
        "Breathe in relaxation and relaxation..."
    ]
    return random.choice(messages)

def get_exhale_message():
    """
    Return a random message to display while the user is exhaling.
    """
    messages = [
        "Slowly exhale...",
        "Release any tension or stress...",
        "Breathe out negativity and worry...",
        "Exhale tranquility and calm...",
        "Let go of any fear or anxiety..."
    ]
    return random.choice(messages)

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
