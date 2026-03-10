import reflex as rx
from portafolio.components.heading import heading
from portafolio.state import LanguageState


def about(description_en: str, description_es: str) -> rx.Component:
    return rx.vstack(
        heading(rx.cond(LanguageState.language == "es", "Sobre Mí", "About Me")),
        rx.text(
            rx.cond(
                LanguageState.language == "es",
                description_es if description_es else description_en,
                description_en
            )
        )
    )
