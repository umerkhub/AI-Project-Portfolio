
# Lunar Landing with Deep Q-Learning

**Lunar Landing with Deep Q-Learning** is a reinforcement learning project where the agent learns to control a spacecraft in the Lunar Landing environment. Using the Deep Q-Learning algorithm (DQN), the agent navigates the lunar surface, learns to land safely, and maximizes the reward.
## Features

- Deep Q-Learning (DQN): Trains the agent to control the spacecraft's movement.
- Training Process: The agent explores different strategies for a safe landing and learns from the environment.
- Reward System: The agent is rewarded for safe landings and penalized for crashing.
## Requirements 

- Python 3.x
 
- Required libraries:
  ```bash
   pip install gym keras tensorflow numpy
## Installation

1. Clone this repository:
  ```bash
git clone <repository-link>
cd lunar-landing-dqn
 ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the training script:
   ```bash
   python lunar_landing.py
## How it works:

1. Lunar Landing Environment: The agent interacts with the OpenAI Gym environment for Lunar Landing.
2. Deep Q-Learning: The agent uses Q-Learning with a neural network to approximate the Q-values and decide actions.
3. Training: The agent learns through repeated interactions and adjusts its strategy based on rewards and penalties.
4. Testing: After training, the agent is tested to check how well it can land on the lunar surface.
## Results

- Final Agent Reward: The agent's performance improves as it learns effective strategies.
- Training Time: The training time depends on the complexity and the number of episodes.
## Future enhancements

- Better Neural Network: Experiment with deeper or more complex neural networks for better performance.
- Hyperparameter Tuning: Fine-tune the model’s hyperparameters for improved efficiency.
## Acknowledgements

This project uses OpenAI Gym for the Lunar Landing environment and TensorFlow/Keras for the deep learning model.
