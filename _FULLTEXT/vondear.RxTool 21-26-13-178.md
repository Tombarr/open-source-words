rxtool 工欲善其事必先利其器！ android开发过程经常需要用到各式各样的工具类，虽然大部分只需谷歌 百度一下就能找到； 但是有时候急需使用却苦苦搜寻不到，于是整理了自己平常用到的工具类，以便以后的使用。 如何使用它 step 1 先在 build gradle project xxxx 的 repositories 添加 allprojects repositories maven url https jitpack io step 2 然后在 build gradle module app 的 dependencies 添加 dependencies 基础工具库 implementation com github vondear rxtool rxkit v2 0 4 ui库 implementation com github vondear rxtool rxui v2 0 4 功能库（zxing扫描与生成二维码条形码 支付宝 微信） implementation com github vondear rxtool rxfeature v2 0 4 arcgis for android工具库（api：100 1以上版本） implementation com github vondear rxtool rxarcgiskit v2 0 4 使用方法 在application中初始化 rxtool init this 注：v2 0 0以后版本是分多模块的版本 文档 可以参考文档来调用相对应的api，欢迎指教 点我看文档 点我看文档 点我看文档 近期更新日志 version description v2 0 1 新增（高德 百度）地图导航工具新增arcgis工具类 v2 0 0 重构成多模块 demo介绍 rxphototool操作ucrop裁剪图片 展示头像 选择头像 裁剪头像 二维码与条形码的扫描与生成 扫描二维码 生成二维码 扫描条形码 常用的dialog展示 确认弹窗 确认取消弹窗 输入框弹窗 选择日期弹窗 形状加载弹窗 acfun加载弹窗 其他功能展示 webview的封装（可播放视频） rxtexttool操作demo rxtoast的展示使用 进度条的艺术 网速控件 联系人侧边栏快速导航 图片的缩放艺术 蛛网控件 仿斗鱼验证码控件 demo 与 打赏 demo 扫描二维码 or 点击二维码 下载 微信打赏 支付宝打赏 如果你帮助到了你可以点右上角 star 支持一下 谢谢！ 你也还可以扫描下面的二维码打赏鼓励一下 请作者喝一杯咖啡。 如果在捐赠留言中备注名称将会被记录到列表中 如果你也是github开源作者捐赠时可以留下github项目地址或者个人主页地址链接将会被添加到列表中起到互相推广的作用 捐赠列表 闲聊群 435644020