# 3.9 多模态 🔥

> 视觉、音频、视频——LLM 的感知能力扩展
>
> 返回 [应用层索引](../03_applications.md) | [知识库索引](../../SYLLABUS.md)

---

## 视觉语言模型（VLM）

- **架构** ⭐
  - 视觉编码器（ViT）→ 投影层（MLP / Q-Former）→ 语言模型
  - *核心问题*：投影层的作用？（将视觉特征映射到语言模型的 token 空间）
  - *核心问题*：Q-Former（BLIP-2）和 MLP 投影的区别？（Q-Former 用可学习 query 压缩视觉信息）

- **主流模型**
  - 闭源：GPT-4o（原生多模态）/ Gemini 2.0 / Claude Vision
  - 开源：Qwen2-VL 🔥（视频理解强）/ InternVL2 / LLaVA-1.6 / MiniCPM-V

---

## 图像生成

- **Diffusion Model** ⭐
  - *核心思想*：前向过程逐步加噪（马尔可夫链），反向过程学习去噪
  - *核心问题*：为什么 Diffusion 比 GAN 更稳定？（不需要对抗训练，优化目标更简单）
  - *延伸*：DDPM → DDIM（加速采样）→ LDM（潜空间扩散，Stable Diffusion 基础）

- **Flow Matching（Rectified Flow）** 🔥
  - *核心思想*：学习从噪声到图像的直线路径，比 Diffusion 的曲线路径更高效
  - *为什么重要*：SD3 / FLUX.1 都用这个，采样步数更少，质量更高

- **主流模型**
  - FLUX.1（Black Forest Labs）🔥：目前开源最强图像生成
  - Stable Diffusion 3.5 / SDXL
  - DALL-E 3 / Midjourney v6 / Ideogram

- **DiT（Diffusion Transformer）** 🔥 ⭐
  - *核心思想*：用 Transformer 替代 U-Net 作为 Diffusion 的骨干网络
  - *为什么重要*：Sora / FLUX / SD3 都用 DiT，Scaling 效果更好

---

## 视频生成

- **主流模型**：Sora / Kling 2.0 / Runway Gen-3 / Pika 2.0 / Hailuo
- *核心挑战*：时序一致性（前后帧连贯）/ 运动控制 / 长视频生成
- *核心问题*：视频生成为什么比图像生成难？（需要建模时序依赖，计算量 × 帧数）

---

## 音频

- **ASR（语音识别）**：Whisper v3 / Paraformer / SenseVoice
  - Whisper：OpenAI 开源，多语言，端到端，工业界标配
- **TTS（语音合成）** 🔥：VITS / ChatTTS / Fish Speech / CosyVoice 2
  - *核心问题*：零样本语音克隆（Voice Cloning）的原理？（Speaker Embedding + 扩散生成）

---

> 💡 **面试拷问 — 多模态**
> - VLM 中视觉 token 和文本 token 的比例对模型效果有什么影响？⭐
> - GPT-4o 的"原生多模态"和 LLaVA 的"投影层拼接"有什么本质区别？⭐
> - Diffusion Model 的前向过程和反向过程分别在做什么？一句话解释？⭐
> - DiT 用 Transformer 替代 U-Net，为什么 Scaling 效果更好？⭐
> - Flow Matching 和 Diffusion 的核心区别？为什么更高效？⭐
> - 视频生成中的时序一致性问题怎么解决？Sora 用了什么方案？
