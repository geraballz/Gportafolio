import reflex as rx


class LanguageState(rx.State):
    language: str = "en"

    def set_language(self, lang: str):
        self.language = lang
