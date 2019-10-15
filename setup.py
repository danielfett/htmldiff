from setuptools import setup, find_packages

setup(
    name="htmldiff",
    version="1.1",
    author="Daniel Fett - https://github.com/danielfett",
    description=("Utility to create html diffs"),
    packages=find_packages('src'),
    package_dir={"": "src"},
    install_requires=["boltons>=17.1.0", "six"],
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "htmldiff = htmldiff.entry_point:main",
        ]
    }
)
