# RAGFlow 从 Elasticsearch 切换到 Infinity 完整指南

## 概述

RAGFlow 支持两种文档引擎：
- **Elasticsearch**（默认）：成熟的搜索引擎，适合大规模部署
- **Infinity**：InfiniFlow 自研的 AI 原生数据库，专为 RAG 场景优化

## 为什么选择 Infinity？

根据 RAGFlow 官方文档，Infinity 相比其他开源向量数据库具有以下优势：
1. **混合搜索支持**：同时支持全文搜索和向量搜索
2. **短语搜索**：支持精确的短语匹配
3. **高级排序功能**：提供更好的搜索结果排序
4. **AI 原生设计**：专为 RAG 应用场景优化

## 切换步骤

### 第一步：备份现有数据

**⚠️ 重要警告：切换过程会清除所有现有数据！**

```bash
# 1. 备份重要配置文件
cp /data/ragflow/docker/.env /data/ragflow/docker/.env.backup
cp /data/ragflow/docker/service_conf.yaml.template /data/ragflow/docker/service_conf.yaml.template.backup

# 2. 如果有重要数据，请先导出
# 注意：切换引擎后需要重新上传和处理文档
```

### 第二步：停止所有服务

```bash
# 进入 RAGFlow 目录
cd /data/ragflow

# 停止所有容器并删除卷（这会清除所有数据）
docker compose -f docker/docker-compose.yml down -v

# 确认所有容器已停止
docker ps | grep ragflow
```

### 第三步：修改配置文件

编辑 `/data/ragflow/docker/.env` 文件：

```bash
# 使用文本编辑器打开配置文件
vim /data/ragflow/docker/.env

# 或者使用 sed 命令直接替换
sed -i 's/DOC_ENGINE=${DOC_ENGINE:-elasticsearch}/DOC_ENGINE=${DOC_ENGINE:-infinity}/g' /data/ragflow/docker/.env
```

**关键配置项：**
```bash
# 将文档引擎设置为 Infinity
DOC_ENGINE=${DOC_ENGINE:-infinity}

# 确保 COMPOSE_PROFILES 设置正确
COMPOSE_PROFILES=${DOC_ENGINE}

# Infinity 相关端口配置（通常不需要修改）
INFINITY_HOST=infinity
INFINITY_THRIFT_PORT=23817
INFINITY_HTTP_PORT=23820
INFINITY_PSQL_PORT=5432
```

### 第四步：启动服务

```bash
# 启动所有服务
docker compose -f docker/docker-compose.yml up -d

# 查看服务状态
docker compose -f docker/docker-compose.yml ps

# 查看 Infinity 容器日志
docker logs ragflow-infinity

# 查看 RAGFlow 主服务日志
docker logs ragflow-server
```

### 第五步：验证切换成功

```bash
# 1. 检查容器状态
docker ps | grep ragflow

# 应该看到以下容器运行：
# - ragflow-server
# - ragflow-infinity
# - ragflow-mysql
# - ragflow-redis
# - ragflow-minio

# 2. 检查 Infinity 健康状态
curl http://localhost:23820/admin/node/current

# 3. 检查 RAGFlow 服务
curl http://localhost:9380/v1/system/health
```

## Infinity 配置优化

### 内存配置

Infinity 的配置文件位于 `/data/ragflow/docker/infinity_conf.toml`：

```toml
[general]
version                  = "0.6.0-dev5"
time_zone                = "Asia/Shanghai"
time_zone_bias           = 8
cpu_limit                = 0

[system]
data_dir                 = "/var/infinity/data"
default_row_size         = 8192
buffer_manager_size      = "4GB"
temp_dir                 = "/var/infinity/tmp"
result_cache             = "off"
memindex_memory_quota    = "1GB"

[wal]
wal_dir                  = "/var/infinity/wal"

[resource]
resource_dir             = "/var/infinity/resource"
```

**推荐优化：**
- `buffer_manager_size`：根据系统内存调整（建议设置为系统内存的 25-50%）
- `memindex_memory_quota`：内存索引配额（建议 1-2GB）

### 性能监控

```bash
# 监控 Infinity 容器资源使用
docker stats ragflow-infinity

# 查看 Infinity 性能指标
curl http://localhost:23820/admin/stats

# 查看数据库信息
curl http://localhost:23820/admin/databases
```

## 常见问题和解决方案

### 1. 容器启动失败

**问题**：Infinity 容器无法启动

**解决方案**：
```bash
# 检查日志
docker logs ragflow-infinity

# 检查端口占用
netstat -tlnp | grep 23817
netstat -tlnp | grep 23820

# 如果端口被占用，修改 .env 文件中的端口配置
```

### 2. 内存不足

**问题**：系统内存不足导致 Infinity 性能下降

**解决方案**：
```bash
# 调整内存限制
vim /data/ragflow/docker/.env
# 修改 MEM_LIMIT=8073741824 (8GB)

# 或者调整 Infinity 配置
vim /data/ragflow/docker/infinity_conf.toml
# 减少 buffer_manager_size 和 memindex_memory_quota
```

### 3. 数据迁移

**问题**：需要从 Elasticsearch 迁移现有数据

**解决方案**：
```bash
# 目前不支持直接数据迁移，需要：
# 1. 重新上传文档到知识库
# 2. 重新进行文档解析和向量化
# 3. 重新训练和配置模型
```

### 4. 架构兼容性

**问题**：在 Linux/arm64 架构上运行

**解决方案**：
```bash
# 官方暂不支持 arm64 架构
# 建议使用 x86_64 架构的服务器
# 或者继续使用 Elasticsearch
```

## 性能对比

| 特性 | Elasticsearch | Infinity |
|------|---------------|----------|
| 全文搜索 | ✅ 优秀 | ✅ 优秀 |
| 向量搜索 | ✅ 支持 | ✅ 原生支持 |
| 混合搜索 | ✅ 支持 | ✅ 优化 |
| 短语搜索 | ✅ 支持 | ✅ 增强 |
| 内存使用 | 较高 | 优化 |
| 启动速度 | 较慢 | 较快 |
| 生态成熟度 | 非常成熟 | 发展中 |

## 回滚到 Elasticsearch

如果需要回滚到 Elasticsearch：

```bash
# 1. 停止服务
docker compose -f docker/docker-compose.yml down -v

# 2. 恢复配置
cp /data/ragflow/docker/.env.backup /data/ragflow/docker/.env

# 3. 或者直接修改
sed -i 's/DOC_ENGINE=${DOC_ENGINE:-infinity}/DOC_ENGINE=${DOC_ENGINE:-elasticsearch}/g' /data/ragflow/docker/.env

# 4. 重新启动
docker compose -f docker/docker-compose.yml up -d
```

## 总结

切换到 Infinity 的主要优势：
1. **专为 RAG 优化**：更好的混合搜索性能
2. **资源效率**：更低的内存占用
3. **启动速度**：更快的服务启动时间
4. **功能增强**：更好的短语搜索和排序

**注意事项：**
- 切换过程会清除所有现有数据
- 需要重新上传和处理文档
- 目前不支持 arm64 架构
- Infinity 相对较新，生态不如 Elasticsearch 成熟

**建议：**
- 在测试环境先验证切换效果
- 根据实际使用场景选择合适的引擎
- 定期备份重要配置和数据