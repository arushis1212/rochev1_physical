# Registration and stitch formation

The fixture defines the hook’s approach relative to the held chain. A clearance check can establish that the hook reaches the opening. Which strands it captures depends on how the yarn deforms during contact.

## Loop count and stitch structure

A single crochet starts with one live loop. Drawing yarn through the selected chain leaves two loops on the hook. Drawing yarn through both leaves one live loop again. The intermediate two-loop state distinguishes this sequence from a slip stitch. Inspecting the finished sample shows whether the new stitch is anchored through the intended chain.

## Where geometry helps

A rigid model can establish that the hook has a path past the supports. Yarn can still flatten against a pin, split at the hook, or follow the hook back out. Each event can occur while the carrier completes its full travel.

The CAD image documents the fixture design. Establishing repeatability requires independently loaded physical samples assessed against a hand-worked reference.

## CAD verification

Fabrication revision 0.2.0 was checked at five hook positions, twelve rotation angles and three pin positions, giving 180 sampled configurations. Across 10,281 rigid-part pair comparisons, the interference check flagged zero collisions. A separate check included the modeled envelopes of 23 screws, 23 nuts and 12 washers. The result describes nominal rigid geometry at the sampled poses. Print variation, yarn deformation and stitch formation are evaluated on the bench.

Three of the part models are available for independent inspection. Each STEP file reimported as one valid solid. The mesh checker reads the STL triangles, checks for opposite winding across shared edges and computes enclosed volume. The maximum difference between a sample mesh volume and its STEP solid was 0.094% when rounded upward. [Models and per-part results](../cad/README.md) · [Mesh checker](../tools/check_models.py)
