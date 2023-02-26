import pynecone

from app import Global


class Logo:
    inline = pynecone.heading(
        "my-O.KR",
        display="inline-block",
        size="3xl",
        font_family=Global.FontFamily.LOGO,
        color=Global.Palette.RAISIN,
    )
    big = pynecone.box(
        inline,
        display="flex",
        flex_flow="column",
        justify_content="center",
        font_size="50vw",
        text_align="center",
    )
