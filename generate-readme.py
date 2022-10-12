import json
import pathlib


def main():
    lines = [
        "```shell",
        "scoop bucket add trim21 https://github.com/trim21/scoop-bucket",
        "```",
        "",
        "",
        "| 应用 | 介绍 | 主页 |",
        "| :-: | :-: | :-: |",
    ]

    proj_root = pathlib.Path(__file__).parent

    for file in sorted(proj_root.joinpath("bucket").iterdir()):
        with file.open("r", encoding="utf8") as app_file:
            app = json.load(app_file)
            name = file.name.split(".")[0]
            description = app["description"]
            homepage = app["homepage"]
            lines.append(f"| {name} | {description} | <{homepage}> |")

    with open("./README.md", "w", encoding="utf8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
