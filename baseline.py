from env import EmailTriageEnv
import random

env = EmailTriageEnv()

state = env.reset()

done = False

actions = ["work", "personal", "promotion", "urgent", "spam"]

while not done:

    action = random.choice(actions)

    state, reward, done, info = env.step(action)

    print("Action:", action)
    print("Reward:", reward)
    print("Next Email:", state)
    print("-------------------")

    import time

print("Environment execution finished. Keeping container alive...")

while True:
    time.sleep(60)