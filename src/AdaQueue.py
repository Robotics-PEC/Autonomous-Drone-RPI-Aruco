# QueueManager.py
import queue

# Initialize the global queue
result_queue = queue.Queue()


# Function to get the result from the queue (thread-safe)
def get_result():
    return result_queue.get() if not result_queue.empty() else None


# Function to push result into the queue (thread-safe)
def push_result(result):
    result_queue.put(result)
