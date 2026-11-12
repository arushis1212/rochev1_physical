# Selected part models

These are three original components of the Roche V1 Physical fixture. The tail-clamp stand is installed on the base. The journal and coupon are bench tools used to check fit before committing to the larger parts.

| Part | Design detail | CAD solid | Triangle mesh |
| --- | --- | --- | --- |
| P06 · Tail-clamp stand | An offset fin carries the foundation-tail clip and leaves access to the two mounting screws. | [STEP](P06_chain_clamp_stand.step) | [STL](P06_chain_clamp_stand.stl) |
| P00B · Test journal | A cylindrical journal with a flange provides a repeatable specimen for assessing sliding and rotational fit. | [STEP](P00B_test_journal.step) | [STL](P00B_test_journal.stl) |
| P00C · Hardware-fit coupon | Hexagonal pockets and round bores let the same print sample be checked against purchased nuts and rod. | [STEP](P00C_hardware_coupon.step) | [STL](P00C_hardware_coupon.stl) |

## Geometry checks

Each STEP model reimported as one valid solid. The STLs use millimetres. The triangle meshes approximate curved surfaces, which accounts for small volume differences between the two formats.

| Part | STL triangles | STEP volume (mm³) | STL volume (mm³) |
| --- | ---: | ---: | ---: |
| Tail-clamp stand | 708 | 5,928.55 | 5,928.65 |
| Test journal | 836 | 5,362.70 | 5,357.70 |
| Hardware-fit coupon | 2,124 | 10,078.43 | 10,078.55 |

From the repository root, run the following command with Python 3. The checker uses the standard library, verifies that each edge has one opposite traversal and reports the triangle counts and signed volumes.

```sh
python3 tools/check_models.py
```

[Illustrated component catalog](../docs/components.md) · [Parts register](../docs/parts.csv)
