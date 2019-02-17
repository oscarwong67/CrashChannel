<template>
  <div class="text">
    <h1>Submit your photo</h1>
    <form @submit.prevent="handleSubmit">
      <label>
        Photo URL:
        <input type="url" v-model="url"/>
      </label>
      <button v-on: click="handleSubmit">Submit</button><br><br>
      <img v-bind:src="url" placeholder="">
    </form>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      url: ''
    };
  },
  methods: {
    handleSubmit () {
      const url = encodeURI(this.url);
      axios.get('/test?img=', {params: url}).then((response) => {
        console.log(response);
      })
    }
  }
};
</script>
