from setuptools import setup, find_namespace_packages

setup(
    name="assistant",
    version="1.0.0",
    description="Command line helper",
    author="Team 9",
    license="MIT",
    url="https://github.com/sergiokapone/console_assistant",
    include_package_data=True,
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["assistant = console_assistant.CLI:main"]},
    install_requires=[
        "prettytable==3.7.0",
        "Pygments",
        "transliterate",
        "prompt-toolkit==3.0",
        "requests",
        "beautifulsoup4",
    ],
    package_data={
        "": ["README.md"],
    },
)
