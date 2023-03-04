一、Doze 模式

当设备处于非充电、灭屏状态下静止一段时间，设备将进入睡眠状态，进入Doze模式，延长电池使用时间。Doze模式下系统会定期恢复正常操作，异步执行app的一些同步数据等操作。比如很长时间不使用，系统会允许设备一天访问一次网络等。当设备处于充电状态下，系统将进入标准模式，app执行操作将不被限制。

#二、空闲状态下，优化app耗电
在用户没有使用app的情况下，系统会使app处于idle 状态,
在空闲状态下，系统将会禁止app网络访问以及数据同步

#三、Doze 模式下的限制措施

1.禁止网络访问
2.忽略Wake lock
3.忽略Alarms(setAlarmClock() 、AlarmManager.setAndAllowwhileIdle() 这两个方法除外)
4.忽略WIFI 扫描
5.同步作业调度程序将不被执行

#六、Doze 模式状态

ACTIVE：手机设备处于激活活动状态
INACTIVE：屏幕关闭进入非活动状态
IDLE_PENDING：每隔30分钟让App进入等待空闲预备状态
IDLE：空闲状态
IDLE_MAINTENANCE：处理挂起任务


### 七、Doze 白名单 ###

电量优化白名单 设置 --电池 --电量优化（menu菜单） 会设置查看app 电池优化使用情况 白名单是以xml形式存储(deviceidle.xml) 查看白名单命令


#八、Doze 模式测试方法

1.开启Doze

    adb shell dumpsys deviceidle enable
    // or MTK addadb shell setprop persist.config.AutoPowerModes 1

2.拔掉电池

adb shell dumpsys battery unplug

3.调试Doze状态

    Active ---idle_pending---sensing--location---idle --idle_mantenance
    adb shell dumpsys deviceidle step

4.Dump Doze 状态分析

Doze模式下的信息，包括电池电量优化白名单等

    adb shell dumpsys deviceidle

#九、开启Doze dubug 调试开关

默认false 关闭，设置为true 开启DeviceIdleController.java
private static final boolean DEBUG = false;

作者：程序员Android
链接：https://juejin.cn/post/6844904058189250567
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。