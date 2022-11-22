<script setup lang="ts">
import 'leaflet/dist/leaflet.css';
import leaflet from 'leaflet';

definePageMeta({
    layout: false,
});

let mymap;
onMounted(() => {
    mymap = leaflet.map('mapid').setView([51.505, -0.09], 13);
    leaflet
        .tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        })
        .addTo(mymap);
});
</script>
<template>
    <section class="w-full flex flex-col gap-y-1">
        <div class="search-bar-hero w-full flex flex-col items-center justify-center gap-y-2 sm:gap-y-3 py-2">
            <h3 class="capitalize text-xl sm:text-2xl tracking-wide font-semibold text-gray-50">Search your area</h3>
            <div class="search-input flex flex-row w-full items-center justify-center">
                <input type="search" name="search" id="search" placeholder="search" />
                <button class="px-2 py-1.5 bg-gray-50 border border-gray-300 rounded-r focus:bg-default text-default focus:text-gray-50">
                    <div class="i-carbon-chevron-right text-2xl"></div>
                </button>
            </div>
        </div>
        <div class="map-section min-h-[500px] max-h-[600px] w-full">
            <div id="mapid" style="height: 80vh">
                <l-map class="w-full" :center="[47.41322, -1.219482]" style="height: 80vh">
                    <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"></l-tile-layer>
                </l-map>
            </div>
        </div>
    </section>
</template>

<style scoped>
.search-bar-hero {
    background-image: url('@/assets/images/pattern-bg.avif');
    @apply bg-cover min-h-[6rem] sm:min-h-[8rem];
}

.search-input input {
    @apply px-3 py-1.5 rounded-l w-[80%] sm:w-[40%] outline-none border-y border-l border-gray-300 focus:border-gray-500 tracking-wide;
}
.search-input:focus-within button {
    @apply border-gray-500;
}
</style>
