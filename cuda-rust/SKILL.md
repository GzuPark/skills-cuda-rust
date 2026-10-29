---
name: cuda-rust
description: Choose and work with NVIDIA CUDA Rust programming models and shared runtime. Use for CUDA Rust projects when identifying the existing model or choosing between cuda-oxide SIMT and cuTile Rust.
---

# CUDA Rust

Inspect the project's manifests, lockfile, toolchain configuration, and existing kernels before choosing documentation or changing code. Respect the model and dependency versions already in use. NVIDIA CUDA Rust is early-stage software, and APIs and requirements change.

For API or compatibility claims, prefer documentation and examples from the project's resolved release or Git revision. Treat the fixed links below as references to their stated snapshot, not as evidence for another version. If the resolved version or matching source cannot be established, say so and label any guidance from a different revision as unverified for the project.

For a new kernel, choose cuda-oxide when the work needs explicit thread, warp, shared-memory, or synchronization control, or when porting a SIMT kernel. Choose cuTile Rust when tensor operations fit tile partitions and the compiler can handle thread scheduling. A program can use both. Ask for requirements if neither model's trade-offs can be decided from the task.

Use the specialized `cuda-oxide`, `cutile-rust`, or `cuda-rust-runtime` skill if installed and relevant. Each is independently usable. Verify APIs against the target project's version, not an unrelated example. The [CUDA Rust overview](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/README.md) describes the models at a fixed source revision. When working in this repository, consult `llms.txt` at the repository root for additional sources. Otherwise use NVIDIA's [current documentation](https://nvidia.github.io/cuda-rust/).

Validate with the project's build and tests. When GPU execution is unavailable, report that runtime correctness remains unverified.
