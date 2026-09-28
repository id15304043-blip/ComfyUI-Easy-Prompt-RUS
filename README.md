# ComfyUI-Easy-Prompt-RUS 🇷🇺

Русскоязычная локализация и адаптация узла **`Prompt`** (`easy prompt`) из популярного набора **[ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)**.

> [!NOTE]
> **Важное пояснение и отсылка к оригиналу:**
> Данный проект является **исключительно локализацией интерфейса и базы тегов** существующего узла. 
> - Оригинальный автор и проект: **[ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)** by **[yolain](https://github.com/yolain)**.
> - Все права на оригинальную кодовую базу и архитектуру Easy-Use принадлежат первоначальному автору. Модуль оформлен как отдельный легковесный custom node, чтобы вам не приходилось модифицировать файлы пакета вручную при обновлениях.

---

## 💡 Особенности и как это работает

1. **Русский интерфейс с сохранением английских токенов**:
   - В выпадающих меню отображается понятный русский перевод с оригинальным английским тегом в скобках.
   - При выборе любого пункта скрипт **автоматически извлекает рабочий английский токен** и вставляет его в текстовое поле промпта.
   - Таким образом, итоговый промпт отправляется в нейросети (**Qwen 2.1, FLUX, SDXL, SD 1.5, MiniMax**) в стандартном англоязычном виде, без ошибок и без искажения смысла.

2. **356 переведенных тегов по 7 категориям**:
   - ✨ **Префиксы стиля**: фотография шедевр (masterpiece photograph), концепт-арт (concept art), аниме стиль (anime style), гиперреализм и др.
   - 👤 **Объекты / Субъекты**: 1 парень (1boy), 1 девушка (1girl), кот (cat), воин (warrior), пара (couple) и др.
   - 🎬 **Действия / Позы**: стоит (standing), сидит (sitting), бежит (running), взгляд в камеру (looking at camera), динамичная поза и др.
   - 👚 **Одежда / Аксессуары**: повседневная одежда (casual clothes), деловой костюм (business suit), кибер-костюм (cyberpunk suit), кожаная куртка и др.
   - ☀️ **Освещение / Окружение**: кинематографичный свет (cinematic lighting), золотой час (golden hour), объемный свет (volumetric light), контровой свет и др.
   - 🎞️ **Локации / Фон**: городская улица (city street), неоновый мегаполис (cyberpunk city), студийный фон (studio background), природа и др.
   - 🔞 **NSFW / Цензура**: теги взрослого контента и анатомические маркеры.

3. **Удобство**:
   - После клика по категории селектор автоматически возвращается в исходное состояние — можно непрерывно кликать и собирать сложный промпт как из конструктора.

---

## 📦 Установка

### Вариант 1: Через Git (рекомендуется)
1. Откройте терминал в папке `ComfyUI/custom_nodes/`:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/id15304043-blip/ComfyUI-Easy-Prompt-RUS.git
   ```
2. Перезапустите ComfyUI.
3. Обновите страницу в браузере (`Ctrl + F5`).

### Вариант 2: Через ComfyUI Manager
1. В ComfyUI откройте **Manager ➔ Install via Git URL**.
2. Вставьте ссылку: `https://github.com/id15304043-blip/ComfyUI-Easy-Prompt-RUS`
3. Нажмите **Install**, перезапустите ComfyUI и обновите вкладку браузера.

---

## 🚀 Использование на холсте

- **Поиск узла**: нажмите дважды ЛКМ на холсте ComfyUI и введите `Prompt_RUS` или `easy prompt_RUS`.
- **В меню**: `Add Node ➔ EasyUse ➔ Prompt ➔ Prompt_RUS`.
- Соедините выходной сокет `prompt` с CLIP Text Encode, узлом улучшения промптов (Prompt Enhancer) или любым генеративным пайплайном.

---

## 🧠 Ссылки на Prompt Enhancer модели и их размещение

Узел отлично сочетается с моделями автоматического расширения и детализации промптов (Prompt Enhancers), включая семейство **Qwen 2.1 / Gemma**:

* **Hugging Face репозиторий моделей (Adahm)**:
  * [PE-Heretic-INT8-ConvRot-for-Qwen-Image-2.1](https://huggingface.co/Adahm/PE-Heretic-INT8-ConvRot-for-Qwen-Image-2.1)
  * Доступны варианты:
    * `qwen3.5_9b_qwen_image_2.1_pe_t2i_heretic.int8_convrot.safetensors` — Text-to-Image Prompt Enhancer (чистый текст).
    * `qwen3.5_9b_qwen_image_2.1_pe_i2i_heretic.int8_convrot.safetensors` — Image-to-Image / Edit Prompt Enhancer (работает с изображением-референсом и инструкцией правки).

### Куда помещать скачанные файлы моделей:
* **Текстовые энкодеры и языковые модели (Prompt Generator / Enhancer)**:
  `ComfyUI/models/text_encoders/` или `ComfyUI/models/prompt_generator/`
* **Проекторы зрения (Vision / mmproj)** (если используется многомодальный GGUF loader):
  `ComfyUI/models/text_encoders/` (например, `mmproj-qwen3vl_8b_heretic-f16.gguf`)
* **GGUF квантованные модели**:
  `ComfyUI/models/clip/` или `ComfyUI/models/text_encoders/`

---

## 📄 Лицензия

Распространяется под лицензией **GNU General Public License v3.0 (GPL-3.0)** в соответствии с лицензией оригинального репозитория [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use).
