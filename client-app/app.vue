<template>
    <main>
        <NuxtLoadingIndicator class="absolute top-0 left-0 right-0" />
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

.layout-enter-active,
.layout-leave-active {
    transition: all 0.3s;
}

.layout-enter-from {
    opacity: 0;
}
.layout-leave-to {
    opacity: 0;
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

::-webkit-scrollbar {
    width: 5px;
    height: 5px;
    border-radius: 32px;
}

::-webkit-scrollbar-corner {
    background-color: #f9fbff;
}

::-webkit-scrollbar-thumb {
    @apply bg-gray-300;
    border-radius: 32px;
}
::-webkit-scrollbar-track {
    background-color: #f9fbff;
}
</style>
