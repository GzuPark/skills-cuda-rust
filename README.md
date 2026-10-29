# CUDA Rust agent skills

These Agent Skills help coding agents work with NVIDIA CUDA Rust. The repository contains a model selection skill, SIMT and Tile kernel skills, and a shared host runtime skill. [llms.txt](llms.txt) indexes NVIDIA documentation at a fixed source revision and links to current documentation.

CUDA Rust is early-stage software. Match the sources and examples to the target project's dependencies. The pinned snapshot is not a claim that every API is present in a published release.

## Skills

- `cuda-rust` selects a programming model and identifies the project's existing dependencies.
- `cuda-oxide` covers SIMT kernel development and launch contracts.
- `cutile-rust` covers tile programs and tensor partitions.
- `cuda-rust-runtime` covers host resources, streams, and interoperability.

## Install

Install Node.js and npm, then run this command from the project where you want to use the skills:

```sh
npx skills add GzuPark/skills-cuda-rust
```

Select the skills and agents in the prompts. Choose **Project** to install in the current project or **Global** to install for your user. Run `npx skills list` from the project to inspect project installations, or `npx skills list --global` for global installations.

Start a new agent session after installation. Skills link directly to NVIDIA's sources, so an installed skill does not depend on this checkout or its `llms.txt`. The index is available when working in this repository; agents do not necessarily discover it automatically.

## License

This repository is licensed under the [Apache License 2.0](LICENSE). The vector addition example is adapted from NVIDIA CUDA Rust material; its [README](examples/simt-vecadd/README.md) records the source and modifications. NVIDIA CUDA Rust and its dependencies retain their own licenses.
