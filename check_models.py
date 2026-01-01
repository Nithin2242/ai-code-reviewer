import google.generativeai as genai

# PASTE YOUR KEY HERE
MY_API_KEY = "AIzaSyBA1aes6VFJlW-aaLBomOlghQrR1Uut1NQ"
genai.configure(api_key=MY_API_KEY)

print("--- Checking Available Models ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print("Error:", e)