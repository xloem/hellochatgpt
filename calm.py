import random
import time
import messages
import timer

def calm(num_minutes):
    """
    Display calming messages, guide the user through deep breathing exercises, and suggest standing up and moving around for a specified number of minutes.
    """
    end_time = time.time() + 60 * num_minutes
    while time.time() < end_time:
        print(messages.get_inhale_message())
        timer.time_breath(10)
        print(messages.get_exhale_message())
        timer.time_breath(10)
        if random.random() < 0.5:
            print(messages.get_stand_up_message())
