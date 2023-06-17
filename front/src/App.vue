<template>
  <NavBar/>
  <div class="flex my-4 px-8">
    <p class="text-3xl">Liste des salariés</p>
  </div>
  <div class="grid grid-cols-3 gap-4 w-11/12 mx-auto">
    <button v-for="salarie in salaries" :key="salarie.id_salarie" class="relative font-thin text-xl">
      <div class="absolute inset-x-0 h-full -bottom-2 bg-slate-300 border border-gray-500 rounded-lg"></div>
      <div class="relative bg-slate-200 border border-gray-500 rounded-lg py-4 px-10 transition transform duration-100 hover:translate-y-2">
        <h3 class="text-lg text-gray-900 font-semibold">{{ salarie.id_salarie }}</h3>
        <p class="text-gray-900">{{ salarie.first_name }} {{ salarie.last_name }}</p>
        <p class="text-gray-900">{{ salarie.phone_number || '-' }}</p>
        <p class="text-gray-900">{{ salarie.email }}</p>
      </div>
    </button>
  </div>
</template>


<script>
import NavBar from './components/NavBar.vue';
// import SalarieCard from './components/SalarieCard.vue';
// import testCompo from './components/testCompo.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    // SalarieCard,
    // testCompo
  },
  data() {
    return {
      salaries: []
    };
  },
  methods: {
  async fetchData() {
    try {
      var response = await fetch('http://127.0.0.1:8000/api/salarie/');
      let data = await response.json();
      console.log(data);
      this.salaries = data;
    } catch (error) {
      console.error(error);
    }
  }
},
mounted() {
  this.fetchData();
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
