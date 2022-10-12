import json
import os
import os.path


raw = """
```shell
scoop bucket add trim21 https://github.com/trim21/scoop-bucket
```
"""

raw += '''
| 应用 | 介绍 |
|:-:|:-:|
'''

proj_root = os.path.dirname(__file__)

for file in sorted(os.listdir(os.path.join(proj_root, "bucket"))):
    with open(os.path.join(proj_root, 'bucket', file), 'r', encoding='utf8') as app_file:
        app = json.load(app_file)
        name = file.split('.')[0]
        description = app['description']
        raw += f'| {name} | {description} |\n'

with open('./README.md', 'w', encoding='utf8') as f:
    f.write(raw)
