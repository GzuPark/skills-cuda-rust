---
name: cuda-rust-runtime
description: Work with NVIDIA CUDA Rust host runtime, device buffers, streams, asynchronous operations, and interoperability between SIMT and Tile kernels. Use when managing GPU memory, execution, or external CUDA resources in CUDA Rust.
---

# CUDA Rust host runtime

Identify the versions and runtime APIs already used by the project before changing host code. The shared runtime includes `cuda-bindings`, `cuda-core`, and `cuda-async`; consult the matching source and API documentation. The snapshot's [host API reference](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/cutile-book/reference/host-api.md) and [device operations guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/cutile-book/guide/device-operations.md) provide starting points.

Trace ownership and lifetimes of each device buffer through allocation, transfer, launch, completion, and reuse. Keep borrowed or externally owned resources alive until GPU work completes. Preserve ordering on the stream used for dependent operations. When work crosses streams, establish the required synchronization explicitly rather than assuming an implicit ordering.

For external pointers, libraries, or streams, inspect the version-matched [interoperability guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cutile-rs/cutile-book/guide/interoperability.md). Document unsafe ownership, device, lifetime, aliasing, and synchronization invariants. For a mixed SIMT and Tile pipeline, consult the [inter-kernel example](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/crates/rustc-codegen-cuda/examples/cutile_inter_kernel/README.md); do not infer support for arbitrary intra-kernel interoperability.

Validate results against a host reference and run relevant asynchronous or interop tests on a compatible GPU. Report any unavailable GPU checks. When available, the repository's `llms.txt` indexes additional sources.
