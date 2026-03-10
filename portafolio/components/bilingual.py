import reflex as rx
from portafolio.styles.styles import Size


def bilingual_heading(text_en: str, text_es: str, h1: bool = False) -> rx.Component:
    return rx.heading(
        rx.box(text_en, class_name="lang-en", display="inline"),
        rx.box(text_es, class_name="lang-es", display="inline"),
        as_="h1" if h1 else "h2",
        size=Size.BIG.value if h1 else Size.MEDIUM.value,
    )
