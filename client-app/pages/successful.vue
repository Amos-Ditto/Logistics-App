<script setup lang="ts">
definePageMeta({
    layout: false,
});
</script>
<template>
    <main class="w-full flex flex-col">
        <NuxtLayout name="home">
            <header class="w-full flex flex-col py-2 px-4 mt-2">
                <h3 class="text-2xl md:text-3xl tracking-wide">Hey Amos!</h3>
            </header>
            <div class="body w-full flex flex-col gap-y-3">
                <div class="icon w-full flex items-center justify-center py-2 flex-col">
                    <img src="@/assets/images/check-circle.svg" alt="" />
                </div>
                <article class="w-full flex flex-row items-center justify-center">
                    <h3 class="text-3xl md:text-5xl font-bold text-default capitalize tracking-wide text-center">
                        order <br />
                        successful
                    </h3>
                </article>
                <div class="tracking-details w-full flex flex-col gap-y-2 items-center justify-center pt-6 pb-3">
                    <h4 class="text-xl font-light font-serif">Tracking Code</h4>
                    <code class="text-2xl text-default tracking-wide font-bold">686634973847483088</code>
                </div>
                <div class="track w-full flex flex-col items-center justify-center py-3">
                    <button class="text-lg py-1.5 px-4 rounded-lg border border-default font-serif text-default tracking-wide">
                        Track Now
                    </button>
                </div>
            </div>
        </NuxtLayout>
    </main>
</template>
