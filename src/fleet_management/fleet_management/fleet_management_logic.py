# fleet_management_logic.py

def manage_fleet(fleet_size):
    # Example: A simple fleet management logic
    if fleet_size <= 0:
        raise ValueError("Fleet size must be a positive integer.")

    # Allocate vehicles and calculate routes (simplified example)
    vehicles = [f"Vehicle {i + 1}" for i in range(fleet_size)]
    routes = [f"Route for {vehicle}" for vehicle in vehicles]

    # Calculate completion percentage (simplified example)
    completion_percentage = 100.0

    return routes, completion_percentage

if __name__ == '__main__':
    # This part is for testing the logic
    fleet_size = 5  # You can change the fleet size as needed
    routes, completion_percentage = manage_fleet(fleet_size)
    print("Routes:")
    for route in routes:
        print(route)
    print(f"Completion Percentage: {completion_percentage}%")
