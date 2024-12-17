import argparse
from miniobj import MiniObj

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("obj_file", type=str, help="Path to the .obj file")
    parser.add_argument(
        "--as_triangles", action="store_true", help="Convert quads to triangles"
    )
    parser.add_argument(
        "--output", type=str, help="Path to the output .obj file", default="output.obj"
    )
    args = parser.parse_args()

    obj_mesh = MiniObj(args.obj_file)
    obj_mesh.load(as_triangles=args.as_triangles)

    print("Num Vertices: ", len(obj_mesh.v))
    print("Num UVs: ", len(obj_mesh.vt))
    print("Num Normals: ", len(obj_mesh.vn))

    if obj_mesh.has_fvn:
        assert len(obj_mesh.fv) == len(
            obj_mesh.fvn
        ), f"Face vertex and normal count mismatch: {len(obj_mesh.fv)} != {len(obj_mesh.fvn)}"
    if obj_mesh.has_fvt:
        assert len(obj_mesh.fv) == len(
            obj_mesh.fvt
        ), f"Face vertex and UV count mismatch: {len(obj_mesh.fv)} != {len(obj_mesh.fvt)}"

    print("Materials: ", obj_mesh.mtl)

    for k, faces in obj_mesh.mtl_f_map.items():
        print("Checking Material: ", k)

        face_vertices = [obj_mesh.fv[i] for i in faces]
        face_uvs = [obj_mesh.fvt[i] for i in faces]
        face_normals = [obj_mesh.fvn[i] for i in faces]

    obj_mesh.export(args.output)
