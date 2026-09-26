# Skill Box 私域知识库种子包

本包汇集用户上传的 8 份 SkillForge/Skill BOX 材料的去重提炼，以及 2026-09-26 核查的 Agent Skills 与 Agent 框架一手来源。它只提供知识、方案模板和评测案例，不包含第三方源码、用户原件或可执行的 Agent。

## 上传和接入

1. 在 `wakazhangjiahuang` 名下新建 **Private** 仓库，建议名称 `skill-box-private-kb`。当前 `wakazhangjiahuang/skill-box` 是公开仓库，不能作为此包的私域位置。
2. 解压后将本目录**内部文件**上传到私有仓库根目录，保持 `knowledge/`、`research/`、`templates/`、`evals/` 路径；不要只上传 ZIP 文件。
3. 上传后读取这批资产所在的真实提交 SHA，将 `KB-MANIFEST.json` 的 `ref` 由 `UNPUBLISHED` 改为该固定提交 SHA，再提交 Manifest。
4. 将 `REPO-REGISTRY.example.json` 中的 `ref` 改为 **Manifest 的提交 SHA**，按需放在实际 Registry 位置；两个 ref 各指向不同层级，不能混用。
5. 核实 GitHub 连接器对该私有仓库有读取权限；按 Manifest 精确取回 D 任务资源并核对 SHA256。完成前 D 模式使用随包流程，私域资料状态为“待接入”。

本包中的项目链接用于研究与选型，不自动安装依赖，也不授予外部写入权限。平台规则与开源许可在具体项目使用前再核实。

## 文件

- `SOURCE-AUDIT.md`：8 份附件的去重、保留和排除依据。
- `knowledge/skill-design.md`：B/C 可复用的 Skill 设计方法。
- `knowledge/agent-design.md`：D 模式的架构与运行时契约。
- `knowledge/qa-delivery.md`：触发、功能、权限和打包验证。
- `research/verified-sources.md`：官方规范与开源候选清单。
- `templates/D-agent-spec.md`：D 模式架构与逐文件交付模板。
- `evals/creator-cases.json`：B/C/D 的边界与失败案例。
- `KB-MANIFEST.json`：按任务选择资源；`UNPUBLISHED` 表示尚未部署。
