# SIMT vector addition

This example adds two 1024-element `f32` vectors with cuda-oxide. Its dependencies use NVIDIA/cuda-rust commit `0d62b682be98a12897867b23ff0dfc0d765e9fa3`. Use the matching compiler version and follow NVIDIA's [installation guide](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/cuda-oxide-book/getting-started/installation.md) for CUDA, GPU, and system prerequisites.

The program is adapted from NVIDIA's [Writing Your First Kernel](https://github.com/NVIDIA/cuda-rust/blob/0d62b682be98a12897867b23ff0dfc0d765e9fa3/cuda-oxide/cuda-oxide-book/getting-started/hello-gpu.md) example. It changes the input and result checking code and uses a fixed block size. NVIDIA CUDA Rust is Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES and is licensed under Apache-2.0.

Install the matching build tool, then run from this directory:

```sh
cargo +1.99.1 install --git https://github.com/NVIDIA/cuda-rust.git --rev 0d62b682be98a12897867b23ff0dfc0d765e9fa3 cargo-oxide
cargo oxide doctor
cargo oxide run
```

A successful run prints `PASSED: all 1024 elements correct` after checking every result against the host calculation. The first run builds the compiler backend and may take longer.

The kernel declares a one-dimensional launch contract with 256 threads per block. `prepare_vecadd` validates the launch configuration before the typed launch. Four blocks cover all 1024 elements. Each thread receives a distinct index, and `DisjointSlice::get_mut` checks the output bound before returning a mutable element. Both input arrays have the same length as the output, so the guarded index is valid for both inputs. The three device buffers are separate allocations. The inputs are read-only, and threads do not share writable elements.

The unsafe module load requires the generated embedded device bundle to match the kernel module. The `cuda_module` macro generates that bundle for this package. The launch and result copy use the same stream. `to_host_vec` synchronizes that stream before returning, so the host compares completed results. This kernel uses no shared memory or barriers.
