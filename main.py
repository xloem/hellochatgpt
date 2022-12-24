import random
import time

def calm(num_minutes):
    """
    Display calming messages and breathe in and out for a specified number of minutes.
    """
    messages = [
        "Take a deep breath in...",
        "Hold it for a moment...",
        "And slowly exhale...",
        "Close your eyes and focus on your breath...",
        "Let go of any tension in your body...",
        "Allow yourself to feel relaxed and calm...",
        "You are doing great!"
    ]
    
    end_time = time.time() + 60 * num_minutes
    while time.time() < end_time:
        print(random.choice(messages))
        time.sleep(5)

calm(10)
