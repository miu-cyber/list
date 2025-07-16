import pandas as pd
import os

# 文件夹路径，包含待处理的CSV文件
folder_path = '/Users/margolee/Desktop/Participants'  # 请替换为实际的文件夹路径
output_file = '最终合并结果.csv'  # 合并后的输出文件名

# 创建一个空的DataFrame，用于存储合并后的数据
all_data = pd.DataFrame(columns=["Email", "Name（Original Name）", "来源文件"])

# 遍历文件夹中的所有CSV文件
for file in os.listdir(folder_path):
    # 检查文件是否为CSV文件
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)
        
        # 读取当前CSV文件
        df = pd.read_csv(file_path)
        
        # 修改列名（如果列存在的话）
        if 'User Email' in df.columns:
            df = df.rename(columns={'User Email': 'Email'})
        if 'Name（original name）' in df.columns:
            df = df.rename(columns={'Name（original name）': 'Name（Original Name）'})

        # 检查是否包含所需列，提取并添加“来源文件”列
        if 'Email' in df.columns and 'Name（Original Name）' in df.columns:
            df_subset = df[['Email', 'Name（Original Name）']].copy()
            df_subset['来源文件'] = file
            all_data = pd.concat([all_data, df_subset], ignore_index=True)
        else:
            # 如果文件不包含所需的列，则跳过
            print(f"文件 {file} 缺少 'Email' 或 'Name（Original Name）' 列，已跳过。")

# 将合并后的数据保存为新的CSV文件
all_data.to_csv(output_file, index=False)

print(f"文件合并完成，保存至 {output_file}")


