# 统一即降级 (unification-as-demotion)

> 一个为了好玩而建的思想试验仓库。不是严肃科研项目。

## 这仓库是干嘛的

从 E=mc² 出发，一路追问到万物理论。记录推演、开放问题、还有几个能直接在手机上跑的模拟脚本。

**纯属娱乐和技术练习。** 欢迎随便拿去跑着玩、拿去改、拿去删。

## 「降级」是什么意思

不是倒退，是有效场论视角下的必然：

- 狭义相对论 = 广义相对论在局部惯性系的近似
- 量子电动力学 = 标准模型在低能下的有效场论
- 广义相对论和量子场论，可能都是某个更底层结构的近似

统一理论，就是把旧理论"降级"为特例。

## 文件都在哪

| 文件 | 干什么的 |
|---|---|
| `report.html` | 报告正文，从 E=mc² 到量子引力的推演 |
| `open_questions.csv` | 15 条开放问题，E3 八条 / E2 七条 |
| `GRADING.md` | E0—E3 证据分级规则，还有"放弃条件"怎么写 |
| `PROMPTS.md` | 生成新脚本用的提示词模板，想加东西就照它改 |
| `relativity_plot.py` | 狭义相对论：长度收缩可视化 |
| `double_slit.py` | 量子力学：双缝干涉条纹模拟 |
| `calculations.py` | 质能方程 E=mc² 的基础计算 |
| `requirements.txt` | 依赖清单 |

## 怎么跑

装依赖：

```bash
pip install -r requirements.txt
```

然后随便挑一个：

```bash
python relativity_plot.py
python double_slit.py
python calculations.py
```

**手机党注意**：QPython 里装 scipy 有时会失败。真装不上，把 `calculations.py` 里那行 `from scipy.constants import c` 删掉，改成手写 `c = 299792458`，其它文件不受影响。

## 想加新东西？

看 `PROMPTS.md`。复制里面的模板，改掉【】里的字，让 AI 生成，然后把结果粘成一个新的 `.py` 文件扔进来就行。

手机上不用传文件，GitHub 网页点 `...` → Create new file，粘贴，提交，完事。

## 欢迎来改

加、删、改都无所谓。这仓库本来就是个玩票的。

只有一个请求：**提新猜想时，顺手写下"什么结果会让你放弃它"**。写不出来就还不是假说，只是偏好。这条规矩的详细版在 `GRADING.md`。

## 许可证

CC BY-SA 4.0
