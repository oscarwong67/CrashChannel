import Vue from 'vue';
import App from './App.vue';
import router from './router';
import VueFire from 'vuefire';
import firebase from 'firebase/app';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'firebase/firestore';

Vue.use(VueFire);

firebase.initializeApp({
  apiKey: 'AIzaSyBVyu1423KMWAn0Mn3OMxiEshRlpi01IlU',
  authDomain: 'calgaryhacks-2019-mibros-521ab.firebaseapp.com',
  databaseURL: 'https://calgaryhacks-2019-mibros-521ab.firebaseio.com',
  projectId: 'calgaryhacks-2019-mibros-521ab',
  storageBucket: 'calgaryhacks-2019-mibros-521ab.appspot.com',
  messagingSenderId: '224334429078'
});

window.mapboxgl = require('mapbox-gl');

export const db = firebase.firestore();

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
