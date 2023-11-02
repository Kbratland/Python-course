from requests import *

result = get("https://mclainonline.com")
try:
    result.raise_for_status()
except Exception as e:
    print(f"Error retrieving webpage: {e}")
    exit()
print("Yippee")