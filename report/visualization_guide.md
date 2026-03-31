# 可视化整理与解读

这份整理基于 [`model_comparison_v3.ipynb`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/model_comparison_v3.ipynb) 里已经跑出来的结果。现有图像统一放在 [`report/figures`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures)。

先说结论：

- 你的主结论是稳定的：DHVT 明显强于 AlexNet，最佳验证准确率约 `0.8062` 对 `0.6848`。
- 这不只是总体 accuracy 的优势，DHVT 在大多数类别上也更稳，宏平均 `precision / recall / F1` 都更高。
- 现在最需要补上的不是“更多花哨图”，而是把那些真正有分析价值但之前没单独导出的图放进结果集里。

## 当前图表清单

### 01 `01_validation_curves.png`

文件：[`report/figures/01_validation_curves.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/01_validation_curves.png)

作用：

- 对比两个模型随 epoch 的验证损失和验证准确率变化。
- 这是最核心的图，因为它说明 DHVT 的优势不是偶然单点，而是整个训练过程中逐渐拉开的。

怎么讲：

- 看 loss 曲线：DHVT 下降更平稳，最终更低。
- 看 accuracy 曲线：DHVT 更早进入高位，并且最终上限更高。
- 如果老师只给你时间讲一张图，这张优先级最高。

### 02 `02_confusion_matrices.png`

文件：[`report/figures/02_confusion_matrices.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/02_confusion_matrices.png)

作用：

- 展示每个真实类别最容易被错分到哪里。
- 适合说明“模型错得像不像人”“哪些类天然容易混”。

怎么讲：

- 两个模型都容易在相近类别上混淆，比如 `cat <-> dog`、`airplane -> ship`。
- DHVT 的对角线整体更亮，说明多数类的正确率更高。

注意：

- 这张图依赖完整评估结果。如果你之后把本地 DHVT checkpoint 补齐，建议重新导出一次，作为最终版。

### 03 `03_misclassified_examples.png`

文件：[`report/figures/03_misclassified_examples.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/03_misclassified_examples.png)

作用：

- 做定性分析，直接看“错例长什么样”。
- 非常适合报告答辩时解释：为什么这个样本难。

怎么讲：

- 关注背景干扰、主体过小、姿态异常、低分辨率这几类典型失败原因。
- 如果一张图里 AlexNet 错而 DHVT 对，可以直接说 DHVT 对全局结构更敏感。

### 04 `04_both_models_wrong_examples.png`

文件：[`report/figures/04_both_models_wrong_examples.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/04_both_models_wrong_examples.png)

作用：

- 这组图显示“最难样本”。
- 它能把讨论从“谁更强”推进到“数据本身哪里难”。

怎么讲：

- 两个模型都错，通常说明样本有天然歧义，或者类别之间视觉边界本来就模糊。
- 这一页能让分析更完整，不会显得只在报喜。

### 05 `05_confidence_distribution.png`

文件：[`report/figures/05_confidence_distribution.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/05_confidence_distribution.png)

作用：

- 比较两个模型的置信度分布，以及正确/错误预测上的置信度表现。
- 这是“模型准不准”和“模型敢不敢”的桥梁。

关键数字：

- AlexNet mean confidence: `0.6663`
- AlexNet wrong confidence: `0.4948`
- AlexNet ECE: `0.0211`
- DHVT mean confidence: `0.8254`
- DHVT wrong confidence: `0.6228`
- DHVT ECE: `0.0198`

怎么讲：

- DHVT 更自信，而且大多数时候这种自信是有依据的，因为它整体准确率更高。
- 但 DHVT 在错的时候置信度也不低，这说明它虽然更强，也仍然会出现“自信地错”。
- 所以只看 accuracy 不够，置信度分析是必要补充。

### 06 `06_agreement_analysis.png`

文件：[`report/figures/06_agreement_analysis.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/06_agreement_analysis.png)

作用：

- 统计两模型同对、AlexNet 单独对、DHVT 单独对、同错的比例。
- 这是最适合一句话总结模型相对优势的图。

关键数字：

- Both correct: `0.6304`
- AlexNet only correct: `0.0544`
- DHVT only correct: `0.1758`
- Both wrong: `0.1394`

怎么讲：

- `DHVT only correct` 明显高于 `AlexNet only correct`，这说明 DHVT 不是“和 AlexNet 差不多”，而是实打实额外救回了很多样本。

## 补上的重要图

下面这些其实是 notebook 里已经做过、但之前没有单独整理出来的关键图。我已经补进 `report/figures` 里了。

### 07 `07_per_class_accuracy.png`

文件：[`report/figures/07_per_class_accuracy.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/07_per_class_accuracy.png)

为什么重要：

- 这是最应该补上的图之一。
- 总 accuracy 只能说明整体，per-class accuracy 才能说明 DHVT 的优势到底是“全面提升”还是“只赢少数类”。

这张图可以重点讲：

- `bird`: `0.513 -> 0.748`
- `deer`: `0.582 -> 0.794`
- `dog`: `0.565 -> 0.740`
- `ship`: `0.791 -> 0.898`

结论：

- DHVT 不是只在某一个类特别强，而是在几乎所有类上都有提升。
- 提升最明显的是细粒度、纹理复杂、容易混淆的类别。

### 08 `08_precision_recall_f1.png`

文件：[`report/figures/08_precision_recall_f1.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/08_precision_recall_f1.png)

为什么重要：

- 这是把 confusion matrix 进一步量化后的结果。
- 对课程报告来说，这张图会让评估部分完整很多。

关键数字：

- AlexNet macro precision: `0.6811`
- AlexNet macro recall: `0.6848`
- AlexNet macro F1: `0.6814`
- DHVT macro precision: `0.8057`
- DHVT macro recall: `0.8062`
- DHVT macro F1: `0.8056`

结论：

- DHVT 的优势在 precision、recall、F1 三条线上都成立，不是单一指标偶然偏高。

### 09 `09_dhvt_attention_visualization.png`

文件：[`report/figures/09_dhvt_attention_visualization.png`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/report/figures/09_dhvt_attention_visualization.png)

为什么重要：

- 这张图是“模型为什么更强”的解释性证据。
- 如果你要体现 transformer-style 模型的特点，这张图比单纯报准确率更有说服力。

怎么讲：

- 看 DHVT 的 attention 是否更集中在主体区域，而不是被背景牵着走。
- 如果某些样本里 AlexNet 错而 DHVT 对，这张图尤其值钱，因为你可以直接用它解释结构优势。

## 建议你报告里保留的最小图集

如果你想压缩到最有价值的一组图，建议保留这 6 张：

- `01_validation_curves.png`
- `02_confusion_matrices.png`
- `05_confidence_distribution.png`
- `06_agreement_analysis.png`
- `07_per_class_accuracy.png`
- `09_dhvt_attention_visualization.png`

这套图已经覆盖：

- 训练动态
- 类别级错误模式
- 置信度与校准
- 两模型互补关系
- 类别级收益来源
- Transformer 可解释性

## 现在还缺什么

严格来说，还差一张真正值得补、但目前本地没法稳妥重跑的图：

- `Calibration-only` 单图版可靠性图。如果后面你把本地 `cifar10_dhvt_best.pth` 补回来，我建议单独再导出一张 AlexNet 与 DHVT 的 reliability diagram 对比图，适合和 `05_confidence_distribution.png` 配套使用。

次一级可选项：

- 自定义测试图片预测可视化。如果你想把 `test_images` 里的真实图片也放进报告，可以再补一页“自定义图片预测结果”，更贴近 demo 展示。

## 当前限制

本地目前只有 [`models/cifar10_efficientnet_b0_pretrained_best.pth`](C:/Users/yangh/OneDrive/GitSpace/classification-deep-learning-project/models/cifar10_efficientnet_b0_pretrained_best.pth)，没有 notebook 里那份 `cifar10_dhvt_best.pth`。所以这次整理采用的是：

- 复用 notebook 已经跑出来并保存在输出里的图
- 把之前没整理出来的重要图补导出
- 不冒险伪造“本地重新评估”的新结果

如果你把 DHVT checkpoint 同步到本地，我下一步可以直接把这些图全部按当前代码链路重跑一遍，并把说明同步更新成最终版。
