# 🚀 快速配置 Gitee 自动同步

已经为你准备好了自动同步配置！只需要 **5 分钟** 完成设置。

## 📋 配置清单

### ✅ 第一步：生成 SSH 密钥（2分钟）

打开终端，执行：

```bash
ssh-keygen -t rsa -C "你的邮箱" -f ~/.ssh/gitee_deploy_key
```

一路回车（不设置密码）。

---

### ✅ 第二步：添加公钥到 Gitee（1分钟）

1. **查看公钥**：
   ```bash
   cat ~/.ssh/gitee_deploy_key.pub
   ```

2. **复制输出内容**

3. **添加到 Gitee**：
   - 打开：https://gitee.com/bayue8/ai_learning_camp/settings/deploy_keys
   - 点击 **「添加部署公钥」**
   - 标题：`GitHub Actions`
   - 公钥：粘贴刚才复制的内容
   - ✅ **必须勾选「赋予推送权限」**
   - 点击 **「确定」**

---

### ✅ 第三步：添加私钥到 GitHub（1分钟）

1. **查看私钥**：
   ```bash
   cat ~/.ssh/gitee_deploy_key
   ```

2. **复制完整内容**（包括 BEGIN 和 END 行）

3. **添加到 GitHub**：
   - 打开：https://github.com/WuYan2501/ai_learning_camp/settings/secrets/actions
   - 点击 **「New repository secret」**
   - Name: `GITEE_PRIVATE_KEY`
   - Secret: 粘贴私钥内容
   - 点击 **「Add secret」**

---

### ✅ 第四步：添加 Gitee 密码（1分钟）

**推荐方式：使用私人令牌（更安全）**

1. **生成令牌**：
   - 访问：https://gitee.com/profile/personal_access_tokens
   - 点击 **「生成新令牌」**
   - 描述：`GitHub Actions`
   - 权限：勾选 `projects`
   - 点击 **「提交」**
   - **复制生成的令牌**（只显示一次！）

2. **添加到 GitHub**：
   - 打开：https://github.com/WuYan2501/ai_learning_camp/settings/secrets/actions
   - 点击 **「New repository secret」**
   - Name: `GITEE_PASSWORD`
   - Secret: 粘贴刚才的令牌
   - 点击 **「Add secret」**

**或者直接使用 Gitee 密码**（不推荐）：
- Name: `GITEE_PASSWORD`
- Secret: 你的 Gitee 账号密码

---

### ✅ 第五步：启动 Gitee Pages（1分钟）

1. 访问：https://gitee.com/bayue8/ai_learning_camp/pages
2. 选择分支：`master`
3. 点击 **「启动」**
4. 等待部署完成

---

## 🎉 完成！测试一下

配置完成后，推送一次代码测试：

```bash
cd ~/IdeaProjects/ai_learning_camp
git commit --allow-empty -m "test: trigger Gitee sync"
git push github master
```

然后：
1. 查看 Actions 执行：https://github.com/WuYan2501/ai_learning_camp/actions
2. 等待 2-3 分钟
3. 访问 Gitee Pages：https://bayue8.gitee.io/ai_learning_camp

---

## 🔍 检查配置是否正确

### 检查清单

- [ ] Gitee 部署公钥已添加，**并勾选了推送权限**
- [ ] GitHub Secrets 中有 `GITEE_PRIVATE_KEY`
- [ ] GitHub Secrets 中有 `GITEE_PASSWORD`
- [ ] Gitee Pages 已手动启动过一次

### 常见问题

**Q: Actions 失败，提示 "Permission denied"**
- 检查 Gitee 公钥是否勾选了「赋予推送权限」

**Q: "Host key verification failed"**
- 正常，第一次运行会出现，Actions 会自动处理

**Q: Gitee Pages 没更新**
- 检查 `GITEE_PASSWORD` 是否正确
- 确认 Gitee Pages 已经手动启动过

---

## 💡 配置后的效果

- ✅ 每次推送到 GitHub → 自动同步到 Gitee
- ✅ Gitee Pages 自动更新
- ✅ 完全免费
- ✅ 无需手动操作

---

**遇到问题？**
查看详细说明：`.github/GITEE_SYNC_SETUP.md`
或查看 Actions 日志排查错误
