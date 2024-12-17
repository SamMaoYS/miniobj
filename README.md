# miniobj
Minimum wavefront .obj file parser in Python

## Installation
```bash
pip install miniobj
```

## Usage
```python
from miniobj import MiniObj

obj_mesh = MiniObj("mesh.obj")
# convert quad faces to triangles, ngon faces are not supported yet
obj_mesh.load(as_triangles=False)

obj_mesh.export("output.obj")
```

Check out [main.py](main.py) for more examples.
