# GitHub Actions 自动同步到 Gitee 配置指南

## 🎯 功能说明

这个 GitHub Actions 工作流会自动：
1. 将 GitHub 仓库代码同步到 Gitee
2. 触发 Gitee Pages 自动重新部署
3. 完全免费，无需手动操作

## 🔑 配置步骤

### 1. 生成 SSH 密钥对

在本地终端执行：

```bash
ssh-keygen -t rsa -C "your_email@example.com" -f ~/.ssh/gitee_deploy_key
```

这会生成两个文件：
- `~/.ssh/gitee_deploy_key` (私钥)
- `~/.ssh/gitee_deploy_key.pub` (公钥)

### 2. 添加公钥到 Gitee

1. 查看公钥内容：
   ```bash
   cat ~/.ssh/gitee_deploy_key.pub
   ```

2. 复制公钥内容

3. 访问 Gitee 仓库设置：
   - 打开 https://gitee.com/bayue8/ai_learning_camp/settings
   - 点击 **「部署公钥管理」** → **「添加公钥」**
   - 标题：`GitHub Actions Deploy Key`
   - 公钥：粘贴刚才复制的内容
   - ✅ 勾选 **「赋予推送权限」**
   - 点击 **「确定」**

### 3. 添加私钥到 GitHub Secrets

1. 查看私钥内容：
   ```bash
   cat ~/.ssh/gitee_deploy_key
   ```

2. 复制私钥内容（包括 `-----BEGIN` 和 `-----END` 行）

3. 访问 GitHub 仓库设置：
   - 打开 https://github.com/WuYan2501/ai_learning_camp/settings/secrets/actions
   - 点击 **「New repository secret」**
   - Name: `GITEE_PRIVATE_KEY`
   - Secret: 粘贴私钥内容
   - 点击 **「Add secret」**

### 4. 添加 Gitee 密码到 GitHub Secrets

1. 在 GitHub Secrets 页面再添加一个 Secret：
   - Name: `GITEE_PASSWORD`
   - Secret: 你的 Gitee 账号密码
   - 点击 **「Add secret」**

⚠️ **安全提示**：建议使用 Gitee 的私人令牌（Personal Access Token）代替密码：
- 访问 https://gitee.com/profile/personal_access_tokens
- 创建新令牌，勾选 `projects` 权限
- 将令牌作为 `GITEE_PASSWORD` 的值

### 5. 启用 Gitee Pages

1. 访问 https://gitee.com/bayue8/ai_learning_camp
2. 点击 **「服务」** → **「Gitee Pages」**
3. 选择 `master` 分支
4. 点击 **「启动」**

首次启动后，后续更新会由 GitHub Actions 自动触发。

---

## ✅ 验证配置

完成以上步骤后：

1. 推送一次代码到 GitHub：
   ```bash
   git push github master
   ```

2. 访问 GitHub Actions 页面查看执行情况：
   https://github.com/WuYan2501/ai_learning_camp/actions

3. 等待几分钟后，访问 Gitee Pages：
   https://bayue8.gitee.io/ai_learning_camp

---

## 🔍 常见问题

### Q: Actions 失败，提示 "Permission denied"
**A**: 检查是否正确添加了公钥到 Gitee，并勾选了「赋予推送权限」

### Q: Gitee Pages 没有更新
**A**: 
1. 检查 `GITEE_PASSWORD` 是否正确
2. 确保 Gitee Pages 已经首次手动启动过
3. 查看 GitHub Actions 日志中的错误信息

### Q: 不想暴露 Gitee 密码
**A**: 使用 Gitee 私人令牌代替密码（更安全）

---

## 🎉 完成后的效果

- ✅ 推送到 GitHub 后自动同步到 Gitee
- ✅ Gitee Pages 自动更新部署
- ✅ 完全免费，无需付费版
- ✅ 无需手动操作

---

## 📞 需要帮助？

如果配置过程中遇到问题，可以：
1. 查看 GitHub Actions 执行日志
2. 检查 Secrets 是否正确配置
3. 确认 Gitee Pages 服务已启动
