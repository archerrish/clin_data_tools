import pandas as pd
import argparse

def check_col(file_path, col_name):
    """
    检查文件中指定列是否唯一，是否有空值
    :param file_path: 文件路径
    :param col_name: 列名
    :return: 字典，包含是否有空值和是否唯一
    """
    try:
        file_path = str(file_path)  # Convert LocalPath to string
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

        if col_name not in df.columns:
            raise KeyError(f"Column '{col_name}' does not exist in the file.")

        return {
            "missing_values": df[col_name].isnull().any(),
            "duplicates": not df[col_name].is_unique
        }

    except Exception as e:
        raise RuntimeError(f"Error in check_col: {e}")

def main():
    """
    命令行入口函数，解析参数并调用 check_col
    """
    parser = argparse.ArgumentParser(description="Check a column in a file for missing values and uniqueness.")
    parser.add_argument("file_path", help="Path to the input file (CSV or Excel).")
    parser.add_argument("col_name", help="Name of the column to check.")
    args = parser.parse_args()

    try:
        result = check_col(args.file_path, args.col_name)
        print(f"Column '{args.col_name}' in file '{args.file_path}':")
        print(f"  - Missing values: {result['missing_values']}")
        print(f"  - Duplicates: {result['duplicates']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
