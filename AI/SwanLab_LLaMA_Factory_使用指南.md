# SwanLab + LLaMA-Factory 使用指南

## 概述

本指南将帮助您在 LLaMA-Factory 中集成 SwanLab 进行实验监控和可视化。

## 前提条件

1. **SwanLab 自托管服务已部署**
   - 访问地址：`http://192.168.211.110:8000`
   - 确保服务正常运行

2. **LLaMA-Factory 已安装**
   - 项目路径：`f:\JBGS\AI\LLaMA-Factory`

## 配置方法

### 方法一：修改现有配置文件

1. **选择配置文件**
   - 基础 LoRA 训练：`examples/train_lora/llama3_lora_sft.yaml`
   - QLoRA 训练：`examples/train_qlora/llama3_lora_sft_*.yaml`
   - 全参数训练：`examples/train_full/llama3_full_sft.yaml`

2. **修改配置参数**
   ```yaml
   ### output 部分
   report_to: swanlab  # 将 none 改为 swanlab
   
   ### 添加 SwanLab 配置部分
   use_swanlab: true
   swanlab_project: your-project-name
   swanlab_run_name: your-experiment-name
   swanlab_mode: cloud  # 或 local
   ```

### 方法二：使用预配置文件

我们已为您创建了一个完整的配置示例：
- 文件路径：`examples/train_lora/llama3_lora_sft_swanlab.yaml`
- 包含完整的 SwanLab 配置参数

## SwanLab 配置参数说明

| 参数 | 说明 | 示例值 |
|------|------|--------|
| `report_to` | 实验监控工具 | `swanlab` |
| `use_swanlab` | 启用 SwanLab | `true` |
| `swanlab_project` | 项目名称 | `llama3-lora-sft` |
| `swanlab_run_name` | 实验运行名称 | `experiment-001` |
| `swanlab_mode` | 运行模式 | `cloud` 或 `local` |
| `swanlab_api_key` | API 密钥（可选） | 通过环境变量设置 |
| `swanlab_workspace` | 工作空间（可选） | `your-workspace` |
| `swanlab_logdir` | 本地日志目录 | `./logs` |

## 身份验证配置

### 方法一：环境变量（推荐）
```bash
# Windows PowerShell
$env:SWANLAB_API_KEY="your_api_key_here"

# 或在配置文件中设置
swanlab_api_key: your_api_key_here
```

### 方法二：命令行登录
```bash
swanlab login
```

## 启动训练

### 使用预配置文件
```bash
# 进入 LLaMA-Factory 目录
cd f:\JBGS\AI\LLaMA-Factory

# 启动训练
llamafactory-cli train examples/train_lora/llama3_lora_sft_swanlab.yaml
```

### 使用命令行参数覆盖
```bash
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml \
    report_to=swanlab \
    use_swanlab=true \
    swanlab_project=my-project \
    swanlab_run_name=test-run
```

## 监控功能

SwanLab 将自动记录以下信息：

1. **训练指标**
   - 损失函数（loss）
   - 学习率（learning_rate）
   - 训练步数（step）
   - 训练轮数（epoch）

2. **模型参数**
   - 模型架构信息
   - 超参数设置
   - LoRA 配置

3. **系统资源**
   - GPU 使用率
   - 内存占用
   - 训练时间

## 访问实验结果

1. **Web 界面**
   - 访问：`http://192.168.211.110:8000`
   - 登录您的账户
   - 查看项目和实验

2. **实时监控**
   - 训练过程中实时查看指标变化
   - 比较不同实验的性能
   - 下载训练日志和图表

## 常见问题

### 1. 连接失败
- 检查 SwanLab 服务是否正常运行
- 确认网络连接和防火墙设置
- 验证 API 密钥是否正确

### 2. 数据未显示
- 确认 `report_to: swanlab` 设置正确
- 检查 `use_swanlab: true` 是否启用
- 查看训练日志中的 SwanLab 相关信息

### 3. 权限问题
- 确保有项目的写入权限
- 检查工作空间设置

## 高级配置

### 本地模式
```yaml
swanlab_mode: local
swanlab_logdir: ./swanlab_logs
```

### 飞书通知（可选）
```yaml
swanlab_lark_webhook_url: your_webhook_url
swanlab_lark_secret: your_secret
```

## 文件修改总结

您需要修改的主要文件：
1. **训练配置文件**：`examples/train_lora/llama3_lora_sft.yaml`（或其他配置文件）
2. **环境变量**：设置 `SWANLAB_API_KEY`
3. **使用示例**：参考 `llama3_lora_sft_swanlab.yaml`

通过以上配置，您就可以在 LLaMA-Factory 训练过程中使用 SwanLab 进行实验监控和可视化了。