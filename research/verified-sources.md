# 官方规范与开源项目筛选

核查日期：2026-09-26。仅保存项目定位、具体路径、许可和采用条件；不复制第三方源代码。具体创建任务再次核查目标版本、依赖和平台支持。

| 项目/规范 | 核查文件 | 许可 | 适配结论 |
| --- | --- | --- | --- |
| [Agent Skills 开放规范](https://agentskills.io/specification)、[agentskills/agentskills](https://github.com/agentskills/agentskills) | 规范、README、LICENSE | 仓库代码 Apache-2.0；规范文档依各自许可 | 作为 Skill 结构与渐进加载的规范依据；不等同 Agent 运行时 |
| [anthropics/skills 的 skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | `SKILL.md`、该目录 `LICENSE.txt` | 该目录 Apache-2.0；仓库没有统一根许可证，逐目录核查 | 借鉴草稿→案例评测→迭代方法；不直接复制 vendor 指令或脚本 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | README、LICENSE、examples、官方[调度](https://openai.github.io/openai-agents-python/multi_agent/)与[护栏](https://openai.github.io/openai-agents-python/guardrails/) | MIT | OpenAI SDK 目标时优先参考 Agent/Runner、工具、handoff、session、trace；不成为 Skill Box 运行依赖 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | README、LICENSE、[持久执行](https://docs.langchain.com/oss/python/langgraph/durable-execution) | MIT | 长时状态、恢复和显式工作流适用；简单单 Agent 项目不引入 |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | README、LICENSE、Python/.NET samples | MIT | Microsoft/.NET 或跨语言工作流场景候选；按目标环境选用 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) 与 [Copilot custom agents 官方文档](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents) | LICENSE、agents/ 示例、官方配置 | 仓库 MIT；单个社区样例仍核查来源 | Copilot profile 的格式/样例参考；不能拿一份 agent profile 代替 SDK 应用 |
| [CatchTheTornado/open-agents-builder](https://github.com/CatchTheTornado/open-agents-builder) | README、仓库元信息 | MIT | 商业多 Agent 可视化平台参考；体量与集成较重，当前不直接复用 |

## 来源排序与停止

1. 用户任务与原始资料定义目标；官方规范决定格式和平台行为；原始仓库展示具体实现；市场榜单只做发现线索。
2. 每项候选记录目标文件、版本/提交、许可、依赖、维护、任务匹配、可替换模块及直接采用/二改/参考/排除。许可证允许并不代表实现适配；引用思想优先自行表达。
3. 当格式、工具权限、关键架构取舍与测试路径均有一手依据，且新候选不改变选择时停止检索。

现有 [`wakazhangjiahuang/skill-box`](https://github.com/wakazhangjiahuang/skill-box) 经 GitHub 仓库元信息核实为 **public**；本私域种子包不写入该仓库。
