import numpy as np

class DeliveryRobotDynamics:
    def __init__(self, wheel_base=0.5):
        self.wheel_base = wheel_base

    def state_transition(self, state, control_input, dt):
        """
        State transition function for the robot.
        
        state: [x, y, theta] (position and orientation)
        control_input: [v, omega] (linear velocity, angular velocity)
        dt: time step
        """
        x, y, theta = state
        v, omega = control_input

        # Update the state based on the robot's kinematics
        x += v * np.cos(theta) * dt
        y += v * np.sin(theta) * dt
        theta += omega * dt

        return np.array([x, y, theta])
