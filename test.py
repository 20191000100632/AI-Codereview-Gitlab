import pandas as pd
import json

def excel_to_jsonl(excel_path, jsonl_path):
    """
    将 Excel 文件转换为 JSONL 格式数据集
    :param excel_path: 输入的 Excel 文件路径
    :param jsonl_path: 输出的 JSONL 文件路径
    """
    # 读取 Excel 文件
    df = pd.read_excel(excel_path, usecols=[0, 1], header=None, names=["question", "answer"])

    # 检查数据是否为空
    if df.empty:
        raise ValueError("Excel 文件为空或未包含有效数据。")
    df = df.sample(frac=1).reset_index(drop=True)

    # 构造 JSONL 数据
    jsonl_data = []
    for _, row in df.iterrows():
        question = row["question"]
        answer = row["answer"]

        # 构造符合要求的 JSON 对象
        json_object = {
            "messages": [
                {"role": "system", "content": "你是多乐游戏的客服，请根据用户的问题提供准确的回答。"},
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer}
            ]
        }
        jsonl_data.append(json_object)

    # 写入 JSONL 文件
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for item in jsonl_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"JSONL 数据集已保存到 {jsonl_path}")

# 示例用法
if __name__ == "__main__":
    excel_to_jsonl("/opt/workspace/all.xlsx", "/opt/workspace/all_0.jsonl")
