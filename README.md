# 💱 currency_desktop_app

A simple yet powerful **Python desktop currency converter app** built using **Tkinter** and powered by the [GetGeoAPI](https://www.getgeoapi.com/) currency API.  
It converts currencies in real-time and displays conversion rates in a clean, beginner-friendly interface.

---

## 🚀 Features

✅ Fetches a live list of global currencies from GetGeoAPI  
✅ Select **“From”** and **“To”** currencies via intuitive listboxes  
✅ Enter any amount to instantly get the converted value  
✅ Displays both **conversion rate** and **final amount**  
✅ Minimal, responsive **Tkinter GUI** for a smooth experience  

---

## 🧠 Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3** | Core programming language |
| **Tkinter** | Graphical User Interface (GUI) |
| **Requests** | Handles HTTP API requests |
| **GetGeoAPI** | Provides live exchange rate data |

---

## ⚙️ How It Works

1. On startup, the app fetches a full list of currencies using  
   `https://api.getgeoapi.com/v2/currency/list`.
2. You pick your **source ("From")** and **target ("To")** currencies.  
3. Input your desired amount.  
4. Click **Convert**, and the app fetches live conversion data from  
   `https://api.getgeoapi.com/v2/currency/convert`.
5. The result and rate are displayed instantly in the right panel.

---

## 🪟 UI Overview

🟦 **Left Panel:** Currency selection & amount input  
🟩 **Right Panel:** Displays conversion details, selected currencies, and results  

---

## 🛠️ Installation & Setup

Clone the repository:
```bash
git clone https://github.com/your-username/currency_desktop_app.git
cd currency_desktop_app
Install required dependencies:

pip install requests


Run the app:

python main.py


🗝️ Note: Replace the placeholder api_key in the code with your personal API key from getgeoapi.com
.

🧩 Example Output
From: EUR  
To: GBP  
Amount: 10  
Result: 8.67  
Rate: 0.8670

✨ Future Improvements

🔁 Add Reverse Conversion button

🧭 Use dropdowns (Comboboxes) instead of listboxes

🖼️ Display country flags beside currencies

⚡ Add a loading spinner during API fetch

❗ Enhanced error handling for invalid input or network failure

👨‍💻 Author

Precious Oluwasegun Olonade
📍 Developer & Innovator
💼 @precious_segun (IG)

🪪 License

This project is licensed under the MIT License — you’re free to modify, use, and distribute it.

⭐ Pro tip: If you find this project helpful, drop a star on the repo to support future updates!
