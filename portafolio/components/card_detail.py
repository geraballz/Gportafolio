import reflex as rx
from portafolio.data import Extra
from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(
                rx.el.span(extra.title, class_name="lang-en"),
                rx.el.span(
                    extra.title_es if extra.title_es else extra.title,
                    class_name="lang-es"
                ),
            ),
            rx.text(
                rx.el.span(extra.description, class_name="lang-en"),
                rx.el.span(
                    extra.description_es if extra.description_es else extra.description,
                    class_name="lang-es"
                ),
                size=Size.SMALL.value,
                color_scheme="gray"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True
    )
