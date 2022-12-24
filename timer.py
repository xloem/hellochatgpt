# timer.py

import time

def time_breath(duration):
    """
    Display a timer to help the user pace their breathing for a specified duration.
    """
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time < duration:
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time
        print(f"{remaining_time:.1f} seconds remaining...", end="\r")
        time.sleep(1)
