from functools import partial

import pynecone
from pynecone import Component


class Container:
    wrapper = partial(
        pynecone.container,
        width="100%",
        padding="0 32px 0 32px",
    )

    @classmethod
    def with_cta(
        cls,
        *inner_components,
        cta_left: Component = "",
        cta_right: Component = "",
        **component_options,
    ):
        return pynecone.box(
            Container.wrapper(
                *inner_components,
                height="calc(100% - 80px)",
                **component_options,
            ),
            Container.wrapper(
                pynecone.button_group(
                    cta_left,
                    cta_right,
                    width="100%",
                    spacing=2,
                ),
                height="80px",
                display="flex",
                align_items="center",
            ),
            width="100%",
            height="100%",
            max_height="800px",
        )
