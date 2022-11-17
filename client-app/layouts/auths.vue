<template>
    <main class="fixed top-0 bottom-0 right-0 left-0 flex flex-col overflow-x-hidden overflow-y-auto">
        <section class="w-full">
            <slot />
        </section>
        <footer class="w-full rotate-180 -z-10">
            <IconsFooterWave />
        </footer>
    </main>
</template>
