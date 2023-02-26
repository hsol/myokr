from functools import partial

import pynecone
from pynecone import Component


class Container:
    wrapper = partial(
        pynecone.container,
        width="100%",
        padding="0 32px 0 32px",
        height="100%",
    )

    @classmethod
    def with_cta(
        cls,
        *inner_components,
        cta_left: Component = pynecone.box(),
        cta_right: Component = pynecone.box(),
        **component_options,
    ):
        return pynecone.box(
            Container.wrapper(
                *inner_components,
                height="calc(100% - 80px)",
                **component_options,
            ),
            Container.wrapper(
                pynecone.hstack(
                    cta_left,
                    cta_right,
                    height="100%",
                ),
                height="auto",
                padding="1em 1em 1em 1em",
            ),
            height="100%",
            max_height="800px",
        )
