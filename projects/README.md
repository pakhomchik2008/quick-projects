# Projects

Four complete mini-applications that apply OOP, algorithms, and data structures
to solve real-world problems.

---

## Weather Application

**File:** [`weather-app/weather_app.py`](weather-app/weather_app.py)

A command-line weather app consuming the OpenWeatherMap REST API.

**Design patterns:**
- Abstract Base Classes (`WeatherService`, `WeatherFormatter`)
- Template Method pattern (shared `_request()` method)
- Strategy pattern (swap formatters without changing logic)

**Features:**
- Current weather (temperature, humidity, wind speed, description)
- 5-day daily forecast at noon

**Setup:** Set `OPENWEATHER_API_KEY` environment variable or replace the placeholder in the file.

---

## Social Network

**File:** [`social-network/social_network.py`](social-network/social_network.py)

A graph-based social network with real graph algorithm implementations.

**Data structure:** Weighted undirected adjacency list graph.

**Features:**
- Add/remove members with profile metadata
- Add friendships with connection strength weights
- Mutual friends discovery
- Friend suggestions (friends-of-friends)
- Shortest social path (BFS)
- Community detection (DFS connected components)
- Influence scores (degree centrality)

---

## Bank Account

**File:** [`bank-account/bank_account.py`](bank-account/bank_account.py)

A fully object-oriented banking application with authentication and transaction history.

**Concepts:** Encapsulation, `@property`, `@dataclass(frozen=True)`, composition.

**Features:**
- User registration and login
- Deposit and withdrawal with validation
- Immutable `Transaction` records
- Formatted account statement

---

## Vehicle Rental System

**File:** [`vehicle-rental/vehicle_rental.py`](vehicle-rental/vehicle_rental.py)

A rental fleet management system demonstrating inheritance hierarchies.

**Hierarchy:** `Vehicle → Car / Truck / Motorcycle`

**Features:**
- Fleet management (add/list vehicles)
- Customer records with `@dataclass`
- Date-range rentals with automatic cost calculation
- Availability tracking and rental reports

---

## How to Run

```bash
# Weather app (requires API key)
python projects/weather-app/weather_app.py

# All others run standalone
python projects/social-network/social_network.py
python projects/bank-account/bank_account.py
python projects/vehicle-rental/vehicle_rental.py
```
