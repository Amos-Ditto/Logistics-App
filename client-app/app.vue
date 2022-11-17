<template>
    <NuxtLayout>
        <NuxtPage />
    </NuxtLayout>
</template>

<style>
body {
    line-height: 1.5;
    font-family: 'Mulish', Arial, sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    position: relative;
    padding: 0%;
    margin: 0%;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    outline: none;
    @apply bg-[#f0f0f0] text-dark;
}

.layout-enter-active,
.layout-leave-active {
    transition: all 0.4s;
}

.layout-enter-from,
.layout-leave-to {
    filter: grayscale(1);
    @apply opacity-5;
}

.page-enter-active,
.page-leave-active {
    transition: all 0.4s;
}
.page-enter-from {
    opacity: 0;
    @apply -translate-y-2;
}
.page-leave-to {
    opacity: 0;
}
</style>
