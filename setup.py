from setuptools import setup

if __name__ == '__main__':
    setup(
        name="cartpole",
        description="Cartpole environment",
        license="BSD-3-Clause",
        author=u"Pierre Delaunay",
        author_email="pierre@delaunay.io",
        url="https://github.com/Delaunay/cartpole",
        packages=[
            "cartpole"
        ],
        package_dir={"": "Source/python"},
        include_package_data=True,
    )
