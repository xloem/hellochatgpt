import random
import time
import breathing_messages
import standing_messages
import timer

def calm(num_minutes, standing):
    """
    Display calming messages, guide the user through deep breathing exercises, and suggest standing up and moving around for a specified number of minutes.
    """
    end_time = time.time() + 60 * num_minutes
    while time.time() < end_time:
        print(breathing_messages.get_inhale_message())
        timer.time_breath(10)
        print(breathing_messages.get_exhale_message())
        timer.time_breath(10)
        if standing:
            print(standing_messages.get_exercise_or_progress_message())
        else:
            print(standing_messages.get_stand_up_message())
