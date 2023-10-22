
## The Map of B&R 一带一路覆盖区域地图

作为小约翰可汗的歌迷，为可汗献图大家可以理解吧。

### preview 地图预览

![地图预览](/map.png)

### basic info 介绍

![logo](/logo.png)

"The Belt and Road Initiative (BRI), also known as the Silk Road Economic Belt and the 21st-century Maritime Silk Road, is a cooperative initiative proposed by Chinese President Xi Jinping in September and October 2013 to build the "New Silk Road Economic Belt" and the "21st-century Maritime Silk Road." Relying on existing bilateral and multilateral mechanisms between China and relevant countries, and leveraging effective regional cooperation platforms, the BRI aims to use the historical symbol of the ancient Silk Road, raise the banner of peaceful development, actively develop economic cooperation relationships with partners, and jointly create a community of shared interests, destiny, and responsibility with political mutual trust, economic integration, and cultural inclusiveness.

From 2013 to 2022, China's total imports and exports with BRI countries reached 19.1 trillion US dollars, with an average annual growth rate of 6.4%; the cumulative two-way investment with BRI countries exceeded 380 billion US dollars, of which China's outward direct investment exceeded 240 billion US dollars.

As of the end of June 2023, China has signed more than 230 cooperation documents with more than 150 countries and more than 30 international organizations to jointly build the Belt and Road. From October 17th to 18th, 2023, the third Belt and Road International Cooperation Forum was held in Beijing, which became the most solemn event commemorating the tenth anniversary of the Belt and Road Initiative. The theme of this event was "Building the Belt and Road with High Quality, and Working Together to Achieve Common Development and Prosperity."

“一带一路”（The Belt and Road，缩写B&R）是“丝绸之路经济带”和“21世纪海上丝绸之路”的简称，2013年9月和10月由中国国家主席习近平分别提出建设“新丝绸之路经济带”和“21世纪海上丝绸之路”的合作倡议 [1] 。依靠中国与有关国家既有的双多边机制，借助既有的、行之有效的区域合作平台，一带一路旨在借用古代丝绸之路的历史符号，高举和平发展的旗帜，积极发展与合作伙伴的经济合作关系，共同打造政治互信、经济融合、文化包容的利益共同体、命运共同体和责任共同体。
2013—2022年，中国与共建国家进出口总额累计达到19.1万亿美元，年均增长6.4%；与共建国家双向投资累计超过3800亿美元，其中中国对外直接投资超过2400亿美元。
截至2023年6月底，中国与150多个国家、30多个国际组织签署了230多份共建‘一带一路’合作文件。2023年10月17日至18日，第三届“一带一路”国际合作高峰论坛在北京举行，成为纪念“一带一路”倡议十周年最隆重的活动，此次活动主题为“高质量共建‘一带一路’，携手实现共同发展繁荣”
https://baike.baidu.com/item/%E4%B8%80%E5%B8%A6%E4%B8%80%E8%B7%AF/13132427

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Build

```sh
npm run build-only
```

### Build docker image
```
docker build -t tongliao-universe .
```

### run docker 
```shell
docker run -p 8080:80 --name tongliao-universe -d tongliao-universe
```

## 本站技术分析

总的来说，项目包括数据获取与数据展示部分。其中工作量主要在界面绘制与数据整理。

### 界面部分
界面使用echarts + vue  + antdv处理。echarts主要用来处理大地图展示地图geo数据，antdv提供界面组件。地图展示有我们自己标注的数据需要手动渲染处理一下。

### 数据部分
数据包括两个，一是up主小约翰可汗的视频数据与up信息数据的爬取与整理，二是世界地图数据的获取与整理。视频信息与up可以通过接口爬取，这里使用了python写了一个爬虫工具将数据存在json文件了，但是直接获取到的数据是不能直接使用的，需要识别出视频内容讲的是什么人什么国家什么组织，有的视频会在视频简介中写明，有些则没有，一个通用的方式是，提取视频语音转成文字后交给AI提取主题，但是这个硬件要求太高了，我这个办公本显然不能胜任，最后还是选择手动补全。地图数据网上是可以找到的，但是通辽、回龙观与天通苑是需要自己手动标注的，于是自己标了一下，非专业人士，所以不太美观。