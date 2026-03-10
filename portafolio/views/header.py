import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size=Size.BIG.value
        ),
        rx.vstack(
            heading(data.name, True),
            rx.heading(
                rx.el.span(data.skill, class_name="lang-en"),
                rx.el.span(
                    data.skill_es if data.skill_es else data.skill,
                    class_name="lang-es"
                ),
                as_="h2",
                size=Size.MEDIUM.value,
            ),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )
