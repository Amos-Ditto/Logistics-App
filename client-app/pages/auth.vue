<script setup lang="ts">
definePageMeta({
    layout: false,
});
</script>
<template>
    <NuxtLayout name="auths">
        <section class="flex flex-col relative w-full">
            <!-- Body Design -->
            <div
                class="bg-curve absolute top-0 right-0 w-[50vw] lg:w-[20vw] h-[40vh] sm:h-[40vh] translate-x-1/2 -translate-y-1/2 rounded-full bg-default transition duration-200"
            ></div>
            <main class="w-full flex flex-col">
                <NuxtPage />
            </main>
        </section>
    </NuxtLayout>
</template>
