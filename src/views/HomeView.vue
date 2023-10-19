<script setup lang="ts">
import MapView from './map/MapView.vue';
import {
  QuestionCircleOutlined,
  SyncOutlined,
  ShareAltOutlined,
  EyeOutlined,
  CopyOutlined
} from '@ant-design/icons-vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import liganma from '@/assets/liganma.json'
import ClipboardJS from 'clipboard'
import { message } from 'ant-design-vue';
import Card from '@/components/Card.vue';
import List from '@/components/List.vue';
import countryList from '@/assets/countryList.json'


const [messageApi, contextHolder] = message.useMessage();

const map = ref()

const qrcodeVisible = ref<boolean>(false);

const shareVisible = ref<boolean>(false);

const aeraInfoVisible = ref<boolean>(false);

const unitInfoVisible = ref<boolean>(false)

const activeTitle = ref<string>();

const personInfo = ref<Array<{
  
}>>([]);

const countryInfo = ref<Array<{
  
}>>([]);

const organizationInfo = ref<Array<{

}>>([]);

const href = window.location.href

const followInfo = {
  liganma: liganma
}
const router = useRouter()

function toAbout() {
  router.push({ name: "about" })

}

function resize() {
  map.value.mapResize()
}

function share() {
  console.log(href)
  // 打开弹窗展示二维码
  shareVisible.value = true
  new ClipboardJS("#copyShareLink")
}

function follow() {
  // 打开李干嘛与小约翰的弹窗
  qrcodeVisible.value = true
}

const activeUnit = ref<{
  title?:string,
  sign?:string
}>()

function clickArea(params: any) {
  // 如果data有数据则打开弹窗
  console.log(params)
  
}

</script>

<template>
  <div class="content">
    <MapView ref="map" @click-area="clickArea"></MapView>

    <!-- <Card></Card> -->
    <a-float-button-group shape="square" :style="{ right: '64px' }">
      <!-- 关于  -->
      <a-float-button @click="toAbout" tooltip="关于">
        <template #icon>
          <QuestionCircleOutlined />
        </template>
      </a-float-button>
      <!-- 同步  -->
      <a-float-button @click="resize" tooltip="重置地图">
        <template #icon>
          <SyncOutlined />
        </template>
      </a-float-button>
      <!-- 分享  -->
      <a-float-button @click="share" tooltip="分享">
        <template #icon>
          <ShareAltOutlined />
        </template>
      </a-float-button>
      <!-- 关注  -->
      <a-float-button @click="follow" tooltip="关注">
        <template #icon>
          <EyeOutlined />
        </template>
      </a-float-button>
    </a-float-button-group>

    <div class="models">
      <a-modal v-model:open="qrcodeVisible" title="感谢关注" centered @ok="qrcodeVisible = false">
        <a-row :gutter="[16, 24]" justify="space-around" >
          <a-col :span="11" justify="space-around" align="middle" class="space-box">
            <Card :title="followInfo.liganma.name" :avatar="'image/'+ followInfo.liganma.avatar" :qrcode="followInfo.liganma.space" :sign="followInfo.liganma.sign"></Card>

          </a-col>
        </a-row>

        <template #footer>
        </template>
      </a-modal>

      <a-modal v-model:open="shareVisible" title="分享给朋友" centered @ok="shareVisible = false">
        <a-row :gutter="[16, 24]" justify="space-around" align="middle">
          <a-col :span="24" justify="space-around" align="middle">

            <a-space direction="vertical" style="width: 100%;">
              <a-input-group compact>
                <a-button>
                  链接
                </a-button>
                <a-input :value="href" style="width: calc(100% - 200px)" id="shareLink" />
                <a-tooltip title="复制链接">
                  <a-button id="copyShareLink" data-clipboard-action="copy" data-clipboard-target="#shareLink">
                    <template #icon>
                      <CopyOutlined />
                    </template>
                  </a-button>
                </a-tooltip>
              </a-input-group>
              <a-qrcode error-level="H" :value="href" icon="favicon.ico" />
            </a-space>

          </a-col>
        </a-row>

        <template #footer></template>
      </a-modal>

      <a-modal v-model:open="aeraInfoVisible" :title="activeTitle" centered @ok="aeraInfoVisible = false" width="1080px" >
        <a-row justify="space-around" >
          <a-col :span="7" justify="space-around" align="middle" class="space-box">
            
            <List title="奇葩小国" :list="countryInfo"></List>

          </a-col>

          <a-col :span="7" justify="space-around" align="middle" class="space-box">
            
            <List title="硬核狠人" :list="personInfo"></List>

          </a-col>

          <a-col :span="7" justify="space-around" align="middle" class="space-box">
            <List title="神奇组织" :list="organizationInfo"></List>
          </a-col>
        </a-row>

        <template #footer></template>
      </a-modal>

      <a-modal v-model:open="unitInfoVisible" title="单位信息" centered @ok="unitInfoVisible = false" >
        <a-row justify="space-around" >
          <a-col :span="24" justify="space-around" align="middle">
            
            <Card :title="activeUnit?.title" :sign="activeUnit?.sign" ></Card>

          </a-col>
        </a-row>

        <template #footer></template>
      </a-modal>
    </div>
  </div>
</template>

<style scoped>
.content {
  position: relative;
}

.space-box{
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px; 
  border-radius: 15px; 
  padding: 10px;
}
</style>
