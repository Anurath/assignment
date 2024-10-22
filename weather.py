def aggr_weather(records):
    total_temp, total_humidity = 0, 0
    count_temp, count_humidity = 0, 0
    
    for record in records:
        if 'temperature' in record:
            total_temp += record.get('temperature', 0)
            count_temp += 1
        if 'humidity' in record:
            total_humidity += record.get('humidity', 0)
            count_humidity += 1
    
    avg_temp = total_temp / count_temp if count_temp else None
    avg_humidity = total_humidity / count_humidity if count_humidity else None
    
    return {'average_temperature': avg_temp, 'average_humidity': avg_humidity}

data = [
    {'city': 'Pune', 'temperature': 25, 'humidity': 70},
    {'city': 'Delhi', 'temperature': 28, 'humidity': 60},
    {'city': 'Mumbai', 'temperature': 30, 'humidity': 65},  
    {'city': 'Ranchi', 'temperature': 22, 'humidity': 75},
]

result = aggr_weather(data)

print(f"Aggregated Weather Data: {result}")
