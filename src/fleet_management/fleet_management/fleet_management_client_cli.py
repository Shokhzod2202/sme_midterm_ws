import rclpy
from rclpy.action import ActionClient
from fleet_management_msgs.action import FleetManagement
from fleet_management_msgs.action import FleetManagement_SendGoal_Request

def main():
    rclpy.init()
    node = rclpy.create_node('fleet_management_client')

    action_client = ActionClient(node, FleetManagement, 'fleet_management')

    goal_msg = FleetManagement_SendGoal_Request()
    goal_msg.goal.fleet_size = 5  # You can change the fleet size as needed

    action_client.wait_for_server()
    future = action_client.send_goal_async(goal_msg.goal)

    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        result = future.result().result()
        for route in result.vehicle_routes:
            print(f"Vehicle Route: {route}")
        print(f"Completion Percentage: {result.completion_percentage * 100}%")
    else:
        print("Action failed")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
