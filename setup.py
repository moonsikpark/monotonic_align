from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="monotonic_align.core",
            sources=["src/core.pyx"],
        ),
    ]
)
