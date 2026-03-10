import reflex as rx


# Renders two versions of text, toggled via JS/CSS
def bilingual(text_en: str, text_es: str, tag: str = "span") -> rx.Component:
    return rx.fragment(
        rx.el.span(text_en, class_name="lang-en"),
        rx.el.span(text_es, class_name="lang-es"),
    )


def bilingual_text(text_en: str, text_es: str) -> rx.Component:
    return rx.text(
        rx.el.span(text_en, class_name="lang-en"),
        rx.el.span(text_es, class_name="lang-es"),
    )


def bilingual_strong(text_en: str, text_es: str) -> rx.Component:
    return rx.text.strong(
        rx.el.span(text_en, class_name="lang-en"),
        rx.el.span(text_es, class_name="lang-es"),
    )


def bilingual_heading(text_en: str, text_es: str, h1: bool = False) -> rx.Component:
    from portafolio.styles.styles import Size
    return rx.heading(
        rx.el.span(text_en, class_name="lang-en"),
        rx.el.span(text_es, class_name="lang-es"),
        as_="h1" if h1 else "h2",
        size=Size.BIG.value if h1 else Size.MEDIUM.value,
    )
