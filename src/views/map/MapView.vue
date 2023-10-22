<script setup lang="ts">
// 地图主页
import * as echarts from 'echarts/core';

import {
    TitleComponent,
    VisualMapComponent,
    GeoComponent,
} from 'echarts/components';

import type {
    TitleComponentOption,
    VisualMapComponentOption,
    GeoComponentOption,

} from 'echarts/components'

import { MapChart, EffectScatterChart, CustomChart } from 'echarts/charts';
import type { MapSeriesOption, EffectScatterSeriesOption, CustomSeriesOption } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';
import { inject, onMounted } from 'vue';
import type { Axios } from 'axios';
import usaJson from '@/assets/world.geo.json'
import country from '@/assets/countryList.json'

const clickArea = defineEmits(['clickArea'])

echarts.use([
    TitleComponent,
    VisualMapComponent,
    GeoComponent,
    MapChart,
    EffectScatterChart,
    CustomChart,
    CanvasRenderer
]);

type EChartsOption = echarts.ComposeOption<
    | TitleComponentOption
    | VisualMapComponentOption
    | GeoComponentOption
    | MapSeriesOption
    | EffectScatterSeriesOption
    | CustomSeriesOption
>;

let mapChart: any

let option: EChartsOption

let countrySet = new Set<string>(country.flatMap(item => item.children.flatMap(i=>i.label)))

let countryList = Array.from(countrySet).map(item => {
    return {name:item,value:1}
})

onMounted(() => {

    const chartDom = document.getElementById('map')!

    resize()

    mapChart = echarts.init(chartDom, 'dark');

    mapChart.showLoading();

    const axios = inject<Axios>("axios")

    mapChart.hideLoading();

    echarts.registerMap('world', usaJson as any, {
        // 此处需要将回龙观、天通苑与通辽标出
    });
    option = {
        title: {
            show: true,
            text: '一带一路地图',
            borderColor: "#FFF",
            // 殷红
            textStyle: {
                color: "#82111f"
            },
            subtextStyle: {
                color: "#82111f"
            },
            subtext: 'the map of B&R',
            top: 64,
            right: 64
        },
        // 藏花红、金黄、姜红
        visualMap: [
            {
                type: 'piecewise',
                show: true,
                hoverLink: false,
                itemWidth: 32,
                id: 'color',
                seriesIndex: 0,
                pieces: [
                    { gte: 1, lte: 1, label: "一带一路合作国家", color: "#ec2d7a" },
                    { gte: 4, lte: 4, label: "还未合作国家", color: "#eeb8c3" },
                ],
                inverse: true,
                orient: 'vertical',
                left: 64,
                top: 64,
                selectedMode: false,
                textStyle: {
                    color: "#FFF"
                }
            },
        ],
        geo: [
            {
                name: '一带一路',
                type: 'map',
                roam: true,
                zoom: 1.1,
                selectedMode: false,
                map: 'world',
                label: {
                    color: "#FFF"
                },
                itemStyle: {
                    areaColor: "#eeb8c3",
                    borderWidth: 0
                },
                emphasis: {
                    label: {
                        color: "#FFF",
                        show: true
                    },
                    itemStyle: {
                        areaColor: "#1661ab",
                        shadowColor: 'rgba(0, 0, 0, 0.7)',
                        shadowBlur: 10
                    }
                }
            }
        ],
        series: [
            {
                name: '一带一路',
                type: 'map',
                geoIndex: 0,
                selectedMode: false,
                map: 'world',
                data: countryList
            }
        ]
    };

    mapChart.setOption(option);

    mapChart.on("click", (params: any) => {
        clickArea('clickArea', params)
    })

    window.onresize = () => {
        resize()
        mapChart.resize()
    };

    function resize() {
        chartDom.style.width = window.innerWidth + 'px'
        chartDom.style.height = window.innerHeight + 'px'
    }

})



function mapResize() {
    console.log('mapResize')
    mapChart.setOption(option, true)
}

defineExpose({
    mapResize,
})

</script>

<template>
    <div id="map"></div>
</template>

<style scoped></style>
