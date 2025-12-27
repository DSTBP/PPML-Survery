import os
import re
from collections import OrderedDict

# ===================== 配置信息 =====================
# 论文目录路径（请确保路径正确）
PDF_DIR = r"C:\Users\r0xanne\Downloads"
# 论文数据文本文件路径
PAPER_FILE_PATH = r"C:\Users\r0xanne\Desktop\1.txt"

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

def read_paper_data_from_file(file_path):
    """
    从文本文件读取论文数据
    """
    if not os.path.exists(file_path):
        print(f"错误：论文数据文件不存在 - {file_path}")
        return []
    
    paper_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                # 跳过空行和注释行
                if not line or line.startswith('//') or line.startswith('#'):
                    continue
                paper_data.append(line)
        
        print(f"从文件成功读取 {len(paper_data)} 条论文记录")
        return paper_data
    except Exception as e:
        print(f"错误：读取论文数据文件失败 - {str(e)}")
        return []

def process_papers():
    """
    处理论文数据：读取文件、去重并结构化
    """
    # 从文件读取原始论文数据
    raw_papers = read_paper_data_from_file(PAPER_FILE_PATH)
    if not raw_papers:
        return []
    
    # 使用OrderedDict去重并保持顺序
    unique_papers = OrderedDict()
    
    for paper in raw_papers:
        # 按制表符分割
        parts = paper.strip().split('\t')
        if len(parts) == 3:
            title, venue, year = parts
            # 作为唯一键去重（避免标题相同但会议/年份不同的论文被误判）
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
    重命名PDF文件（匹配1.pdf到164.pdf）
    """
    # 处理论文数据（读取+去重）
    papers = process_papers()
    if not papers:
        print("没有可用的论文数据，无法执行重命名")
        return
    
    # 检查目录是否存在
    if not os.path.exists(PDF_DIR):
        print(f"错误：目录不存在 - {PDF_DIR}")
        return
    
    # 配置PDF文件范围：1.pdf到164.pdf（共164个文件）
    pdf_start = 1
    pdf_end = 164
    expected_pdf_count = pdf_end - pdf_start + 1  # 164个文件
    
    # 检查论文数量和预期PDF文件数量是否匹配
    if len(papers) != expected_pdf_count:
        print(f"警告：去重后论文数量({len(papers)})与预期PDF文件数量({expected_pdf_count})不匹配！")
        print(f"预期匹配：{pdf_start}.pdf 到 {pdf_end}.pdf")
        # 确认是否继续
        confirm = input("是否继续执行重命名？(y/n): ")
        if confirm.lower() != 'y':
            return
    
    # 遍历论文列表，对应1.pdf到164.pdf
    success_count = 0
    fail_count = 0
    
    for idx, paper in enumerate(papers):
        # 计算对应的PDF文件名（从1开始）
        pdf_num = pdf_start + idx  # 1,2,...,164
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
        
        # 处理重复的新文件名（避免覆盖已存在的文件）
        counter = 1
        temp_new_filepath = new_filepath
        while os.path.exists(temp_new_filepath):
            # 如果目标文件已存在，添加编号后缀
            name, ext = os.path.splitext(new_filename)
            temp_new_filepath = os.path.join(PDF_DIR, f"{name}_{counter}{ext}")
            counter += 1
        
        try:
            # 重命名文件
            os.rename(old_filename, temp_new_filepath)
            print(f"成功：{os.path.basename(old_filename)} -> {os.path.basename(temp_new_filepath)}")
            success_count += 1
        except Exception as e:
            print(f"失败：{os.path.basename(old_filename)} - 错误：{str(e)}")
            fail_count += 1
    
    # 输出统计信息
    print("\n=== 重命名结果 ===")
    print(f"目标PDF范围：{pdf_start}.pdf 到 {pdf_end}.pdf")
    print(f"成功：{success_count} 个文件")
    print(f"失败：{fail_count} 个文件")

if __name__ == "__main__":
    print("开始执行PDF重命名脚本...")
    print(f"目标PDF目录：{PDF_DIR}")
    print(f"论文数据文件：{PAPER_FILE_PATH}")
    print(f"目标PDF范围：1.pdf 到 164.pdf（共164个文件）")
    print("-" * 60)
    
    # 执行重命名
    rename_pdf_files()
    
    print("-" * 60)
    print("脚本执行完成！")