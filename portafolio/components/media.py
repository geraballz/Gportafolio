import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.styles.styles import Size


def media(email: str, cv: str, github: str, linkedin: str) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{email}",
            email,
            True
        ),
        rx.hstack(
            icon_button(
                "file-text",
                cv
            ),
            icon_button(
                "github",
                github
            ),
            icon_button(
                "linkedin",
                linkedin
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )
