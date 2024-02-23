import random

import gymnasium as gym
import pygame
pygame.init()
env = gym.make('Taxi-v3')
# env = gym.make('Taxi-v3' , render_mode="human")
state, info = env.reset()
epoch = 0
epoch_limit = 1000
results = {}
time_spent = 0
time_limit = 50
wins = 0
while epoch < epoch_limit:
    terminated = False
    epoch_reward = 0
    while (terminated is not True) and (time_spent < time_limit):
        print(state)
        for event in pygame.event.get():
            # if event object type is QUIT
            # then quitting the pygame
            # and program both
            if event.type == pygame.QUIT:
                # This will exit the while loop
                running = False
        action = env.action_space.sample(info["action_mask"])
        # action = input("action")
        print("action", action)
        obs, reward, terminated, truncated, info = env.step(int(action))
        print("obs:", obs, "reward:", reward, "terminated", terminated, "truncated", truncated, "info", info)
        epoch_reward += reward
        time_spent += 1
        print(str(time_spent)+"/"+str(time_limit))
        print(env.render())

    if terminated is True:
        wins += 1
    epoch += 1
    results["epoch_"+str(epoch)] = {"finished": terminated, "epoch reward": epoch_reward, "render": env.render()}
    # results["epoch_"+str(epoch)] = str(epoch_reward) + str(terminated)
    print("Epoch reward :", epoch_reward)
    print(str(epoch)+"/"+str(epoch_limit))
    epoch_reward = 0
    env.reset()
    time_spent = 0
print(results)
print('win counter:', wins)
