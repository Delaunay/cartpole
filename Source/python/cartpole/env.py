from MLAdapter import UnrealEnv
from MLAdapter.core import AgentConfig

import pkg_resources


def load_exec(name):
    try:
        return pkg_resources.resource_filename(__name__, name)
    except Exception:
        return None


cartpole_linux = load_exec("Cooked/LinuxNoEditor/Cartpole.sh")
cartpole_windows = load_exec("Cooked/WindowsNoEditor/Cartpole.exe")


class Cartpole(UnrealEnv):
    """
    Parameters
    ----------
    path: str
        path to the project file (.uproject), leave to None to use the packaged version

    ue4params: UE4Params
        Unreal Engine additional parameters, leave to None to connect to a running instance

    """

    MAP = "/Game/CartPole/CartPole.umap"
    PROJECT_NAME = None
    USE_IMAGE = True

    def __init__(self, path=None, ue4params=None, **kwargs):
        if path is None:
            path = cartpole_windows

        Cartpole.PROJECT_NAME = path

        if ue4params is not None:
            ue4params.set_default_map_name(Cartpole.MAP)

        super().__init__(
            ue4params=ue4params, standalone=cartpole_windows is not None, **kwargs
        )

    @staticmethod
    def default_agent_config():
        agent_config = AgentConfig()

        # Our pawn that the agent is controlling
        agent_config.avatarClassName = "Pawn_Cart_C"

        # Actuators define the action space
        agent_config.add_actuator(
            "InputKey", dict(ignore_keys="esc", ignore_actions="Quit")
        )

        # Sensors define the observation space
        if Cartpole.USE_IMAGE:
            agent_config.add_sensor(
                "Camera",
                {
                    "width": "32",
                    "height": "32",
                },
            )
            return agent_config

        # Add our pawn movement (i.e cart movement)
        agent_config.add_sensor(
            "Movement", {"location": "absolute", "velocity": "absolute"}
        )

        # Add sight so we can see the pole
        agent_config.add_sensor(
            "AIPerception",
            {
                "count": "2",  # Number of actors it can see
                "sort": "distance",  # how the actors are sorted `distance`` or `in_front`
                "peripheral_angle": 180,  # sight cone
                "mode": "rotator",  # vector (HeadingVector) or rotator
                # max_age
            },
        )

        return agent_config
