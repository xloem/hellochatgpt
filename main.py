import random
import time

def calm(num_minutes):
    """
    Display calming messages, guide the user through deep breathing exercises, and suggest standing up and moving around for a specified number of minutes.
    """
    messages = [
        "It's okay to feel scared. It's a natural response to difficult situations.",
        "Take a deep breath in...",
        "Hold it for a moment...",
        "And slowly exhale...",
        "Close your eyes and focus on your breath...",
        "As you breathe in, remind yourself that you are safe and loved.",
        "As you exhale, let go of any tension or fear you may be feeling.",
        "Allow yourself to feel calm and centered.",
        "You are strong and capable of handling whatever comes your way.",
        "Take a break from sitting and stand up for a moment.",
        "Stretch your arms and legs.",
        "Take a few steps around the room or go outside for a short walk."
    ]
    
    end_time = time.time() + 60 * num_minutes
    while time.time() < end_time:
        print(random.choice(messages))
        print("Inhale for 5 seconds...")
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < 5:
            elapsed_time = time.time() - start_time
            remaining_time = 5 - elapsed_time
            print(f"{remaining_time:.1f} seconds remaining...")
            time.sleep(1)
        print("Exhale for 5 seconds...")
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < 5:
            elapsed_time = time.time() - start_time
            remaining_time = 5 - elapsed_time
            print(f"{remaining_time:.1f} seconds remaining...")
            time.sleep(1)

calm(10)
