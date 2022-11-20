<script setup lang="ts">
import '@/assets/dist/leaflet.css';
definePageMeta({
    layout: false,
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
            <div id="map-id" class="h-full w-full bg-gray-300">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium placeat modi velit, ut amet nihil. Voluptatibus aperiam
                repellat ipsa beatae, delectus, sed quod aliquam adipisci at blanditiis ab dolorem ipsum!
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
