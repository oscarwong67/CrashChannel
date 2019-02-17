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
      url: '',
      result: ''
    };
  },
  methods: {
    handleSubmit () {
      const parsedUrl = encodeURI(this.url);
      axios.get('http://127.0.0.1:5000/test?img=' + parsedUrl).then((response) => {
        this.result = parseFloat(response.data.crashes) > 0.30 ? 'This is likely an image of a crash.' : 'This is image likely does not contain a crash.';
      })
    }
  }
};
</script>
