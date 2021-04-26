# Odoo 12开发手册

本手册包含五个部分，首先是 Odoo 框架的概述：创建开发环境并一起开发第一个 Odoo 应用。在对 Odoo 主要组件渐渐熟悉后，我们将深入更进一步的细节-模型、业务逻辑、视图这三个主要应用层。最后我们需要把应用部署到生产环境、进行维护，这将在最后一章进行讲述。

TODO: 图片地址修改为公共图床或其它CDN 

## 全书目录

➣第一章 [使用开发者模式快速入门 Odoo 12](1.md)

*初稿完成时间：2018年12月30日深夜（今天上海下雪了❄️❄️❄️☃️，显然地上并无积雪）*

➣第二章 [Odoo 12开发之开发环境准备](2.md)

*初稿完成于2019年1月4日 @神奇的地铁16号线上*

➣第三章 [Odoo 12 开发之创建第一个 Odoo 应用](3.md)

*初稿完成于2019年1月6日（ 数了数页数快完成1/3了，嗯，今天晚餐加🍗）*

➣第四章 [Odoo 12 开发之模块继承](4.md)

*初稿完成时间：2019年1月8日凌晨*

➣第五章 [Odoo 12开发之导入、导出以及模块数据](5.md)

*初稿完成时间：2019年1月9日*

➣第六章 [Odoo 12开发之模型 - 结构化应用数据](6.md)

*初稿完成时间：2019年1月11日深夜*

➣第七章 [Odoo 12开发之记录集 - 使用模型数据](7.md)

*初稿完成时间：2019年1月12日（行程过半了，但真正的挑战才刚刚开始💪💪💪）*

➣第八章 [Odoo 12开发之业务逻辑 - 业务流程的支持](8.md)

*初稿完成时间：2019年1月14日凌晨*

➣第九章 [Odoo 12开发之外部 API - 集成第三方系统](9.md)

*初稿完成时间：2019年1月15日*

➣第十章 [Odoo 12开发之后台视图 - 设计用户界面](10.md)

*初稿完成时间：2019年1月17日*

➣第十一章 [Odoo 12开发之看板视图和用户端 QWeb](11.md)

*初稿完成时间：2019年1月19日*

➣第十二章 [Odoo 12开发之报表和服务端 QWeb](12.md)

*初稿完成时间：2019年1月20日*

➣第十三章 [Odoo 12开发之创建网站前端功能](13.md)

*初稿完成时间：2019年1月21日*

➣第十四章 [Odoo 12开发之部署和维护生产实例](14.md)

*初稿完成时间：2019年1月23日*

代码地址：[Source Code](source-code)

Notes:

1、文中 Model 一并译为模型，Module 译为模块，而 extend/extension 则根据具体上下文使用扩展和继承。

2、Base View 原译为基视图，后修改为 base 视图

3、部分代码在测试中发现错误将直接进行修改并不在文中单独注明

4、文中插件(Addon)、应用(Application)和 Addon Module（插件模块）将出现混用的情况。但熟悉 Odoo 的朋友都知道仅当在__manifest__.py 中声明 application:True 时才可在 Apps 过滤中显示

5、原书在进行不同功能测试时使用了多个不同数据库，我做了一定程度上的统一

6、关于 in-place 和 addons：我的理解in-place即是不创建新模型在原处进行修改，本系列中部分保留了 in-place 未予翻译；而 addons 我译为插件，但总觉得不太合适，因为它与传统认为的 plugins 又不尽相同

7、Action 文中多译为操作，如 Window Action 译为窗口操作，或可译为动作或行动

8、Transient model在文章中使用了过渡模型和临时模型的译法

9、Compose 在文中译为了重构，因 Recordset本身是不可变的，似为 decompose 多译为解构，因此译作重构

10、关于 function(函数) 和 method(方法)：方法一般是类中的函数，而函数则是类以外的函数，原文中混用比较严重，我对大部分做了调整，但可能也保留了部分原文的说法

11、follower 一般根据语境译为粉丝、追随者，其实订阅者可能更为贴切，但本系列中出于笔者习惯大多数未予以翻译，保持了原英文；partner 也基本如此

12、按照 PEP8规范，类上方应空两行，方法上方应空一行，Alan 在代码中为节省空间，类的代码上方仅空了一行