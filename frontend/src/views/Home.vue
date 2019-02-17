<template>
  <div class="home text">
    <Map />
  </div>
</template>

<script>
// @ is an alias to /src
import Map from '@/components/Map.vue';

export default {
  name: 'home',
  components: {
    Map
  }
};
</script>

<style>
  html{
    background-color:  #E6ECF0;
  }
  .text{
    color: #32496d;
  }

</style>
