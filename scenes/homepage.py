from bdh_sdk import ALL_MODES, Shortcut

from .views import activate_scene, get_scenes

SCENE_PREFIX = "scene."


def shortcuts():
    return [
        Shortcut(
            id=scene["id"].removeprefix(SCENE_PREFIX),
            title=scene["name"],
            icon=scene["icon"],
            order=10,
            modes=ALL_MODES,
        )
        for scene in get_scenes()
    ]


def run_shortcut(shortcut_id):
    activate_scene(SCENE_PREFIX + shortcut_id)
    return None
