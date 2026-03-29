from env import EmailTriageEnv
import random

env = EmailTriageEnv()

state = env.reset()
actions = ["work", "personal", "promotion", "urgent", "spam"]

# limit the number of steps so the program finishes
for step in range(10):

    action = random.choice(actions)

    state, reward, done, info = env.step(action)

    print("Action:", action)
    print("Reward:", reward)
    print("Next Email:", state)
    print("--------------------")

    if done:
        break

print("Finished execution")