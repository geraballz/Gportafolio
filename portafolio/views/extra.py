import reflex as rx
from portafolio.components.card_detail import card_detail
from portafolio.components.heading import heading
from portafolio.styles.styles import Size


def extra(extras: list[dict]) -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.mobile_only(
            rx.vstack(
                rx.foreach(
                    extras,
                    lambda extra: card_detail(extra)
                ),
                spacing=Size.DEFAULT.value
            ),
            width="100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                rx.foreach(
                    extras,
                    lambda extra: card_detail(extra)
                ),
                spacing=Size.DEFAULT.value,
                columns="3"
            ),
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
