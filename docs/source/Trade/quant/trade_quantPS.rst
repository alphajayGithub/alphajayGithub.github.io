========================================
QuantPS
========================================

Overview
-----------------

`QuickLook <https://www.alphajay.online/MDs/Quant>`_

Language
-----------------

C++:

    跑策略用,实盘交易

    C++是大型项目里不可或缺的部分, 所以基础一定要比Python Matlab R这种研究语言的更牢固才行


Python:


    做策略用,历史模拟

    逻辑简单代码少,运行效率则C/C++更佳稳定快速

    数据处理 NumPy SciPy Pandas; 可视化 Matplotlib PyQT wxPython

    社区: Joinquant 优矿 使用体验好,回测速度感人

Matlab:
`Auto-Trader <http://www.atrader.com.cn/>`_

    做策略用,历史模拟, 需要用到大量复杂计算

    平台 Auto-trader数据非常全，提供了各种强大的金融函数与金融工具箱，且速度非常快！

    社区: DigQuant论坛大量基于matlab的策略代码可参考,适合上手

R:



Tutorial
-----------------

视频教程:

`金融数据用JQData <https://zhuanlan.zhihu.com/p/55964843>`_

`VNPY架构与量化策略实现 <https://www.bilibili.com/video/BV1yJ411u7WG>`_

`quantaxis量化解决方案 <https://www.bilibili.com/video/av47284727/>`_

`清华计算机博士带你学-Python金融量化分析 <https://www.bilibili.com/video/BV1i741147LS/>`_

`量化投资全集(投资策略、搭建平台)  <https://www.bilibili.com/video/BV1CJ411Y7j9>`_

Repos
-----------------

QUANTAXIS:
`QUANTAXIS.gitee   <https://gitee.com/ecoteam/QUANTAXIS>`_
`QUANTAXIS   <https://github.com/QUANTAXIS/QUANTAXIS>`_

vnpy:
`vnpy   <https://github.com/vnpy/vnpy>`_

`[精]量化交易，你选择用什么平台？ - 余天的回答 - 知乎
<https://www.zhihu.com/question/326160252/answer/852531737>`_


    余天:

    * 从最小的FAAS的服务：云条件单（文华）

    * 到中型的PAAS服务：提供云量化环境 **JoinQuant/ricequant,推荐聚宽** `JoinQuant <https://www.joinquant.com/study>`_

    * 再到落地的本地软件框架:  **quantaxis/tqsdk**

    都绕不开对于这几个流的处埋至于怎么有效的进行组织，每个作者都给出了不同的解决方案

    * vnpy最开始基于qt的timer/py的thread来做事件引擎在vn2．0改成了自研的事件框架

    * tqsdk是基于asyncLoop来构也基于OTGMG两个服务来分别提供交易流/数据流

    * quantaxise基于迭代器/rabbitmq/qapubsub*实现的事件的分发和处理

    要注意的是解决方案是面向场景的脱离了场景来比较优劣没有任何意义, quantaxis我遇到的场景主要是对于多策略（量比较大）/多账户成百上千个期货账户和股票账户实盘/模拟）场景进行的优化

    木十一:

    EasyTrader，不错，可以说是当下散户和小机构唯一可行的股票自动交易程序了，不够成熟，不稳定。

    我们的主要都是自己写，喜欢轻便灵活，价格要便宜，最好免费，主要针对国内。

    数据源：爬新浪和Tushare(不错，数据种类有限)，通达信数据文件也可以读，存在Mysql。

    分析和回测：大多用SQL和Excel，python，借鉴PyAlgoTrade。

    策略：python和GoLang自己写。

    自动交易：RabbitMQ、python、C#

    链接：https://www.zhihu.com/question/326160252/answer/695566139








