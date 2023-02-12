from concurrent.futures import ThreadPoolExecutor, as_completed

# update values of timestamped video segments dict using specified function
def update_segment(func, vid_dict, timestamp, text):
    vid_dict[timestamp] = func(text) # assign new text to dict key
    return timestamp, vid_dict[timestamp]


# function to run tasks in parallel
def thread_runner(func, vid_segments):
    threads = []
    # with ThreadPoolExecutor(max_workers=len(vid_segments)) as executor:
    with ThreadPoolExecutor(max_workers=len(vid_segments)) as executor:
        for stamp, text in vid_segments.items():
            # pass necessary values and intented func to helper
            threads.append(executor.submit(update_segment, func, vid_segments, stamp, text))
            
    return [task.result() for task in as_completed(threads)]
