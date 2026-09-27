# Skill Box 知识资产

本仓库公开存放 Skill Box 的 A/B/C/D 四模式 Skill 文件及从用户上传的 8 份材料去重提炼的知识资产。仅存提炼后的方法、方案模板、来源台账和测试案例，不存原始附件或第三方源码。

## 入口与读取

- Skill 文件：`skill-box/SKILL.md`；各模式专项位于 `skill-box/references/`。
- 资产入口：`REPO-REGISTRY.json` → 固定提交的 `KB-MANIFEST.json` → Manifest 的固定资产提交 → 按 A/B/C/D/qa 选择资源并核对 SHA256。
- 资料：`knowledge/`、`research/`、`templates/`、`evals/`；`SOURCE-AUDIT.md` 记录上传资料的合并和排除依据。

本仓库的提炼资料已获用户授权公开（2026-09-27）。将来需要非公开的资料应另设私有仓库和访问授权，不沿用本仓库的公开路由。开源项目链接用于研究和选型，具体采用前仍需核对目标版本、许可及依赖。
