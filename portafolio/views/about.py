import reflex as rx
from portafolio.components.bilingual import bilingual_heading


def about(description_en: str, description_es: str) -> rx.Component:
    return rx.vstack(
        bilingual_heading("About Me", "Sobre Mí"),
        rx.text(
            rx.el.span(description_en, class_name="lang-en"),
            rx.el.span(description_es, class_name="lang-es"),
        )
    )
