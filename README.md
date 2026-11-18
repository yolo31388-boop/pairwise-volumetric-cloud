# pairwise-volumetric-cloud

云层穿帮、闪烁、飞行穿过时一块块：raymarch 步长按屏幕空间固定；时域重投影用上一帧深度但云没深度；光照只采样单点；阴影图分辨率随视角变；噪声纹理三线性在低精度；云层边界没做 early out；半分辨率升采样按颜色不按深度；风向和云移动速度不同步；相机进入云体时近平面裁掉；多光源散射没归一。render/volumetric_cloud.py 是核心，tests/test_volumetric_cloud.py 15个红。要修的是：世界空间步长；云深度重投影；多点光照采样；稳定阴影级联；噪声精度；边界提前退出；深度感知升采样；风向同步；近平面云体；散射能量归一。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
