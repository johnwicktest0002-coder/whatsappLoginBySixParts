#!/usr/bin/env python3
import argparse

DESCRIPTION_TEMPLATE = '''# WhatsApp iOS 项目描述

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

## 软件版本更新

- 网站地址：https://sayworld8.com/
- 联系方式：tg @john20222222
'''


def generate_description(output_path=None):
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(DESCRIPTION_TEMPLATE)
        print(f'项目描述已写入：{output_path}')
    else:
        print(DESCRIPTION_TEMPLATE)


def main():
    parser = argparse.ArgumentParser(description='生成 WhatsApp iOS 项目描述文档')
    parser.add_argument('--output', '-o', help='输出文件路径（例如 whatsapp_project_description.md）')
    args = parser.parse_args()
    generate_description(args.output)


if __name__ == '__main__':
    main()
