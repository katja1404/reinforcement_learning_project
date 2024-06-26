from gym.envs.registration import register

register(
    id="environments/Maze-v0",
    entry_point="environments.envs:Maze",
)
register(
    id="environments/AdvancedMaze-v0",
    entry_point="environments.envs:AdvancedMaze",
)
register(
    id="environments/ExampleMaze-v0",
    entry_point="environments.envs:ExampleMaze",
)
register(
    id="environments/ExampleMaze-v2",
    entry_point="environments.envs:ExampleMaze2",
)
