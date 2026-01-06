# 隐私保护机器学习综述

[English](README.md) | 简体中文

一个关于隐私保护机器学习（PPML）技术的综合性研究论文集合，重点关注基于密码学的方法，包括安全多方计算（MPC）、同态加密（HE）和混合协议。

## 概述

本仓库包含从2015年到2025年的精选学术论文集合，涵盖隐私保护机器学习领域的最新进展。论文组织在两个主要目录中：

- **Paper/**：特定PPML技术和框架的研究论文（180+篇）
- **Survery/**：提供该领域系统性综述的重要综述论文

## 研究领域

### 1. 安全多方计算（MPC）
关于神经网络推理和训练的安全计算协议的论文：
- 两方计算框架（ABY、ABY2.0、ABY3）
- 三方计算协议（SecureNN、Falcon、SWIFT）
- 混合协议框架（Chameleon、Motion、CrypTFlow）
- 基于函数秘密共享（FSS）的方法（AriaNN、Pika、Sigma）

### 2. 同态加密（HE）
关于深度学习加密计算的研究：
- 全同态加密（FHE）框架（SEAL、TFHE、CKKS）
- HE编译器和优化器（CHET、EVA、HECO、Porcupine）
- HE的GPU加速（TensorFHE、Phantom、HE-Booster）
- 自举优化（DaCapo、HALO、ELASM）

### 3. 混合方法
结合MPC和HE以获得最佳性能：
- DELPHI、Cheetah、Bolt（HE + 混淆电路）
- GAZELLE、CrypTFlow2（混合协议）
- Piranha、Orca（GPU加速混合系统）

### 4. 面向隐私的模型优化
为高效隐私推理设计的神经架构：
- 激活函数近似（多项式、ReLU约简）
- 神经架构搜索（NASS、CryptoNAS、AutoPrivacy）
- 模型压缩和量化
- 用于隐私推理的视觉Transformer（MPCViT、SAL-ViT、PRIVIT）

### 5. 大语言模型（LLMs）
Transformer隐私推理的最新进展：
- 安全Transformer推理（Iron、MPCFormer、SecFormer）
- 隐私LLM推理（Puma、CipherGPT、Sigma）
- 注意力机制优化（THE-X、Powerformer）

## 重要综述论文

`Survery/`目录包含三篇综合性综述论文：

1. **[2023] SoK: Cryptographic Neural-Network Computation**（IEEE S&P）
   - 密码学神经网络计算的知识系统化
   - MPC和HE方法的全面分析

2. **[2025] Privacy-Preserving Machine Learning Based on Cryptography: A Survey**（TKDD）
   - 涵盖密码学PPML技术的最新综述
   - 详细的方法分类和比较

3. **[2025] Towards Efficient Privacy-Preserving Machine Learning**（arXiv）
   - 从协议、模型和系统角度的系统性综述
   - 关注效率优化策略

## 主要贡献时间线

### 2015-2017：基础阶段
- **ABY**（NDSS 2015）：两方计算的混合协议框架
- **CryptoNets**（ICML 2016）：首个实用的基于HE的神经网络
- **MiniONN**（CCS 2017）：不经意神经网络预测
- **SecureML**（IEEE S&P 2017）：可扩展的隐私保护机器学习

### 2018-2019：框架发展
- **GAZELLE**（USENIX Security 2018）：低延迟安全推理
- **ABY3**（CCS 2018）：三方计算框架
- **CHET**（PLDI 2019）：HE优化编译器
- **SecureNN**（PoPETs 2019）：三方安全神经网络训练

### 2020-2021：性能优化
- **CrypTFlow2**（CCS 2020）：实用的两方安全推理
- **DELPHI**（USENIX Security 2020）：密码学推理服务
- **EVA**（PLDI 2020）：加密向量算术编译器
- **CryptGPU**（IEEE S&P 2021）：GPU加速的隐私机器学习
- **Porcupine**（PLDI 2021）：向量化HE编译器

### 2022-2023：模型协同设计
- **Cheetah**（USENIX Security 2022）：精简快速的两方计算推理
- **Iron**（NeurIPS 2022）：隐私Transformer推理
- **MPCFormer**（ICLR 2023）：基于MPC的快速隐私Transformer
- **HECO**（USENIX Security 2023）：FHE编译器框架

### 2024-2025：大模型时代
- **Bolt**（IEEE S&P 2024）：隐私Transformer推理
- **Puma**（arXiv 2024）：5分钟内完成安全LLaMA-7B推理
- **Orion**（ASPLOS 2025）：深度学习的FHE框架
- **Cheddar**（ASPLOS 2025）：面向GPU的快速FHE库

## 仓库结构

```
PPML-Survery/
├── Paper/                  # 180+篇研究论文（2015-2025）
│   ├── [年份]_[会议]_[标题].pdf
│   └── ...
├── Survery/               # 重要综述论文
│   ├── [2023]_[IEEE S&P]_SoK Cryptographic Neural-Network Computation.pdf
│   ├── [2025]_[TKDD]_Privacy-Preserving Machine Learning Based on Cryptography A Survey.pdf
│   └── [2025]_[arVix]_Towards Efficient Privacy-Preserving Machine Learning.pdf
├── Survery5.xlsx          # 论文组织和元数据
├── LICENSE                # MIT许可证
└── README.md              # 英文说明文件
```

## 按会议分类的论文

### 顶级安全会议
- **IEEE S&P**（安全与隐私）：15+篇
- **USENIX Security**：20+篇
- **CCS**（计算机与通信安全）：15+篇
- **NDSS**（网络与分布式系统安全）：5+篇

### 机器学习会议
- **NeurIPS**：8+篇
- **ICML**：10+篇
- **ICLR**：5+篇

### 系统与架构会议
- **PLDI**（编程语言设计与实现）：8+篇
- **ASPLOS**（编程语言与操作系统的架构支持）：6+篇
- **MICRO**：2+篇
- **HPCA**：2+篇

### 隐私与应用密码学
- **PoPETs**（隐私增强技术）：10+篇
- **CSCML**（机器学习安全与密码学会议）：5+篇

### 期刊
- **IEEE TDSC**（可信与安全计算汇刊）：5+篇
- **IEEE TIFS**（信息取证与安全汇刊）：5+篇
- **IEEE Access**：5+篇

## 关键技术方法

### 安全多方计算（MPC）
MPC使多方能够在保持输入隐私的情况下联合计算函数。

**协议：**
- **混淆电路**：低轮复杂度的布尔电路评估
- **秘密共享**：高吞吐量的算术运算
- **不经意传输**：许多两方计算协议的基础

**关键框架：**
- ABY、ABY2.0、ABY3：混合协议框架
- CrypTFlow、CrypTFlow2：自动化协议生成
- Motion、MP-SPDZ：通用MPC平台

### 同态加密（HE）
HE允许在不解密的情况下对加密数据进行计算。

**方案：**
- **BFV/BGV**：整数算术，适用于CNN
- **CKKS**：近似算术，高效的浮点运算
- **TFHE**：快速自举，适用于深度电路

**关键编译器：**
- CHET、EVA、HECO：领域特定的HE编译器
- Porcupine、Coyote：向量化和优化
- ELASM、DaCapo、HALO：自举管理

**GPU加速：**
- TensorFHE、Cheddar、Phantom：GPU加速的HE库
- HE-Booster、CARM：HE的硬件优化

### 混合协议
结合MPC和HE以获得最佳性能：
- **线性层**：使用HE进行矩阵乘法
- **非线性层**：使用混淆电路或秘密共享处理ReLU/softmax
- **示例**：DELPHI、GAZELLE、Cheetah、Bolt

## 应用场景

### 神经网络推理
- **CNN**：图像分类、目标检测
- **RNN**：语音识别、时间序列分析
- **Transformer**：自然语言处理任务、LLM推理
- **视觉Transformer**：基于注意力机制的图像理解

### 神经网络训练
- 安全梯度下降和反向传播
- 具有隐私保证的联邦学习
- 多方协作训练

### 其他机器学习任务
- **聚类**：k-means、DBSCAN
- **决策树**：隐私树评估
- **线性模型**：逻辑回归、SVM
- **图神经网络**：安全GNN推理

## 性能指标

评估PPML系统时的关键指标包括：

- **延迟**：端到端推理/训练时间
- **通信**：各方之间交换的数据量
- **计算**：所需的CPU/GPU周期
- **准确性**：模型准确性保持
- **安全性**：威胁模型和安全保证

## 研究趋势

### 早期阶段（2015-2018）
- 建立密码学机器学习的可行性
- 两方和三方计算的基础框架
- 初步的基于HE的神经网络

### 成长阶段（2019-2021）
- 混合协议优化
- 编译器和自动化工具
- HE的GPU加速
- 神经架构协同设计

### 成熟阶段（2022-2023）
- Transformer和注意力机制
- HE的自举优化
- 量化感知的安全推理
- 用于隐私推理的视觉Transformer

### 当前焦点（2024-2025）
- 大语言模型（LLM）推理
- 高效的注意力近似
- 软硬件协同设计
- 实际部署和可扩展性

## 入门指南

### 对于研究人员
1. 从`Survery/`目录中的综述论文开始
2. 探索基础论文（2015-2018）以理解基本概念
3. 查看最新论文（2023-2025）了解最先进的技术
4. 查看`Survery5.xlsx`获取有组织的论文元数据

### 推荐阅读路径

**入门级：**
- [2023] SoK: Cryptographic Neural-Network Computation（IEEE S&P）
- [2016] CryptoNets（ICML）
- [2017] SecureML（IEEE S&P）
- [2018] GAZELLE（USENIX Security）

**中级（MPC方向）：**
- [2015] ABY（NDSS）
- [2020] CrypTFlow2（CCS）
- [2021] ABY2.0（USENIX Security）
- [2022] Cheetah（USENIX Security）

**中级（HE方向）：**
- [2019] CHET（PLDI）
- [2020] EVA（PLDI）
- [2021] Porcupine（PLDI）
- [2023] HECO（USENIX Security）

**高级（Transformer与LLM）：**
- [2022] Iron（NeurIPS）
- [2023] MPCFormer（ICLR）
- [2024] Bolt（IEEE S&P）
- [2024] Puma（arXiv）

## 贡献

这是一个精选的研究论文集合。欢迎贡献：

1. Fork本仓库
2. 按照命名规范添加新论文：`[年份]_[会议]_[标题].pdf`
3. 更新`Survery5.xlsx`中的论文元数据
4. 提交Pull Request

## 相关资源

### 开源框架
- **Microsoft SEAL**：C++的HE库
- **OpenFHE**：开源FHE库
- **MP-SPDZ**：通用MPC框架
- **CrypTen**：基于PyTorch的安全机器学习框架
- **TenSEAL**：用于张量HE的Python库

### 研究团队
- **Microsoft Research**：CrypTFlow、SEAL、EVA
- **Meta AI**：CrypTen
- **UC Berkeley**：DELPHI、Piranha
- **CMU**：ABY框架系列
- **ETH Zurich**：MP-SPDZ

## 引用

如果您觉得这个论文集合对您的研究有用，请考虑引用综述论文：

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

## 许可证

本仓库采用MIT许可证 - 详见[LICENSE](LICENSE)文件。

## 致谢

本论文集合用于研究和教育目的。所有论文的版权归各自作者和出版商所有。

## 联系方式

如有问题、建议或贡献，请在GitHub上提交Issue。

---

**最后更新**：2026年1月
**论文总数**：180+篇
**覆盖年份**：2015-2025
