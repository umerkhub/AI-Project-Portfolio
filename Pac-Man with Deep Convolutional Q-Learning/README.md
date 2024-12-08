
# Pac-Man with Deep Convolutional Q-Learning

**Pac-Man with Deep Convolutional Q-Learning** is a reinforcement learning project that uses Deep Convolutional Q-Learning (DQN) to train an agent to play Pac-Man. The agent learns to navigate the maze, avoid ghosts, and collect pellets to maximize its score.
## Features

- Deep Convolutional Q-Learning (DQN): Utilizes convolutional neural networks (CNNs) to process the visual input from the game.
- Environment: The agent interacts with a Pac-Man environment where it learns optimal policies for gameplay.
- Reward System: The agent receives rewards for collecting pellets and avoiding ghosts.
## Requirements 

- Python 3.x
 
- Required libraries:
  ```bash
   pip install gym[atari] keras tensorflow numpy opencv-python
## Installation

1. Clone this repository:
  ```bash
git clone <repository-link>
cd pacman-dqn
 ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the training script:
   ```bash
   python pacman_dqn.py
## How it works:

1. Pac-Man Environment: The agent interacts with the Atari-based Pac-Man environment from OpenAI Gym.
2. Deep Convolutional Q-Learning: The agent uses a deep convolutional network to process the game’s visual input and learn policies for action selection.
3. Training: The agent learns by maximizing rewards from eating pellets and avoiding ghosts, training over multiple episodes.
4. Testing: After training, the agent plays Pac-Man autonomously, aiming to achieve the highest possible score.
## Results

- Performance: The agent learns to navigate the game effectively, scoring high as it avoids ghosts and collects pellets.
- Training Time: The time taken for training depends on the number of episodes and complexity of the environment.
## Future enhancements

- Improved Convolutional Architecture: Experiment with deeper CNN architectures for better performance.
- Multi-Agent System: Implement multiple agents to play Pac-Man collaboratively or competitively.
- Real-Time Performance: Optimize the model for real-time gameplay with faster decision-making.
## Acknowledgements

his project uses OpenAI Gym's Atari environments and TensorFlow/Keras for deep learning.
