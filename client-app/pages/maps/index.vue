<script setup lang="ts">
import 'leaflet/dist/leaflet.css';
import * as L from 'leaflet';

definePageMeta({
    layout: false,
});

const currentpin = ref<number[]>([-0.28572, 36.053389]);

let mymap: L.Map | L.LayerGroup<any>;
onMounted(() => {
    mymap = L.map('mapid').setView([-0.28572, 36.063389], 15);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(mymap);

    // L.marker([-0.28572, 36.063389]).addTo(mymap).bindPopup('My current location pin.').openPopup();
    // plotGeoLocation();
    L.marker([-0.28572, 36.063389]).addTo(mymap).bindPopup('My current location pin.').openPopup();
    mymap.on('click', function (e) {
        alert(e.latlng);
    });
});

const plotGeoLocation = (): void => {
    L.marker(currentpin.value as unknown as L.LatLngExpression)
        .addTo(mymap)
        .bindPopup('My current location pin.')
        .openPopup();
};
</script>
<template>
    <section class="w-full flex flex-col gap-y-1">
        <div class="search-bar-hero w-full flex flex-col items-center justify-center gap-y-2 md:gap-y-3 py-2 relative">
            <h3 class="capitalize text-xl sm:text-2xl tracking-wide font-semibold text-gray-50">Search your area</h3>
            <div class="search-input flex flex-row w-full items-center justify-center">
                <input type="search" name="search" id="search" placeholder="search" />
                <button
                    @click="plotGeoLocation"
                    class="px-2 py-1.5 bg-gray-50 border border-gray-300 rounded-r focus:bg-default text-default focus:text-gray-50"
                >
                    <div class="i-carbon-chevron-right text-2xl"></div>
                </button>
            </div>
            <div class="back-btn absolute left-2 top-2 sm:top-3">
                <button class="px-2 py-1 flex items-center justify-center text-gray-50">
                    <div class="i-carbon-arrow-left text-xl transition duration-200"></div>
                </button>
            </div>
        </div>
        <div class="map-section min-h-[500px] max-h-[600px] w-full">
            <div id="mapid" style="height: 80vh">
                <l-map class="w-full h-full" :center="[-0.28572, 36.063389]">
                    <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"></l-tile-layer>
                </l-map>
            </div>
        </div>
    </section>
</template>

<style scoped>
.search-bar-hero {
    background-image: url('@/assets/images/pattern-bg.avif');
    @apply bg-cover min-h-[8rem] sm:min-h-[8rem];
}

.search-input input {
    @apply px-3 py-1.5 rounded-l w-[80%] md:w-[40%] outline-none border-y border-l border-gray-300 focus:border-gray-500 tracking-wide;
}
.search-input:focus-within button {
    @apply border-gray-500;
}

.back-btn button:hover .i-carbon-arrow-left {
    @apply -translate-x-0.5;
}
</style>
