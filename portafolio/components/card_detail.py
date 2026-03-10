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
                rx.box(extra.title, class_name="lang-en", display="inline"),
                rx.box(
                    extra.title_es if extra.title_es else extra.title,
                    class_name="lang-es",
                    display="inline"
                ),
            ),
            rx.text(
                rx.box(extra.description, class_name="lang-en", display="inline"),
                rx.box(
                    extra.description_es if extra.description_es else extra.description,
                    class_name="lang-es",
                    display="inline"
                ),
                size=Size.SMALL.value,
                color_scheme="gray"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True
    )
