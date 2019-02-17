<template>
  <div class="hello">
    <h1 style="font-weight: 700">{{ msg }}</h1>
    <p
      style="font-size: 20px"
    >Get live updates about traffic incidents in your area and during your everyday commute!</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  computed: {
    objects: function () {
      return null;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
.list{
  margin: 0px 50px 50px 50px;
}
/* ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
</style>
