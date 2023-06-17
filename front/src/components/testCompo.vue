<template>
    <div class="grid grid-cols-3 gap-4">
      <div v-for="item in items" :key="item.id" class="bg-white p-4 shadow rounded-md">
        <h3 class="text-lg font-semibold">{{ item.title }}</h3>
        <p class="text-gray-500">{{ item.description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name:'testCompo',
    data() {
      return {
        items: [
          {
            id: 1,
            title: "Card 1",
            description: "This is the description of card 1."
          },
          {
            id: 2,
            title: "Card 2",
            description: "This is the description of card 2."
          },
          {
            id: 3,
            title: "Card 3",
            description: "This is the description of card 3."
          },
          {
            id: 4,
            title: "Card 4",
            description: "This is the description of card 1."
          },
          {
            id: 5,
            title: "Card 5",
            description: "This is the description of card 2."
          },
          {
            id: 6,
            title: "Card 6",
            description: "This is the description of card 3."
          }
        ]
      };
    }
  };
  </script>
  