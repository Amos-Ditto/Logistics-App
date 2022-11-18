<template>
    <main class="fixed top-0 bottom-0 left-0 right-0 flex flex-col overflow-y-auto overflow-x-hidden items-center">
        <nav class="w-full md:shadow flex flex-col items-center justify-center sticky top-0 z-20 bg-[#f0f0f0]">
            <LayoutsHomeNavbar />
        </nav>
        <section class="px-2 md:px-12 lg:px-0 w-full lg:w-[1100px] flex flex-col py-1 sm:py-2">
            <slot />
        </section>
    </main>
</template>
