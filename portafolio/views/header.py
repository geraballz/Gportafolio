import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.state import LanguageState
from portafolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size=Size.BIG.value
        ),
        rx.vstack(
            heading(data.name, True),
            heading(
                rx.cond(
                    LanguageState.language == "es",
                    data.skill_es if data.skill_es else data.skill,
                    data.skill
                )
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
