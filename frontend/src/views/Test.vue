<template>
  <div>
    <h1>This is the testing page</h1>
    <form @submit.prevent="handleSubmit">
      <label>
        Photo URL:
        <input type="url" v-model="url"/>
      </label>
    </form>
    <img v-bind:src="url" placeholder="">
  </div>
</template>

<script>
export default {
  data () {
    return {
      url: ''
    };
  },
  methods: {
    handleSubmit () {
      const parsedUrl = encodeURI(this.url);
      axios.get('/test?img=' + parsedUrl).then((response) => {

      })
    }
  }
};
</script>
