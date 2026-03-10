import reflex as rx
from portafolio.components.media import media
from portafolio.styles.styles import Size


def footer(email: str, cv: str, github: str, linkedin: str) -> rx.Component:
    return rx.vstack(
        rx.text("Name"),
        media(email, cv, github, linkedin),
        spacing=Size.SMALL.value
    )
