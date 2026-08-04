# ✈️ Flight Deal Finder

A Python application that automatically searches for low-cost flights using the Google Flights API (SerpApi), compares them against target prices stored in Google Sheets, and sends SMS notifications when a cheaper flight is found.

This project was developed as part of **Day 39** of the **100 Days of Code: The Complete Python Pro Bootcamp**.

---

## 🚀 Features

- Retrieve destinations and target prices from Google Sheets.
- Search flight prices using Google Flights (SerpApi).
- Compare current prices with predefined target prices.
- Send SMS alerts using Twilio.
- Request caching to reduce API calls.
- Object-Oriented Programming (OOP) architecture.

---

## 🛠 Technologies

- Python 3
- SerpApi
- Sheety API
- Twilio API
- Requests Cache
- Dateutil

---

## 📂 Project Structure

```
Flight_deal_finder/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
└── README.md
```

---

## 📖 Class Responsibilities

### DataManager

Retrieves destination information and target prices from Google Sheets.

### FlightSearch

Searches flights through the Google Flights API using SerpApi.

### FlightData

Extracts and structures only the relevant flight information from the API response.

### NotificationManager

Sends SMS notifications using Twilio.

---

## ⚙️ Workflow

1. Read destination data from Google Sheets.
2. Search available flights for multiple travel dates.
3. Compare the current flight price with the target price.
4. If a cheaper flight is found:
   - Structure the flight information.
   - Send an SMS notification.

---

## 🔐 Environment Variables

The following environment variables are required:

```text
SHEETY_URL=
SHEETY_AUTH=
SERP_API_KEY=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
MY_PHONE_NUMBER=
```

---

## 📚 What I Learned

During this project I practiced:

- Object-Oriented Programming (OOP)
- API integration
- HTTP requests
- JSON parsing
- SMS automation with Twilio
- Request caching
- Working with dates and time ranges
- Designing classes with single responsibilities

---

## 👨‍💻 Author

David Gonzalez

Part of my **100 Days of Python** journey.