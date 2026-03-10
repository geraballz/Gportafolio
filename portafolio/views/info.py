import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.data import Info
from portafolio.state import LanguageState
from portafolio.styles.styles import Size


def info(title_en: str, title_es: str, info_list: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(rx.cond(LanguageState.language == "es", title_es, title_en)),
        rx.vstack(
            *[
                info_detail(item)
                for item in info_list
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
