
from setuptools import setup, find_packages

setup(
    name="factorengine",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi", "uvicorn", "pydantic"
    ],
    entry_points={
        "console_scripts": [
            "factorengine=engine_core:main_factoring_engine"
        ]
    },
)
