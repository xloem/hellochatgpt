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
