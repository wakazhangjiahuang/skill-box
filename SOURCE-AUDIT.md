# 上传资料提炼与去重台账

审计日期：2026-09-26。逐份读取本次上传的 8 个 TXT；这些文件是历史 GPTS/SkillForge 材料，不等于当前平台规范。

| 来源 | 保留的独有价值 | 目标文件 | 合并或排除 |
| --- | --- | --- | --- |
| `你是「Skill BOX」…txt` | 任务卡、资料审计、研究和验收的总体顺序 | `knowledge/skill-design.md`、已安装 Skill Box 的四模式路由 | 与 KB02/03 重复的通则合并；“一律确认外部写入/安装”改为尊重当前用户授权 |
| `02_GPTS配置与使用建议.txt` | Instructions 与 Knowledge 分工、Preview 测试 | `knowledge/skill-design.md` | 旧 GPTS 名称、固定字数、开关建议和历史配置不进入当前 Skill |
| `KB01_Agent-Skills标准与平台适配.txt` | 格式、渐进加载、跨平台差异 | `knowledge/skill-design.md`、`research/verified-sources.md` | 与官网规范相同的长定义压缩；具体限制以当前官方文档为准 |
| `KB02_Skill研究设计与交互工作流.txt` | 需求卡、Skill 边界、自由度、证据分层 | `knowledge/skill-design.md`、`knowledge/agent-design.md` | 与旧 Prompt 相同的审计和确认步骤只维护一份 |
| `KB03_质量安全评测与ZIP打包规范.txt` | 可观察断言、失败路径、ZIP 复检 | `knowledge/qa-delivery.md`、`evals/creator-cases.json` | 大段通用安全清单缩为目标相关验证；不用结构检查冒充实测 |
| `KB04_上传示例Skill提炼与改写规则.txt` | 账号规划与单题验证的触发边界、证据包和降级 | `knowledge/skill-design.md`、`evals/creator-cases.json` | 两个示例 ZIP 未在本次上传，不声称已审计源码；小红书业务规则不并入通用 Agent |
| `KB05_联网检索来源地图与可信度规则.txt` | 来源优先级、项目许可证筛选、检索停止条件 | `research/verified-sources.md` | 市场和趋势站只作发现线索；静态“热门项目”列表不当当前事实 |
| `KB06_标准Skill模板与交付模板.txt` | 输出契约、文件树、可观察验收 | `templates/D-agent-spec.md`、`knowledge/qa-delivery.md` | 不复制占位符密集的通用模板；原件的嵌套代码围栏需重新排版 |

原则：保留可迁移的判断和流程，记录来源；不复制八份原文到仓库，不把旧 GPTS 的“先确认一切”提升为当前用户任务的授权规则。新增 D 模式知识来自目标平台官方文档与原始仓库，与上传材料分开标注。
