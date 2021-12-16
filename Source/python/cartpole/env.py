from ue4ml import UnrealEnv
from ue4ml.core import AgentConfig


class Cartpole(UnrealEnv):
    MAP = '/Game/CartPole/CartPole.umap'
    PROJECT_NAME = None
    USE_IMAGE = True

    def __init__(self, path, ue4params=None, **kwargs):
        Cartpole.PROJECT_NAME = path

        if ue4params is not None:
            ue4params.set_default_map_name(Cartpole.MAP)

        super().__init__(ue4params=ue4params, **kwargs)

    @staticmethod
    def default_agent_config():
        agent_config = AgentConfig()

        # Our pawn that the agent is controlling
        agent_config.avatarClassName = "Pawn_Cart_C"

        # Actuators define the action space
        agent_config.add_actuator("InputKey")

        # Sensors define the observation space
        if Cartpole.USE_IMAGE:
            agent_config.add_sensor(
                "Camera",
                {
                    "width": "32",
                    "height": "32",
                }
            )
            return agent_config

        # Add our pawn movement (i.e cart movement)
        agent_config.add_sensor(
            "Movement",
            {
                "location": "absolute",
                "velocity": "absolute"
            }
        )

        # Add sight so we can see the pole
        agent_config.add_sensor(
            "AIPerception",
            {
                "count": "2",                   # Number of actors it can see
                'sort': 'distance',             # how the actors are sorted `distance`` or `in_front`
                'peripheral_angle': 180,        # sight cone
                'mode': 'rotator',               # vector (HeadingVector) or rotator
                                                # max_age
            }
        )

        return agent_config
