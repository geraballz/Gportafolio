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
                rx.box(data.skill, class_name="lang-en", display="inline"),
                rx.box(
                    data.skill_es if data.skill_es else data.skill,
                    class_name="lang-es",
                    display="inline"
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
