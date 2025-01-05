import pandas as pd

def check_col(file_path, col_name):
    """
    检查文件中指定列是否唯一，是否有空值
    :param file_path: 文件路径
    :param col_name: 列名
    :return: 字典，包含是否有空值和是否唯一
    """
    try:
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
