import reflex as rx
from portafolio.state import LanguageState


def language_selector() -> rx.Component:
    return rx.hstack(
        rx.icon("globe", size=16),
        rx.button(
            "EN",
            on_click=LanguageState.set_language("en"),
            variant=rx.cond(LanguageState.language == "en", "solid", "ghost"),
            size="1",
            cursor="pointer",
        ),
        rx.text("|", size="1", color_scheme="gray"),
        rx.button(
            "ES",
            on_click=LanguageState.set_language("es"),
            variant=rx.cond(LanguageState.language == "es", "solid", "ghost"),
            size="1",
            cursor="pointer",
        ),
        spacing="1",
        align="center",
    )
