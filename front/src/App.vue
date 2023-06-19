<template>
  <NavBar/>
  <div class="flex my-4 px-8">
    <p class="text-3xl">Liste des salariés</p>
  </div>
  <div class="grid grid-cols-3 gap-4 w-11/12 mx-auto">
    <button v-for="salarie in salaries" :key="salarie.id_salarie" class="relative font-thin text-xl" @click="openModal(salarie)">
      <div class="absolute inset-x-0 h-full -bottom-2 bg-slate-300 border border-gray-500 rounded-lg"></div>
      <div class="relative bg-slate-200 border border-gray-500 rounded-lg py-4 px-10 transition transform duration-100 hover:translate-y-2">
        <h3 class="text-lg text-gray-900 font-semibold">{{ salarie.id_salarie }}</h3>
        <p class="text-gray-900">{{ salarie.first_name }} {{ salarie.last_name }}</p>
        <p class="text-gray-900">{{ salarie.phone_number || '-' }}</p>
        <p class="text-gray-900">{{ salarie.email }}</p>
      </div>
    </button>

    <button class="relative font-thin text-xl" @click="openCreateModal(null)">
      <div class="relative bg-slate-200 border border-gray-500 rounded-lg py-4 px-10">
        <h3 class="text-lg text-gray-900 font-semibold">Créer un salarié</h3>
      </div>
    </button>
  </div>

    <!-- Fenêtre CREATE modale -->
    <div v-if="isCreateModalOpen" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white rounded-lg p-8">
      <h3 class="text-lg font-semibold">{{ selectedSalarie.id_salarie }}</h3>
      <form @submit.prevent="createSalarie" class="space-y-4">
        <div>
          <label class="block text-gray-700 font-semibold">Prénom</label>
          <input v-model="selectedSalarie.first_name" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div>
          <label class="block text-gray-700 font-semibold">Nom</label>
          <input v-model="selectedSalarie.last_name" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div>
          <label class="block text-gray-700 font-semibold">Numéro de téléphone</label>
          <input v-model="selectedSalarie.phone_number" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div>
          <label class="block text-gray-700 font-semibold">Email</label>
          <input v-model="selectedSalarie.email" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div class="flex justify-end">
          <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md">Créer</button>
          <button type="button" class="px-4 py-2 bg-gray-500 text-white rounded-md ml-2" @click="closeCreateModal()">Annuler</button>
        </div>
      </form>
    </div>
  </div>

  
  <!-- Fenêtre UPDATE modale -->
  <div v-if="isModalOpen" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white rounded-lg p-8">
      <h3 class="text-lg font-semibold">{{ selectedSalarie.id_salarie }}</h3>
      <form @submit.prevent="updateSalarie" class="space-y-4">
        <div>
          <label class="block text-gray-700 font-semibold">Prénom</label>
          <input v-model="selectedSalarie.first_name" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div>
          <label class="block text-gray-700 font-semibold">Nom</label>
          <input v-model="selectedSalarie.last_name" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div>
          <label class="block text-gray-700 font-semibold">Numéro de téléphone</label>
          <input v-model="selectedSalarie.phone_number" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div>
          <label class="block text-gray-700 font-semibold">Email</label>
          <input v-model="selectedSalarie.email" type="text" class="border border-gray-300 rounded-md p-2 w-full" />
        </div>
        <div class="flex justify-end">
          <button type="button" class="px-4 py-2 bg-red-500 text-white rounded-md mr-2" @click="deleteSalarie()" v-if="selectedSalarie">Supprimer</button>
          <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-md">Mettre à jour</button>
          <button type="button" class="px-4 py-2 bg-gray-500 text-white rounded-md ml-2" @click="closeModal()">Annuler</button>
        </div>
      </form>
    </div>
  </div>

</template>


<script>
import NavBar from './components/NavBar.vue';


export default {
  name: 'App',
  components: {
    NavBar,

  },
  data() {
    return {
      salaries: [],
      isModalOpen: false,
      isCreateModalOpen:false,
      selectedSalarie: {},
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
  },

  async updateSalarie() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/salarie/${this.selectedSalarie.id_salarie}/`, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.selectedSalarie),
        });
        if (response.ok) {
          // Mise à jour réussie
          console.log('Salarie mis à jour');
          this.closeModal()
          this.fetchData()
        } else {
          // Erreur lors de la mise à jour
          console.error('Erreur lors de la mise à jour du salarie');
        }
      } catch (error) {
        console.error(error);
      }
  },

  async createSalarie() {
    try {
      console.log(this.selectedSalarie);
      const response = await fetch('http://127.0.0.1:8000/api/salarie/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.selectedSalarie),
      });
      if (response.ok) {
        console.log('Salarie créé');
        this.closeCreateModal();
        this.fetchData();
      } else {
        console.error('Erreur lors de la création du salarié');
      }
    } catch (error) {
      console.error(error);
    }
  },

  async deleteSalarie() {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/salarie/${this.selectedSalarie.id_salarie}/`, {
        method: 'DELETE',
      });
      if (response.ok) {
        console.log('Salarie supprimé');
        this.closeModal();
        this.fetchData()
      } else {
        console.error('Erreur lors de la suppression du salarie');
      }
    } catch (error) {
      console.error(error);
    }

  },

  openCreateModal() {
    const maxId = this.salaries.reduce((max, salarie) => {
      const id = parseInt(salarie.id_salarie);
      return id > max ? id : max;
    }, 0);
    this.selectedSalarie = { id_salarie: (maxId + 1).toString(), first_name: '', last_name: '', phone_number: '', email: '' };
    this.isCreateModalOpen = true;
  },

  closeCreateModal() {
    this.selectedSalarie = null;
    this.isCreateModalOpen = false;
  },

  openModal(salarie) {
    this.selectedSalarie = salarie ? { ...salarie } : { first_name: '', last_name: '', phone_number: '', email: '' };
    this.isModalOpen = true;
  },
  
  closeModal() {
    this.selectedSalarie = null;
    this.isModalOpen = false;
  },
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
