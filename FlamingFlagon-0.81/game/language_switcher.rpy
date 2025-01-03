# language_switcher.rpy

# Инициализация доступных языков
init python:
    # Список доступных языков с их кодами
    languages = [
        ("None", "English"),
        ("russian", "Русский"),
    ]

    # Индекс текущего языка
    def get_current_language_index():
        current_lang = renpy.get_language()
        for i, (code, name) in enumerate(languages):
            if code == current_lang:
                return i
        return 0  # По умолчанию первый язык

    # Переключение языка по индексу
    def switch_language(direction=1):
        current_index = get_current_language_index()
        new_index = (current_index + direction) % len(languages)
        new_lang_code = languages[new_index][0]
        renpy.change_language(new_lang_code)
        renpy.notify(f"Language switched to: {languages[new_index][1]}")

# Добавление горячих клавиш
define keymap["switch_language_next"] = [ "shift+L" ]  # Переключить язык вперёд
define keymap["switch_language_prev"] = [ "shift+K" ]  # Переключить язык назад

# Реализация действий для горячих клавиш
label main_menu:
    $ renpy.input.bind("switch_language_next", lambda: switch_language(1))
    $ renpy.input.bind("switch_language_prev", lambda: switch_language(-1))
    return