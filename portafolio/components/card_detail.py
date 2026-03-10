import reflex as rx
from portafolio.data import Extra
from portafolio.state import LanguageState
from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    title_text = rx.cond(
        LanguageState.language == "es",
        extra.title_es if extra.title_es else extra.title,
        extra.title
    )
    description_text = rx.cond(
        LanguageState.language == "es",
        extra.description_es if extra.description_es else extra.description,
        extra.description
    )

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
            rx.text.strong(title_text),
            rx.text(
                description_text,
                size=Size.SMALL.value,
                color_scheme="gray"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True
    )
