from setuptools import setup

REQUIREMENTS = [
    "fastapi==0.63.0",
    "pydantic==1.7.3",
    "starlette==0.13.6",
    "chardet==3.0.4",
    "uvicorn"
]

DEV_REQUIREMENTS = [
    "tox==3.24.4",
    "black==21.9b0"
]

setup(
    name='action_validation_passporting_api',
    version='0.0.1',
    description='api for creating and validating chains of actions',
    author='Matt Smith <08msmith6@gmail.com>',
    install_requires=REQUIREMENTS,
    extra_require={
        'dev': DEV_REQUIREMENTS
    }
)
