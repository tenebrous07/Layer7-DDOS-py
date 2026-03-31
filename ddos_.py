import requests
import threading
import time
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# Lists to store request and response times
request_times = []
response_times = []

# Function to get current time in milliseconds
def current_mil_time():
    return round(time.time() * 1000)

# Initialize User Agents
software_names = [
    SoftwareName.CHROME.value,
    SoftwareName.FIREFOX.value,
    SoftwareName.BRAVE.value,
    SoftwareName.SAFARI.value,
    SoftwareName.BINGBOT.value
]
operating_systems = [
    OperatingSystem.WINDOWS.value,
    OperatingSystem.LINUX.value,
    OperatingSystem.ANDROID.value,
    OperatingSystem.IOS.value,
    OperatingSystem.MACOS.value
]
user_agent_rotator = UserAgent(
    software_names=software_names,
    operating_systems=operating_systems,
    limit=100
)

# Function to make HTTP request
def make_request(url):
    while True:
        try:
            start_time = current_mil_time()
            user_agent = user_agent_rotator.get_random_user_agent()
            headers = {'User-Agent': user_agent}

            r = requests.get(url, headers=headers)
            end_time = current_mil_time()

            request_time = end_time - start_time
            response_time = r.elapsed.total_seconds() * 1000  # in ms

            request_times.append(request_time)
            response_times.append(response_time)

            print(f"[{threading.current_thread().name}] Request made to {url} "
                  f"with UA: {user_agent[:50]}... | Response: {response_time:.2f} ms")

        except requests.exceptions.RequestException as e:
            print(f"Error occurred during request: {str(e)}")
            time.sleep(1)  # prevent tight loop if errors occur

# Function to calculate average response time
def calculate_average_response_time():
    while True:
        time.sleep(5)
        if len(response_times) > 0:
            avg_response_time = sum(response_times) / len(response_times)
            print(f"\n[Monitor] Average response time: {avg_response_time:.2f} ms\n")
        else:
            print("\n[Monitor] No responses yet...\n")

# Main function
def main(url, num_threads):
    # Start response monitor thread
    avg_thread = threading.Thread(target=calculate_average_response_time, daemon=True)
    avg_thread.start()

    # Start threads for making requests
    for i in range(num_threads):
        t = threading.Thread(target=make_request, args=(url,), name=f"Thread-{i+1}", daemon=True)
        t.start()

# Run the script
if __name__ == "__main__":
    url = "URL"
    num_threads = 500  # ⚠️ Reduce threads for safety testing (1000 is excessive)
    main(url, num_threads)
    while True:
        time.sleep(1)
