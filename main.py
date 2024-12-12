import argparse
from miniobj import MiniObjLoader

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("obj_file", type=str, help="Path to the .obj file")
    args = parser.parse_args()

    loader = MiniObjLoader(args.obj_file)
    loader.load()

    print("Num Vertices: ", len(loader.v))
    print("Num UVs: ", len(loader.vt))
    print("Num Normals: ", len(loader.vn))

    if len(loader.fvn) > 0:
        assert len(loader.fv) == len(loader.fvn), "Face vertex and normal count mismatch"
    if len(loader.fvt) > 0:
        assert len(loader.fv) == len(loader.fvt), "Face vertex and UV count mismatch"
    
    print("Materials: ", loader.mtl)

    for k, faces in loader.mtl_f_map.items():
        print("Checking Material: ", k)
        
        face_vertices = [loader.fv[i] for i in faces]
        face_uvs = [loader.fvt[i] for i in faces]
        face_normals = [loader.fvn[i] for i in faces]
