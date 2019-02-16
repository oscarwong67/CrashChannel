import Vue from 'vue';
import App from './App.vue';
import router from './router';
import VueFire from 'vuefire';
import firebase from 'firebase/app';
import 'firebase/firestore';

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');

Vue.use(VueFire);

firebase.initializeApp({
  projectId: 'calgaryhacks-2019-mibros-521ab',
  databaseURL: 'https://calgaryhacks-2019-mibros-521ab.firebaseio.com'
});
