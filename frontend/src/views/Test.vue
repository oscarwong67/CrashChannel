<template>
  <div class="text">
    <h1>Submit your photo</h1>
    <h3>{{ result }}</h3>
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
      this.result = 'Calculating...';
      const parsedUrl = encodeURI(this.url);
      axios.get('http://127.0.0.1:5000/test?img=' + parsedUrl).then((response) => {
        console.log(response);
        this.result = parseFloat(response.data.crashes) > 0.70 ? `With ${(response.data.crashes * 100).toFixed(2)}% certainty, I think this is a crash.` : `With ${(response.data['normal traffic'] * 100).toFixed(2)}% certainty, I think this is NOT a crash.`;
      })
    }
  }
};
</script>
