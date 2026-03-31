⚡ Layer 7 HTTP Load Tester (Python)

📌 Overview

This project is a multi-threaded Layer 7 HTTP load testing tool built in Python. It simulates concurrent clients sending requests to a target server while measuring response times and performance behavior.
It includes user-agent rotation and real-time monitoring, making it useful for basic performance testing and experimentation.

⚠️ Disclaimer: This tool is intended for authorized testing and educational purposes only. Do not use it against systems without explicit permission.


🚀 Features

🔁 Continuous HTTP request generation
🧵 Multi-threaded traffic simulation
🕵️ Randomized User-Agent rotation
⏱️ Request & response time tracking
📊 Real-time average response monitoring
⚠️ Error handling with retry delay


🧠 How It Works

Multiple threads continuously send HTTP GET requests to a target URL
Each request:
Uses a random User-Agent
Tracks total request time and server response time
A background monitoring thread calculates:
📊 Average response time every 5 seconds
This mimics high user traffic and helps observe how a server behaves under load.


🛠️ Tech Stack

Python 3.x
requests
threading
random-user-agent


⚙️ Installation

git clone https://github.com/tenebrous07/Layer7-DDOS-py.git
cd your-repo-name
pip install requests random-user-agent


▶️ Usage

Update the script before running:
url = "https://example.com"
num_threads = 100  # Recommended safe range
Then run:
python main.py


📊 Output Example

[Thread-1] Request made to https://example.com | Response: 120.45 ms
[Thread-2] Request made to https://example.com | Response: 98.12 ms

[Monitor] Average response time: 110.23 ms


⚠️ Important Notes

Using 500+ threads can overwhelm:
Your system
The target server
Start with low thread counts (10–100) and scale gradually
This script runs in an infinite loop until manually stopped


📌 Limitations

Uses threading (not optimal for extreme scale)
No rate limiting or request control
No distributed execution
Memory grows as logs accumulate


🔮 Future Improvements

Async version using aiohttp
Request rate limiting
Proxy support
Export metrics (CSV / JSON)
Dashboard visualization


⚠️ Legal & Ethical Use

This tool must only be used on:
Systems you own
Systems you have explicit permission to test
Unauthorized usage may be illegal.


📜 License

MIT License
