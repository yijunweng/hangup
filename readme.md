### 使用 `pipreqs` 生成 `requirements.txt`

`pipreqs` 是一个可以自动生成 `requirements.txt` 文件的工具。它会扫描项目目录并生成一个包含所有导入包的 `requirements.txt` 文件：

1. 安装 `pipreqs`：

    ```sh
    pip install pipreqs
    ```

2. 生成 `requirements.txt` 文件：

    ```sh
    pipreqs /path/to/your/project
    ```

3. 安装依赖：

    ```sh
    pip install -r requirements.txt
    ```