"""Check triangle edge incidence, winding and signed volume of the three public STLs."""
import math
import struct
from collections import Counter
from pathlib import Path

CAD = Path(__file__).resolve().parents[1] / "cad"
MODELS = ("P06_chain_clamp_stand", "P00B_test_journal", "P00C_hardware_coupon")
TRIANGLE = struct.Struct("<12fH")


def inspect_mesh(data):
    if len(data) < 84:
        raise ValueError("Missing binary STL header")
    faces = struct.unpack_from("<I", data, 80)[0]
    if faces == 0 or len(data) != 84 + faces * TRIANGLE.size:
        raise ValueError("Triangle count and file size disagree")

    edges = Counter()
    signed_volumes = []
    for record in TRIANGLE.iter_unpack(data[84:]):
        a, b, c = (record[i:i + 3] for i in (3, 6, 9))
        if not all(math.isfinite(x) for x in a + b + c):
            raise ValueError("Nonfinite vertex")
        # Coincident tessellation seams can differ in the last decimal places.
        # The coordinates are in mm. Only incidence uses the rounded keys.
        ring = [tuple(round(x, 6) for x in point) for point in (a, b, c)]
        if len(set(ring)) != 3:
            raise ValueError("Triangle collapses at the incidence resolution")
        edges.update(zip(ring, ring[1:] + ring[:1]))
        signed_volumes.append((
            a[0] * (b[1]*c[2] - b[2]*c[1]) +
            a[1] * (b[2]*c[0] - b[0]*c[2]) +
            a[2] * (b[0]*c[1] - b[1]*c[0])
        ) / 6)

    if any(n != 1 or edges[v, u] != 1 for (u, v), n in edges.items()):
        raise ValueError("An edge lacks exactly one opposite traversal")
    volume = math.fsum(signed_volumes)
    if volume <= 0:
        raise ValueError("Expected positive signed volume from outward winding")
    return faces, volume


if __name__ == "__main__":
    for model in MODELS:
        faces, volume = inspect_mesh((CAD / (model + ".stl")).read_bytes())
        print(f"{model}   {faces:,} triangles   {volume:,.2f} mm³")
