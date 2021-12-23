from setuptools import setup
import subprocess
import os
import shutil


def cook_environment():
    ue4editor = os.environ.get("UE4Editor", None)
    if ue4editor is None:
        print("Cannot cook game")
        return

    platform = "Linux"
    args = [
        ue4editor,
        "Cartpole.uproject",
        "-run=cook",
        f"-targetplatform={platform}",
    ]
    subprocess.call(args)
    shutil.move("Saved/Sandboxes/Cooked-Linux", "Source/python/cartpole/Cooked")


def find_package_data(root="Source/python/cartpole/Cooked", data=None):
    first = False
    if data is None:
        data = []
        first = True

    for root, dirs, files in os.walk(root):
        for dir in dirs:
            find_package_data(os.path.join(root, dir), data)

        for file in files:
            if "Saved" in root:
                continue

            data.append(os.path.join(root, file))

    if first:
        data = list(set(data))
        rm = "Source/python/cartpole/"
        for i in range(len(data)):
            data[i] = data[i][len(rm) :]

    return data


if __name__ == "__main__":

    setup(
        name="cartpole",
        description="Cartpole environment",
        license="BSD-3-Clause",
        author="Pierre Delaunay",
        author_email="pierre@delaunay.io",
        url="https://github.com/Delaunay/cartpole",
        packages=["cartpole"],
        package_dir={"": "Source/python"},
        package_data={"cartpole": find_package_data()},
        # include_package_data=True,
    )
