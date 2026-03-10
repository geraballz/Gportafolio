import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.data import Extra
from portafolio.state import LanguageState
from portafolio.styles.styles import Size


def extra(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        heading(rx.cond(LanguageState.language == "es", "Extra", "Extra")),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(item)
                    for item in extras
                ],
                spacing=Size.DEFAULT.value
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(item)
                    for item in extras
                ],
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
