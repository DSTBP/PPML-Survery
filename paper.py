import os
import re
from collections import OrderedDict

# ===================== 配置信息 =====================
# 论文目录路径（请确保路径正确）
PDF_DIR = r"C:\Users\Lenovo\Desktop\12\12"
# 原始论文数据
paper_data = [
    "HE-Booster: An Efficient Polynomial Arithmetic Acceleration on GPUs for Fully Homomorphic Encryption\tTPDS\t2023",
    "SAL-ViT: Towards Latency Efficient Private Inference on ViT using Selective Attention Search with a Learnable Softmax Approximation\tICCV\t2023",
    "Accelerating Encrypted Computing on Intel GPUs\tIPDPS\t2022",
    "GPU Acceleration for FHEW/TFHE Bootstrapping\tTCHES\t2025",
    "ELASM: Error-Latency-Aware Scale Management for Fully Homomorphic Encryption\tUSENIX Security\t2023",
    "HECATE: Performance-Aware Scale Optimization for Homomorphic Encryption Compiler\tCGO\t2022",
    "Hunter: HE-Friendly Structured Pruning for Efficient Privacy-Preserving Deep Learning\tASIA CCS\t2022",
    "Athena: Accelerating KeySwitch and Bootstrapping for Fully Homomorphic Encryption on CUDA GPU\tESORCIS\t2025",
    "CipherPrune: Efficient and Scalable Private Transformer Inference\tICLR\t2025",
    "ReSBM: Region-based Scale and Minimal-Level Bootstrapping Management for FHE via Min-Cut\tASPLOS\t2025",
    "Securing Neural Networks with Knapsack Optimization\tarXiv\t2023",
    "LLMs Can Understand Encrypted Prompt: Towards Privacy-Computing Friendly Transformers\tarXiv\t2023",
    "Antelope: Fast and Secure Neural Network Inference\tTDSC\t2025",
    "Cheddar: A Swift Fully Homomorphic Encryption  Library Designed for GPU Architectures\tASPLOS\t2025",
    "Accelerating Fully Homomorphic Encryption Through Architecture-Centric Analysis and Optimization\tIEEE Access\t2021",
    "Over 100x Faster Bootstrapping in Fully Homomorphic Encryption through Memory-centric Optimization with GPUs\tTCHES\t2021",
    "MPCache: MPC-Friendly KV Cache Eviction for Efficient Private Large Language Model Inference\tarXiv\t2025",
    "EQO: Exploring Ultra-Efficient Private Inference with Winograd-Based Protocol and Quantization Co-Optimization\tarXiv\t2024",
    "EQO: Exploring Ultra-Efficient Private Inference with Winograd-Based Protocol and Quantization Co-Optimization\tarXiv\t2024",
    "EQO: Exploring Ultra-Efficient Private Inference with Winograd-Based Protocol and Quantization Co-Optimization\tarXiv\t2024",
    "MPCViT: Searching for Accurate and Efficient MPC-Friendly Vision Transformer with Heterogeneous Attention\tICCV\t2023",
    "MPCViT: Searching for Accurate and Efficient MPC-Friendly Vision Transformer with Heterogeneous Attention\tICCV\t2023",
    "MPCViT: Searching for Accurate and Efficient MPC-Friendly Vision Transformer with Heterogeneous Attention\tICCV\t2023",
    "CoPriv: Network/Protocol Co-Optimization for Communication-Efficient Private Inference\tNeurIPS\t2023",
    "CoPriv: Network/Protocol Co-Optimization for Communication-Efficient Private Inference\tNeurIPS\t2023",
    "CoPriv: Network/Protocol Co-Optimization for Communication-Efficient Private Inference\tNeurIPS\t2023",
    "Bumblebee: Secure two-party inference framework for large transformers\tNDSS\t2025",
    "Efficient ML Models for Practical Secure Inference\tarXiv\t2022",
    "THE-X: Privacy-Preserving Transformer Inference with Homomorphic Encryption\tACL\t2022",
    "THE-X: Privacy-Preserving Transformer Inference with Homomorphic Encryption\tACL\t2022",
    "Breaking the layer barrier: Remodeling private Transformer inference with hybrid CKKS and MPC\tUSENIX Security\t2025",
    "Breaking the layer barrier: Remodeling private Transformer inference with hybrid CKKS and MPC\tUSENIX Security\t2025",
    "PrivQuant: Communication-Efficient Private Inference with Quantized Network/Protocol Co-Optimization\tICCAD\t2024",
    "PrivQuant: Communication-Efficient Private Inference with Quantized Network/Protocol Co-Optimization\tICCAD\t2024",
    "Falcon: Accelerating homomorphically encrypted convolutions for efficient private mobile network inference\tICCAD\t2023",
    "PrivCirNet: Efficient Private Inference via Block Circulant Transformation\tNeurIPS\t2024",
    "PrivCirNet: Efficient Private Inference via Block Circulant Transformation\tNeurIPS\t2024",
    "PrivCirNet: Efficient Private Inference via Block Circulant Transformation\tNeurIPS\t2024",
    "Privacy-Preserving Inference for Quantized BERT Models\tarXiv\t2025",
    "Privacy-Preserving Inference for Quantized BERT Models\tarXiv\t2025",
    "Learning to Linearize Deep Neural Networks for Secure and Efficient Private Inference\tICLR\t2023",
    "MLFormer: a high performance MPC linear inference framework for transformers\tJournal of Cryptographic Engineering\t2025",
    "A General Purpose Transpiler for Fully Homomorphic Encryption\tArXiv\t2021",
    "VeloFHE: GPU Acceleration for FHEW and TFHE Bootstrapping\tTCHES\t2025",
    "CARM: CUDA-Accelerated RNS Multiplication in Word-Wise Homomorphic Encryption Schemes for Internet of Things\tTC\t2022",
    "GPU Acceleration of High-Precision Homomorphic Computation Utilizing Redundant Representation\tWAHC\t2023",
    "TensorFHE: Achieving Practical Computation on Encrypted Data Using GPGPU\tHPCA\t2023",
    "HALO: Loop-aware Bootstrapping Management for Fully Homomorphic Encryption\tASPLOS\t2025",
    "DaCapo: Automatic Bootstrapping Management for Efficient Fully Homomorphic Encryption\tUSENIX Security\t2024",
    "EVA: An Encrypted Vector Arithmetic Language and Compiler for Efficient Homomorphic Computation\tPLDI\t2020",
    "Coyote: A Compiler for Vectorizing Encrypted Arithmetic Circuits\tASPLOS\t2023",
    "CAT: A GPU-Accelerated FHE Framework with Its Application to High-Precision Private Dataset Query\tarXiv\t2025",
    "PRIVIT: VISION TRANSFORMERS FOR FAST PRIVATE INFERENCE\tarXiv\t2023",
    "PRIVIT: VISION TRANSFORMERS FOR FAST PRIVATE INFERENCE\tarXiv\t2023",
    "DeepReShape: Redesigning Neural Networks for Efficient Private Inference\tTMLR\t2024",
    "AERO: Softmax-Only LLMs for Efficient Private Inference\tarXiv\t2024",
    "AERO: Softmax-Only LLMs for Efficient Private Inference\tarXiv\t2024",
    "Secure human action recognition by encrypted neural network inference\tNature Communications\t2022",
    "Selective Network Linearization for Efficient Private Inference\tICML\t2022",
    "Porcupine: A Synthesizing Compiler for Vectorized Homomorphic Encryption\tPLDI\t2021"
]

def clean_filename(filename):
    """
    清理文件名中的非法字符
    """
    # Windows系统非法字符
    illegal_chars = r'[\/:*?"<>|]'
    # 替换为空格
    cleaned = re.sub(illegal_chars, ' ', filename)
    # 去除多余空格
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def process_papers():
    """
    处理论文数据：去重并结构化
    """
    # 使用OrderedDict去重并保持顺序
    unique_papers = OrderedDict()
    
    for paper in paper_data:
        # 按制表符分割
        parts = paper.strip().split('\t')
        if len(parts) == 3:
            title, venue, year = parts
            # 作为唯一键去重
            key = f"{title}_{venue}_{year}"
            if key not in unique_papers:
                unique_papers[key] = {
                    'title': title,
                    'venue': venue,
                    'year': year
                }
    
    # 转换为列表
    result = list(unique_papers.values())
    print(f"去重后论文总数：{len(result)}")
    return result

def rename_pdf_files():
    """
    重命名PDF文件
    """
    # 处理论文数据
    papers = process_papers()
    
    # 检查目录是否存在
    if not os.path.exists(PDF_DIR):
        print(f"错误：目录不存在 - {PDF_DIR}")
        return
    
    # 检查论文数量和文件数量是否匹配
    pdf_count = 46  # 2.pdf到47.pdf共46个文件
    if len(papers) != pdf_count:
        print(f"警告：去重后论文数量({len(papers)})与PDF文件数量({pdf_count})不匹配！")
        # 确认是否继续
        confirm = input("是否继续执行重命名？(y/n): ")
        if confirm.lower() != 'y':
            return
    
    # 遍历论文列表，对应2.pdf到47.pdf
    success_count = 0
    fail_count = 0
    
    for idx, paper in enumerate(papers):
        # 计算对应的PDF文件名（从2开始）
        pdf_num = idx + 2
        old_filename = os.path.join(PDF_DIR, f"{pdf_num}.pdf")
        
        # 检查文件是否存在
        if not os.path.exists(old_filename):
            print(f"跳过：文件不存在 - {old_filename}")
            fail_count += 1
            continue
        
        # 构建新文件名
        title = clean_filename(paper['title'])
        venue = paper['venue']
        year = paper['year']
        
        new_filename = f"[{year}]_[{venue}]_{title}.pdf"
        new_filepath = os.path.join(PDF_DIR, new_filename)
        
        # 处理重复的新文件名
        counter = 1
        temp_new_filepath = new_filepath
        while os.path.exists(temp_new_filepath):
            # 如果目标文件已存在，添加编号
            name, ext = os.path.splitext(new_filename)
            temp_new_filepath = os.path.join(PDF_DIR, f"{name}_{counter}{ext}")
            counter += 1
        
        try:
            # 重命名文件
            os.rename(old_filename, temp_new_filepath)
            print(f"成功：{old_filename} -> {os.path.basename(temp_new_filepath)}")
            success_count += 1
        except Exception as e:
            print(f"失败：{old_filename} - 错误：{str(e)}")
            fail_count += 1
    
    # 输出统计信息
    print("\n=== 重命名结果 ===")
    print(f"成功：{success_count} 个文件")
    print(f"失败：{fail_count} 个文件")

if __name__ == "__main__":
    print("开始执行PDF重命名脚本...")
    print(f"目标目录：{PDF_DIR}")
    print("-" * 50)
    
    # 执行重命名
    rename_pdf_files()
    
    print("-" * 50)
    print("脚本执行完成！")