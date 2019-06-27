# 非正式用例

Use Case 1 用户注册登录

主成功场景：
用户输入账号及其密码，通过验证后，登录。

交替场景：
用户尚未注册；
用户忘记密码；
用户看不清验证图。

![用例图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%94%A8%E4%BE%8B4.png?raw=true)

![活动图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E6%B4%BB%E5%8A%A84.png?raw=true)


Use Case 2 任务者接受任务

主成功场景：
任务者接受任务，发布者确认后同意请求，任务者成功在在我的任务界面获取任务信息。

交替场景：
任务者接受任务后发现任务无法完成，联系发布者，任务取消；
发布者审核后不同意任务者接受任务，任务取消；
任务者在任务期限内未完成任务，任务失败，扣除积分。

![用例图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%94%A8%E4%BE%8B1.png?raw=true)

![活动图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E6%B4%BB%E5%8A%A81.png?raw=true)

Use case 3 发布者发布任务

主成功场景：
发布者发布任务后，任务者接受任务，发布者同意，任务开始。

交替场景：
发布者发布任务后，没有任务者接受任务，任务超过时间期限；
发布者发布任务后，自行取消任务；
发布者发布任务后，任务者接受任务，发布者不同意，任务重新回到任务中心。

![用例图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%94%A8%E4%BE%8B2.png?raw=true)

![活动图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E6%B4%BB%E5%8A%A82.png?raw=true)

Use case 4 任务者提交任务

主成功场景：
任务者完成任务后，发布者确认任务完成，系统发放积分和酬劳。

交替场景：
发布者对任务完成的情况不满意，积分和酬劳不予发放；
其他任务者先于提交任务并确认。

![用例图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%94%A8%E4%BE%8B3.png?raw=true)

![活动图](https://github.com/strugglinggreenhands/SpareMoney_Documents/blob/gh-pages/images/%E6%B4%BB%E5%8A%A83.png?raw=true)

# 简述用例

Use case 5.1 修改密码
Actor：用户
Type：Primary
Description：用户进入页面，切换到个人中心的页面，选择修改密码，并输入新密码并提交。
