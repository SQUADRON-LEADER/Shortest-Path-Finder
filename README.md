# 🚀Shortest Path Finder using Dijkstra's Algorithm

This project is a Flask-based web application that finds the shortest path between two cities using **Dijkstra's Algorithm**. The application allows users to input a starting city and a destination city and returns the shortest route.

## ✨ Features
- Implementation of **Dijkstra's Algorithm** for shortest path computation
- Interactive web interface with Flask
- Predefined city network with distances
- JSON-based API responses for easy integration

## 🚀 Technologies Used
- **Python** (Flask for backend)
- **HTML/CSS** (for UI)
- **JavaScript** (for API interaction)

# 📌 Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/shortest-path-finder.git
   ```
2. Navigate to the project directory:
   ```sh
   cd shortest-path-finder
   ```
3. Install dependencies:
   ```sh
   pip install flask
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open your browser and go to:
   ```sh
   http://127.0.0.1:5000/
   ```

## 🌍  API Endpoints
- **`GET /shortest-path?start=<city>&end=<city>`**
  - Returns the shortest path between the two cities.
  - Example:
    ```sh
    http://127.0.0.1:5000/shortest-path?start=Mumbai&end=Delhi
    ```
  - Response:
    ```json
    {
      "path": ["Mumbai", "Jaipur", "Delhi"]
    }
    ```
## 📸 Screenshots
Here are some screenshots of the application in action:
![Screenshot 2025-03-27 105622](https://github.com/user-attachments/assets/18bacb32-a3b2-4b08-8240-4cf0975efb22)


## 📊 Dijkstra's Algorithm Overview
Dijkstra's Algorithm finds the shortest path in a weighted graph. It uses:
- A priority queue to always expand the shortest known path first.
- A distance dictionary initialized to infinity, except for the start node.
- A previous node dictionary to reconstruct the shortest path.

## ✅  Advantages of Dijkstra's Algorithm
- **Guaranteed shortest path**: Works efficiently for graphs with non-negative weights.
- **Versatile**: Can be applied to road networks, network routing, AI pathfinding, etc.
- **Efficient for dense graphs**: Works well with priority queues (O(V + E log V) complexity).

## 📜License
This project is open-source and available under the MIT License.

## 🤝 Contributing
Feel free to open an issue or submit a pull request if you have suggestions or improvements!
