<script setup lang="ts">
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

const currentpin = ref<number[]>([-0.28572, 36.053389]);
const mapelement = ref<HTMLDivElement>();
type Coords = {
    lat: number;
    long: number;
};
const coords = ref<Coords | null>();
let mymap: L.Map | L.LayerGroup<any>;
onMounted(() => {
    console.log('Page launched');
    launchMap();
    mymap.on('click', function (e) {
        coords.value = { lat: e.latlng.lat, long: e.latlng.lng };
    });
    setTimeout(function () {
        window.dispatchEvent(new Event('resize'));
    }, 500);
});

const launchMap = (): void => {
    mymap = L.map(mapelement.value as HTMLElement).setView([-0.28572, 36.063389], 15);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(mymap);
    L.marker([-0.28572, 36.063389]).addTo(mymap).bindPopup('My current location pin.').openPopup();
};
const plotGeoLocation = (): void => {
    L.marker(currentpin.value as unknown as L.LatLngExpression)
        .addTo(mymap)
        .bindPopup('My current location pin.')
        .openPopup();
};

const toggleLocationBar = (): void => {
    coords.value = null;
};
</script>
<template>
    <section class="w-full flex flex-col gap-y-1">
        <div class="search-bar-hero w-full flex flex-col items-center justify-center gap-y-2 md:gap-y-3 py-2 relative z-30">
            <h3 class="capitalize text-xl sm:text-2xl tracking-wide font-semibold text-gray-50">Search your area</h3>
            <div class="search-input flex flex-row w-full items-center justify-center">
                <input type="search" name="search" id="search" placeholder="Search for any place or scan through the map" />
                <button
                    @click="plotGeoLocation"
                    class="px-2 py-1.5 bg-gray-50 border border-gray-300 rounded-r focus:bg-default text-default focus:text-gray-50"
                >
                    <div class="i-carbon-chevron-right text-xl md:text-2xl"></div>
                </button>
            </div>
            <div class="back-btn absolute left-2 top-2 sm:top-3">
                <button class="px-2 py-1 flex items-center justify-center text-gray-50" @click="useRouter().back()">
                    <div class="i-carbon-arrow-left text-xl transition duration-200"></div>
                </button>
            </div>
            <Transition name="fade-in">
                <div
                    v-if="coords != null"
                    class="selected-loc absolute top-[94%] right-4 md:right-auto min-w-[80%] md:min-w-[40%] max-w-[80%] md:max-w-[60%] min-h-[4rem] bg-gray-50 rounded z-30 shadow-md px-2 py-1 flex flex-col items-end md:items-start gap-y-2"
                >
                    <div class="description flex flex-row gap-x-2 justify-between w-full">
                        <div class="name flex flex-col gap-y-1">
                            <span class="text-default opacity-80 uppercase text-sm tracking-wide">Location</span>
                            <span class="text-default text-base tracking-wide">Kabarak</span>
                        </div>
                        <div class="country flex flex-col gap-y-1">
                            <span class="text-default opacity-80 uppercase text-sm tracking-wide">country</span>
                            <span class="text-default text-base tracking-wide">Kenya</span>
                        </div>
                        <div class="name flex flex-col gap-y-1">
                            <span class="text-default opacity-80 uppercase text-sm tracking-wide">Lat</span>
                            <span class="text-default text-base tracking-wide truncate">{{ coords?.lat.toFixed(4) || 'null' }}</span>
                        </div>
                        <div class="country flex flex-col gap-y-1">
                            <span class="text-default opacity-80 uppercase text-sm tracking-wide">long</span>
                            <span class="text-default text-base tracking-wide truncate">{{ coords?.long.toFixed(4) || 'null' }}</span>
                        </div>
                    </div>
                    <div class="submit flex md:flex-row gap-x-4 flex-row-reverse">
                        <button
                            @click="useRouter().back()"
                            class="bg-default opacity-90 rounded text-sm tracking-wide text-gray-50 px-2 py-0.5 hover:opacity-75 transition duration-200"
                        >
                            Submit
                        </button>
                        <button
                            @click="toggleLocationBar"
                            class="opacity-90 rounded text-sm tracking-wide text-tomato px-2 py-0.5 hover:opacity-75 transition duration-200 hover:underline"
                        >
                            Cancel
                        </button>
                    </div>
                </div>
            </Transition>
        </div>
        <div class="map-section min-h-[500px] max-h-[600px] w-full z-10">
            <div id="mapid" ref="mapelement" style="height: 80vh; width: 100vw" class="m-0 p-0">
                <l-map :center="[-0.28572, 36.063389]" :zoom="5">
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
    @apply px-3 py-1.5 rounded-l w-[80%] md:w-[40%] text-sm md:text-base outline-none border-y border-l border-gray-300 focus:border-gray-500 tracking-wide;
}
.search-input:focus-within button {
    @apply border-gray-500;
}

.back-btn button:hover .i-carbon-arrow-left {
    @apply -translate-x-0.5;
}

/* Transitions */
.fade-in-enter-from,
.fade-in-leave-to {
    @apply -translate-y-2 opacity-0;
}
.fade-in-enter-active,
.fade-in-leave-active {
    @apply transition duration-300;
}
</style>
