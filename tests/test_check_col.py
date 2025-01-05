import pytest
from clin_data_tools.check_col import check_col
import pandas as pd
from io import StringIO

def test_check_col(tmpdir):
    # 准备测试数据
    csv_data = StringIO("""id,name,age
    1,Alice,30
    2,Bob,25
    3,Charlie,35
    4,,40
    5,Alice,30
    """)
    df = pd.read_csv(csv_data)
    
    # 使用 tmpdir 创建临时文件
    temp_csv = tmpdir.join("test.csv")
    df.to_csv(temp_csv, index=False)

    # 测试列 'name'
    result = check_col(temp_csv, "name")
    assert result["missing_values"] == True
    assert result["duplicates"] == True

    # 测试列 'id'
    result = check_col(temp_csv, "id")
    assert result["missing_values"] == False
    assert result["duplicates"] == False
