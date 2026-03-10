import reflex as rx
from portafolio.components.bilingual import bilingual_heading


def about(description_en: str, description_es: str) -> rx.Component:
    return rx.vstack(
        bilingual_heading("About Me", "Sobre Mí"),
        rx.text(
            rx.box(description_en, class_name="lang-en", display="inline"),
            rx.box(description_es, class_name="lang-es", display="inline"),
        )
    )
