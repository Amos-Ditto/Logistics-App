<template>
    <main class="fixed top-0 bottom-0 left-0 right-0 flex flex-col">
        <slot />
        <footer class="absolute bottom-0 w-full rotate-180 -z-10">
            <IconsFooterWave />
        </footer>
    </main>
</template>
