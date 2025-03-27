from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Graph of cities with distances
graph = {
    "Mumbai": {"Delhi": 1400, "Bangalore": 980, "Hyderabad": 710, "Chennai": 1330, "Pune": 150},
    "Delhi": {"Mumbai": 1400, "Bangalore": 2150, "Hyderabad": 1580, "Chennai": 2200, "Jaipur": 280, "Lucknow": 550},
    "Bangalore": {"Mumbai": 980, "Delhi": 2150, "Hyderabad": 570, "Chennai": 350, "Kolkata": 1860},
    "Hyderabad": {"Mumbai": 710, "Delhi": 1580, "Bangalore": 570, "Chennai": 630, "Kolkata": 1490},
    "Chennai": {"Mumbai": 1330, "Delhi": 2200, "Bangalore": 350, "Hyderabad": 630, "Kolkata": 1660},
    "Kolkata": {"Bangalore": 1860, "Hyderabad": 1490, "Chennai": 1660, "Lucknow": 1000},
    "Pune": {"Mumbai": 150, "Bangalore": 840, "Hyderabad": 560},
    "Jaipur": {"Delhi": 280, "Lucknow": 600, "Ahmedabad": 660},
    "Ahmedabad": {"Jaipur": 660, "Mumbai": 530},
    "Lucknow": {"Delhi": 550, "Kolkata": 1000, "Jaipur": 600},
    # New cities added
    "Surat": {"Mumbai": 270, "Ahmedabad": 260},
    "Nagpur": {"Mumbai": 840, "Hyderabad": 500, "Bhopal": 350},
    "Bhopal": {"Nagpur": 350, "Delhi": 780, "Lucknow": 580},
    "Indore": {"Bhopal": 190, "Ahmedabad": 400, "Jaipur": 520},
    "Patna": {"Lucknow": 610, "Kolkata": 580, "Delhi": 1100},
    
}

# Dijkstra's Algorithm for shortest path
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    queue = distances.copy()

    while queue:
        min_node = min(queue, key=queue.get)
        queue.pop(min_node)

        if min_node == end:
            break

        for neighbor, cost in graph[min_node].items():
            alt = distances[min_node] + cost
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = min_node
                queue[neighbor] = alt

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    return path if distances[end] != float('inf') else []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shortest-path', methods=['GET'])
def shortest_path():
    start = request.args.get('start')
    end = request.args.get('end')

    if not start or not end:
        return jsonify({"error": "Missing start or end city parameter."}), 400
    if start not in graph or end not in graph:
        return jsonify({"error": "Invalid city name(s) provided."}), 400

    path = dijkstra(graph, start, end)
    
    if not path:
        return jsonify({"error": "No path found between the selected cities."}), 404

    return jsonify({"path": path})

if __name__ == '__main__':
    app.run(debug=True)
