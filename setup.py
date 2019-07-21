from setuptools import find_packages, setup

setup(
    name="fo",
    version="0.2",
    url="https://github.com/ixai/fo",
    author="Ixai Lanzagorta",
    author_email="ixai.lanzagorta@gmail.com",
    description="Fraction Operations",
    packages=find_packages(),
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        fo=fo:fraction_operation
    """,
)
