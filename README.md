# Safe-and-Robust-Autonomous-Driving-for-Delivery-Robots

### Project Overview
This project aims to develop a safe and robust control system for small autonomous delivery robots, such as those used for last-mile delivery. The system will ensure that the robot operates safely in dynamic environments, such as urban streets or sidewalks, while maintaining high performance. The project will combine modern machine learning techniques, nonlinear control theory, and optimization to achieve formal safety guarantees like safe-set invariance, reachability, and input-to-state stability. The robot will be able to navigate safely, avoid obstacles, and handle uncertainties in real-time, all while being interpretable and data-efficient.

### Project Goals
  #### Model the Robot’s Dynamics: 
  Develop a nonlinear dynamical model of the delivery robot, capturing its kinematics and sensor inputs.
  
  #### Safe-Set Learning: 
  Implement machine learning algorithms to learn safe control policies that guarantee safe-set invariance.
  
  #### Optimization for Robustness: 
  Use optimization techniques to ensure that the control policies are robust to uncertainties and disturbances.
  
  #### Formal Verification: 
  Apply formal verification methods to ensure that the robot’s control policies meet safety requirements under all conditions.
  
  #### Simulation and Real-World Testing: 
  Test the system in simulations and, if possible, in real-world environments to validate its safety and performance.
  

### Implementation Steps
1. Modeling the Robot’s Dynamics
First, define a nonlinear model of the delivery robot’s dynamics, focusing on its movement and control inputs (e.g., wheel velocities, steering angle).
2. Safe-Set Learning
Implement a safe control policy using reinforcement learning (RL) or a supervised learning approach, ensuring that the robot stays within a safe set.
3. Optimization for Robustness
Incorporate optimization techniques to refine the control policy, ensuring that it is robust to disturbances while maintaining safety.
4. Formal Verification
Use formal verification methods to ensure the safety of the learned control policies. This could involve reachability analysis to guarantee the robot’s safety under all possible conditions.
5. Simulation and Real-World Testing
Simulate the robot's behavior in a virtual environment, testing the control policies in various scenarios. If possible, deploy the system on a real robot for further validation.
