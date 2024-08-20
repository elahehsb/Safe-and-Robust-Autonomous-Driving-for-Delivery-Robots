import torch
import torch.nn as nn
import torch.optim as optim

class SafeControlPolicy(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(SafeControlPolicy, self).__init__()
        self.fc1 = nn.Linear(state_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, action_dim)
    
    def forward(self, state):
        x = torch.relu(self.fc1(state))
        x = torch.relu(self.fc2(x))
        action = torch.tanh(self.fc3(x))  # Output in the range [-1, 1]
        return action

# Initialize the policy network
state_dim = 3  # [x, y, theta]
action_dim = 2  # [v, omega]
policy_network = SafeControlPolicy(state_dim, action_dim)

# Optimizer and loss function for training
optimizer = optim.Adam(policy_network.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

# Example training loop (simplified)
for epoch in range(1000):
    # Sample state and desired next state (supervised learning setup)
    state = torch.randn(state_dim)
    desired_action = torch.randn(action_dim)
    
    # Forward pass to predict action
    predicted_action = policy_network(state)
    
    # Compute loss and backpropagate
    loss = loss_fn(predicted_action, desired_action)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
