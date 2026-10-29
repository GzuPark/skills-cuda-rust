---
name: cuda-oxide
description: Write, port, build, or debug NVIDIA cuda-oxide SIMT GPU kernels in Rust. Use when working with cargo oxide, explicit CUDA threads, shared memory, or cuda-oxide launch contracts.
---

# cuda-oxide

Identify the project's cuda-oxide revision, Rust toolchain, CUDA toolkit, driver, and GPU architecture before selecting instructions. Use the installation guide for that revision. Check the toolkit with `nvcc --version`; the CUDA version shown by `nvidia-smi` describes driver compatibility, not necessarily the installed toolkit. Run `cargo oxide doctor` to check prerequisites and backend status. The first build may need to build the backend. The fixed snapshot's [installation guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/cuda-oxide-book/getting-started/installation.md) and [README](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/README.md) describe the requirements. Do not assume older nightly instructions apply to the target version.

Start from a version-matched example, such as the snapshot's [first kernel](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/cuda-oxide-book/getting-started/hello-gpu.md). Keep host and device code and their build steps consistent with the existing project. In this snapshot, `DisjointSlice::get_mut(index)` consumes the `ThreadIndex`; read `index.get()` before passing it to `get_mut` if the numeric index is also needed. The [launch guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/cuda-oxide-book/gpu-programming/launching-kernels.md) explains contracts and prepared launches. Check launch geometry against each kernel's contract and input bounds.

An output bounds check does not prove that the same index is within each input. Verify every input's length independently. Keep device buffers alive until GPU work completes, and ensure stream ordering and synchronization before consuming results. Disjoint output access does not remove the need to reason about shared memory or barriers. Read the version-matched [safety model](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/cuda-oxide-book/gpu-safety/the-safety-model.md) when changing synchronization or unsafe code. State the invariants for any unsafe operation.

Run the project's build and correctness tests against representative inputs. If GPU execution or required tooling is unavailable, report exactly which checks were not run. For other models or host runtime work, use the relevant CUDA Rust skill if installed. When available, the repository's `llms.txt` indexes additional sources.
