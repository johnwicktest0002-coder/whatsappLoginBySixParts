# WhatsApp iOS 项目描述

本项目为 `WhatsAppLoginBySixParts` 提供 iOS 端专用的项目描述与生成工具。它围绕 WhatsApp 直登与提取方案构建，支持定制插件与多个环境。

## 核心功能

- iOS 下的 WhatsApp 六段直登方案
- 支持“巨魔环境”和“越狱环境”
- 支持定制 WhatsApp 插件
- 支持定制海外 App 的插件
- 提供 iOS 环境下的 WhatsApp 提取工具：
  - 5 段提取工具
  - 6 段提取工具
  - 全参数提取工具

## 适用场景

- 需要在 iOS 环境下实现 WhatsApp 直登或快速登录的项目
- 需要支持特殊运行环境（如越狱设备）
- 需要对 WhatsApp 或海外 App 进行定制插件开发与扩展
- 需要提取 WhatsApp 登录参数、会话信息或会话识别数据

## 目标输出

该项目描述工具将生成一份结构化说明文档，包含项目特点、目标组件与提取工具说明，方便后续开发与传播。

## 文件说明

- `whatsapp_project_description.md`：本项目的描述文件
- `project_description_tool.py`：用于自动生成项目描述内容的工具脚本
