<template>
    <main>
        <NuxtLoadingIndicator />
        <NuxtLayout>
            <NuxtPage />
        </NuxtLayout>
    </main>
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

.layout-enter-active {
    transition: all 0.3s;
}

.layout-enter-from {
    opacity: 0;
}
.layout-leave-to {
    opacity: 0;
}

.page-enter-active {
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
