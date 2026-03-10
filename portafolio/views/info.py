import reflex as rx

from portafolio.components.bilingual import bilingual_heading
from portafolio.components.info_detail import info_detail
from portafolio.data import Info
from portafolio.styles.styles import Size


def info(title_en: str, title_es: str, info_list: list[Info]) -> rx.Component:
    return rx.vstack(
        bilingual_heading(title_en, title_es),
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
