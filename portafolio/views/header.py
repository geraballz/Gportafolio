import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.styles.styles import Size


def header(avatar: str, name: str, skill: str, location: str, email: str, cv: str, github: str, linkedin: str) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=avatar,
            size=Size.BIG.value
        ),
        rx.vstack(
            heading(name, True),
            heading(skill),
            rx.text(
                rx.icon("map-pin"),
                location,
                display="inherit"
            ),
            media(email, cv, github, linkedin),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )
