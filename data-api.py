import requests
import json

url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/history"

headers = {
	"x-rapidapi-key": "8e5384f9afmsh6a96c044b56a495p1bb469jsne19cb6abba18",
	"x-rapidapi-host": "yahoo-finance15.p.rapidapi.com"
}
symbols = ["AAPL", "MSFT", "NVDA", "INTC", "AMZN"]

for symbol in symbols:
    querystring = {"symbol": symbol,"interval":"30m","diffandsplits":"false"}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json() 
    
        # Save the JSON response to a file
        with open(f"{symbol}.json", "w") as json_file:
            json.dump(data, json_file, indent=4)  # Save with indentation for readability
        print(f"Data saved to {symbol}.json")
    else:
        print("Failed to retrieve data:", response.status_code)