import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack


class State(rx.State):
    language: str = "en"
    data: dict = data.get_data("en")

    def set_language(self, lang: str):
        self.language = lang
        self.data = data.get_data(lang)

    @rx.var
    def title(self) -> str:
        return self.data["title"]

    @rx.var
    def description(self) -> str:
        return self.data["description"]

    @rx.var
    def image(self) -> str:
        return self.data["image"]

    @rx.var
    def avatar(self) -> str:
        return self.data["avatar"]

    @rx.var
    def name(self) -> str:
        return self.data["name"]

    @rx.var
    def skill(self) -> str:
        return self.data["skill"]

    @rx.var
    def location(self) -> str:
        return self.data["location"]

    @rx.var
    def about_text(self) -> str:
        return self.data["about"]

    @rx.var
    def technologies(self) -> list[dict]:
        return self.data["technologies"]

    @rx.var
    def experience(self) -> list[dict]:
        return self.data["experience"]

    @rx.var
    def projects(self) -> list[dict]:
        return self.data["projects"]

    @rx.var
    def training(self) -> list[dict]:
        return self.data["training"]

    @rx.var
    def extras(self) -> list[dict]:
        return self.data["extras"]

    @rx.var
    def media(self) -> dict:
        return self.data["media"]

    @rx.var
    def email(self) -> str:
        return self.data["media"]["email"]

    @rx.var
    def cv(self) -> str:
        return self.data["media"]["cv"]

    @rx.var
    def github(self) -> str:
        return self.data["media"]["github"]

    @rx.var
    def linkedin(self) -> str:
        return self.data["media"]["likedin"]

    @rx.var
    def sections(self) -> dict:
        return self.data["sections"]


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.hstack(
                rx.spacer(),
                rx.select(
                    ["en", "es"],
                    value=State.language,
                    on_change=State.set_language,
                    width="100px"
                ),
                justify="end",
                width="100%"
            ),
            header(State.avatar, State.name, State.skill, State.location, State.email, State.cv, State.github, State.linkedin),
            about(State.about_text),
            rx.divider(),
            tech_stack(State.technologies),
            info(State.sections["experience"], State.experience),
            info(State.sections["projects"], State.projects),
            info(State.sections["academy"], State.training),
            extra(State.extras),
            rx.divider(),
            footer(State.email, State.cv, State.github, State.linkedin),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="grass",
        radius="full"
    )
)

app.add_page(
    index,
    title=State.title,
    description=State.description,
    image=State.image,
    meta=[
        {"name": "og:title", "content": State.title},
        {"name": "og:description", "content": State.description},
        {"name": "og:image", "content": State.image}
    ]
)
