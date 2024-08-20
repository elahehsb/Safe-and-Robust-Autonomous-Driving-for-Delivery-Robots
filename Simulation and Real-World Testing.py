import matplotlib.pyplot as plt

# Simulate the robot's trajectory
state = np.zeros(state_dim)
trajectory = [state]

for t in range(100):
    action = policy_network(torch.tensor(state, dtype=torch.float32)).detach().numpy()
    state = DeliveryRobotDynamics().state_transition(state, action, dt=0.1)
    trajectory.append(state)

trajectory = np.array(trajectory)
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.title('Robot Trajectory')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
