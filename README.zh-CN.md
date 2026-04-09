<div align="center">

# ⚡ Power Automate 开发者技能库

**最全面的 GitHub Copilot Power Automate 开发技能**

让你的 AI 助手拥有专家级 Power Automate 知识 —
从触发条件到企业级 Saga 模式。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Lint](https://github.com/kylehuang0323-ai/power-automate-dev-skills/actions/workflows/lint.yml/badge.svg)](https://github.com/kylehuang0323-ai/power-automate-dev-skills/actions/workflows/lint.yml)
[![Skill: Power Automate](https://img.shields.io/badge/Copilot_Skill-Power_Automate-0078D4)](https://github.com/kylehuang0323-ai/power-automate-dev-skills)
[![Docs: 15 modules](https://img.shields.io/badge/Docs-15_modules-green)](#知识覆盖)
[![Patterns: 8 designs](https://img.shields.io/badge/Patterns-8_designs-orange)](#知识覆盖)

🌐 [English](README.md) | [中文](README.zh-CN.md)

[快速开始](#快速开始) · [为什么需要？](#为什么需要这个技能) · [知识库](#知识覆盖) · [示例](#示例) · [贡献指南](CONTRIBUTING.md)

</div>

---

## 为什么需要这个技能？

用 Copilot 构建 Power Automate 流程时，你会遇到这些问题：

| 问题 | 没有此技能 | 安装后 |
|------|-----------|--------|
| 触发器语法 | ❌ 只给 UI 操作建议 | ✅ 直接生成 `@equals(triggerBody()?['Status']?['Value'],'Approved')` |
| 无限循环 | ❌ 不知道自触发陷阱 | ✅ 自动添加守护条件 + 标记列 |
| DLP 合规 | ❌ 推荐被封锁的 HTTP 连接器 | ✅ 只使用 Business 组连接器并提供替代方案 |
| 错误处理 | ❌ 没有 Scope/Try-Catch 模式 | ✅ Scope_Try → Scope_Catch + Saga 回滚 |
| Flow JSON | ❌ 无法生成可导入的定义 | ✅ 完整的 Logic Apps JSON + 连接引用 |
| SharePoint | ❌ 列名错误（显示名 vs 内部名） | ✅ REST API 发现 + 正确的 `InternalName` |

## 这是什么？

这是一个 **可复用的 GitHub Copilot 技能库**，为 AI 助手提供专家级 Power Automate 知识。集成到项目后，Copilot 可以帮你：

- ✅ 使用正确的架构模式构建云端流
- ✅ 编写和调试复杂表达式
- ✅ 实现企业级错误处理（Try-Catch、Saga、重试）
- ✅ 检查 DLP（数据丢失防护）合规性
- ✅ 使用 PAC CLI 设置 CI/CD 管道
- ✅ 优化 SharePoint 查询和流程性能

## 快速开始

### 方式 1：复制到项目

```bash
git clone https://github.com/kylehuang0323-ai/power-automate-dev-skills.git
cp -r power-automate-dev-skills/.github/ your-project/.github/
cp -r power-automate-dev-skills/docs/ your-project/docs/
```

### 方式 2：作为 Git 子模块

```bash
cd your-project
git submodule add https://github.com/kylehuang0323-ai/power-automate-dev-skills.git skills/power-automate
```

### 方式 3：在 VS Code Copilot Chat 中使用

1. 打开命令面板 → `Chat: Use Prompt from File`
2. 选择 `.github/prompts/` 中的模板（如 `build-flow.prompt.md`）

## 知识覆盖

| 主题 | 核心内容 |
|------|---------|
| **基础** | 5 种流类型、触发器、操作、连接、表达式 |
| **表达式** | 50+ 函数（字符串、日期、逻辑、集合、类型转换） |
| **错误处理** | Try-Catch-Finally、Saga 补偿、指数退避重试 |
| **DLP 策略** | 3 个连接器组、策略叠加、HTTP 替代方案 |
| **专家模式** | 子流程、解决方案生命周期、CI/CD (PAC CLI)、8 种设计模式 |
| **设计模式** | Saga、断路器、扇出/扇入、状态机、队列、观察者、幂等消费者 |
| **生态** | AI Builder + GPT、Teams 自适应卡片、Power Apps、RPA 桌面流、Dataverse |

## Prompt 模板

| 模板 | 描述 | 使用场景 |
|------|------|---------|
| `build-flow` | 从场景设计完整流程 | 开始新的自动化 |
| `debug-flow` | 诊断和修复流程故障 | 流程失败或行为异常 |
| `review-expression` | 验证和优化表达式 | 表达式返回错误结果 |
| `dlp-check` | 检查 DLP 合规性 | 部署到企业环境前 |

## 示例

> 🚧 **即将推出** — `examples/` 目录中的可导入流程定义。

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)

---

<div align="center">

由 [@kylehuang0323-ai](https://github.com/kylehuang0323-ai) 制作 ⚡

如果这个技能帮到了你，请给个 ⭐

</div>
