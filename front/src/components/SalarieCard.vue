<template>
<div class="main-container ">
    <div class="data-container absolute flex p-2">
        <div class="absolute top-0 right-0">
            <button class="edit-button bg-slate-600 text-white rounded-full w-8 h-8">X</button>
        </div>
        <div class="flex grid-cols-2 gap-0 rounded-xl">
            <div class="flex-col px-2 bg-slate-900 rounded-l-xl flex items-center">
                <div class="row m-auto text-sky-50 font-bold text-4xl">{{ id }}</div>
            </div>
            <div class="flex-col bg-slate-50 rounded-r-xl p-2 ">
                <ul class="my-4 grid grid-rows-4 gap-4">
                    <li class="row">{{ nom }}</li>
                    <li class="row">{{prenom  }}</li>
                    <li class="row">{{ tel }}</li>
                    <li class="row">{{ email }}</li>
                </ul>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'SalarieCard',
    props: {
        id: {
        type: String,
        required: true
        },
        nom: {
        type: String,
        required: true
        },
        prenom: {
        type: String,
        required: true
        },
        tel: {
        type: String,
        required: true
        },
        email: {
        type: String,
        required: true
        }
    }
    }
</script>