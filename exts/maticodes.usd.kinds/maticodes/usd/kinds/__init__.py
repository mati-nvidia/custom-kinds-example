from pathlib import Path

from pxr import Plug

kinds_plugin_path = Path(__file__).parent.parent.parent.parent / "plugins" / "MatiCodesKinds" / "resources"
print(kinds_plugin_path)
Plug.Registry().RegisterPlugins(str(kinds_plugin_path))
