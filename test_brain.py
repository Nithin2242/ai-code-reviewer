import requests

# We are sending data to your local server on Port 5001
url = "http://127.0.0.1:5001/review"

# This is the buggy code we are pretending to send
buggy_code = """
def calculate_sum(a, b)
    return a + b
"""

data = {"code": buggy_code}

print("Sending code to your AI Server...")
try:
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("\n--- SUCCESS! AI RESPONSE BELOW ---")
        print(response.json()['review'])
    else:
        print("Error:", response.text)
        
except Exception as e:
    print("Connection failed:", e)