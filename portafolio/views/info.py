import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.styles.styles import Size


def info(title: str, info: list[dict]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            rx.foreach(
                info,
                lambda item: info_detail(item)
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
