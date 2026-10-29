---
name: cutile-rust
description: Write, build, or debug NVIDIA cuTile Rust tensor kernels. Use for cutile modules, tile operations, tensor partitions, JIT compilation, and cuTile kernel launches.
---

# cuTile Rust

Identify the project's `cutile` version, Rust toolchain, CUDA toolkit, driver, and GPU before choosing examples. Consult the matching release documentation. The snapshot's [README](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/README.md) and [compatibility guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/cutile-book/reference/compatibility.md) record prerequisites; current requirements can differ.

Start from a version-matched tutorial or example. Distinguish host tensor setup from the device tile program. Partition mutable outputs into disjoint regions, check shapes and boundary behavior, and use the generated operation with the execution mode required by the project. The [tensors and tiles guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/cutile-book/guide/tensors-and-tiles.md) and [vector addition tutorial](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/cutile-book/tutorials/02-vector-addition.md) describe the snapshot's model.

cuTile compiles kernels through Tile IR at runtime. For compilation or launch failures, inspect the version-matched [JIT guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/cutile-book/guide/jit-compilation.md). Do not assume SIMT thread indexing or synchronization APIs apply to a tile program. For unsafe pointers or external allocations, document and verify the ownership, lifetime, and synchronization contracts.

Run the project's build and correctness tests, including non-divisible shapes where supported. Report when GPU execution was unavailable. For host runtime or SIMT work, use the relevant CUDA Rust skill if installed. When available, the repository's `llms.txt` indexes additional sources.
