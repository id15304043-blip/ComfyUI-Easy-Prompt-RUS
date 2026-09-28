import json
import os
from comfy_api.latest import io

# Load mappings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "mapping.json"), "r", encoding="utf-8") as f:
    ALL_MAPS = json.load(f)

PREFIX_OPTIONS = ["✨ Выберите префикс стиля..."] + [f"{ru} ({en})" for en, ru in ALL_MAPS["prefix"].items()]
SUBJECT_OPTIONS = ["👤 Выберите объект / персонажа..."] + [f"{ru} ({en})" for en, ru in ALL_MAPS["subject"].items()]
ACTION_OPTIONS = ["🎬 Выберите действие / позу..."] + [f"{ru} ({en})" for en, ru in ALL_MAPS["action"].items()]
CLOTHES_OPTIONS = ["👚 Выберите одежду / аксессуары..."] + [f"{ru} ({en})" for en, ru in ALL_MAPS["clothes"].items()]
ENVIRONMENT_OPTIONS = ["☀️ Выберите освещение / окружение..."] + [f"{ru} ({en})" for en, ru in ALL_MAPS["environment"].items()]
BACKGROUND_OPTIONS = ["🎞️ Выберите задний план / локацию..."] + [f"{ru} ({en})" for en, ru in ALL_MAPS["background"].items()]
NSFW_OPTIONS = ["🔞 Выберите NSFW тег..."] + [f"{ru} ({en})" for en, ru in ALL_MAPS["nsfw"].items()]

class PromptRUS(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="easy prompt_RUS",
            display_name="Prompt_RUS",
            category="EasyUse/Prompt",
            description="Русская версия палитры тегов Prompt от EasyUse с мгновенной вставкой рабочих английских токенов",
            inputs=[
                io.String.Input("text", default="", multiline=True, placeholder="Введите промпт (Prompt)..."),
                io.Combo.Input("prefix", options=PREFIX_OPTIONS, default=PREFIX_OPTIONS[0]),
                io.Combo.Input("subject", options=SUBJECT_OPTIONS, default=SUBJECT_OPTIONS[0]),
                io.Combo.Input("action", options=ACTION_OPTIONS, default=ACTION_OPTIONS[0]),
                io.Combo.Input("clothes", options=CLOTHES_OPTIONS, default=CLOTHES_OPTIONS[0]),
                io.Combo.Input("environment", options=ENVIRONMENT_OPTIONS, default=ENVIRONMENT_OPTIONS[0]),
                io.Combo.Input("background", options=BACKGROUND_OPTIONS, default=BACKGROUND_OPTIONS[0]),
                io.Combo.Input("nsfw", options=NSFW_OPTIONS, default=NSFW_OPTIONS[0]),
            ],
            outputs=[
                io.String.Output("prompt"),
            ],
            hidden=[
                io.Hidden.prompt,
                io.Hidden.extra_pnginfo,
                io.Hidden.unique_id,
            ],
        )

    @classmethod
    def execute(cls, text, **kwargs):
        return io.NodeOutput(text)

# Classic fallback API
class PromptRUSLegacy:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True, "placeholder": "Введите промпт (Prompt)..."}),
                "prefix": (PREFIX_OPTIONS, {"default": PREFIX_OPTIONS[0]}),
                "subject": (SUBJECT_OPTIONS, {"default": SUBJECT_OPTIONS[0]}),
                "action": (ACTION_OPTIONS, {"default": ACTION_OPTIONS[0]}),
                "clothes": (CLOTHES_OPTIONS, {"default": CLOTHES_OPTIONS[0]}),
                "environment": (ENVIRONMENT_OPTIONS, {"default": ENVIRONMENT_OPTIONS[0]}),
                "background": (BACKGROUND_OPTIONS, {"default": BACKGROUND_OPTIONS[0]}),
                "nsfw": (NSFW_OPTIONS, {"default": NSFW_OPTIONS[0]}),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
                "unique_id": "UNIQUE_ID"
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "execute"
    CATEGORY = "EasyUse/Prompt"

    def execute(self, text, **kwargs):
        return (text,)
