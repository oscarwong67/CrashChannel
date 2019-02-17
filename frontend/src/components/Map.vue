<template>
  <div>
    <MglMap
      v-bind:accessToken='key'
      v-bind:mapStyle='mapStyle'
      container='map'
      v-bind:minZoom='10'
      v-bind:center='center'
      @load='mapLoaded'
    >
      <MglMarker v-for="(camera, index) in cameras" v-bind:key="index" v-bind:coordinates="processCoords(camera)" v-bind:color="processColor(camera)" />
    </MglMap>
  </div>
</template>

<script>
import { db } from '../main.js';
import { MglMap, MglMarker } from 'vue-mapbox';
import keys from '@/keys.json';
import mapboxgl from 'mapbox-gl';

export default {
  name: 'Map',
  components: {
    MglMap,
    MglMarker
  },
  data: function () {
    return {
      key: keys['mapbox-key'],
      mapStyle: 'mapbox://styles/mapbox/streets-v10?optimize=true',
      center: new mapboxgl.LngLat(-114.0708, 51.0486),
      cameras: []
    };
  },  
  firestore () {
    console.log('yo');
    return {
      cameras: db.collection('cameras'),
    };
  },
  methods: {
    mapLoaded (event) {
      this.map = event.map;
    },
    processCoords (camera) {
      return [
        camera.coords.lng,
        camera.coords.lat
      ]
    },
    processColor (camera) {
      if (camera.crashData.isCrash) {
        return "red";
      } else {
        return "green";
      }
    }
  },
  created () {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = mapboxgl;
  }
};
</script>

<style>
#map {
  width: 100%;
  height: 500px;
}

.mapboxgl-canvas {
  left: 8px;
}
</style>
