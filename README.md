# Final-Project-Part-1-Optimization-Technique-and-Implementation-Project-Report

## Project Overview
This project demonstrates the performance impact of transforming data from an Array of Structures (AoS) layout to a Structure of Arrays (SoA) layout in a high-performance computing context. It targets the enhancement of the memory access pattern, usage of caches, as well as the possibility to introduce vectorization to data-intensive operations. The implementation time measures the difference between two layouts by a huge set of numeric sets that indicate coordinates.

## Optimization Technique
The chosen optimization technique is the Structure of Arrays (SoA) layout transformation. It groups all attributes in a data entity into separate contiguous arrays, which allows sequential access to memory easily and minimal use of SIMD instructions. Such an approach is justified through the empirical analysis of bugs in HPC performance and can be considered common and effective optimization in relation to heavy-compute workloads.

## Requirements
It needs Python 3.x and the libraries NumPy and Matplotlib to execute. Such dependencies support effective work with arrays and their performance representation.

## Execution Instructions
The program loads large selection of data, performs summation in AoS and SoA layouts, and logs the execution time. A bar chart that compared the results of performances is created, as well as a formal diagram that visually showed the difference the two layouts had to organize the data.

## Expected Output
The result consists of a printed comparison of execution times of the two layouts, a comparison of performance table, and an AoS vs. SoA schematic diagram. The results should demonstrate decreased execution time of SoA layout because of optimised memory access patterns and increased potential of vectors.
