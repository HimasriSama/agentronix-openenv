from env import EmailTriageEnv
import random

def grade():

    env = EmailTriageEnv()

    state = env.reset()

    done = False

    actions = ["work", "personal", "promotion", "urgent", "spam"]

    total_reward = 0

    while not done:

        action = random.choice(actions)

        state, reward, done, info = env.step(action)

        total_reward += reward

    print("Total Reward:", total_reward)

    return total_reward


if __name__ == "__main__":
    grade()