@echo off
chcp 65001 >nul
echo ====================================
echo       PDF文件分割工具
echo ====================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未找到Python，请先安装Python
    pause
    exit /b 1
)

REM 检查PyPDF2是否安装
python -c "import PyPDF2" >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装PyPDF2...
    pip install PyPDF2
    if %errorlevel% neq 0 (
        echo 错误：PyPDF2安装失败
        pause
        exit /b 1
    )
)

echo 可用的PDF文件：
echo.
dir /b big\*.pdf 2>nul
if %errorlevel% neq 0 (
    echo 在big目录中未找到PDF文件
)
echo.

REM 分割【CRCC】盾构机操作手培训教材.pdf
if exist "big\【CRCC】盾构机操作手培训教材.pdf" (
    echo 正在分割：【CRCC】盾构机操作手培训教材.pdf
    python pdf_splitter.py "big\【CRCC】盾构机操作手培训教材.pdf" "big_output\【CRCC】盾构机操作手培训教材5-（过程稿-接收所有修订）20170724(2)" 50
    echo.
)

REM 分割盾构施工标准化手册.pdf
if exist "big\盾构施工标准化手册.pdf" (
    echo 正在分割：盾构施工标准化手册.pdf
    python pdf_splitter.py "big\盾构施工标准化手册.pdf" "big_output\附件：2" 30
    echo.
)

echo ====================================
echo 所有PDF文件分割完成！
echo 输出目录：big_output
echo ====================================
pause