import reflex as rx
from portafolio.components.bilingual import bilingual_heading
from portafolio.data import Technology
from portafolio.styles.styles import Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        bilingual_heading("Technologies", "Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="24px"
                    ),
                    rx.text(technology.name),
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
