# Privacy-Preserving Machine Learning Survey

English | [简体中文](README_CH.md)

A comprehensive collection of research papers on Privacy-Preserving Machine Learning (PPML) techniques, focusing on cryptographic approaches including Secure Multi-Party Computation (MPC), Homomorphic Encryption (HE), and hybrid protocols.

## Overview

This repository contains a curated collection of academic papers spanning from 2015 to 2025, covering the latest advances in privacy-preserving machine learning. The papers are organized into two main directories:

- **Paper/**: Research papers on specific PPML techniques and frameworks (180+ papers)
- **Survery/**: Comprehensive survey papers providing systematic reviews of the field

## Research Areas

### 1. Secure Multi-Party Computation (MPC)
Papers on secure computation protocols for neural network inference and training:
- Two-party computation frameworks (ABY, ABY2.0, ABY3)
- Three-party computation protocols (SecureNN, Falcon, SWIFT)
- Mixed-protocol frameworks (Chameleon, Motion, CrypTFlow)
- Function Secret Sharing (FSS) based approaches (AriaNN, Pika, Sigma)

### 2. Homomorphic Encryption (HE)
Research on encrypted computation for deep learning:
- Fully Homomorphic Encryption (FHE) frameworks (SEAL, TFHE, CKKS)
- HE compilers and optimizers (CHET, EVA, HECO, Porcupine)
- GPU acceleration for HE (TensorFHE, Phantom, HE-Booster)
- Bootstrapping optimization (DaCapo, HALO, ELASM)

### 3. Hybrid Approaches
Combining MPC and HE for optimal performance:
- DELPHI, Cheetah, Bolt (HE + Garbled Circuits)
- GAZELLE, CrypTFlow2 (Mixed protocols)
- Piranha, Orca (GPU-accelerated hybrid systems)

### 4. Model Optimization for Privacy
Neural architecture design for efficient private inference:
- Activation function approximation (polynomial, ReLU reduction)
- Network architecture search (NASS, CryptoNAS, AutoPrivacy)
- Model compression and quantization
- Vision Transformers for private inference (MPCViT, SAL-ViT, PRIVIT)

### 5. Large Language Models (LLMs)
Recent advances in private inference for transformers:
- Secure transformer inference (Iron, MPCFormer, SecFormer)
- Private LLM inference (Puma, CipherGPT, Sigma)
- Attention mechanism optimization (THE-X, Powerformer)

## Key Survey Papers

The `Survery/` directory contains three comprehensive survey papers:

1. **[2023] SoK: Cryptographic Neural-Network Computation** (IEEE S&P)
   - Systematization of Knowledge on cryptographic NN computation
   - Comprehensive analysis of MPC and HE approaches

2. **[2025] Privacy-Preserving Machine Learning Based on Cryptography: A Survey** (TKDD)
   - Latest survey covering cryptographic PPML techniques
   - Detailed taxonomy and comparison of methods

3. **[2025] Towards Efficient Privacy-Preserving Machine Learning** (arXiv)
   - Systematic review from protocol, model, and system perspectives
   - Focus on efficiency optimization strategies

## Timeline of Major Contributions

### 2015-2017: Foundations
- **ABY** (NDSS 2015): Mixed-protocol framework for 2PC
- **CryptoNets** (ICML 2016): First practical HE-based neural network
- **MiniONN** (CCS 2017): Oblivious neural network predictions
- **SecureML** (IEEE S&P 2017): Scalable privacy-preserving ML

### 2018-2019: Framework Development
- **GAZELLE** (USENIX Security 2018): Low-latency secure inference
- **ABY3** (CCS 2018): 3-party computation framework
- **CHET** (PLDI 2019): Optimizing compiler for HE
- **SecureNN** (PoPETs 2019): 3-party secure NN training

### 2020-2021: Performance Optimization
- **CrypTFlow2** (CCS 2020): Practical 2-party secure inference
- **DELPHI** (USENIX Security 2020): Cryptographic inference service
- **EVA** (PLDI 2020): Encrypted vector arithmetic compiler
- **CryptGPU** (IEEE S&P 2021): GPU-accelerated private ML
- **Porcupine** (PLDI 2021): Vectorized HE compiler

### 2022-2023: Model Co-Design
- **Cheetah** (USENIX Security 2022): Lean and fast 2PC inference
- **Iron** (NeurIPS 2022): Private transformer inference
- **MPCFormer** (ICLR 2023): Fast private transformer with MPC
- **HECO** (USENIX Security 2023): FHE compiler framework

### 2024-2025: LLM Era
- **Bolt** (IEEE S&P 2024): Private transformer inference
- **Puma** (arXiv 2024): Secure LLaMA-7B inference in 5 minutes
- **Orion** (ASPLOS 2025): FHE framework for deep learning
- **Cheddar** (ASPLOS 2025): Swift FHE library for GPUs

## Repository Structure

```
PPML-Survery/
├── Paper/                  # 180+ research papers (2015-2025)
│   ├── [Year]_[Venue]_[Title].pdf
│   └── ...
├── Survery/               # Key survey papers
│   ├── [2023]_[IEEE S&P]_SoK Cryptographic Neural-Network Computation.pdf
│   ├── [2025]_[TKDD]_Privacy-Preserving Machine Learning Based on Cryptography A Survey.pdf
│   └── [2025]_[arVix]_Towards Efficient Privacy-Preserving Machine Learning.pdf
├── Survery5.xlsx          # Paper organization and metadata
├── LICENSE                # MIT License
└── README.md              # This file
```

## Paper Categories by Venue

### Top-Tier Security Conferences
- **IEEE S&P** (Security and Privacy): 15+ papers
- **USENIX Security**: 20+ papers
- **CCS** (Computer and Communications Security): 15+ papers
- **NDSS** (Network and Distributed System Security): 5+ papers

### Machine Learning Conferences
- **NeurIPS**: 8+ papers
- **ICML**: 10+ papers
- **ICLR**: 5+ papers

### Systems and Architecture Conferences
- **PLDI** (Programming Language Design and Implementation): 8+ papers
- **ASPLOS** (Architectural Support for Programming Languages and Operating Systems): 6+ papers
- **MICRO**: 2+ papers
- **HPCA**: 2+ papers

### Privacy and Applied Cryptography
- **PoPETs** (Privacy Enhancing Technologies): 10+ papers
- **CSCML** (Conference on Security and Cryptography for Machine Learning): 5+ papers

### Journals
- **IEEE TDSC** (Transactions on Dependable and Secure Computing): 5+ papers
- **IEEE TIFS** (Transactions on Information Forensics and Security): 5+ papers
- **IEEE Access**: 5+ papers

## Key Technical Approaches

### Secure Multi-Party Computation (MPC)
MPC enables multiple parties to jointly compute a function over their inputs while keeping those inputs private.

**Protocols:**
- **Garbled Circuits**: Boolean circuit evaluation with low round complexity
- **Secret Sharing**: Arithmetic operations with high throughput
- **Oblivious Transfer**: Foundation for many 2PC protocols

**Key Frameworks:**
- ABY, ABY2.0, ABY3: Mixed-protocol frameworks
- CrypTFlow, CrypTFlow2: Automated protocol generation
- Motion, MP-SPDZ: General-purpose MPC platforms

### Homomorphic Encryption (HE)
HE allows computation on encrypted data without decryption.

**Schemes:**
- **BFV/BGV**: Integer arithmetic, suitable for CNNs
- **CKKS**: Approximate arithmetic, efficient for floating-point operations
- **TFHE**: Fast bootstrapping, suitable for deep circuits

**Key Compilers:**
- CHET, EVA, HECO: Domain-specific HE compilers
- Porcupine, Coyote: Vectorization and optimization
- ELASM, DaCapo, HALO: Bootstrapping management

**GPU Acceleration:**
- TensorFHE, Cheddar, Phantom: GPU-accelerated HE libraries
- HE-Booster, CARM: Hardware optimization for HE

### Hybrid Protocols
Combining MPC and HE for optimal performance:
- **Linear layers**: HE for matrix multiplication
- **Non-linear layers**: Garbled circuits or secret sharing for ReLU/softmax
- **Examples**: DELPHI, GAZELLE, Cheetah, Bolt

## Applications

### Neural Network Inference
- **CNNs**: Image classification, object detection
- **RNNs**: Speech recognition, time series analysis
- **Transformers**: NLP tasks, LLM inference
- **Vision Transformers**: Image understanding with attention mechanisms

### Neural Network Training
- Secure gradient descent and backpropagation
- Federated learning with privacy guarantees
- Multi-party collaborative training

### Other ML Tasks
- **Clustering**: k-means, DBSCAN
- **Decision Trees**: Private tree evaluation
- **Linear Models**: Logistic regression, SVM
- **Graph Neural Networks**: Secure GNN inference

## Performance Metrics

When evaluating PPML systems, key metrics include:

- **Latency**: End-to-end inference/training time
- **Communication**: Data exchanged between parties
- **Computation**: CPU/GPU cycles required
- **Accuracy**: Model accuracy preservation
- **Security**: Threat model and security guarantees

## Research Trends

### Early Years (2015-2018)
- Establishing feasibility of cryptographic ML
- Basic frameworks for 2PC and 3PC
- Initial HE-based neural networks

### Growth Phase (2019-2021)
- Mixed-protocol optimization
- Compiler and automation tools
- GPU acceleration for HE
- Neural architecture co-design

### Maturation (2022-2023)
- Transformer and attention mechanisms
- Bootstrapping optimization for HE
- Quantization-aware secure inference
- Vision Transformers for private inference

### Current Focus (2024-2025)
- Large Language Model (LLM) inference
- Efficient attention approximation
- Hardware-software co-design
- Practical deployment and scalability

## Getting Started

### For Researchers
1. Start with the survey papers in `Survery/` directory
2. Explore foundational papers (2015-2018) to understand basic concepts
3. Review recent papers (2023-2025) for state-of-the-art techniques
4. Check `Survery5.xlsx` for organized paper metadata

### Recommended Reading Path

**Beginners:**
- [2023] SoK: Cryptographic Neural-Network Computation (IEEE S&P)
- [2016] CryptoNets (ICML)
- [2017] SecureML (IEEE S&P)
- [2018] GAZELLE (USENIX Security)

**Intermediate (MPC Focus):**
- [2015] ABY (NDSS)
- [2020] CrypTFlow2 (CCS)
- [2021] ABY2.0 (USENIX Security)
- [2022] Cheetah (USENIX Security)

**Intermediate (HE Focus):**
- [2019] CHET (PLDI)
- [2020] EVA (PLDI)
- [2021] Porcupine (PLDI)
- [2023] HECO (USENIX Security)

**Advanced (Transformers & LLMs):**
- [2022] Iron (NeurIPS)
- [2023] MPCFormer (ICLR)
- [2024] Bolt (IEEE S&P)
- [2024] Puma (arXiv)

## Contributing

This is a curated collection of research papers. Contributions are welcome:

1. Fork the repository
2. Add new papers following the naming convention: `[Year]_[Venue]_[Title].pdf`
3. Update the paper metadata in `Survery5.xlsx`
4. Submit a pull request

## Related Resources

### Open-Source Frameworks
- **Microsoft SEAL**: HE library for C++
- **OpenFHE**: Open-source FHE library
- **MP-SPDZ**: General-purpose MPC framework
- **CrypTen**: PyTorch-based secure ML framework
- **TenSEAL**: Python library for HE on tensors

### Research Groups
- **Microsoft Research**: CrypTFlow, SEAL, EVA
- **Meta AI**: CrypTen
- **UC Berkeley**: DELPHI, Piranha
- **CMU**: ABY frameworks
- **ETH Zurich**: MP-SPDZ

## Citation

If you find this collection useful for your research, please consider citing the survey papers:

```bibtex
@inproceedings{sok2023cryptographic,
  title={SoK: Cryptographic Neural-Network Computation},
  booktitle={IEEE Symposium on Security and Privacy (S\&P)},
  year={2023}
}

@article{ppml2025survey,
  title={Privacy-Preserving Machine Learning Based on Cryptography: A Survey},
  journal={ACM Transactions on Knowledge Discovery from Data (TKDD)},
  year={2025}
}
```

## License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This collection is maintained for research and educational purposes. All papers are copyrighted by their respective authors and publishers.

## Contact

For questions, suggestions, or contributions, please open an issue on GitHub.

---

**Last Updated**: January 2026
**Total Papers**: 180+
**Coverage**: 2015-2025
