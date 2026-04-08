from fastapi import FastAPI
from env import EmailTriageEnv

app = FastAPI()
env = EmailTriageEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: str):
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
