import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "Comfy.EasyUse.PromptRUS",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "easy prompt_RUS") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const r = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;
                const node = this;

                const prompt_text_widget = node.widgets.find(w => w.name === "text");
                if (!prompt_text_widget) return r;

                // Function to extract english tag from "Русский текст (english_tag)"
                function extractTag(val) {
                    if (!val) return "";
                    const m = val.match(/\(([^)]+)\)$/);
                    return m ? m[1].trim() : val.trim();
                }

                function appendTag(tag, isPrefix = false) {
                    if (!tag) return;
                    let current = prompt_text_widget.value || "";
                    if (!current.trim()) {
                        prompt_text_widget.value = tag;
                    } else if (isPrefix) {
                        prompt_text_widget.value = tag + " " + current.trim();
                    } else {
                        current = current.trim();
                        if (current.endsWith(",")) {
                            prompt_text_widget.value = current + " " + tag;
                        } else {
                            prompt_text_widget.value = current + ", " + tag;
                        }
                    }
                    if (prompt_text_widget.callback) {
                        prompt_text_widget.callback(prompt_text_widget.value);
                    }
                }

                // Setup combo hooks for 7 categories
                const combos = [
                    { name: "prefix", defaultTitle: "✨ Выберите префикс стиля...", isPrefix: true },
                    { name: "subject", defaultTitle: "👤 Выберите объект / персонажа...", isPrefix: false },
                    { name: "action", defaultTitle: "🎬 Выберите действие / позу...", isPrefix: false },
                    { name: "clothes", defaultTitle: "👚 Выберите одежду / аксессуары...", isPrefix: false },
                    { name: "environment", defaultTitle: "☀️ Выберите освещение / окружение...", isPrefix: false },
                    { name: "background", defaultTitle: "🎞️ Выберите задний план / локацию...", isPrefix: false },
                    { name: "nsfw", defaultTitle: "🔞 Выберите NSFW тег...", isPrefix: false }
                ];

                combos.forEach(cfg => {
                    const w = node.widgets.find(item => item.name === cfg.name);
                    if (w) {
                        Object.defineProperty(w, "value", {
                            set: (val) => {
                                if (val && val !== cfg.defaultTitle && w.options?.values?.includes(val)) {
                                    const tag = extractTag(val);
                                    appendTag(tag, cfg.isPrefix);
                                }
                            },
                            get: () => cfg.defaultTitle
                        });
                        w.serializeValue = () => cfg.defaultTitle;
                    }
                });

                return r;
            };
        }
    }
});
