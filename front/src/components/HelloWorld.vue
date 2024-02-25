<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>This {{ dbVal }} comes from the database.</h3>
  </div>
</template>

<script lang="ts">
import axios from "axios";

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      dbVal: "",
    };
  },
  mounted() {
    const path = `http://localhost:8000/`;
    axios
      .get(path)
      .then((res) => {
        if (res.data != null) {
          this.dbVal = res.data["val"];
        }
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>
