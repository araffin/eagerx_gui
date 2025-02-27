# EAGERx imports
import eagerx
from eagerx.core.graph import Graph

# Implementation specific
import eagerx.bridges.openai_gym as eagerx_gym
import eagerx.nodes

if __name__ == "__main__":
    roscore = eagerx.initialize(
        "eagerx_core", anonymous=True, log_level=eagerx.log.INFO
    )

    # Define rate (depends on rate of gym env)
    rate = 20

    # Define object
    gym_id = "Acrobot-v1"  # 'Pendulum-v0', 'Acrobot-v1', 'CartPole-v1', 'MountainCarContinuous-v0'
    name = gym_id.split("-")[0]
    obj = eagerx.Object.make(
        "GymObject",
        name,
        env_id=gym_id,
        sensors=["observation", "reward", "done", "image"],
        rate=rate,
        default_action=0,
        render_shape=[300, 300],
    )

    # Define graph
    graph = Graph.create(objects=[obj])
    graph.connect(source=obj.sensors.observation, observation="observation", window=1)
    graph.connect(source=obj.sensors.reward, observation="reward", window=1)
    graph.connect(source=obj.sensors.done, observation="done", window=1)
    graph.connect(action="action", target=obj.actuators.action, window=1)
    graph.render(source=obj.sensors.image, rate=10)

    # Open gui
    obj.gui("GymBridge")
    graph.gui()

    # Define bridge
    bridge = eagerx.Bridge.make(
        "GymBridge",
        rate=rate,
        is_reactive=True,
        real_time_factor=1,
        process=eagerx.process.NEW_PROCESS,
    )

    env = eagerx_gym.EagerxGym(name="rx", rate=rate, graph=graph, bridge=bridge)

    # Turn on rendering
    env.render(mode="human")

    # First reset
    obs, done = env.reset(), False
    for j in range(5):
        print("\n[Episode %s]" % j)
        iter = 0
        while not done and iter < 10:
            iter += 1
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
        obs = env.reset()
        done = False
    print("\n[Finished]")
    env.shutdown()
    print("\n[shutdown]")
