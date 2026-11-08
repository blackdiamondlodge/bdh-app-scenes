from bdh_sdk import PluginSpec, Tile

spec = PluginSpec(
    id="scenes",
    app="scenes",
    urls="scenes.urls",
    shortcuts="scenes.homepage.shortcuts",
    run_shortcut="scenes.homepage.run_shortcut",
    tiles=(
        Tile(
            title="Lights & Scenes",
            url_name="scenes",
            icon="scenes/hub/icon.svg",
            section="lodge",
            subtitle="Set the mood",
            order=10,
        ),
    ),
)
