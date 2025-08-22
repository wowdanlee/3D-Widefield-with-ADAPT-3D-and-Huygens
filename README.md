# 3D Widefield Imaging with ADAPT-3D and Huygens

A custom pipeline for rapid, large-volume 3D tissue imaging using a benchtop widefield microscopy combined with depth-variant deconvolution on [Huygens](https://svi.nl/Huygens-Widefield-Software) (Scientific Volume Imaging). Examples are demonstrated with the tissue preparation method called ADAPT-3D (link). Implements optimized prefiltering, PSF-based deconvolution, and Z-bricking to recover subnuclear resolution in thick, cleared tissues. Enables stitched, high-resolution volumetric analysis using accessible widefield systems.

This tool automates depth-aware 3D deconvolution on widefield-acquired microscopy stacks. Built around Scientific Volume Imaging’s Huygens software and leveraging Python scripting, it includes:

- Gaussian + local minimum background filtering
- Segmented Z-brick deconvolution
- Batch processing and stitching of large tiled volumes
- Compatible with 0.5 mm thick samples and high-NA long working distance objectives
- Achieves axial resolution of nuclei and subcellular features at 10x faster speed using standard widefield setups
  
This code accompanies the paper and pre-print, which can be viewed for more details:
