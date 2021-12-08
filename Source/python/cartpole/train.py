
import random
import math
from itertools import count

import torch
import torch.nn as nn
import torch.optim as optim
import gym.spaces
import ue4ml.logger as logger
from torch.distributions import Categorical
from ue4ml.utils import random_action

from cartpole.env import Cartpole
from cartpole.model import Model
from cartpole.replay import ReplayMemory, Transition


logger.set_level(logger.DEBUG)

project = 'E:/cartpole/UE4RL.uproject'


env = Cartpole(project)

def space_size(x):
    def prod(lst):
        n = 1
        for i in lst:
            n *= i
        return n

    if isinstance(x, gym.spaces.Discrete):
        return x.n

    if isinstance(x, gym.spaces.MultiDiscrete):
        return sum([n for n in x.nvec])

    if isinstance(x, gym.spaces.Box):
        return prod([n for n in x.shape])

    if isinstance(x, gym.spaces.Dict):
        n = 0
        for _, item in x.spaces.items():
            n += space_size(item)
        return n

    if isinstance(x, gym.spaces.Tuple):
        n = 0
        for item in x.spaces:
            n += space_size(item)
        return n


def flatten_obs(obs, size):
    t = torch.zeros((size,))

    s = 0
    e = 0
    for ob in obs:
        v = torch.flatten(torch.Tensor(ob))
        e = v.shape[0]
        t[s:s+e] = v
        s = s + e

    return t


BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200
TARGET_UPDATE = 10


class DDQTrainer:
    def __init__(self) -> None:
        self.input_size = space_size(env.observation_space)
        self.output_size = space_size(env.action_space)

        self.device = 'cuda'
        self.policy = Model(self.input_size, self.output_size).to(self.device)
        self.target = Model(self.input_size, self.output_size).to(self.device)

        self.target.load_state_dict(self.policy.state_dict())
        self.target.eval()

        self.optimizer = optim.RMSprop(self.policy.parameters())
        self.memory = ReplayMemory(10000)
        self.loss = 0
        self.loss_count = 0

    def select_action(self, state):
        """Our model does not return the action perse but the distribution of all the action"""


        with torch.no_grad():
            # Our batch is size=1 here
            state = state.unsqueeze(0).to(self.device)

            weights = self.policy(state)
            dist = Categorical(weights)
            action = dist.sample()

            print('Action: ', action.item(), random_action(env))

            log_prob = dist.log_prob(action).unsqueeze(1)
            return action, log_prob, dist.entropy()

    def optimize(self):
        if len(self.memory) < BATCH_SIZE:
            return

        transitions = self.memory.sample(BATCH_SIZE)
        batch = Transition(*zip(*transitions))

        # 128x1 = True if next_state exists
        non_final_mask = torch.tensor(
            tuple(map(lambda s: s is not None, batch.next_state)),
            device=self.device,
            dtype=torch.bool
        )

        non_final_next_states = torch.stack(
            [s for s in batch.next_state if s is not None]).to(self.device)

        # Shape is 128x11
        state_batch = torch.stack(batch.state).to(self.device)

        # Shape: 128x1
        action_batch = torch.stack(batch.action).to(self.device)

        # Shape: 128
        reward_batch = torch.cat(batch.reward).to(self.device)

        # Compute Q(s_t, a) - the model computes Q(s_t), then we select the
        # columns of actions taken. These are the actions which would've been taken
        # for each batch state according to policy_net
        state_action_values = self.policy(state_batch).gather(1, action_batch)

        next_state_values = torch.zeros(BATCH_SIZE, device=self.device)

        # Get the largest action probability, shape: 128
        expected = self.target(non_final_next_states).max(1)[0].detach()
        next_state_values[non_final_mask] = expected

        # Compute the expected Q values
        expected_state_action_values = ((next_state_values * GAMMA) + reward_batch).unsqueeze(1)

        criterion = nn.SmoothL1Loss()
        loss = criterion(state_action_values, expected_state_action_values)

        # Optimize the model
        self.optimizer.zero_grad()
        loss.backward()
        for param in self.policy.parameters():
            param.grad.data.clamp_(-1, 1)
        self.optimizer.step()

        self.loss += loss.item()
        self.loss_count += 1;

    def train(self):
        num_episodes = 50

        for i_episode in range(num_episodes):
            # Initialize the environment and state
            state = flatten_obs(env.reset(), self.input_size)

            for t in count():
                # Select and perform an action
                action, log_prob, entropy = self.select_action(state)

                obs, reward, done, _ = env.step(action.item())
                obs = flatten_obs(obs, self.input_size)

                reward = torch.tensor([reward], device=self.device)

                # Store the transition in memory
                self.memory.push(state, action, obs, reward)

                # Move to the next state
                state = obs

                # Perform one step of the optimization (on the policy network)
                self.optimize()

                if done:
                    break

            if (self.loss_count > 100):
                print(f'{i_episode} {t} Loss {self.loss / self.loss_count}')
                self.loss_count = 0
                self.loss = 0

            # Update the target network, copying all weights and biases in DQN
            if i_episode % TARGET_UPDATE == 0:
                self.target.load_state_dict(self.policy.state_dict())


if __name__ == '__main__':
    trainer = DDQTrainer()
    trainer.train()
