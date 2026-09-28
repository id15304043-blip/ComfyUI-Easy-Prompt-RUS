import os
from .prompt_rus import PromptRUS, PromptRUSLegacy
from comfy_api.latest import ComfyExtension

class PromptRUSExtension(ComfyExtension):
    async def get_node_list(self):
        return [PromptRUS]

async def comfy_entrypoint():
    return PromptRUSExtension()

NODE_CLASS_MAPPINGS = {
    "easy prompt_RUS": PromptRUSLegacy
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "easy prompt_RUS": "Prompt_RUS"
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY", "comfy_entrypoint"]
