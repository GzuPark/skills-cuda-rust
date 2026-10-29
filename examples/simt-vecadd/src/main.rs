use cuda_core::{CudaContext, DeviceBuffer, LaunchConfig1D};
use cuda_device::{DisjointSlice, kernel, launch_bounds, launch_contract, thread};
use cuda_host::cuda_module;

const N: usize = 1024;
const BLOCK_SIZE: u32 = 256;

#[cuda_module]
mod kernels {
    use super::*;

    #[kernel]
    #[launch_bounds(256)]
    #[launch_contract(domain = 1, block = (256, 1, 1))]
    pub fn vecadd(a: &[f32], b: &[f32], mut c: DisjointSlice<f32>) {
        let index = thread::index_1d();
        let i = index.get();
        if let Some(output) = c.get_mut(index) {
            *output = a[i] + b[i];
        }
    }
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let context = CudaContext::new(0)?;
    let stream = context.default_stream();
    let a: Vec<f32> = (0..N).map(|i| i as f32).collect();
    let b: Vec<f32> = (0..N).map(|i| (2 * i) as f32).collect();
    let a_device = DeviceBuffer::from_host(&stream, &a)?;
    let b_device = DeviceBuffer::from_host(&stream, &b)?;
    let mut result_device = DeviceBuffer::<f32>::zeroed(&stream, N)?;

    // SAFETY: this package owns the device bundle generated for `kernels`.
    let module = unsafe { kernels::load(&context)? };
    let launch = module.prepare_vecadd(LaunchConfig1D::new(
        (N as u32).div_ceil(BLOCK_SIZE),
        BLOCK_SIZE,
        0,
    ))?;
    module.vecadd(&stream, &launch, &a_device, &b_device, &mut result_device)?;
    let result = result_device.to_host_vec(&stream)?;

    for (i, &value) in result.iter().enumerate() {
        assert_eq!(value, a[i] + b[i], "incorrect result at index {i}");
    }
    println!("PASSED: all {N} elements correct");
    Ok(())
}
