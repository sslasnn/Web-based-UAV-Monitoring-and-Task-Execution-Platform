from aerialist.px4.drone_test import DroneTest
from aerialist.px4.docker_agent import DockerAgent
from aerialist.px4.obstacle import Obstacle
from aerialist.px4.trajectory import Trajectory

test = DroneTest.from_yaml("samples/tests/mission1-local.yaml")
agent = DockerAgent(test)
test_results = agent.run()
DroneTest.plot(test, test_results)
trajectory = test_results[0].record
trajectory.plot()
distance = trajectory.distance_to_obstacles(test.simulation.obstacles)
