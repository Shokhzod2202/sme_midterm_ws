import rclpy
from rclpy.action import ActionServer
from fleet_management_msgs.action import FleetManagement
from fleet_management_logic import manage_fleet

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('fleet_management_server')

    action_server = ActionServer(node, FleetManagement, 'fleet_management', manage_fleet)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
