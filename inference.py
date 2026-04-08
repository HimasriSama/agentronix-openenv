from env import EmailTriageEnv

env = EmailTriageEnv()

def reset():
    state = env.reset()
    return {"state": state}

def step(action):
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }