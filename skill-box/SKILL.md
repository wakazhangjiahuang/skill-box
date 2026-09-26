---
name: skill-box
description: 用于 GPTS 内容迁移为 Plugin/Skill 的深度分析与构建、从有限需求创建新 Skill、诊断并升级已有 Skill。适用于用户上传 GPTS Instructions/Knowledge/Prompt、要求创建或优化 SKILL.md、GitHub 知识资产路由、打包和回归测试的任务；只参与开发维护，不接管业务 Skill 的日常执行。
---

# Skill Box

把任务分为 A｜GPTS Migration Builder、B｜Skill Creator Studio、C｜Skill Upgrade Auditor。每次只处理当前目标。最终业务 Skill 独立运行，不依赖 Skill Box。

## 共同规则

1. 盘点实际收到的材料，逐项标记已读、仅获路径、缺失、不可访问。读取源文件内容并保存来源与版本；不要把未知资料写成已审计。检查当前可见的 Skill 和目标仓库，避免覆盖与重复命名。
2. 区分事实、用户要求、推断与待核实项。对易变化的 Plugin、模型、API、连接器和 GitHub 项目联网核实，优先官方文档和原始仓库；记录访问日期、版本或 commit、链接与实际可复用能力。
3. 建立任务契约：目标用户、触发、输入、输出、成功标准、边界、工具和失败路径。有限信息时根据证据提出合理默认值并明确假设；仅对阻止正确执行的缺口提问。
4. 进行深度审计和差距分析，按影响排序，提出逐文件变更、保留项、风险和验收案例。不要以泛化 Prompt 替代专业判断。
5. 先按业务用途去重，再决定资产位置。SKILL.md 放触发与必要执行协议，短小稳定的规则放 references/，可复用模板放 assets/，确定性处理放 scripts/。仅当体量、更新频率、跨 Skill 共享或权限要求有依据时，才规划 GitHub 仓库。保留来源记录，避免包内与仓库重复维护同一正文；仅写 URL 不代表资源可读。
6. 按需使用已安装的 skill-creator 创建、验证、安装和保存目标 Skill；复杂系统判断可参考 ai-system-architecture-advisor，外部应用可参考相应 App/MCP 技能。遵守当前环境和实际权限。它们都不是目标业务 Skill 的运行依赖。
7. 区分方案已核实、本地包已验证、远端仓库与连接已实测。未执行的写入、安装、迁移或运行测试标记未验证。

## A｜GPTS Migration Builder

读取 [迁移专项](references/A-migration.md)。输入包括 GPTS 名称、描述、Instructions、启动 Prompt、Knowledge、Actions、Capabilities 和反馈。按可检查的方案门禁执行：逐份读取并建立证据台账 → 还原旧能力、反馈与目标业务链 → 逐段去重、查冲突和核实事实 → 决定 SKILL.md、references、assets、scripts、GitHub 或归档的唯一去向 → 检索开源候选并核查许可、适配、依赖和可复用模块 → 比较单 Skill 多模式、拆分 Skill、必要工具服务 → 推荐架构并给出取舍、链路图、逐文件方案和测试 → 用户核实。先定义目标 Skill 做什么，再决定文件放哪里；不得凭两份上传材料就预设拆成两个 Skill。

用户要求 A 先核实方案：在其确认该目标方案之前，不生成或安装目标升级 Skill 包，不写入目标知识仓库，不迁移原 GPT。确认后执行构建、验证、打包和已授权的写入，不对已确认的范围重复征求许可。单独核实原 GPT 迁移、发布和分享权限的当前平台行为，不把本地 ZIP 称作已迁移的 Plugin。

## B｜Skill Creator Studio

读取 [创建专项](references/B-creation.md)。从有限需求建立可检验的假设，检索官方规范和相关原始 GitHub 项目，提炼可复用方法，制定任务、输入、输出、质量、资源和权限契约。给出简明的架构及关键假设后直接创建并验证目标 Skill；用户明确要求先审核方案时停在方案阶段。只创建必要文件。

## C｜Skill Upgrade Auditor

读取 [升级专项](references/C-upgrade.md)。基于反馈重现问题，审计 Trigger → 输入 → GitHub 资产 → 路由 → 工具 → 生成 → 输出 → QA 的链路。提供根因证据及针对性升级方案，再按授权范围修改；保留旧能力，执行回归测试和版本差异说明。用户明确要求先审核方案时停在修改前。

## GitHub 资产与运行时契约

需要 GitHub 知识时读取 [资产路由规范](references/github-assets.md)，使用 [Manifest 示例](assets/KB-MANIFEST.example.json) 作为结构参考。选择已有仓库或按专业 Skill 规划独立仓库，复用现有命名。记录公开/私有、目标分支或 commit、访问方式、路径、标签、来源和校验值。外部写入不可用时交付可审查的本地资产与待执行清单；不伪造远端写入或读取。

本工具箱自身的包外资产定位为 resource_id = skill-box，仓库 wakazhangjiahuang/skill-box，入口 KB-MANIFEST.json。仅在使用包外模板或资料时通过实际可用的 GitHub 工具读取 Manifest 与当前任务资源；随 Skill 打包的规则不依赖网络。不得把 brush、iphub 等业务仓库用作 Skill Box 的存储位置。

对采用示例 schema 的新仓库，可运行 scripts/select_assets.py <manifest> <task-id> 列出精确资源；已有仓库采用自身 Manifest schema 时按其真实结构解析，不强制套用示例脚本。

目标业务 Skill 的日常链路：启动 Prompt 给出任务与输入 → 专业 Skill 判断 → 读取随包 references/assets；仅在批准的架构需要外部资料时读取 Registry/Manifest 并精确取回 → 校验来源与版本 → 执行 → GPT/Codex 生成 → QA → 交付。关键资料缺失时停止依赖它的结论，非关键资料按契约降级。Skill Box 仅负责开发维护，不参与日常执行。

## 验证和交付

读取 [QA 规范](references/qa-contract.md)。静态验证、实际取回、正负触发、正常和缺失输入、工具失败、输出及旧案例回归分别报告，不能用静态检查冒充运行通过。可运行 scripts/validate_release.py 核验目标 Skill 和本地 Manifest，scripts/package_skill.py 生成并核对 Skill ZIP；脚本都不连接 GitHub。Plugin ZIP 另按当前官方规范加入 manifest，裸 Skill ZIP 不能称为 Plugin ZIP。

交付阶段状态、分析证据与方案、目标文件与 GitHub 资产位置、测试记录及未验证项。A 的方案阶段只交付可核实方案；确认后才交付目标包及实际结果。

需要可复制的调用语句时，读取 [三模式启动 Prompt](assets/START-PROMPTS.md)。
